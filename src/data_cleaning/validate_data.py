from pathlib import Path
import pandas as pd


# ============================================================
# IMBONI AGRITECH
# NISR SEASON B 2026
# CLEANED DATA VALIDATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================================
# 1. CHECK PROCESSED FOLDER
# ============================================================

if not PROCESSED_DIR.exists():
    raise FileNotFoundError(
        f"Processed data folder not found:\n{PROCESSED_DIR}"
    )


# ============================================================
# 2. DATASETS TO VALIDATE
# ============================================================

datasets = [
    "agricultural_land.csv",
    "agricultural_practices.csv",
    "cultivated_area.csv",
    "harvested_area.csv",
    "average_yield.csv",
    "large_scale_farmer_yield.csv",
    "crop_production.csv",
    "production_use.csv",
    "cropping_system.csv",
    "sowing_dates_district.csv",
    "sowing_dates_crop.csv",
    "improved_seed_use.csv",
    "seed_type.csv",
    "improved_seed_sources.csv",
    "seed_sources_crop.csv",
    "organic_fertilizer.csv",
    "inorganic_fertilizer.csv",
    "inorganic_fertilizer_sources.csv",
    "fertilizer_types.csv",
    "fertilizer_types_district.csv",
    "pesticide_use.csv",
    "pesticide_types.csv",
    "agricultural_practice_rates.csv",
    "irrigation_types.csv",
    "water_sources.csv",
    "erosion_control.csv",
    "erosion_degree.csv",
]


# ============================================================
# 3. VALIDATION REPORT
# ============================================================

report_file = (
    PROCESSED_DIR
    / "validation_report.txt"
)

report = []

report.append(
    "IMBONI AGRITECH"
)

report.append(
    "NISR SEASON B 2026"
)

report.append(
    "CLEANED DATA VALIDATION REPORT"
)

report.append(
    "=" * 70
)

report.append("")


successful = 0
failed = 0


# ============================================================
# 4. VALIDATE EACH DATASET
# ============================================================

for filename in datasets:

    file_path = PROCESSED_DIR / filename

    print("\n" + "-" * 70)
    print(f"VALIDATING: {filename}")

    report.append(
        f"DATASET: {filename}"
    )

    report.append(
        "-" * 50
    )

    # --------------------------------------------------------
    # Check file exists
    # --------------------------------------------------------

    if not file_path.exists():

        print("ERROR: File does not exist.")

        report.append(
            "STATUS: FAILED - FILE NOT FOUND"
        )

        report.append("")

        failed += 1

        continue

    try:

        # ----------------------------------------------------
        # Load CSV
        # ----------------------------------------------------

        df = pd.read_csv(
            file_path
        )

        rows = df.shape[0]
        columns = df.shape[1]

        print(
            f"Rows    : {rows}"
        )

        print(
            f"Columns : {columns}"
        )

        report.append(
            f"Rows: {rows}"
        )

        report.append(
            f"Columns: {columns}"
        )


        # ----------------------------------------------------
        # Column names
        # ----------------------------------------------------

        print("\nColumns:")

        print(
            list(df.columns)
        )

        report.append(
            f"Columns names: {list(df.columns)}"
        )


        # ----------------------------------------------------
        # Missing values
        # ----------------------------------------------------

        missing = df.isna().sum()

        total_missing = int(
            missing.sum()
        )

        print(
            f"\nTotal missing values: {total_missing}"
        )

        report.append(
            f"Total missing values: {total_missing}"
        )


        # ----------------------------------------------------
        # Duplicate rows
        # ----------------------------------------------------

        duplicates = int(
            df.duplicated().sum()
        )

        print(
            f"Duplicate rows: {duplicates}"
        )

        report.append(
            f"Duplicate rows: {duplicates}"
        )


        # ----------------------------------------------------
        # District information
        # ----------------------------------------------------

        district_columns = [
            column
            for column in df.columns
            if "district" in column.lower()
        ]

        if district_columns:

            for district_column in district_columns:

                district_count = (
                    df[district_column]
                    .dropna()
                    .nunique()
                )

                print(
                    f"Unique values in "
                    f"{district_column}: "
                    f"{district_count}"
                )

                report.append(
                    f"Unique {district_column}: "
                    f"{district_count}"
                )


        # ----------------------------------------------------
        # Numeric columns
        # ----------------------------------------------------

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        print(
            f"Numeric columns: "
            f"{len(numeric_columns)}"
        )

        report.append(
            f"Numeric columns: "
            f"{len(numeric_columns)}"
        )


        # ----------------------------------------------------
        # Negative values
        # ----------------------------------------------------

        negative_values = 0

        for column in numeric_columns:

            negative_values += int(
                (df[column] < 0).sum()
            )

        print(
            f"Negative numeric values: "
            f"{negative_values}"
        )

        report.append(
            f"Negative numeric values: "
            f"{negative_values}"
        )


        # ----------------------------------------------------
        # Dataset preview
        # ----------------------------------------------------

        print("\nFirst 3 rows:")

        print(
            df.head(3).to_string(
                index=False
            )
        )


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        report.append(
            "STATUS: PASSED BASIC VALIDATION"
        )

        report.append("")

        successful += 1


    except Exception as error:

        print(
            f"ERROR: {error}"
        )

        report.append(
            f"STATUS: FAILED - {error}"
        )

        report.append("")

        failed += 1


# ============================================================
# 5. SAVE REPORT
# ============================================================

report.append(
    "=" * 70
)

report.append(
    "FINAL VALIDATION SUMMARY"
)

report.append(
    f"Datasets checked: {len(datasets)}"
)

report.append(
    f"Successful: {successful}"
)

report.append(
    f"Failed: {failed}"
)


report_file.write_text(
    "\n".join(report),
    encoding="utf-8"
)


# ============================================================
# 6. FINAL TERMINAL OUTPUT
# ============================================================

print("\n")
print("=" * 70)
print("             VALIDATION COMPLETE")
print("=" * 70)

print(
    f"\nDatasets checked: {len(datasets)}"
)

print(
    f"Successful: {successful}"
)

print(
    f"Failed: {failed}"
)

print(
    "\nValidation report:"
)

print(
    report_file
)