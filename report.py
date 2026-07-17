"""
report.py
Handles saving scan results to TXT and CSV files.
"""

import csv
import os
from datetime import datetime


def save_results(results):
    """
    Save scan results to TXT and CSV files.
    """

    # Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    txt_file = os.path.join(
        "results",
        f"scan_{timestamp}.txt"
    )

    csv_file = os.path.join(
        "results",
        f"scan_{timestamp}.csv"
    )

    save_txt(txt_file, results)
    save_csv(csv_file, results)

    print("\nReports Saved")
    print(f"TXT : {txt_file}")
    print(f"CSV : {csv_file}")


def save_txt(filename, results):
    """
    Save results as a formatted text report.
    """

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("Python Port Scanner Report\n")
        file.write("=" * 60 + "\n\n")

        if not results:
            file.write("No open ports were found.\n")
            return

        for result in sorted(results, key=lambda x: x["Port"]):

            file.write(f"Port    : {result['Port']}\n")
            file.write(f"Service : {result['Service']}\n")
            file.write(f"Banner  : {result['Banner']}\n")
            file.write("-" * 60 + "\n")


def save_csv(filename, results):
    """
    Save results as CSV.
    """

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Port",
                "Service",
                "Banner"
            ]
        )

        writer.writeheader()

        for result in sorted(results, key=lambda x: x["Port"]):
            writer.writerow(result)