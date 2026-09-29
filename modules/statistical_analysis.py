import numpy as np


def perform_statistical_analysis(data):
    """
    Perform basic statistical analysis on employee data.
    """

    print("\n========================================")
    print("         STATISTICAL ANALYSIS")
    print("========================================")

    # ----------------------------------------
    # Numerical columns for analysis
    # ----------------------------------------

    columns = [
        "Age",
        "Monthly_Salary",
        "Years_At_Company",
        "Work_Hours_Per_Week",
        "Overtime_Hours",
        "Training_Hours",
        "Promotions",
        "Employee_Satisfaction_Score"
    ]

    # ----------------------------------------
    # 1. Mean
    # ----------------------------------------

    print("\n1. Mean")

    mean_values = data[columns].mean()

    print(
        mean_values.round(2)
    )

    # ----------------------------------------
    # 2. Median
    # ----------------------------------------

    print("\n2. Median")

    median_values = data[columns].median()

    print(
        median_values.round(2)
    )

    # ----------------------------------------
    # 3. Standard Deviation
    # ----------------------------------------

    print("\n3. Standard Deviation")

    standard_deviation = data[columns].std()

    print(
        standard_deviation.round(2)
    )

    # ----------------------------------------
    # 4. Minimum
    # ----------------------------------------

    print("\n4. Minimum Values")

    minimum_values = data[columns].min()

    print(
        minimum_values.round(2)
    )

    # ----------------------------------------
    # 5. Maximum
    # ----------------------------------------

    print("\n5. Maximum Values")

    maximum_values = data[columns].max()

    print(
        maximum_values.round(2)
    )

    # ----------------------------------------
    # 6. NumPy calculation
    # ----------------------------------------

    print("\n6. NumPy Calculation")

    salary_array = data[
        "Monthly_Salary"
    ].to_numpy()

    numpy_mean_salary = np.mean(
        salary_array
    )

    numpy_standard_deviation = np.std(
        salary_array
    )

    print(
        "Average Monthly Salary:",
        round(
            numpy_mean_salary,
            2
        )
    )

    print(
        "Salary Standard Deviation:",
        round(
            numpy_standard_deviation,
            2
        )
    )

    # ----------------------------------------
    # 7. Correlation with resignation
    # ----------------------------------------

    print(
        "\n7. Correlation with Resignation"
    )

    correlation_columns = [
        "Age",
        "Monthly_Salary",
        "Years_At_Company",
        "Work_Hours_Per_Week",
        "Overtime_Hours",
        "Training_Hours",
        "Promotions",
        "Employee_Satisfaction_Score",
        "Resigned_Flag"
    ]

    correlation = (
        data[correlation_columns]
        .corr()["Resigned_Flag"]
        .drop("Resigned_Flag")
        .sort_values()
    )

    print(
        correlation.round(3)
    )

    print("\n========================================")
    print("     STATISTICAL ANALYSIS COMPLETED")
    print("========================================")