# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# HYPOTHESIS TESTING MODULE
# ============================================================

from typing import Any

from scipy import stats


# ============================================================
# HYPOTHESIS TESTING FUNCTION
# ============================================================

def perform_hypothesis_testing(data):
    """
    Test whether employee satisfaction is significantly
    different between employees who resigned and employees
    who stayed.
    """

    print("\n========================================")
    print("         HYPOTHESIS TESTING")
    print("========================================")


    # ========================================================
    # 1. CHECK REQUIRED COLUMNS
    # ========================================================

    required_columns = [
        "Resigned",
        "Employee_Satisfaction_Score"
    ]


    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]


    if missing_columns:

        print(
            "\nERROR: Required columns are missing:"
        )

        for column in missing_columns:

            print(
                f"- {column}"
            )

        return None


    # ========================================================
    # 2. SEPARATE EMPLOYEES INTO TWO GROUPS
    # ========================================================

    stayed_employees = data.loc[
        data["Resigned"] == False,
        "Employee_Satisfaction_Score"
    ]


    resigned_employees = data.loc[
        data["Resigned"] == True,
        "Employee_Satisfaction_Score"
    ]


    # ========================================================
    # 3. CHECK BOTH GROUPS
    # ========================================================

    if len(stayed_employees) == 0:

        print(
            "\nERROR: No employees found in "
            "the stayed group."
        )

        return None


    if len(resigned_employees) == 0:

        print(
            "\nERROR: No employees found in "
            "the resigned group."
        )

        return None


    # ========================================================
    # 4. CALCULATE AVERAGE SATISFACTION
    # ========================================================

    stayed_mean = stayed_employees.mean()

    resigned_mean = resigned_employees.mean()


    print("\n1. Average Satisfaction")


    print(
        "Employees who stayed:",
        round(stayed_mean, 2)
    )


    print(
        "Employees who resigned:",
        round(resigned_mean, 2)
    )


    # ========================================================
    # 5. STATE HYPOTHESES
    # ========================================================

    print("\n2. Hypotheses")


    print(
        "H0: There is no significant difference "
        "in average satisfaction between employees "
        "who stayed and employees who resigned."
    )


    print(
        "H1: There is a significant difference "
        "in average satisfaction between employees "
        "who stayed and employees who resigned."
    )


    # ========================================================
    # 6. PERFORM INDEPENDENT TWO-SAMPLE T-TEST
    # ========================================================

    print(
        "\n3. Independent Two-Sample T-Test"
    )


    # --------------------------------------------------------
    # SciPy type information can vary between versions.
    # Any prevents Pylance from incorrectly treating the
    # t-test result as an unsupported internal type.
    # The actual calculation is still performed by SciPy.
    # --------------------------------------------------------

    test_result: Any = stats.ttest_ind(
        stayed_employees,
        resigned_employees,
        equal_var=False
    )


    t_statistic = float(
        test_result.statistic
    )


    p_value = float(
        test_result.pvalue
    )


    print(
        "T-statistic:",
        round(t_statistic, 4)
    )


    print(
        "P-value:",
        f"{p_value:.6f}"
    )


    # ========================================================
    # 7. SIGNIFICANCE LEVEL
    # ========================================================

    significance_level = 0.05


    print(
        "Significance level:",
        significance_level
    )


    # ========================================================
    # 8. DECISION
    # ========================================================

    print("\n4. Decision")


    if p_value < significance_level:

        print(
            "P-value is less than 0.05."
        )

        print(
            "Reject the null hypothesis (H0)."
        )

        decision = (
            "Reject the null hypothesis (H0)."
        )

    else:

        print(
            "P-value is greater than or equal to 0.05."
        )

        print(
            "Fail to reject the null hypothesis (H0)."
        )

        decision = (
            "Fail to reject the null hypothesis (H0)."
        )


    # ========================================================
    # 9. INTERPRETATION
    # ========================================================

    print("\n5. Interpretation")


    if p_value < significance_level:

        interpretation = (
            "There is a statistically significant "
            "difference in employee satisfaction "
            "between employees who stayed and "
            "employees who resigned."
        )

    else:

        interpretation = (
            "There is not enough statistical evidence "
            "to conclude that employee satisfaction "
            "differs between the two groups."
        )


    print(
        interpretation
    )


    # ========================================================
    # 10. RETURN RESULTS
    # ========================================================

    results = {
        "stayed_mean": stayed_mean,
        "resigned_mean": resigned_mean,
        "t_statistic": t_statistic,
        "p_value": p_value,
        "significance_level": significance_level,
        "decision": decision,
        "interpretation": interpretation
    }


    print("\n========================================")
    print("     HYPOTHESIS TESTING COMPLETED")
    print("========================================")


    return results