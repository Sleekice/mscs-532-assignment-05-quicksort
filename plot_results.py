
"""
University of the Cumberlands
MSCS 532 - Algorithms and Data Structures
Assignment 5: Quicksort Performance Visualization

Student: Peter Nwochie Tiewah
Date: November 15, 2026
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


RESULTS_DIR = Path("results")
CSV_FILE = RESULTS_DIR / "quicksort_benchmark.csv"
OUTPUT_FILE = RESULTS_DIR / "quicksort_comparison.png"


def main():
    with CSV_FILE.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    distributions = ["random", "sorted", "reverse"]

    for ax, distribution in zip(axes, distributions):
        for algorithm in ["deterministic", "randomized"]:
            selected = [
                row for row in rows
                if row["distribution"] == distribution
                and row["algorithm"] == algorithm
            ]

            selected.sort(key=lambda row: int(row["size"]))

            sizes = [int(row["size"]) for row in selected]
            times = [float(row["median_ms"]) for row in selected]

            ax.plot(
                sizes,
                times,
                marker="o",
                label=algorithm.capitalize()
            )

        ax.set_title(f"{distribution.capitalize()} Input")
        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Median Execution Time (ms)")
        ax.grid(True, alpha=0.3)
        ax.legend()

    fig.suptitle("Deterministic vs. Randomized Quicksort")
    fig.tight_layout()

    fig.savefig(OUTPUT_FILE, dpi=300)
    plt.close(fig)

    print(f"Graph saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
