
"""
University of the Cumberlands
MSCS 532 - Algorithms and Data Structures
Assignment 5: Quicksort Performance Analysis

Student: Peter Nwochie Tiewah
Date: November 15, 2026
"""

import csv
import platform
import random
import statistics
import time
from pathlib import Path

from src.quicksort import quicksort
from src.randomized_quicksort import randomized_quicksort


SIZES = [100, 250, 500]
REPEATS = 7
SEED = 42


def generate_data(size, distribution, rng):
    """Generate reproducible input datasets."""

    if distribution == "random":
        return [rng.randint(0, 100000) for _ in range(size)]

    if distribution == "sorted":
        return list(range(size))

    if distribution == "reverse":
        return list(range(size, 0, -1))

    raise ValueError("Unknown distribution")


def measure(algorithm, numbers):
    """Measure execution time in milliseconds."""

    start = time.perf_counter()
    result = algorithm(numbers.copy())
    elapsed = (time.perf_counter() - start) * 1000

    if result != sorted(numbers):
        raise AssertionError("Sorting result is incorrect")

    return elapsed


def main():
    rng = random.Random(SEED)

    algorithms = {
        "deterministic": quicksort,
        "randomized": randomized_quicksort,
    }

    rows = []

    for size in SIZES:
        for distribution in ("random", "sorted", "reverse"):
            numbers = generate_data(size, distribution, rng)

            for name, algorithm in algorithms.items():
                times = []

                for _ in range(REPEATS):
                    times.append(measure(algorithm, numbers))

                median_ms = statistics.median(times)

                rows.append({
                    "algorithm": name,
                    "size": size,
                    "distribution": distribution,
                    "median_ms": round(median_ms, 6),
                })

                print(
                    f"{name:15} "
                    f"n={size:<5} "
                    f"{distribution:8} "
                    f"{median_ms:.4f} ms"
                )

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    with (results_dir / "quicksort_benchmark.csv").open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    environment = (
        f"Python: {platform.python_version()}\n"
        f"Platform: {platform.platform()}\n"
        f"Sizes: {SIZES}\n"
        f"Repeats: {REPEATS}\n"
        f"Data seed: {SEED}\n"
    )

    (results_dir / "environment.txt").write_text(
        environment, encoding="utf-8"
    )

    print("\nBenchmark completed successfully.")


if __name__ == "__main__":
    main()
