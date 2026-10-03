# ============================================================
# IMBONI AGRITECH
# BUILD AGRICULTURAL INTELLIGENCE DATASET
# ============================================================

from pathlib import Path
import pandas as pd
import numpy as np
import re


# ============================================================
# 1. PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

INTELLIGENCE_DIR = PROCESSED_DIR / "intelligence"

INTELLIGENCE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("=" * 70)
print("IMBONI AGRITECH - AGRICULTURAL INTELLIGENCE")
print("=" * 70)

print()
print(f"Processed data: {PROCESSED_DIR}")
print(f"Intelligence output: {INTELLIGENCE_DIR}")
print()


# ============================================================
# 2. GENERAL HELPERS
# ============================================================

def make_unique_columns(columns):

    counts = {}
    result = []

    for column in columns:

        column = str(column).strip()

        if column not in counts:

            counts[column] = 1
            result.append(column)

        else:

            counts[column] += 1

            result.append(
                f"{column}_{counts[column]}"
            )

    return result


def clean_column_name(column):

    column = str(column).strip().lower()

    column = re.sub(
        r"[^a-z0-9]+",
        "_",
        column
    )

    column = column.strip("_")

    return column


def normalize_columns(df):

    df = df.copy()

    df.columns = [
        clean_column_name(column)
        for column in df.columns
    ]

    df.columns = make_unique_columns(
        df.columns
    )

    return df


def clean_number(value):

    if pd.isna(value):
        return np.nan

    if isinstance(value, (int, float, np.number)):

        return float(value)

    value = str(value).strip()

    if value == "":
        return np.nan

    value = value.replace(",", "")

    value = value.replace("%", "")

    value = value.replace(
        "–",
        "-"
    )

    value = value.replace(
        "—",
        "-"
    )

    try:

        return float(value)

    except:

        return np.nan


def numeric_series(series):

    return series.apply(
        clean_number
    )


def find_district_column(df):

    possible_names = [
        "district",
        "district_name",
        "districts",
        "district_crop"
    ]

    for column in df.columns:

        if column in possible_names:

            return column

    for column in df.columns:

        if "district" in column:

            return column

    return df.columns[0]


def prepare_dataframe(filename):

    path = PROCESSED_DIR / filename

    print(
        f"Loading: {filename}"
    )

    if not path.exists():

        print(
            f"[WARNING] File not found: {path}"
        )

        return pd.DataFrame()

    df = pd.read_csv(
        path
    )

    df = normalize_columns(
        df
    )

    district_column = find_district_column(
        df
    )

    df = df.rename(
        columns={
            district_column: "district"
        }
    )

    df["district"] = (
        df["district"]
        .astype(str)
        .str.strip()
    )

    # Remove obvious header/subheader rows
    bad_districts = [
        "",
        "nan",
        "district",
        "district/crop",
        "district crop",
        "overall"
    ]

    df = df[
        ~df["district"]
        .str.lower()
        .isin(bad_districts)
    ]

    df = df[
        df["district"]
        .str.len() > 1
    ]

    # Convert numeric-looking columns
    for column in df.columns:

        if column == "district":
            continue

        converted = numeric_series(
            df[column]
        )

        numeric_count = converted.notna().sum()

        if numeric_count > 0:

            df[column] = converted

    df = df.reset_index(
        drop=True
    )

    print(
        f"  -> {len(df)} rows x "
        f"{len(df.columns)} columns"
    )

    return df


def find_column(df, keywords):

    for column in df.columns:

        column_lower = column.lower()

        for keyword in keywords:

            if keyword in column_lower:

                return column

    return None


def get_numeric_columns(df):

    columns = []

    for column in df.columns:

        if column == "district":
            continue

        if pd.api.types.is_numeric_dtype(
            df[column]
        ):

            columns.append(
                column
            )

    return columns


def get_crop_columns(df):

    excluded_words = [
        "district",
        "total",
        "area",
        "land",
        "farmer",
        "plot",
        "percent",
        "percentage",
        "overall",
        "ssf",
        "lsf",
        "source",
        "other"
    ]

    crop_columns = []

    for column in df.columns:

        if column == "district":
            continue

        if not pd.api.types.is_numeric_dtype(
            df[column]
        ):
            continue

        column_lower = column.lower()

        if any(
            word in column_lower
            for word in excluded_words
        ):
            continue

        crop_columns.append(
            column
        )

    return crop_columns


def safe_mean(df, column):

    if column is None:
        return np.nan

    if column not in df.columns:
        return np.nan

    values = numeric_series(
        df[column]
    )

    if values.dropna().empty:
        return np.nan

    return values.mean()


def safe_sum(df, column):

    if column is None:
        return np.nan

    if column not in df.columns:
        return np.nan

    values = numeric_series(
        df[column]
    )

    if values.dropna().empty:
        return np.nan

    return values.sum()


def district_average(df, column):

    if (
        df.empty
        or column is None
        or column not in df.columns
    ):
        return pd.DataFrame(
            columns=[
                "district",
                "value"
            ]
        )

    result = (
        df.groupby(
            "district",
            as_index=False
        )[column]
        .mean()
    )

    result = result.rename(
        columns={
            column: "value"
        }
    )

    return result


def merge_indicator(
    master,
    df,
    source_column,
    output_name
):

    if df.empty:
        return master

    if source_column is None:
        return master

    if source_column not in df.columns:
        return master

    temp = (
        df[
            [
                "district",
                source_column
            ]
        ]
        .copy()
    )

    temp[source_column] = numeric_series(
        temp[source_column]
    )

    temp = (
        temp.groupby(
            "district",
            as_index=False
        )[source_column]
        .mean()
    )

    temp = temp.rename(
        columns={
            source_column: output_name
        }
    )

    temp.columns = make_unique_columns(
        temp.columns
    )

    master = master.merge(
        temp,
        on="district",
        how="left"
    )

    master.columns = make_unique_columns(
        master.columns
    )

    return master


# ============================================================
# 3. LOAD DATASETS
# ============================================================

print("1. LOADING DATA")
print("-" * 70)

cultivated = prepare_dataframe(
    "cultivated_area.csv"
)

harvested = prepare_dataframe(
    "harvested_area.csv"
)

average_yield = prepare_dataframe(
    "average_yield.csv"
)

crop_production = prepare_dataframe(
    "crop_production.csv"
)

agricultural_land = prepare_dataframe(
    "agricultural_land.csv"
)

agricultural_practices = prepare_dataframe(
    "agricultural_practices.csv"
)

practice_rates = prepare_dataframe(
    "agricultural_practice_rates.csv"
)

improved_seed = prepare_dataframe(
    "improved_seed_use.csv"
)

organic_fertilizer = prepare_dataframe(
    "organic_fertilizer.csv"
)

inorganic_fertilizer = prepare_dataframe(
    "inorganic_fertilizer.csv"
)

pesticide_use = prepare_dataframe(
    "pesticide_use.csv"
)

irrigation = prepare_dataframe(
    "irrigation_types.csv"
)

water_sources = prepare_dataframe(
    "water_sources.csv"
)

erosion_control = prepare_dataframe(
    "erosion_control.csv"
)

erosion_degree = prepare_dataframe(
    "erosion_degree.csv"
)

print()
print("[OK] Dataset loading complete.")
print()


# ============================================================
# 4. CREATE MASTER DISTRICT LIST
# ============================================================

print("2. BUILDING MASTER DISTRICT LIST")
print("-" * 70)

district_sets = []

for df in [
    cultivated,
    harvested,
    average_yield,
    crop_production,
    agricultural_land,
    agricultural_practices,
    practice_rates,
    improved_seed,
    organic_fertilizer,
    inorganic_fertilizer,
    pesticide_use,
    irrigation,
    water_sources,
    erosion_control,
    erosion_degree
]:

    if not df.empty and "district" in df.columns:

        district_sets.append(
            set(
                df["district"]
                .dropna()
                .astype(str)
                .str.strip()
            )
        )

all_districts = set()

for district_set in district_sets:

    all_districts.update(
        district_set
    )

master = pd.DataFrame(
    {
        "district": sorted(
            all_districts
        )
    }
)

print(
    f"[OK] Districts found: "
    f"{len(master)}"
)

print()


# ============================================================
# 5. CULTIVATED AND HARVESTED AREA
# ============================================================

print("3. CULTIVATED + HARVESTED AREA")
print("-" * 70)


cultivated_total_column = find_column(
    cultivated,
    [
        "total_developed_land"
    ]
)

harvested_total_column = find_column(
    harvested,
    [
        "total_developed_land"
    ]
)

if cultivated_total_column:

    master = merge_indicator(
        master,
        cultivated,
        cultivated_total_column,
        "cultivated_area_ha"
    )

if harvested_total_column:

    master = merge_indicator(
        master,
        harvested,
        harvested_total_column,
        "harvested_area_ha"
    )


if (
    "cultivated_area_ha" in master.columns
    and "harvested_area_ha" in master.columns
):

    master[
        "harvested_to_cultivated_ratio"
    ] = np.where(
        master["cultivated_area_ha"] > 0,
        (
            master["harvested_area_ha"]
            /
            master["cultivated_area_ha"]
        ),
        np.nan
    )

    master[
        "harvested_to_cultivated_percent"
    ] = (
        master[
            "harvested_to_cultivated_ratio"
        ]
        * 100
    )

print(
    "[OK] Area indicators created."
)

print()


# ============================================================
# 6. AGRICULTURAL LAND
# ============================================================

print("4. AGRICULTURAL LAND")
print("-" * 70)

agri_land_column = find_column(
    agricultural_land,
    [
        "agricultural_land"
    ]
)

agri_land_percent_column = find_column(
    agricultural_land,
    [
        "of_agricultural_land"
    ]
)

seasonal_crop_column = find_column(
    agricultural_land,
    [
        "seasonal_crops"
    ]
)

permanent_crop_column = find_column(
    agricultural_land,
    [
        "permanent_crops"
    ]
)

if agri_land_column:

    master = merge_indicator(
        master,
        agricultural_land,
        agri_land_column,
        "agricultural_land_000ha"
    )

if agri_land_percent_column:

    master = merge_indicator(
        master,
        agricultural_land,
        agri_land_percent_column,
        "agricultural_land_percent"
    )

if seasonal_crop_column:

    master = merge_indicator(
        master,
        agricultural_land,
        seasonal_crop_column,
        "seasonal_crop_area_000ha"
    )

if permanent_crop_column:

    master = merge_indicator(
        master,
        agricultural_land,
        permanent_crop_column,
        "permanent_crop_area_000ha"
    )

print(
    "[OK] Agricultural land indicators created."
)

print()


# ============================================================
# 7. DOMINANT CROP
# ============================================================

print("5. DOMINANT CROP")
print("-" * 70)

if not cultivated.empty:

    crop_columns = get_crop_columns(
        cultivated
    )

    dominant_rows = []

    for _, row in cultivated.iterrows():

        district = row["district"]

        values = {}

        for crop in crop_columns:

            value = clean_number(
                row[crop]
            )

            if pd.notna(value):

                values[crop] = value

        if values:

            dominant_crop = max(
                values,
                key=values.get
            )

            dominant_area = values[
                dominant_crop
            ]

        else:

            dominant_crop = np.nan
            dominant_area = np.nan

        dominant_rows.append(
            {
                "district": district,
                "dominant_crop": dominant_crop,
                "dominant_crop_area_ha": dominant_area
            }
        )

    dominant_df = pd.DataFrame(
        dominant_rows
    )

    dominant_df = (
        dominant_df
        .groupby(
            "district",
            as_index=False
        )
        .agg(
            dominant_crop=(
                "dominant_crop",
                "first"
            ),
            dominant_crop_area_ha=(
                "dominant_crop_area_ha",
                "max"
            )
        )
    )

    master = master.merge(
        dominant_df,
        on="district",
        how="left"
    )

print(
    "[OK] Dominant crop indicators created."
)

print()


# ============================================================
# 8. AVERAGE YIELD
# ============================================================

print("6. AVERAGE CROP YIELD")
print("-" * 70)

if not average_yield.empty:

    yield_columns = get_crop_columns(
        average_yield
    )

    yield_rows = []

    for _, row in average_yield.iterrows():

        district = row["district"]

        values = []

        for crop in yield_columns:

            value = clean_number(
                row[crop]
            )

            if pd.notna(value) and value > 0:

                values.append(
                    value
                )

        if values:

            avg_yield = np.mean(
                values
            )

        else:

            avg_yield = np.nan

        yield_rows.append(
            {
                "district": district,
                "average_crop_yield_kg_ha":
                    avg_yield
            }
        )

    yield_df = pd.DataFrame(
        yield_rows
    )

    yield_df = (
        yield_df
        .groupby(
            "district",
            as_index=False
        )[
            "average_crop_yield_kg_ha"
        ]
        .mean()
    )

    master = master.merge(
        yield_df,
        on="district",
        how="left"
    )

print(
    "[OK] Yield indicators created."
)

print()


# ============================================================
# 9. TOP PRODUCTION CROP
# ============================================================

print("7. TOP PRODUCTION CROP")
print("-" * 70)

if not crop_production.empty:

    production_columns = get_crop_columns(
        crop_production
    )

    production_rows = []

    for _, row in crop_production.iterrows():

        district = row["district"]

        values = {}

        for crop in production_columns:

            value = clean_number(
                row[crop]
            )

            if pd.notna(value):

                values[crop] = value

        if values:

            top_crop = max(
                values,
                key=values.get
            )

            top_production = values[
                top_crop
            ]

        else:

            top_crop = np.nan
            top_production = np.nan

        production_rows.append(
            {
                "district": district,
                "top_production_crop":
                    top_crop,
                "top_crop_production_mt":
                    top_production
            }
        )

    production_df = pd.DataFrame(
        production_rows
    )

    production_df = (
        production_df
        .groupby(
            "district",
            as_index=False
        )
        .agg(
            top_production_crop=(
                "top_production_crop",
                "first"
            ),
            top_crop_production_mt=(
                "top_crop_production_mt",
                "max"
            )
        )
    )

    master = master.merge(
        production_df,
        on="district",
        how="left"
    )

print(
    "[OK] Production indicators created."
)

print()


# ============================================================
# 10. AGRICULTURAL PRACTICES
# ============================================================

print("8. AGRICULTURAL PRACTICES")
print("-" * 70)

erosion_protection_column = find_column(
    practice_rates,
    [
        "protected_land_against_erosion"
    ]
)

mechanization_column = find_column(
    practice_rates,
    [
        "mechanical_equipment"
    ]
)

irrigation_practice_column = find_column(
    practice_rates,
    [
        "practiced_irrigation"
    ]
)

agroforestry_column = find_column(
    practice_rates,
    [
        "practiced_agroforestry"
    ]
)

if erosion_protection_column:

    master = merge_indicator(
        master,
        practice_rates,
        erosion_protection_column,
        "erosion_protection_percent"
    )

if mechanization_column:

    master = merge_indicator(
        master,
        practice_rates,
        mechanization_column,
        "mechanization_percent"
    )

if irrigation_practice_column:

    master = merge_indicator(
        master,
        practice_rates,
        irrigation_practice_column,
        "irrigation_percent"
    )

if agroforestry_column:

    master = merge_indicator(
        master,
        practice_rates,
        agroforestry_column,
        "agroforestry_percent"
    )

print(
    "[OK] Agricultural practice indicators created."
)

print()


# ============================================================
# 11. IMPROVED SEEDS
# ============================================================

print("9. IMPROVED SEEDS")
print("-" * 70)

improved_seed_column = find_column(
    improved_seed,
    [
        "percentage_of_farmers_who_used_improved_seeds"
    ]
)

if improved_seed_column:

    master = merge_indicator(
        master,
        improved_seed,
        improved_seed_column,
        "improved_seed_use_percent"
    )

print(
    "[OK] Improved seed indicator created."
)

print()


# ============================================================
# 12. ORGANIC FERTILIZER
# ============================================================

print("10. ORGANIC FERTILIZER")
print("-" * 70)

organic_overall_column = find_column(
    organic_fertilizer,
    [
        "overall"
    ]
)

if organic_overall_column:

    master = merge_indicator(
        master,
        organic_fertilizer,
        organic_overall_column,
        "organic_fertilizer_use_percent"
    )

print(
    "[OK] Organic fertilizer indicator created."
)

print()


# ============================================================
# 13. INORGANIC FERTILIZER
# ============================================================

print("11. INORGANIC FERTILIZER")
print("-" * 70)

inorganic_overall_column = find_column(
    inorganic_fertilizer,
    [
        "overall"
    ]
)

if inorganic_overall_column:

    master = merge_indicator(
        master,
        inorganic_fertilizer,
        inorganic_overall_column,
        "inorganic_fertilizer_use_percent"
    )

print(
    "[OK] Inorganic fertilizer indicator created."
)

print()


# ============================================================
# 14. PESTICIDE USE
# ============================================================

print("12. PESTICIDE USE")
print("-" * 70)

pesticide_overall_column = find_column(
    pesticide_use,
    [
        "overall"
    ]
)

if pesticide_overall_column:

    master = merge_indicator(
        master,
        pesticide_use,
        pesticide_overall_column,
        "pesticide_use_percent"
    )

print(
    "[OK] Pesticide indicator created."
)

print()


# ============================================================
# 15. EROSION
# ============================================================

print("13. EROSION")
print("-" * 70)

erosion_control_column = find_column(
    erosion_control,
    [
        "plots_under_erosion_control",
        "erosion_control"
    ]
)

if erosion_control_column:

    master = merge_indicator(
        master,
        erosion_control,
        erosion_control_column,
        "erosion_control_percent"
    )

if not erosion_degree.empty:

    numeric_erosion_columns = [
        column
        for column in erosion_degree.columns
        if (
            column != "district"
            and
            pd.api.types.is_numeric_dtype(
                erosion_degree[column]
            )
        )
    ]

    if numeric_erosion_columns:

        erosion_degree["erosion_degree_average"] = (
            erosion_degree[
                numeric_erosion_columns
            ]
            .mean(
                axis=1,
                skipna=True
            )
        )

        master = merge_indicator(
            master,
            erosion_degree,
            "erosion_degree_average",
            "erosion_degree_average_percent"
        )

print(
    "[OK] Erosion indicators created."
)

print()


# ============================================================
# 16. DATA-DERIVED OBSERVED GAP INDICATORS
# ============================================================

print("14. AGRICULTURAL GAP INDICATORS")
print("-" * 70)

gap_components = []


def add_gap_component(
    master_df,
    column_name,
    component_name
):

    if column_name not in master_df.columns:

        return master_df

    values = numeric_series(
        master_df[column_name]
    )

    if values.notna().sum() == 0:

        return master_df

    # Normalize each indicator between 0 and 1
    # using the observed district range.
    minimum = values.min()
    maximum = values.max()

    if pd.isna(minimum) or pd.isna(maximum):

        return master_df

    if maximum == minimum:

        normalized = pd.Series(
            0.0,
            index=master_df.index
        )

    else:

        normalized = (
            values - minimum
        ) / (
            maximum - minimum
        )

    master_df[
        component_name
    ] = normalized

    return master_df


# Low observed adoption can indicate a larger observed gap.
# Therefore these are converted to 1 - normalized value.

low_adoption_columns = [
    (
        "improved_seed_use_percent",
        "seed_gap_component"
    ),
    (
        "inorganic_fertilizer_use_percent",
        "inorganic_fertilizer_gap_component"
    ),
    (
        "irrigation_percent",
        "irrigation_gap_component"
    ),
    (
        "mechanization_percent",
        "mechanization_gap_component"
    )
]


for source_column, component_column in low_adoption_columns:

    if source_column in master.columns:

        values = numeric_series(
            master[source_column]
        )

        minimum = values.min()
        maximum = values.max()

        if (
            pd.notna(minimum)
            and
            pd.notna(maximum)
            and
            maximum != minimum
        ):

            normalized = (
                values - minimum
            ) / (
                maximum - minimum
            )

            master[
                component_column
            ] = 1 - normalized


gap_columns = [
    column
    for column in master.columns
    if column.endswith(
        "_gap_component"
    )
]


if gap_columns:

    master[
        "observed_input_gap_index"
    ] = (
        master[
            gap_columns
        ]
        .mean(
            axis=1,
            skipna=True
        )
        * 100
    )

else:

    master[
        "observed_input_gap_index"
    ] = np.nan


print(
    "[OK] Observed agricultural gap indicators created."
)

print()


# ============================================================
# 17. AGRICULTURAL PROFILE LABELS
# ============================================================

print("15. AGRICULTURAL PROFILES")
print("-" * 70)


def create_profile(row):

    profiles = []

    if (
        pd.notna(
            row.get(
                "irrigation_percent",
                np.nan
            )
        )
        and
        row["irrigation_percent"] < 10
    ):

        profiles.append(
            "Low irrigation adoption"
        )

    if (
        pd.notna(
            row.get(
                "mechanization_percent",
                np.nan
            )
        )
        and
        row["mechanization_percent"] < 10
    ):

        profiles.append(
            "Low mechanization adoption"
        )

    if (
        pd.notna(
            row.get(
                "improved_seed_use_percent",
                np.nan
            )
        )
        and
        row["improved_seed_use_percent"] < 20
    ):

        profiles.append(
            "Low improved-seed adoption"
        )

    if (
        pd.notna(
            row.get(
                "inorganic_fertilizer_use_percent",
                np.nan
            )
        )
        and
        row[
            "inorganic_fertilizer_use_percent"
        ] < 50
    ):

        profiles.append(
            "Lower inorganic-fertilizer adoption"
        )

    if not profiles:

        profiles.append(
            "Multiple agricultural practices observed"
        )

    return "; ".join(
        profiles
    )


master[
    "agricultural_profile"
] = master.apply(
    create_profile,
    axis=1
)


print(
    "[OK] District profiles created."
)

print()


# ============================================================
# 18. FINAL CLEANUP
# ============================================================

print("16. FINAL CLEANUP")
print("-" * 70)

master = master.replace(
    [
        np.inf,
        -np.inf
    ],
    np.nan
)


# Make absolutely sure every column name is unique
master.columns = make_unique_columns(
    master.columns
)


# Round numeric values safely
for column in master.columns:

    series = master[column]

    if isinstance(
        series,
        pd.DataFrame
    ):

        continue

    if pd.api.types.is_numeric_dtype(
        series
    ):

        master[column] = (
            series.round(2)
        )


# Remove completely empty columns
empty_columns = []

for column in master.columns:

    if (
        column != "district"
        and
        master[column].isna().all()
    ):

        empty_columns.append(
            column
        )


if empty_columns:

    master = master.drop(
        columns=empty_columns
    )


# Sort districts alphabetically
master = master.sort_values(
    "district"
).reset_index(
    drop=True
)


print(
    f"[OK] Final dataset: "
    f"{len(master)} districts x "
    f"{len(master.columns)} columns"
)

print()


# ============================================================
# 19. SAVE MASTER INTELLIGENCE DATASET
# ============================================================

print("17. SAVING INTELLIGENCE DATASET")
print("-" * 70)

master_output = (
    INTELLIGENCE_DIR
    /
    "district_intelligence.csv"
)

master.to_csv(
    master_output,
    index=False
)

print(
    f"[SAVED] {master_output}"
)

print()


# ============================================================
# 20. CREATE PRIORITY INDICATORS DATASET
# ============================================================

print("18. CREATING PRIORITY INDICATORS")
print("-" * 70)

priority_columns = [
    "district",
    "agricultural_land_percent",
    "cultivated_area_ha",
    "harvested_area_ha",
    "harvested_to_cultivated_percent",
    "average_crop_yield_kg_ha",
    "dominant_crop",
    "dominant_crop_area_ha",
    "top_production_crop",
    "top_crop_production_mt",
    "improved_seed_use_percent",
    "organic_fertilizer_use_percent",
    "inorganic_fertilizer_use_percent",
    "pesticide_use_percent",
    "irrigation_percent",
    "mechanization_percent",
    "agroforestry_percent",
    "erosion_protection_percent",
    "observed_input_gap_index",
    "agricultural_profile"
]


available_priority_columns = [
    column
    for column in priority_columns
    if column in master.columns
]


priority = master[
    available_priority_columns
].copy()


priority_output = (
    INTELLIGENCE_DIR
    /
    "district_priority_indicators.csv"
)

priority.to_csv(
    priority_output,
    index=False
)

print(
    f"[SAVED] {priority_output}"
)

print()


# ============================================================
# 21. CREATE INTELLIGENCE REPORT
# ============================================================

print("19. CREATING REPORT")
print("-" * 70)

report_lines = []

report_lines.append(
    "IMBONI AGRITECH"
)

report_lines.append(
    "DISTRICT AGRICULTURAL INTELLIGENCE REPORT"
)

report_lines.append(
    "=" * 60
)

report_lines.append("")

report_lines.append(
    f"Districts analyzed: {len(master)}"
)

report_lines.append(
    f"Indicators generated: {len(master.columns)}"
)

report_lines.append("")

report_lines.append(
    "DATA SOURCES"
)

report_lines.append(
    "-" * 60
)

report_lines.append(
    "NISR Seasonal Agricultural Survey "
    "Season B 2026 cleaned datasets."
)

report_lines.append("")

report_lines.append(
    "MAIN INDICATORS"
)

report_lines.append(
    "-" * 60
)

for column in master.columns:

    if column == "district":
        continue

    report_lines.append(
        f"- {column}"
    )

report_lines.append("")

report_lines.append(
    "IMPORTANT INTERPRETATION NOTE"
)

report_lines.append(
    "-" * 60
)

report_lines.append(
    "The observed input gap index is a "
    "descriptive data-derived indicator."
)

report_lines.append(
    "It summarizes relative differences "
    "between districts in selected "
    "agricultural input/practice indicators."
)

report_lines.append(
    "It should not be interpreted as a "
    "causal prediction of agricultural failure."
)

report_lines.append("")

report_lines.append(
    "OUTPUT FILES"
)

report_lines.append(
    "-" * 60
)

report_lines.append(
    "district_intelligence.csv"
)

report_lines.append(
    "district_priority_indicators.csv"
)

report_lines.append(
    "intelligence_report.txt"
)


report_output = (
    INTELLIGENCE_DIR
    /
    "intelligence_report.txt"
)

with open(
    report_output,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "\n".join(
            report_lines
        )
    )


print(
    f"[SAVED] {report_output}"
)

print()


# ============================================================
# 22. FINAL SUMMARY
# ============================================================

print("=" * 70)
print("IMBONI AGRITECH INTELLIGENCE BUILD COMPLETE")
print("=" * 70)

print()

print(
    f"Districts: {len(master)}"
)

print(
    f"Columns: {len(master.columns)}"
)

print()

print(
    "Generated:"
)

print(
    "1. district_intelligence.csv"
)

print(
    "2. district_priority_indicators.csv"
)

print(
    "3. intelligence_report.txt"
)

print()

print(
    "Output folder:"
)

print(
    INTELLIGENCE_DIR
)

print()

print("=" * 70)
print("DONE")
print("=" * 70)