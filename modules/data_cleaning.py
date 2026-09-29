import pandas as pd


def clean_data(data):
    """
    Clean the employee dataset.

    The function checks and fixes basic data-quality issues.
    """

    print("\n========================================")
    print("            DATA CLEANING")
    print("========================================")

    # Create a copy so the original dataset is not changed
    cleaned_data = data.copy()

    # ----------------------------------------
    # 1. Check and remove duplicate rows
    # ----------------------------------------

    duplicate_count = cleaned_data.duplicated().sum()

    if duplicate_count > 0:

        cleaned_data = cleaned_data.drop_duplicates()

        print(
            "Duplicate rows removed:",
            duplicate_count
        )

    else:

        print("Duplicate rows found: 0")

    # ----------------------------------------
    # 2. Check duplicate Employee IDs
    # ----------------------------------------

    employee_id_duplicates = (
        cleaned_data["Employee_ID"].duplicated().sum()
    )

    if employee_id_duplicates > 0:

        cleaned_data = cleaned_data.drop_duplicates(
            subset="Employee_ID",
            keep="first"
        )

        print(
            "Duplicate Employee IDs removed:",
            employee_id_duplicates
        )

    else:

        print("Duplicate Employee IDs found: 0")

    # ----------------------------------------
    # 3. Convert Hire_Date to date format
    # ----------------------------------------

    cleaned_data["Hire_Date"] = pd.to_datetime(
        cleaned_data["Hire_Date"],
        errors="coerce"
    )

    invalid_dates = cleaned_data["Hire_Date"].isnull().sum()

    print(
        "Invalid dates found:",
        invalid_dates
    )

    # ----------------------------------------
    # 4. Check missing values
    # ----------------------------------------

    missing_values = cleaned_data.isnull().sum().sum()

    print(
        "Missing values after date conversion:",
        missing_values
    )

    # ----------------------------------------
    # 5. Check Age
    # ----------------------------------------

    invalid_age = (
        (cleaned_data["Age"] < 18) |
        (cleaned_data["Age"] > 70)
    ).sum()

    print(
        "Invalid age values:",
        invalid_age
    )

    # ----------------------------------------
    # 6. Check Years at Company
    # ----------------------------------------

    invalid_years = (
        cleaned_data["Years_At_Company"] < 0
    ).sum()

    print(
        "Invalid Years_At_Company values:",
        invalid_years
    )

    # ----------------------------------------
    # 7. Check Monthly Salary
    # ----------------------------------------

    invalid_salary = (
        cleaned_data["Monthly_Salary"] <= 0
    ).sum()

    print(
        "Invalid salary values:",
        invalid_salary
    )

    # ----------------------------------------
    # 8. Check Overtime Hours
    # ----------------------------------------

    invalid_overtime = (
        cleaned_data["Overtime_Hours"] < 0
    ).sum()

    print(
        "Invalid overtime values:",
        invalid_overtime
    )

    # ----------------------------------------
    # 9. Check Performance Score
    # ----------------------------------------

    invalid_performance = (
        (cleaned_data["Performance_Score"] < 1) |
        (cleaned_data["Performance_Score"] > 5)
    ).sum()

    print(
        "Invalid performance scores:",
        invalid_performance
    )

    # ----------------------------------------
    # 10. Check Satisfaction Score
    # ----------------------------------------

    invalid_satisfaction = (
        (cleaned_data["Employee_Satisfaction_Score"] < 1) |
        (cleaned_data["Employee_Satisfaction_Score"] > 5)
    ).sum()

    print(
        "Invalid satisfaction scores:",
        invalid_satisfaction
    )

    # ----------------------------------------
    # 11. Check Resigned column
    # ----------------------------------------

    print(
        "Resigned column type:",
        cleaned_data["Resigned"].dtype
    )

    # ----------------------------------------
    # 12. Display final information
    # ----------------------------------------

    print("\nFinal dataset shape:")
    print(cleaned_data.shape)

    print(
        "\nData cleaning completed successfully."
    )

    return cleaned_data


def save_cleaned_data(data, file_path):
    """
    Save the cleaned dataset as a CSV file.
    """

    data.to_csv(
        file_path,
        index=False
    )

    print(
        "\nCleaned dataset saved to:",
        file_path
    )