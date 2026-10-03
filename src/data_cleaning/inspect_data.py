from pathlib import Path
import pandas as pd


# ============================================================
# IMBONI AGRITECH
# NISR SEASON B 2026 DATA INSPECTION
# ============================================================

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parents[2]

# Location of the raw Excel dataset
file_path = BASE_DIR / "data" / "raw" / "Tables_2026 Season B.xlsx"


# ------------------------------------------------------------
# 1. CHECK THAT THE DATASET EXISTS
# ------------------------------------------------------------

if not file_path.exists():
    raise FileNotFoundError(
        f"\nDataset not found!\nExpected location:\n{file_path}"
    )


# ------------------------------------------------------------
# 2. OPEN THE EXCEL WORKBOOK
# ------------------------------------------------------------

excel_file = pd.ExcelFile(file_path)

print("\n")
print("=" * 75)
print("              IMBONI AGRITECH")
print("          NISR SEASON B 2026 DATA")
print("=" * 75)

print(f"\nDataset: {file_path.name}")
print(f"Total tables found: {len(excel_file.sheet_names)}")


# ------------------------------------------------------------
# 3. INSPECT EVERY TABLE
# ------------------------------------------------------------

for number, sheet in enumerate(excel_file.sheet_names, start=1):

    print("\n")
    print("=" * 75)
    print(f"TABLE {number}: {sheet}")
    print("=" * 75)

    try:

        # Read the table WITHOUT assuming the first row is a header
        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=None
        )

        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        # ----------------------------------------------------
        # SHOW FIRST 8 ROWS
        # ----------------------------------------------------

        print("\nFirst 8 rows:")
        print("-" * 75)

        print(
            df.head(8).to_string(
                index=True,
                header=False
            )
        )

    except Exception as error:

        print("\nERROR while reading this table:")
        print(error)


# ------------------------------------------------------------
# 4. FINISHED
# ------------------------------------------------------------

print("\n")
print("=" * 75)
print("              INSPECTION COMPLETE")
print("=" * 75)

print("\nAll tables have been inspected.")
print("The raw Excel file has NOT been changed.")
print("\nNext step: identify the useful tables and clean them.")