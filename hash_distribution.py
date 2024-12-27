# Importing necessary libraries

import numpy as np  # For numerical computations, including arrays and statistical calculations
import pandas as pd  # For handling and analyzing tabular data
import matplotlib.pyplot as plt  # For creating plots and visualizations
import io  # For in-memory file handling, such as saving images or data temporarily
from itertools import product  # For generating Cartesian products of iterables, used here for all possible combinations
import xlsxwriter  # For creating and writing to Excel files


# Function to generate hash distribution based on all possible combinations
def generate_hash_distribution(sub_puzzles, bits):
    # Calculate the total possible outcomes for each sub-puzzle
    outcomes_per_puzzle = 2 ** bits

    # Generate all possible combinations for the given number of sub-puzzles
    combinations = product(range(1, outcomes_per_puzzle + 1), repeat=sub_puzzles)

    # Sum the combinations to get total hashes and count frequencies
    hash_totals = np.array([sum(comb) for comb in combinations])
    unique, counts = np.unique(hash_totals, return_counts=True)

    # Create a dictionary for hash totals and their frequencies
    distribution_dict = dict(zip(unique, counts))

    return distribution_dict, hash_totals

# Calculate distributions and hash totals for Puzzle A and Puzzle B
puzzle_a_distribution, puzzle_a_hash_totals = generate_hash_distribution(1, 6)
puzzle_b_distribution, puzzle_b_hash_totals = generate_hash_distribution(6, 4)

# Calculate average and standard deviation for Puzzle A and Puzzle B
average_a = np.mean(puzzle_a_hash_totals)
std_dev_a = np.std(puzzle_a_hash_totals)
average_b = np.mean(puzzle_b_hash_totals)
std_dev_b = np.std(puzzle_b_hash_totals)

# Convert the puzzle distributions to DataFrames for saving to Excel
puzzle_a_df = pd.DataFrame(list(puzzle_a_distribution.items()), columns=["Hashes Needed", "Frequency"])
puzzle_b_df = pd.DataFrame(list(puzzle_b_distribution.items()), columns=["Hashes Needed", "Frequency"])

# Path for the Excel file
excel_path = r'C:\Users\ang_z\Desktop\SIM\CSCI262\A2_AngZiYang_7768436\Q1Graph.xlsx'

# Save data and graphs to an Excel file
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    # Write Puzzle A and Puzzle B data
    puzzle_a_df.to_excel(writer, sheet_name='Puzzle A', index=False)
    puzzle_b_df.to_excel(writer, sheet_name='Puzzle B', index=False)

    # Access the workbook and sheets
    workbook = writer.book
    worksheet_a = writer.sheets['Puzzle A']
    worksheet_b = writer.sheets['Puzzle B']

    # Add average and standard deviation for Puzzle A
    worksheet_a.write('D1', 'Average Hashes')
    worksheet_a.write('D2', average_a)
    worksheet_a.write('E1', 'Standard Deviation')
    worksheet_a.write('E2', std_dev_a)

    # Add average and standard deviation for Puzzle B
    worksheet_b.write('D1', 'Average Hashes')
    worksheet_b.write('D2', average_b)
    worksheet_b.write('E1', 'Standard Deviation')
    worksheet_b.write('E2', std_dev_b)

    # Plotting and saving Puzzle A chart to a BytesIO buffer
    image_buffer_a = io.BytesIO()
    plt.figure()
    plt.plot(puzzle_a_df['Hashes Needed'], puzzle_a_df['Frequency'], color='b')
    plt.title("Hash Distribution for Puzzle A")
    plt.xlabel('Hashes Needed')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(image_buffer_a, format='png')
    plt.close()
    image_buffer_a.seek(0)

    # Plotting and saving Puzzle B chart to a BytesIO buffer
    image_buffer_b = io.BytesIO()
    plt.figure()
    plt.plot(puzzle_b_df['Hashes Needed'], puzzle_b_df['Frequency'], color='r')
    plt.title("Hash Distribution for Puzzle B")
    plt.xlabel('Hashes Needed')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(image_buffer_b, format='png')
    plt.close()
    image_buffer_b.seek(0)

    # Insert the images into the Excel sheets
    worksheet_a.insert_image('G5', 'image.png', {'image_data': image_buffer_a})
    worksheet_b.insert_image('G5', 'image.png', {'image_data': image_buffer_b})

print("Data and plots for both puzzles have been saved successfully in Q1Graph.xlsx.")
