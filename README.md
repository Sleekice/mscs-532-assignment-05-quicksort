# Assignment 5: Quicksort Algorithm — Implementation, Analysis, and Randomization

**University of the Cumberlands**  
**Course:** MSCS 532 — Algorithms and Data Structures  
**Student:** Peter Nwochie Tiewah  
**Date:** November 15, 2026

## Overview

This project implements, tests, and compares two versions of the Quicksort algorithm using Python:

1. **Deterministic Quicksort:** Selects the first element of each subarray as the pivot.
2. **Randomized Quicksort:** Selects a pivot randomly from the current subarray.

Both implementations use recursive, two-way partitioning to return a sorted list in ascending order without modifying the original input.

The project examines how pivot selection influences execution time, particularly for randomly ordered, sorted, and reverse-sorted input datasets.

## Project Structure

```text
mscs-532-assignment-05-quicksort/
├── src/
│   ├── quicksort.py
│   └── randomized_quicksort.py
├── tests/
│   └── test_quicksort.py
├── results/
│   ├── environment.txt
│   ├── quicksort_benchmark.csv
│   └── quicksort_comparison.png
├── benchmark.py
├── plot_results.py
├── Quicksort_Report.docx
├── report.md
├── README.md
└── .gitignore
```

## Requirements

- Python 3
- Matplotlib (required for generating performance graphs)

**Test environment:** Python 3.15.2 on macOS (ARM64).

Install Matplotlib:

```bash
python3 -m pip install matplotlib
```

The sorting algorithms, benchmark script, and automated tests use Python's standard library.

## Running the Implementations

From the project root, run the deterministic implementation:

```bash
python3 -m src.quicksort
```

Run the randomized implementation:

```bash
python3 -m src.randomized_quicksort
```

Both scripts demonstrate sorting a small list of integers.

## Running Automated Tests

Run the tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

The test suite validates both algorithms using seven input cases:

- Empty lists
- Single-element lists
- Unsorted lists
- Already-sorted lists
- Reverse-sorted lists
- Duplicate values
- Negative values

Correctness is verified by comparing each algorithm's output against Python's built-in `sorted()` function.

The tests also verify that neither implementation modifies the original input list.

## Running Performance Benchmarks

Execute:

```bash
python3 benchmark.py
```

### Experimental Configuration

| Parameter | Configuration |
|---|---|
| Algorithms | Deterministic and randomized Quicksort |
| Input sizes | 100, 250, 500 |
| Input distributions | Random, sorted, reverse-sorted |
| Repetitions | 7 per configuration |
| Performance metric | Median elapsed time (milliseconds) |
| Input generation seed | 42 |
| Timing function | `time.perf_counter()` |

Both algorithms receive equivalent input datasets for each size and distribution.

The timed operation includes creating a copy of the input list before sorting. This overhead is present in both implementations.

Random pivot selections are not separately seeded, so their exact sequence can vary between runs.

The script verifies sorting correctness and saves results to:

`results/quicksort_benchmark.csv`

It also records execution-environment details in:

`results/environment.txt`

### Reproducibility

The fixed seed controls dataset generation, while seven repetitions help reduce the influence of individual timing fluctuations.

However, benchmark results may differ between executions because of randomized pivot choices, system activity, and interpreter overhead.

The committed CSV contains the measured results analyzed in the accompanying report. Rerunning the benchmark may produce different timing values.

## Generating Performance Graphs

Execute:

```bash
python3 plot_results.py
```

This script generates the performance comparison figure using the benchmark CSV.

The output is saved to:

`results/quicksort_comparison.png`

## Key Findings

The benchmark results demonstrate how pivot-selection strategies affect Quicksort performance across different input distributions.

### Observed Results at n = 500

| Distribution | Deterministic (ms) | Randomized (ms) |
|---|---:|---:|
| Random | 0.152375 | 0.267292 |
| Sorted | 1.934333 | 0.242042 |
| Reverse-sorted | 2.076167 | 0.242292 |

These values match the benchmark CSV and the results reported in `Quicksort_Report.docx`.

### Random Input

Deterministic Quicksort performed faster than randomized Quicksort across all three tested input sizes for randomly ordered data.

At n = 500:

- Deterministic: 0.152375 ms
- Randomized: 0.267292 ms

The randomized implementation introduces additional overhead through random pivot generation and index-based partitioning.

### Sorted Input

At n = 500:

- Deterministic: 1.934333 ms
- Randomized: 0.242042 ms

Randomized Quicksort was approximately **7.99 times faster**.

The deterministic first-element pivot produces severely unbalanced partitions for already-sorted inputs.

### Reverse-Sorted Input

At n = 500:

- Deterministic: 2.076167 ms
- Randomized: 0.242292 ms

Randomized Quicksort was approximately **8.57 times faster**.

This result is consistent with the theoretical vulnerability of deterministic first-element pivot selection when processing reverse-sorted inputs.

### Performance Interpretation

Randomized pivot selection reduces the probability of repeatedly selecting pivots that generate highly unbalanced partitions.

However, randomization does not guarantee faster execution for every input or eliminate Quicksort's theoretical worst-case complexity.

The results are specific to the tested implementations and experimental conditions.

## Time and Space Complexity

### Time Complexity

| Case | Complexity | Explanation |
|---|---|---|
| Best | O(n log n) | Pivot selections create approximately balanced partitions |
| Average | O(n log n) | Expected behavior under random input permutations or randomized pivoting |
| Worst | O(n²) | Repeatedly unbalanced partitions |

For randomized Quicksort, the expected running time is O(n log n), even for a fixed input arrangement. Its worst-case running time remains O(n²).

### Space Complexity

Both implementations create additional Python lists instead of partitioning the input in place.

For these particular implementations:

- **Balanced partitions:** O(n) peak auxiliary space.
- **Severely unbalanced partitions:** O(n²) peak auxiliary space.
- **Cumulative allocations during balanced execution:** O(n log n).
- **Recursion depth:** O(log n) when balanced and O(n) when severely unbalanced.

Peak memory usage and cumulative memory allocation are different measures.

These space requirements should not be confused with those of conventional in-place Quicksort implementations.

## Limitations

The experiment has several limitations:

- Only three input sizes (100, 250, and 500) were evaluated.
- Performance measurements are sensitive to system activity and interpreter overhead.
- Random pivot selection adds computational overhead.
- The deterministic and randomized versions have minor implementation differences beyond pivot selection.
- Both implementations allocate additional Python lists instead of sorting in place.
- First-element pivot selection can produce deep recursion on sorted and reverse-sorted inputs.
- Random pivot selections were not separately seeded.
- Peak memory consumption was not measured directly.
- The experiments illustrate theoretical behavior but do not independently establish asymptotic complexity bounds.

## Conclusion

This assignment demonstrates the implementation and empirical analysis of deterministic and randomized Quicksort in Python.

Both algorithms produce correct sorted results for the tested cases.

The observed performance indicates that deterministic first-element pivot selection is particularly vulnerable to presorted input distributions, while randomized pivot selection provides more consistent performance across the tested distributions.

Randomized Quicksort performed substantially better on sorted and reverse-sorted datasets, whereas deterministic Quicksort performed faster on the tested randomly ordered datasets.

These results illustrate the importance of pivot-selection strategies, algorithmic complexity, and experimental methodology when evaluating sorting algorithms.

## Report and Documentation

The complete assignment report is available in two formats:

- **Quicksort_Report.docx** — Formatted academic report containing methodology, analysis, results, and references.
- **report.md** — Markdown version of the report for GitHub viewing.

The report contains the theoretical analysis, benchmark results, performance comparison figure, experimental limitations, and conclusions.

The source code, automated tests, benchmark data, and visualization scripts are included in this repository for instructor review.

## Repository

https://github.com/Sleekice/mscs-532-assignment-05-quicksort

**Course:** MSCS 532 — Algorithms and Data Structures  
**Assignment:** 5 — Quicksort Algorithm: Implementation, Analysis, and Randomization
