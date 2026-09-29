import pandas as pd


def load_data(file_path):
    """
    Load employee data from a CSV file.
    """

    try:
        data = pd.read_csv(file_path)

        print("Dataset loaded successfully.")
        print("Number of records:", len(data))

        return data

    except FileNotFoundError:
        print("Error: Dataset file not found.")
        return None

    except Exception as error:
        print("Error while loading dataset:", error)
        return None