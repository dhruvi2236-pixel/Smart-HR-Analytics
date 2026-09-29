# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# CRUD OPERATIONS MODULE
# ============================================================

import os
import pandas as pd


# ============================================================
# CRUD STORAGE FILE
# ============================================================

# This is a separate file used only for CRUD operations.
# The original analytical dataset is NOT modified.

FILE_PATH = "output/hr_employee_records.csv"


# ============================================================
# CREATE
# ============================================================

def create_employee(employee_data):

    os.makedirs("output", exist_ok=True)

    try:

        if os.path.exists(FILE_PATH):
            data = pd.read_csv(FILE_PATH)

        else:
            data = pd.DataFrame(
                columns=[
                    "Employee_ID",
                    "Department",
                    "Job_Title",
                    "Monthly_Salary"
                ]
            )

        # Check whether Employee ID already exists
        if not data.empty:
            if employee_data["Employee_ID"] in data["Employee_ID"].values:
                print("Employee ID already exists.")
                return

        # Add new employee record
        new_employee = pd.DataFrame([employee_data])

        data = pd.concat(
            [data, new_employee],
            ignore_index=True
        )

        # Save the updated data permanently
        data.to_csv(FILE_PATH, index=False)

        print("Employee record created successfully.")
        print("Data saved to:", FILE_PATH)

    except Exception as error:
        print("Error while creating employee record:", error)


# ============================================================
# READ
# ============================================================

def read_employees():

    try:

        if not os.path.exists(FILE_PATH):
            print("CRUD storage file does not exist yet.")
            return

        data = pd.read_csv(FILE_PATH)

        print("\nEmployee Records:")

        if data.empty:
            print("No employee records found.")

        else:
            print(data.to_string(index=False))

    except Exception as error:
        print("Error while reading employee records:", error)


# ============================================================
# UPDATE
# ============================================================

def update_employee(employee_id, updated_data):

    try:

        if not os.path.exists(FILE_PATH):
            print("CRUD storage file does not exist.")
            return

        data = pd.read_csv(FILE_PATH)

        if employee_id not in data["Employee_ID"].values:
            print("Employee ID not found.")
            return

        # Update the requested fields
        for column, value in updated_data.items():

            if column in data.columns:
                data.loc[
                    data["Employee_ID"] == employee_id,
                    column
                ] = value

        # Save the updated data permanently
        data.to_csv(FILE_PATH, index=False)

        print("Employee record updated successfully.")
        print("Updated data saved to:", FILE_PATH)

    except Exception as error:
        print("Error while updating employee record:", error)


# ============================================================
# DELETE
# ============================================================

def delete_employee(employee_id):

    try:

        if not os.path.exists(FILE_PATH):
            print("CRUD storage file does not exist.")
            return

        data = pd.read_csv(FILE_PATH)

        if employee_id not in data["Employee_ID"].values:
            print("Employee ID not found.")
            return

        # Remove the employee record
        data = data[
            data["Employee_ID"] != employee_id
        ]

        # Save the changed data permanently
        data.to_csv(FILE_PATH, index=False)

        print("Employee record deleted successfully.")
        print("Updated data saved to:", FILE_PATH)

    except Exception as error:
        print("Error while deleting employee record:", error)


# ============================================================
# CRUD DEMONSTRATION
# ============================================================

def demonstrate_crud():

    print("\n")
    print("=" * 50)
    print("             CRUD OPERATIONS")
    print("=" * 50)

    # --------------------------------------------------------
    # Explain data storage
    # --------------------------------------------------------

    print("\nORIGINAL ANALYTICAL DATASET")
    print("File:", "dataset/employee_data.csv")
    print("Status: NOT modified by CRUD operations.")

    print("\nCRUD STORAGE FILE")
    print("File:", FILE_PATH)
    print("Purpose: Stores employee records for CRUD operations.")

    print("\nCRUD changes are saved to this separate CSV file.")

    # --------------------------------------------------------
    # Employee record for demonstration
    # --------------------------------------------------------

    employee_id = 100001

    employee_data = {
        "Employee_ID": employee_id,
        "Department": "Engineering",
        "Job_Title": "Software Engineer",
        "Monthly_Salary": 65000
    }

    # --------------------------------------------------------
    # 1. CREATE
    # --------------------------------------------------------

    print("\n1. CREATE")

    create_employee(employee_data)

    # --------------------------------------------------------
    # 2. READ AFTER CREATE
    # --------------------------------------------------------

    print("\n2. READ - AFTER CREATE")

    read_employees()

    # --------------------------------------------------------
    # 3. UPDATE
    # --------------------------------------------------------

    print("\n3. UPDATE")

    updated_data = {
        "Monthly_Salary": 70000
    }

    update_employee(
        employee_id,
        updated_data
    )

    # --------------------------------------------------------
    # 4. READ AFTER UPDATE
    # --------------------------------------------------------

    print("\n4. READ - AFTER UPDATE")

    read_employees()

    # --------------------------------------------------------
    # 5. DELETE
    # --------------------------------------------------------

    print("\n5. DELETE")

    delete_employee(employee_id)

    # --------------------------------------------------------
    # 6. READ AFTER DELETE
    # --------------------------------------------------------

    print("\n6. READ - AFTER DELETE")

    read_employees()

    # --------------------------------------------------------
    # Completion
    # --------------------------------------------------------

    print("\n")
    print("=" * 50)
    print("CRUD DEMONSTRATION COMPLETED")
    print("=" * 50)

    print("\nStorage explanation:")
    print("Original dataset:")
    print("dataset/employee_data.csv")

    print("\nCRUD dataset:")
    print(FILE_PATH)

    print("\nThe original analytical dataset remains unchanged.")