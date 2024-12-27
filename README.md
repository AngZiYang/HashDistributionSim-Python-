# Hash Distribution Simulator

This repository contains a Python-based simulation to compute and analyze the hash distributions for two puzzles with varying sub-puzzles and bit configurations. It provides the distribution, average, standard deviation, and visual representation of the data for both puzzles.

---

## Overview

The task involves two puzzles:
1. **Puzzle A**:
   - Parameters: 1 sub-puzzle, k = 6 bits.
   - Total possible outcomes per sub-puzzle: \(2^6 = 64\).

2. **Puzzle B**:
   - Parameters: 6 sub-puzzles, k = 4 bits.
   - Total possible outcomes per sub-puzzle: \(2^4 = 16\).

For both puzzles, we compute:
1. The distribution of the number of cases that require each number of hashes.
2. Average and standard deviation of the required hashes.
3. Graphs representing the hash distribution.

---

## Features

- **Hash Distribution Calculation**: Generates and counts the frequency of total hashes for all possible combinations.
- **Statistical Analysis**: Computes the average and standard deviation for the number of hashes needed.
- **Visualization**: Produces graphs for the hash distributions.
- **Excel Output**: Saves the data and graphs to an Excel file for further analysis.

---

## Methodology

1. **Distribution Calculation**:
   - For Puzzle A: Each outcome represents a single hash; frequency is calculated for all 64 possibilities.
   - For Puzzle B: All combinations of 6 sub-puzzles are summed, and frequencies are computed.

2. **Implementation**:
   - Python is used with libraries such as NumPy, Pandas, and Matplotlib.
   - The `itertools.product` function generates all possible combinations of outcomes.

3. **Graphing**:
   - Line plots are created to visualize the frequency distribution of the hashes.

4. **Excel Output**:
   - Data and graphs are saved to an Excel file with separate sheets for each puzzle.

**How to run**
- python hash_distribution.py
