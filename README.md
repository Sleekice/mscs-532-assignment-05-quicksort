
# Assignment 5: Quicksort Algorithm

**University of the Cumberlands**  
**Course:** MSCS 532 - Algorithms and Data Structures  
**Student:** Peter Nwochie Tiewah  
**Date:** November 15, 2026

## Overview

This project implements and compares two versions of Quicksort in Python:

1. Deterministic Quicksort using the first element as the pivot.
2. Randomized Quicksort using a randomly selected pivot.

Both algorithms recursively partition the input and return a sorted list.

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
├── report.md
├── README.md
└── .gitignore
```

## Requirements

- Python 3
- Matplotlib (for generating the graph)

Tested with Python 3.15.2 on macOS.

Install Matplotlib:

```bash
python3 -m pip install matplotlib
```

## Running the Implementations

Deterministic Quicksort:

```bash
python3 -m src.quicksort
```

Randomized Quicksort:

```bash
python3 -m src.randomized_quicksort
```

## Running Automated Tests

From the repository root:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover empty lists, single elements, random inputs,
sorted inputs, reverse-sorted inputs, duplicates, and negative values.

## Running Benchmarks

```bash
python3 benchmark.py
```

The experiment compares both algorithms using:

- Input sizes: 100, 250, and 500
- Input distributions: random, sorted, reverse-sorted
- Repetitions: 7
- Reported statistic: median execution time in milliseconds
- Data generation seed: 42

The benchmark saves its results in:

`results/quicksort_benchmark.csv`

## Generating the Graph

```bash
python3 plot_results.py
```

The resulting image is saved as:

`results/quicksort_comparison.png`

## Key Findings

On randomly ordered inputs, deterministic Quicksort performed
faster in the measured experiments.

On sorted and reverse-sorted inputs, randomized Quicksort
performed substantially better.

At n = 500:

| Distribution | Deterministic (ms) | Randomized (ms) |
|---|---:|---:|
| Random | 0.1760 | 0.3133 |
| Sorted | 2.3364 | 0.2533 |
| Reverse | 2.2349 | 0.2347 |

These findings are consistent with the theoretical vulnerability
of first-element pivot selection to unfavorable input ordering.

Randomized pivot selection reduces the likelihood of repeatedly
producing highly unbalanced partitions.

Both implementations use additional lists instead of sorting
in place. Their memory overhead differs from standard
in-place Quicksort implementations.

## Limitations

- Experiments used relatively small datasets.
- Execution times can vary due to system activity.
- Randomized pivot selection adds some overhead.
- The implementations create additional lists.
- First-element pivot selection can cause deep recursion
  on sorted or reverse-sorted inputs.

## Report

See `report.md` for the implementation discussion,
complexity analysis, empirical results, and conclusions.
