import pandas as pd


def preprocess_data(data):
    """
    Prepare the cleaned employee data for analysis
    and machine learning.
    """

    print("\n========================================")
    print("         DATA PREPROCESSING")
    print("========================================")

    # Create a copy so the cleaned dataset is not changed
    processed_data = data.copy()

    # ----------------------------------------
    # 1. Convert Resigned into 0 and 1
    # ----------------------------------------

    processed_data["Resigned_Flag"] = (
        processed_data["Resigned"].astype(int)
    )

    print("\nResigned_Flag created.")

    # ----------------------------------------
    # 2. Create Overtime categories
    # ----------------------------------------

    processed_data["Overtime_Level"] = pd.cut(
        processed_data["Overtime_Hours"],
        bins=[
            -1,
            0,
            5,
            10,
            20,
            float("inf")
        ],
        labels=[
            "No Overtime",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]
    )

    print("Overtime_Level created.")

    # ----------------------------------------
    # 3. Display new columns
    # ----------------------------------------

    print("\nNew columns added:")

    print("- Resigned_Flag")
    print("- Overtime_Level")

    # ----------------------------------------
    # 4. Display sample
    # ----------------------------------------

    print("\nProcessed Data Sample:")

    print(
        processed_data[
            [
                "Employee_ID",
                "Monthly_Salary",
                "Overtime_Hours",
                "Overtime_Level",
                "Resigned",
                "Resigned_Flag"
            ]
        ].head()
    )

    print("\nData preprocessing completed successfully.")

    return processed_data