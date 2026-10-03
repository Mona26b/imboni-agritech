from pathlib import Path
import pandas as pd
import re


# ============================================================
# IMBONI AGRITECH
# NISR SEASON B 2026
# EXPLICIT DATA CLEANING PIPELINE
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "Tables_2026 Season B.xlsx"

PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================================
# 1. CHECK FILE
# ============================================================

if not RAW_FILE.exists():

    raise FileNotFoundError(
        f"""
Dataset not found.

Expected:
{RAW_FILE}
"""
    )


PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. TABLE CONFIGURATION
# ============================================================
#
# Each table has a known header row.
#
# The number is the Excel sheet number.
# header_row is the zero-based row used as the header.
#
# ============================================================

TABLES = {

    7: {
        "name": "agricultural_land",
        "header_row": 1
    },

    8: {
        "name": "agricultural_practices",
        "header_row": 2
    },

    9: {
        "name": "cultivated_area",
        "header_row": 1
    },

    10: {
        "name": "harvested_area",
        "header_row": 1
    },

    11: {
        "name": "average_yield",
        "header_row": 1
    },

    12: {
        "name": "large_scale_farmer_yield",
        "header_row": 1
    },

    13: {
        "name": "crop_production",
        "header_row": 2
    },

    14: {
        "name": "production_use",
        "header_row": 2
    },

    15: {
        "name": "cropping_system",
        "header_row": 3
    },

    16: {
        "name": "sowing_dates_district",
        "header_row": 2
    },

    17: {
        "name": "sowing_dates_crop",
        "header_row": 2
    },

    18: {
        "name": "improved_seed_use",
        "header_row": 3
    },

    19: {
        "name": "seed_type",
        "header_row": 2
    },

    20: {
        "name": "improved_seed_sources",
        "header_row": 2
    },

    21: {
        "name": "seed_sources_crop",
        "header_row": 2
    },

    22: {
        "name": "organic_fertilizer",
        "header_row": 3
    },

    23: {
        "name": "inorganic_fertilizer",
        "header_row": 3
    },

    24: {
        "name": "inorganic_fertilizer_sources",
        "header_row": 2
    },

    25: {
        "name": "fertilizer_types",
        "header_row": 2
    },

    26: {
        "name": "fertilizer_types_district",
        "header_row": 2
    },

    27: {
        "name": "pesticide_use",
        "header_row": 3
    },

    28: {
        "name": "pesticide_types",
        "header_row": 2
    },

    29: {
        "name": "agricultural_practice_rates",
        "header_row": 2
    },

    30: {
        "name": "irrigation_types",
        "header_row": 2
    },

    31: {
        "name": "water_sources",
        "header_row": 2
    },

    32: {
        "name": "erosion_control",
        "header_row": 3
    },

    33: {
        "name": "erosion_degree",
        "header_row": 2
    }
}


# ============================================================
# 3. CLEAN COLUMN NAME
# ============================================================

def clean_column_name(column):

    if pd.isna(column):

        column = "unknown"

    column = str(column).strip()

    column = column.replace(
        "\n",
        " "
    )

    column = re.sub(
        r"\s+",
        " ",
        column
    )

    column = column.replace(
        "/",
        "_"
    )

    column = column.replace(
        "%",
        "percent"
    )

    column = column.replace(
        "(",
        ""
    )

    column = column.replace(
        ")",
        ""
    )

    column = column.replace(
        ",",
        ""
    )

    column = column.replace(
        " ",
        "_"
    )

    return column.lower()


# ============================================================
# 4. MAKE COLUMN NAMES UNIQUE
# ============================================================

def make_unique_columns(columns):

    new_columns = []

    counts = {}

    for column in columns:

        column = clean_column_name(
            column
        )

        if column not in counts:

            counts[column] = 0

            new_columns.append(
                column
            )

        else:

            counts[column] += 1

            new_columns.append(
                f"{column}_{counts[column]}"
            )

    return new_columns


# ============================================================
# 5. CLEAN DISTRICT VALUES
# ============================================================

def clean_district(value):

    if pd.isna(value):

        return value

    value = str(value).strip()

    value = re.sub(
        r"\s+",
        " ",
        value
    )

    return value


# ============================================================
# 6. CONVERT NUMERIC DATA
# ============================================================

def convert_numeric_data(df):

    for column in df.columns:

        column_lower = column.lower()

        # Keep text fields as text
        if any(
            word in column_lower
            for word in [
                "district",
                "crop",
                "name",
                "source",
                "type",
                "stratum"
            ]
        ):

            continue

        # Replace common non-numeric symbols
        df[column] = (
            df[column]
            .replace(
                "-",
                pd.NA
            )
        )

        # Convert numeric-looking values
        converted = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        # Only replace if there are numeric values
        if converted.notna().sum() > 0:

            df[column] = converted

    return df


# ============================================================
# 7. REMOVE EMPTY DATA
# ============================================================

def clean_dataframe(df):

    # Remove completely empty rows
    df = df.dropna(
        how="all"
    )

    # Remove completely empty columns
    df = df.dropna(
        axis=1,
        how="all"
    )

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(
        drop=True
    )

    return df


# ============================================================
# 8. LOAD WORKBOOK
# ============================================================

print("\n")

print("=" * 75)

print(
    "                 IMBONI AGRITECH"
)

print(
    "           NISR SEASON B 2026"
)

print(
    "          EXPLICIT DATA CLEANING"
)

print("=" * 75)


excel_file = pd.ExcelFile(
    RAW_FILE
)


print(
    f"\nWorkbook:"
)

print(
    RAW_FILE.name
)


print(
    f"\nTotal sheets:"
)

print(
    len(excel_file.sheet_names)
)


# ============================================================
# 9. PROCESS TABLES
# ============================================================

successful = []

failed = []


for table_number, config in TABLES.items():

    table_name = config["name"]

    header_row = config["header_row"]

    sheet_name = excel_file.sheet_names[
        table_number - 1
    ]

    print("\n")

    print(
        "-" * 75
    )

    print(
        f"TABLE {table_number}: {sheet_name}"
    )

    print(
        f"Header row: {header_row}"
    )

    try:

        # ----------------------------------------------------
        # READ SHEET
        # ----------------------------------------------------

        df = pd.read_excel(
            RAW_FILE,
            sheet_name=sheet_name,
            header=header_row
        )


        # ----------------------------------------------------
        # CLEAN STRUCTURE
        # ----------------------------------------------------

        df = clean_dataframe(
            df
        )


        # ----------------------------------------------------
        # MAKE COLUMN NAMES UNIQUE
        # ----------------------------------------------------

        df.columns = make_unique_columns(
            df.columns
        )


        # ----------------------------------------------------
        # CLEAN DISTRICT COLUMNS
        # ----------------------------------------------------

        for column in df.columns:

            if "district" in column:

                df[column] = df[column].apply(
                    clean_district
                )


        # ----------------------------------------------------
        # CONVERT NUMBERS
        # ----------------------------------------------------

        df = convert_numeric_data(
            df
        )


        # ----------------------------------------------------
        # SAVE FILE
        # ----------------------------------------------------

        output_file = (
            PROCESSED_DIR
            / f"{table_name}.csv"
        )


        df.to_csv(
            output_file,
            index=False,
            encoding="utf-8-sig"
        )


        successful.append(
            table_number
        )


        print(
            f"SUCCESS: {output_file.name}"
        )

        print(
            f"Rows: {df.shape[0]}"
        )

        print(
            f"Columns: {df.shape[1]}"
        )


    except Exception as error:

        failed.append(
            table_number
        )

        print(
            f"ERROR processing Table {table_number}"
        )

        print(
            str(error)
        )


# ============================================================
# 10. CREATE REPORT
# ============================================================

report_file = (
    PROCESSED_DIR
    / "cleaning_report.txt"
)


report_lines = []


report_lines.append(
    "IMBONI AGRITECH"
)

report_lines.append(
    "NISR SEASON B 2026"
)

report_lines.append(
    "DATA CLEANING REPORT"
)

report_lines.append(
    "=" * 60
)

report_lines.append(
    f"Total configured tables: {len(TABLES)}"
)

report_lines.append(
    f"Successful tables: {len(successful)}"
)

report_lines.append(
    f"Failed tables: {len(failed)}"
)

report_lines.append("")


report_lines.append(
    "Successful tables:"
)


for table_number in successful:

    report_lines.append(
        f"Table {table_number}"
    )


report_lines.append("")


report_lines.append(
    "Failed tables:"
)


if failed:

    for table_number in failed:

        report_lines.append(
            f"Table {table_number}"
        )

else:

    report_lines.append(
        "None"
    )


report_file.write_text(
    "\n".join(
        report_lines
    ),
    encoding="utf-8"
)


# ============================================================
# 11. FINAL RESULT
# ============================================================

print("\n")

print(
    "=" * 75
)

print(
    "             CLEANING FINISHED"
)

print(
    "=" * 75
)


print(
    f"\nSuccessful: {len(successful)}"
)

print(
    f"Failed: {len(failed)}"
)


if failed:

    print(
        f"\nFailed tables: {failed}"
    )

else:

    print(
        "\nALL TABLES PROCESSED SUCCESSFULLY."
    )


print(
    "\nClean files are located at:"
)

print(
    PROCESSED_DIR
)


print(
    "\nReport:"
)

print(
    report_file
)


print(
    "\nOriginal Excel file was NOT modified."
)