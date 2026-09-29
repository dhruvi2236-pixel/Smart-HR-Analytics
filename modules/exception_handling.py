# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# EXCEPTION HANDLING MODULE
# ============================================================

import pandas as pd


def demonstrate_exception_handling():

    print("\n")
    print("=" * 50)
    print("           EXCEPTION HANDLING")
    print("=" * 50)

    # ========================================================
    # 1. FileNotFoundError
    # ========================================================

    print("\n1. FileNotFoundError")

    try:
        # Deliberately trying to open a file that does not exist
        pd.read_csv("dataset/non_existing_employee_file.csv")

        print("File loaded successfully.")

    except FileNotFoundError:
        print("FileNotFoundError handled successfully.")
        print("The requested employee file was not found.")


    # ========================================================
    # 2. KeyError
    # ========================================================

    print("\n2. KeyError")

    try:
        # Load the actual employee dataset
        data = pd.read_csv("dataset/employee_data.csv")

        # This column does not exist in our dataset
        salary = data["Employee_Salary"]

        print("Column found successfully.")
        print(salary.head())

    except KeyError:
        print("KeyError handled successfully.")
        print("The requested column does not exist in the dataset.")


    # ========================================================
    # 3. ValueError
    # ========================================================

    print("\n3. ValueError")

    try:
        # An employee age should be numeric.
        # This invalid text value cannot be converted to integer.
        age = int("twenty")

        print("Employee age:", age)

    except ValueError:
        print("ValueError handled successfully.")
        print("Invalid value: employee age must be a number.")


    # ========================================================
    # 4. General Exception
    # ========================================================

    print("\n4. General Exception")

    try:
        # Deliberately creating an unexpected runtime error
        result = 100 / 0

        print("Result:", result)

    except Exception as error:
        print("General Exception handled successfully.")
        print("Error:", error)


    # ========================================================
    # Completion Message
    # ========================================================

    print("\n")
    print("=" * 50)
    print("EXCEPTION HANDLING DEMONSTRATION COMPLETED")
    print("=" * 50)