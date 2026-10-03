from pathlib import Path
import pandas as pd


# ============================================================
# IMBONI AGRITECH
# NISR SEASON B 2026
# AUTOMATIC TABLE SUMMARY
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

file_path = BASE_DIR / "data" / "raw" / "Tables_2026 Season B.xlsx"

output_file = BASE_DIR / "data" / "processed" / "table_summary.txt"


# ------------------------------------------------------------
# CHECK DATASET
# ------------------------------------------------------------

if not file_path.exists():
    raise FileNotFoundError(
        f"Dataset not found:\n{file_path}"
    )


# ------------------------------------------------------------
# OPEN WORKBOOK
# ------------------------------------------------------------

excel_file = pd.ExcelFile(file_path)

print("\n" + "=" * 70)
print("              IMBONI AGRITECH")
print("          NISR SEASON B 2026")
print("              TABLE SUMMARY")
print("=" * 70)

print(f"\nWorkbook: {file_path.name}")
print(f"Total tables: {len(excel_file.sheet_names)}")


# ------------------------------------------------------------
# CREATE OUTPUT FOLDER
# ------------------------------------------------------------

output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)


# ------------------------------------------------------------
# BUILD SUMMARY
# ------------------------------------------------------------

summary_lines = []

summary_lines.append(
    "IMBONI AGRITECH - NISR SEASON B 2026 TABLE SUMMARY"
)

summary_lines.append(
    f"Total tables: {len(excel_file.sheet_names)}"
)

summary_lines.append("")


for number, sheet in enumerate(
    excel_file.sheet_names,
    start=1
):

    print("\n" + "-" * 70)
    print(f"TABLE {number}: {sheet}")
    print("-" * 70)

    try:

        # Read without assuming headers
        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=None
        )

        rows = df.shape[0]
        columns = df.shape[1]

        print(f"Rows: {rows}")
        print(f"Columns: {columns}")

        summary_lines.append(
            f"TABLE {number}: {sheet} | "
            f"Rows: {rows} | Columns: {columns}"
        )

        # ----------------------------------------------------
        # Find rows containing useful text
        # ----------------------------------------------------

        useful_rows = []

        for index, row in df.iterrows():

            values = []

            for value in row:

                if pd.notna(value):

                    text = str(value).strip()

                    if text:
                        values.append(text)

            if values:

                row_text = " | ".join(values)

                useful_rows.append(
                    f"Row {index}: {row_text}"
                )

        # Show first 6 non-empty rows
        for row_text in useful_rows[:6]:

            print(row_text)

            summary_lines.append(
                "    " + row_text
            )

        summary_lines.append("")


    except Exception as error:

        print(f"ERROR: {error}")

        summary_lines.append(
            f"ERROR reading {sheet}: {error}"
        )


# ------------------------------------------------------------
# SAVE SUMMARY
# ------------------------------------------------------------

output_file.write_text(
    "\n".join(summary_lines),
    encoding="utf-8"
)


# ------------------------------------------------------------
# FINISHED
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("SUMMARY COMPLETE")
print("=" * 70)

print(f"\nSummary saved to:")
print(output_file)

print("\nThe original Excel file was NOT modified.")