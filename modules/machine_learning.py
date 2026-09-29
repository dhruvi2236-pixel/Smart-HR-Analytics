# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# MACHINE LEARNING MODULE
# ============================================================

import os

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# MACHINE LEARNING FUNCTION
# ============================================================

def perform_machine_learning(data):
    """
    Train and evaluate a Logistic Regression model
    for employee resignation prediction.
    """

    print("\n")
    print("========================================")
    print("         MACHINE LEARNING")
    print("========================================")


    # ========================================================
    # 1. COPY DATA
    # ========================================================

    ml_data = data.copy()


    # ========================================================
    # 2. CHECK TARGET COLUMN
    # ========================================================

    if "Resigned_Flag" not in ml_data.columns:

        print(
            "ERROR: Resigned_Flag column is missing."
        )

        return None


    # ========================================================
    # 3. SELECT INPUT FEATURES
    # ========================================================

    features = [
        "Department",
        "Gender",
        "Age",
        "Years_At_Company",
        "Education_Level",
        "Performance_Score",
        "Monthly_Salary",
        "Work_Hours_Per_Week",
        "Projects_Handled",
        "Overtime_Hours",
        "Sick_Days",
        "Remote_Work_Frequency",
        "Team_Size",
        "Training_Hours",
        "Promotions",
        "Employee_Satisfaction_Score"
    ]


    target = "Resigned_Flag"


    # ========================================================
    # 4. CHECK REQUIRED FEATURES
    # ========================================================

    missing_features = [
        column
        for column in features
        if column not in ml_data.columns
    ]


    if missing_features:

        print(
            "\nERROR: Required features are missing:"
        )

        for column in missing_features:

            print(
                f"- {column}"
            )

        return None


    # ========================================================
    # 5. CREATE INPUT DATA AND TARGET DATA
    # ========================================================

    X = ml_data[features]

    y = ml_data[target]


    print("\n1. Features selected:")

    for feature in features:

        print(
            f"- {feature}"
        )


    print(
        f"\nNumber of input features: {len(features)}"
    )


    print(
        "\nTarget variable: Resigned_Flag"
    )


    # ========================================================
    # 6. DEFINE CATEGORICAL FEATURES
    # ========================================================

    categorical_features = [
        "Department",
        "Gender",
        "Education_Level"
    ]


    # ========================================================
    # 7. DEFINE NUMERICAL FEATURES
    # ========================================================

    numerical_features = [
        "Age",
        "Years_At_Company",
        "Performance_Score",
        "Monthly_Salary",
        "Work_Hours_Per_Week",
        "Projects_Handled",
        "Overtime_Hours",
        "Sick_Days",
        "Remote_Work_Frequency",
        "Team_Size",
        "Training_Hours",
        "Promotions",
        "Employee_Satisfaction_Score"
    ]


    # ========================================================
    # 8. DATA PREPROCESSING FOR MACHINE LEARNING
    # ========================================================

    print(
        "\n2. Preparing data for machine learning..."
    )


    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_features
            ),

            (
                "numerical",
                StandardScaler(),
                numerical_features
            )
        ]
    )


    # ========================================================
    # 9. LOGISTIC REGRESSION MODEL
    # ========================================================

    model = LogisticRegression(
        solver="lbfgs",
        max_iter=2000,
        class_weight="balanced"
    )


    # ========================================================
    # 10. CREATE MACHINE LEARNING PIPELINE
    # ========================================================

    machine_learning_pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",
                model
            )
        ]
    )


    # ========================================================
    # 11. TRAIN-TEST SPLIT
    # ========================================================

    print(
        "\n3. Splitting dataset into training and testing data..."
    )


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


    print(
        f"Training records: {len(X_train):,}"
    )


    print(
        f"Testing records: {len(X_test):,}"
    )


    print(
        "Training percentage: 80%"
    )


    print(
        "Testing percentage : 20%"
    )


    # ========================================================
    # 12. TRAIN THE MODEL
    # ========================================================

    print(
        "\n4. Training Logistic Regression model..."
    )


    machine_learning_pipeline.fit(
        X_train,
        y_train
    )


    print(
        "Model training completed successfully."
    )


    # ========================================================
    # 13. PREDICT TEST DATA
    # ========================================================

    print(
        "\n5. Predicting resignation on unseen test data..."
    )


    y_prediction = (
        machine_learning_pipeline.predict(
            X_test
        )
    )


    print(
        "Prediction completed successfully."
    )


    # ========================================================
    # 14. CALCULATE ACCURACY
    # ========================================================

    accuracy = accuracy_score(
        y_test,
        y_prediction
    )


    # ========================================================
    # 15. CALCULATE PRECISION
    # ========================================================

    precision = precision_score(
        y_test,
        y_prediction,
        zero_division=0
    )


    # ========================================================
    # 16. CALCULATE RECALL
    # ========================================================

    recall = recall_score(
        y_test,
        y_prediction,
        zero_division=0
    )


    # ========================================================
    # 17. CALCULATE F1 SCORE
    # ========================================================

    f1 = f1_score(
        y_test,
        y_prediction,
        zero_division=0
    )


    # ========================================================
    # 18. DISPLAY MODEL PERFORMANCE
    # ========================================================

    print("\n")
    print("========================================")
    print("         MODEL PERFORMANCE")
    print("========================================")


    print(
        f"\nAccuracy : {accuracy * 100:.2f}%"
    )


    print(
        f"Precision: {precision * 100:.2f}%"
    )


    print(
        f"Recall   : {recall * 100:.2f}%"
    )


    print(
        f"F1-Score : {f1 * 100:.2f}%"
    )


    # ========================================================
    # 19. CLASSIFICATION REPORT
    # ========================================================

    print(
        "\n6. CLASSIFICATION REPORT"
    )


    report = classification_report(
        y_test,
        y_prediction,
        target_names=[
            "Not Resigned",
            "Resigned"
        ],
        zero_division=0
    )


    print(report)


    # ========================================================
    # 20. CONFUSION MATRIX
    # ========================================================

    matrix = confusion_matrix(
        y_test,
        y_prediction
    )


    print(
        "\n7. CONFUSION MATRIX"
    )


    print(matrix)


    # ========================================================
    # 21. EXPLAIN CONFUSION MATRIX
    # ========================================================

    print(
        "\nConfusion Matrix Interpretation:"
    )


    print(
        "True Negative  : Correctly predicted Not Resigned"
    )


    print(
        "False Positive : Predicted Resigned, "
        "but employee did not resign"
    )


    print(
        "False Negative : Predicted Not Resigned, "
        "but employee resigned"
    )


    print(
        "True Positive  : Correctly predicted Resigned"
    )


    # ========================================================
    # 22. SAVE PREDICTIONS
    # ========================================================

    os.makedirs(
        "output",
        exist_ok=True
    )


    prediction_data = X_test.copy()


    prediction_data[
        "Actual_Resignation"
    ] = y_test.to_numpy()


    prediction_data[
        "Predicted_Resignation"
    ] = y_prediction


    prediction_file = (
        "output/ml_predictions.csv"
    )


    prediction_data.to_csv(
        prediction_file,
        index=False
    )


    print(
        f"\nPrediction results saved to: "
        f"{prediction_file}"
    )


    # ========================================================
    # 23. RETURN RESULTS TO MAIN.PY
    # ========================================================

    results = {
        "model": machine_learning_pipeline,

        "accuracy": accuracy,

        "precision": precision,

        "recall": recall,

        "f1_score": f1,

        "confusion_matrix": matrix,

        "X_test": X_test,

        "y_test": y_test,

        "predictions": y_prediction
    }


    # ========================================================
    # MACHINE LEARNING COMPLETED
    # ========================================================

    print("\n")
    print("========================================")
    print("     MACHINE LEARNING COMPLETED")
    print("========================================")


    return results