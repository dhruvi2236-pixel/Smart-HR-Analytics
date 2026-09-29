def explore_data(data):
    """
    Explore the employee dataset.

    This function displays basic information about
    the structure and contents of the dataset.
    """

    print("\n========================================")
    print("          DATA EXPLORATION")
    print("========================================")

    # 1. Dataset size
    print("\n1. Dataset Shape")
    print("Rows:", data.shape[0])
    print("Columns:", data.shape[1])

    # 2. Column names
    print("\n2. Column Names")

    for column in data.columns:
        print("-", column)

    # 3. First five records
    print("\n3. First Five Records")
    print(data.head())

    # 4. Data types
    print("\n4. Data Types")
    print(data.dtypes)

    # 5. Missing values
    print("\n5. Missing Values")

    missing_values = data.isnull().sum()

    print(missing_values)

    # 6. Duplicate records
    print("\n6. Duplicate Records")

    duplicate_count = data.duplicated().sum()

    print("Number of duplicate rows:", duplicate_count)

    # 7. Resignation distribution
    print("\n7. Resignation Distribution")

    resignation_count = data["Resigned"].value_counts()

    print(resignation_count)

    # 8. Percentage of employees who resigned
    print("\n8. Resignation Percentage")

    resignation_percentage = (
        data["Resigned"].value_counts(normalize=True) * 100
    )

    print(resignation_percentage.round(2))

    # 9. Numerical summary
    print("\n9. Numerical Data Summary")

    print(
        data.describe().round(2)
    )

    print("\n========================================")
    print("       DATA EXPLORATION COMPLETED")
    print("========================================")