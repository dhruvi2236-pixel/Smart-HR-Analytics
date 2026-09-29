def perform_probability_analysis(data):
    """
    Perform probability calculations related to
    employee resignation.
    """

    print("\n========================================")
    print("         PROBABILITY ANALYSIS")
    print("========================================")

    # ----------------------------------------
    # 1. Total employees
    # ----------------------------------------

    total_employees = len(data)

    # ----------------------------------------
    # 2. Resigned employees
    # ----------------------------------------

    resigned_employees = data[
        "Resigned_Flag"
    ].sum()

    # ----------------------------------------
    # 3. Overall probability of resignation
    # ----------------------------------------

    overall_probability = (
        resigned_employees / total_employees
    )

    overall_percentage = (
        overall_probability * 100
    )

    print("\n1. Overall Resignation Probability")

    print(
        "Total employees:",
        total_employees
    )

    print(
        "Employees resigned:",
        resigned_employees
    )

    print(
        "P(Resigned) =",
        round(overall_probability, 4)
    )

    print(
        "Resignation rate =",
        round(overall_percentage, 2),
        "%"
    )

    # ----------------------------------------
    # 4. Probability of staying
    # ----------------------------------------

    staying_probability = (
        1 - overall_probability
    )

    print("\n2. Probability of Staying")

    print(
        "P(Not Resigned) =",
        round(staying_probability, 4)
    )

    print(
        "Staying rate =",
        round(staying_probability * 100, 2),
        "%"
    )

    # ----------------------------------------
    # 5. High overtime group
    # ----------------------------------------

    high_overtime = data[
        data["Overtime_Level"] == "High"
    ]

    if len(high_overtime) > 0:

        high_overtime_resigned = (
            high_overtime["Resigned_Flag"].sum()
        )

        high_overtime_probability = (
            high_overtime_resigned /
            len(high_overtime)
        )

        high_overtime_percentage = (
            high_overtime_probability * 100
        )

        difference_from_overall = (
            high_overtime_percentage -
            overall_percentage
        )

        print(
            "\n3. Resignation Probability "
            "for High Overtime Employees"
        )

        print(
            "Employees in group:",
            len(high_overtime)
        )

        print(
            "Employees resigned:",
            high_overtime_resigned
        )

        print(
            "P(Resigned | High Overtime) =",
            round(
                high_overtime_probability,
                4
            )
        )

        print(
            "Resignation rate =",
            round(
                high_overtime_percentage,
                2
            ),
            "%"
        )

        print(
            "Difference from overall rate =",
            round(
                difference_from_overall,
                2
            ),
            "percentage points"
        )

    # ----------------------------------------
    # 6. Low satisfaction group
    # ----------------------------------------

    low_satisfaction = data[
        data["Employee_Satisfaction_Score"] < 2.5
    ]

    if len(low_satisfaction) > 0:

        low_satisfaction_resigned = (
            low_satisfaction["Resigned_Flag"].sum()
        )

        low_satisfaction_probability = (
            low_satisfaction_resigned /
            len(low_satisfaction)
        )

        low_satisfaction_percentage = (
            low_satisfaction_probability * 100
        )

        difference_from_overall = (
            low_satisfaction_percentage -
            overall_percentage
        )

        print(
            "\n4. Resignation Probability "
            "for Low Satisfaction Employees"
        )

        print(
            "Employees in group:",
            len(low_satisfaction)
        )

        print(
            "Employees resigned:",
            low_satisfaction_resigned
        )

        print(
            "P(Resigned | Low Satisfaction) =",
            round(
                low_satisfaction_probability,
                4
            )
        )

        print(
            "Resignation rate =",
            round(
                low_satisfaction_percentage,
                2
            ),
            "%"
        )

        print(
            "Difference from overall rate =",
            round(
                difference_from_overall,
                2
            ),
            "percentage points"
        )

    # ----------------------------------------
    # 7. Long working hours group
    # ----------------------------------------

    long_hours = data[
        data["Work_Hours_Per_Week"] > 50
    ]

    if len(long_hours) > 0:

        long_hours_resigned = (
            long_hours["Resigned_Flag"].sum()
        )

        long_hours_probability = (
            long_hours_resigned /
            len(long_hours)
        )

        long_hours_percentage = (
            long_hours_probability * 100
        )

        difference_from_overall = (
            long_hours_percentage -
            overall_percentage
        )

        print(
            "\n5. Resignation Probability "
            "for Employees Working More Than 50 Hours"
        )

        print(
            "Employees in group:",
            len(long_hours)
        )

        print(
            "Employees resigned:",
            long_hours_resigned
        )

        print(
            "P(Resigned | >50 Hours) =",
            round(
                long_hours_probability,
                4
            )
        )

        print(
            "Resignation rate =",
            round(
                long_hours_percentage,
                2
            ),
            "%"
        )

        print(
            "Difference from overall rate =",
            round(
                difference_from_overall,
                2
            ),
            "percentage points"
        )

    print("\n========================================")
    print("     PROBABILITY ANALYSIS COMPLETED")
    print("========================================")