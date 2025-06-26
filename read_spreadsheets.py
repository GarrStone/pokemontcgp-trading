import os
import pandas as pd

def read_all_spreadsheets_pandas(folder_name="spreadsheets"):
    """
    Reads data from all CSV and Excel spreadsheet files in a specified folder
    using pandas.

    Args:
        folder_name (str): The name of the folder containing the spreadsheets.
                           This folder should be in the same directory as the script.

    Returns:
        dict: A dictionary where keys are spreadsheet filenames (without extension)
              and values are pandas DataFrames containing the first two columns.
              Returns an empty dictionary if no spreadsheets are found or an error occurs.
    """
    script_dir = os.path.dirname(__file__)
    spreadsheet_folder_path = os.path.join(script_dir, folder_name)
    all_spreadsheet_data = {}

    if not os.path.exists(spreadsheet_folder_path):
        print(f"Error: Folder '{folder_name}' not found in the same directory as the script.")
        return all_spreadsheet_data

    print(f"Searching for spreadsheets in: {spreadsheet_folder_path}")

    for filename in os.listdir(spreadsheet_folder_path):
        file_path = os.path.join(spreadsheet_folder_path, filename)
        spreadsheet_name = os.path.splitext(filename)[0] # Get filename without extension

        try:
            if filename.endswith(".csv"):
                # Read CSV, selecting only the first two columns (0 and 1)
                # usecols can take a list of integer positions or column names
                df = pd.read_csv(file_path, usecols=[0, 1])
                all_spreadsheet_data[spreadsheet_name] = df
                print(f"Successfully read CSV: {filename} into a DataFrame.")
            elif filename.endswith((".xls", ".xlsx")):
                # Read Excel, selecting only the first two columns (0 and 1)
                # If your Excel files have multiple sheets, you might need to specify sheet_name
                # e.g., pd.read_excel(file_path, sheet_name='Sheet1', usecols=[0, 1])
                df = pd.read_excel(file_path, sheet_name='Genetic Apex', usecols=[0, 1])
                all_spreadsheet_data[spreadsheet_name] = df
                print(f"Successfully read Excel: {filename} into a DataFrame.")
            else:
                print(f"Skipping unsupported file type: {filename}")

        except ValueError as ve:
            print(f"Error reading {filename} (check usecols or column count): {ve}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return all_spreadsheet_data

if __name__ == "__main__":
    print("--- Running read_spreadsheet.py directly for demonstration (Pandas version) ---")
    data_frames = read_all_spreadsheets_pandas()
    if data_frames:
        for spreadsheet_name, df in data_frames.items():
            print(f"\nData from '{spreadsheet_name}' (first 5 rows of columns 1 and 2):")
            # Displaying the DataFrame directly is very informative
            print(df.head())
    else:
        print("No data read.")