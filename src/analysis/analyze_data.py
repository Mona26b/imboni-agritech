from pathlib import Path
import pandas as pd
import numpy as np


# ============================================================
# IMBONI AGRITECH
# AGRICULTURAL DATA ANALYSIS ENGINE
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
ANALYSIS_DIR = PROCESSED_DIR / "analysis"

ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_dataset(filename):
    """Load a cleaned dataset."""

    path = PROCESSED_DIR / filename

    if not path.exists():
        print(f"[WARNING] Missing: {filename}")
        return None

    try:
        df = pd.read_csv(path)

        print(
            f"[OK] {filename} "
            f"| {len(df)} rows x {len(df.columns)} columns"
        )

        return df

    except Exception as e:
        print(f"[ERROR] {filename}: {e}")
        return None


def numeric_columns(df):
    """Return numeric columns."""

    return df.select_dtypes(include=np.number).columns.tolist()


def save_analysis(df, filename):
    """Save analysis result."""

    path = ANALYSIS_DIR / filename

    df.to_csv(path, index=False)

    print(f"[SAVED] {filename}")


def summarize_numeric_data(df, value_name):
    """Create a statistical summary for numeric columns."""

    results = []

    for column in numeric_columns(df):

        values = pd.to_numeric(
            df[column],
            errors="coerce"
        ).dropna()

        if values.empty:
            continue

        results.append({
            "indicator": column,
            f"total_{value_name}": values.sum(),
            f"average_{value_name}": values.mean(),
            f"maximum_{value_name}": values.max(),
            f"minimum_{value_name}": values.min()
        })

    return pd.DataFrame(results)


# ============================================================
# 1. CULTIVATED AREA
# ============================================================

def analyze_cultivated_area():

    print("\n" + "=" * 60)
    print("1. CULTIVATED AREA")
    print("=" * 60)

    df = load_dataset("cultivated_area.csv")

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "area"
    )

    if not result.empty:
        save_analysis(
            result,
            "cultivated_area_analysis.csv"
        )


# ============================================================
# 2. HARVESTED AREA
# ============================================================

def analyze_harvested_area():

    print("\n" + "=" * 60)
    print("2. HARVESTED AREA")
    print("=" * 60)

    df = load_dataset("harvested_area.csv")

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "area"
    )

    if not result.empty:
        save_analysis(
            result,
            "harvested_area_analysis.csv"
        )


# ============================================================
# 3. CROP PRODUCTION
# ============================================================

def analyze_crop_production():

    print("\n" + "=" * 60)
    print("3. CROP PRODUCTION")
    print("=" * 60)

    df = load_dataset("crop_production.csv")

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "production"
    )

    if not result.empty:

        result = result.sort_values(
            "total_production",
            ascending=False
        )

        save_analysis(
            result,
            "crop_production_analysis.csv"
        )


# ============================================================
# 4. AVERAGE YIELD
# ============================================================

def analyze_average_yield():

    print("\n" + "=" * 60)
    print("4. AVERAGE CROP YIELD")
    print("=" * 60)

    df = load_dataset("average_yield.csv")

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "yield"
    )

    if not result.empty:

        result = result.sort_values(
            "average_yield",
            ascending=False
        )

        save_analysis(
            result,
            "average_yield_analysis.csv"
        )


# ============================================================
# 5. LARGE-SCALE FARMER YIELD
# ============================================================

def analyze_large_scale_yield():

    print("\n" + "=" * 60)
    print("5. LARGE-SCALE FARMER YIELD")
    print("=" * 60)

    df = load_dataset(
        "large_scale_farmer_yield.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "yield"
    )

    if not result.empty:

        result = result.sort_values(
            "average_yield",
            ascending=False
        )

        save_analysis(
            result,
            "large_scale_yield_analysis.csv"
        )


# ============================================================
# 6. AGRICULTURAL LAND
# ============================================================

def analyze_agricultural_land():

    print("\n" + "=" * 60)
    print("6. AGRICULTURAL LAND USE")
    print("=" * 60)

    df = load_dataset(
        "agricultural_land.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "land"
    )

    if not result.empty:

        save_analysis(
            result,
            "agricultural_land_analysis.csv"
        )


# ============================================================
# 7. AGRICULTURAL PRACTICES
# ============================================================

def analyze_agricultural_practices():

    print("\n" + "=" * 60)
    print("7. AGRICULTURAL PRACTICES")
    print("=" * 60)

    datasets = [
        "agricultural_practices.csv",
        "agricultural_practice_rates.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "agricultural_practices_analysis.csv"
        )


# ============================================================
# 8. EROSION
# ============================================================

def analyze_erosion():

    print("\n" + "=" * 60)
    print("8. EROSION")
    print("=" * 60)

    datasets = [
        "erosion_degree.csv",
        "erosion_control.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "erosion_analysis.csv"
        )


# ============================================================
# 9. IMPROVED SEEDS
# ============================================================

def analyze_improved_seeds():

    print("\n" + "=" * 60)
    print("9. IMPROVED SEEDS")
    print("=" * 60)

    df = load_dataset(
        "improved_seed_use.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "percentage"
    )

    if not result.empty:

        save_analysis(
            result,
            "improved_seed_analysis.csv"
        )


# ============================================================
# 10. SEED SOURCES
# ============================================================

def analyze_seed_sources():

    print("\n" + "=" * 60)
    print("10. SEED SOURCES")
    print("=" * 60)

    datasets = [
        "improved_seed_sources.csv",
        "seed_sources_crop.csv",
        "seed_type.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "seed_analysis.csv"
        )


# ============================================================
# 11. FERTILIZER
# ============================================================

def analyze_fertilizer():

    print("\n" + "=" * 60)
    print("11. FERTILIZER")
    print("=" * 60)

    datasets = [
        "organic_fertilizer.csv",
        "inorganic_fertilizer.csv",
        "inorganic_fertilizer_sources.csv",
        "fertilizer_types.csv",
        "fertilizer_types_district.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "fertilizer_analysis.csv"
        )


# ============================================================
# 12. PESTICIDES
# ============================================================

def analyze_pesticides():

    print("\n" + "=" * 60)
    print("12. PESTICIDES")
    print("=" * 60)

    datasets = [
        "pesticide_use.csv",
        "pesticide_types.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "pesticide_analysis.csv"
        )


# ============================================================
# 13. IRRIGATION
# ============================================================

def analyze_irrigation():

    print("\n" + "=" * 60)
    print("13. IRRIGATION")
    print("=" * 60)

    df = load_dataset(
        "irrigation_types.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "percentage"
    )

    if not result.empty:

        save_analysis(
            result,
            "irrigation_analysis.csv"
        )


# ============================================================
# 14. WATER SOURCES
# ============================================================

def analyze_water_sources():

    print("\n" + "=" * 60)
    print("14. WATER SOURCES")
    print("=" * 60)

    df = load_dataset(
        "water_sources.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "percentage"
    )

    if not result.empty:

        save_analysis(
            result,
            "water_source_analysis.csv"
        )


# ============================================================
# 15. SOWING DATES
# ============================================================

def analyze_sowing_dates():

    print("\n" + "=" * 60)
    print("15. SOWING DATES")
    print("=" * 60)

    datasets = [
        "sowing_dates_district.csv",
        "sowing_dates_crop.csv"
    ]

    results = []

    for filename in datasets:

        df = load_dataset(filename)

        if df is None:
            continue

        for column in numeric_columns(df):

            values = pd.to_numeric(
                df[column],
                errors="coerce"
            ).dropna()

            if values.empty:
                continue

            results.append({
                "dataset": filename,
                "indicator": column,
                "average_percentage": values.mean(),
                "maximum_percentage": values.max(),
                "minimum_percentage": values.min()
            })

    if results:

        save_analysis(
            pd.DataFrame(results),
            "sowing_date_analysis.csv"
        )


# ============================================================
# 16. PRODUCTION USE
# ============================================================

def analyze_production_use():

    print("\n" + "=" * 60)
    print("16. PRODUCTION USE")
    print("=" * 60)

    df = load_dataset(
        "production_use.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "percentage"
    )

    if not result.empty:

        save_analysis(
            result,
            "production_use_analysis.csv"
        )


# ============================================================
# 17. CROPPING SYSTEM
# ============================================================

def analyze_cropping_system():

    print("\n" + "=" * 60)
    print("17. CROPPING SYSTEM")
    print("=" * 60)

    df = load_dataset(
        "cropping_system.csv"
    )

    if df is None:
        return

    result = summarize_numeric_data(
        df,
        "percentage"
    )

    if not result.empty:

        save_analysis(
            result,
            "cropping_system_analysis.csv"
        )


# ============================================================
# 18. MASTER REPORT
# ============================================================

def create_master_report():

    print("\n" + "=" * 60)
    print("18. MASTER ANALYSIS REPORT")
    print("=" * 60)

    files = sorted(
        ANALYSIS_DIR.glob("*.csv")
    )

    report = []

    report.append("IMBONI AGRITECH")
    report.append("AGRICULTURAL DATA ANALYSIS REPORT")
    report.append("=" * 60)
    report.append("")

    report.append(
        f"Analysis datasets generated: {len(files)}"
    )

    report.append("")
    report.append("Generated files:")
    report.append("-" * 40)

    for file in files:

        try:

            df = pd.read_csv(file)

            report.append(
                f"{file.name} | "
                f"{len(df)} rows | "
                f"{len(df.columns)} columns"
            )

        except Exception as e:

            report.append(
                f"{file.name} | ERROR: {e}"
            )

    report.append("")
    report.append("=" * 60)
    report.append("Analysis stage completed.")

    output = ANALYSIS_DIR / "analysis_report.txt"

    with open(
        output,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))

    print(f"[SAVED] {output.name}")


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n")
    print("=" * 60)
    print("        IMBONI AGRITECH")
    print("        AGRICULTURAL DATA ANALYSIS")
    print("=" * 60)

    print("\nProcessed data:")
    print(PROCESSED_DIR)

    print("\nAnalysis output:")
    print(ANALYSIS_DIR)

    analyze_cultivated_area()

    analyze_harvested_area()

    analyze_crop_production()

    analyze_average_yield()

    analyze_large_scale_yield()

    analyze_agricultural_land()

    analyze_agricultural_practices()

    analyze_erosion()

    analyze_improved_seeds()

    analyze_seed_sources()

    analyze_fertilizer()

    analyze_pesticides()

    analyze_irrigation()

    analyze_water_sources()

    analyze_sowing_dates()

    analyze_production_use()

    analyze_cropping_system()

    create_master_report()

    print("\n" + "=" * 60)
    print("ANALYSIS STAGE COMPLETED")
    print("=" * 60)

    print("\nAnalysis files:")
    print(ANALYSIS_DIR)


if __name__ == "__main__":
    main()