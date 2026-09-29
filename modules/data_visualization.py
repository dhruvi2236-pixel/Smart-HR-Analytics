# ============================================================
# HUMAN RESOURCE ANALYTICS
# DATA VISUALIZATION MODULE
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, PercentFormatter


# ============================================================
# PROFESSIONAL COLORS
# ============================================================

PRIMARY_BLUE = "#2F5597"
DARK_BLUE = "#17365D"
ACCENT_ORANGE = "#E67E22"
RESIGNED_RED = "#C0504D"
STAYED_GREEN = "#70AD47"

TEXT_GREY = "#555555"
GRID_GREY = "#BBBBBB"


# ============================================================
# COMMON GRAPH FORMATTING
# ============================================================

def prepare_axes(axis):
    """
    Applies common professional formatting
    to all graphs.
    """

    axis.set_facecolor("white")

    # Remove unnecessary borders
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    axis.spines["left"].set_color(GRID_GREY)
    axis.spines["bottom"].set_color(GRID_GREY)

    # Tick size
    axis.tick_params(
        axis="both",
        labelsize=11
    )

    # Light horizontal grid
    axis.grid(
        axis="x",
        linestyle="--",
        linewidth=0.7,
        alpha=0.25
    )

    axis.set_axisbelow(True)


# ============================================================
# INTEGER FORMATTER
# ============================================================

def thousands_formatter(value, position):
    """
    Converts numbers such as:

    1000  -> 1K
    10000 -> 10K
    """

    return f"{int(value / 1000)}K"


# ============================================================
# DISPLAY AND SAVE GRAPH
# ============================================================

def display_and_save(
    figure,
    file_path,
    graph_number
):
    """
    Saves the graph and displays it.

    The next graph will appear only after
    the current graph window is closed.
    """

    figure.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight",
        facecolor="white"
    )

    print(
        f"\nGraph {graph_number} saved:"
    )

    print(file_path)

    print(
        "Close the graph window "
        "to continue."
    )

    plt.show()

    plt.close(figure)


# ============================================================
# MAIN VISUALIZATION FUNCTION
# ============================================================

def create_visualizations(data):
    """
    Creates six professional HR visualizations.

    Graph 1:
        Workforce distribution by department

    Graph 2:
        Resignation rate by department

    Graph 3:
        Resignation rate by satisfaction level

    Graph 4:
        Resignation rate by overtime level

    Graph 5:
        Average satisfaction by resignation status

    Graph 6:
        Actual employee resignation status
    """

    # ========================================================
    # CREATE GRAPH OUTPUT FOLDER
    # ========================================================

    os.makedirs(
        "graphs",
        exist_ok=True
    )


    # ========================================================
    # COPY DATA
    # ========================================================

    visualization_data = data.copy()


    # ========================================================
    # CHECK REQUIRED COLUMNS
    # ========================================================

    required_columns = (
        "Department",
        "Employee_Satisfaction_Score",
        "Overtime_Level",
        "Resigned_Flag"
    )


    missing_columns = tuple(
        column
        for column in required_columns
        if column not in visualization_data.columns
    )


    if missing_columns:

        print(
            "\nERROR: Required columns are missing:"
        )

        for column in missing_columns:
            print(f"- {column}")

        return


    # ========================================================
    # BASIC DATA VALUES
    # ========================================================

    total_employees = len(
        visualization_data
    )


    total_resigned = int(
        visualization_data[
            "Resigned_Flag"
        ].sum()
    )


    total_not_resigned = (
        total_employees
        - total_resigned
    )


    overall_resignation_rate = (
        total_resigned
        / total_employees
        * 100
    )


    # ========================================================
    # HEADER
    # ========================================================

    print("\n========================================")
    print("         DATA VISUALIZATION")
    print("========================================")

    print(
        f"\nEmployees analyzed: "
        f"{total_employees:,}"
    )

    print(
        f"Employees resigned: "
        f"{total_resigned:,}"
    )

    print(
        f"Overall resignation rate: "
        f"{overall_resignation_rate:.2f}%"
    )


    # ========================================================
    # GRAPH 1
    # WORKFORCE DISTRIBUTION BY DEPARTMENT
    # ========================================================

    print("\n========================================")
    print("GRAPH 1")
    print("WORKFORCE DISTRIBUTION BY DEPARTMENT")
    print("========================================")


    department_counts = (
        visualization_data[
            "Department"
        ]
        .value_counts()
        .sort_values(
            ascending=True
        )
    )


    department_percentages = (
        department_counts
        / total_employees
        * 100
    )


    figure, axis = plt.subplots(
        figsize=(11, 7)
    )


    bars = axis.barh(
        department_counts.index,
        department_counts.values,
        color=PRIMARY_BLUE,
        height=0.62
    )


    axis.set_title(
        "Workforce Distribution by Department",
        fontsize=20,
        fontweight="bold",
        pad=20
    )


    axis.text(
        0,
        1.015,
        "Employee count and percentage of total workforce",
        transform=axis.transAxes,
        fontsize=11,
        color=TEXT_GREY
    )


    axis.set_xlabel(
        "Number of Employees",
        fontsize=12
    )


    axis.set_ylabel(
        "Department",
        fontsize=12
    )


    prepare_axes(axis)


    for index, bar in enumerate(bars):

        count = department_counts.iloc[
            index
        ]

        percentage = department_percentages.iloc[
            index
        ]

        axis.text(
            bar.get_width() + 200,
            bar.get_y()
            + bar.get_height() / 2,
            f"{count:,}  ({percentage:.1f}%)",
            va="center",
            fontsize=10
        )


    maximum_count = department_counts.max()


    axis.set_xlim(
        0,
        maximum_count * 1.20
    )


    axis.xaxis.set_major_formatter(
        FuncFormatter(
            thousands_formatter
        )
    )


    figure.text(
        0.12,
        0.01,
        "HR question: Which departments contain the largest share of employees?",
        fontsize=10,
        color=TEXT_GREY
    )


    figure.tight_layout(
        rect=(0, 0.04, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/01_workforce_distribution_department.png",
        1
    )


    # ========================================================
    # GRAPH 2
    # RESIGNATION RATE BY DEPARTMENT
    # ========================================================

    print("\n========================================")
    print("GRAPH 2")
    print("RESIGNATION RATE BY DEPARTMENT")
    print("========================================")


    department_resignation = (
        visualization_data
        .groupby(
            "Department"
        )[
            "Resigned_Flag"
        ]
        .mean()
        .mul(100)
        .sort_values(
            ascending=True
        )
    )


    highest_department = (
        department_resignation.idxmax()
    )


    highest_rate = (
        department_resignation.max()
    )


    figure, axis = plt.subplots(
        figsize=(11, 7)
    )


    bars = axis.barh(
        department_resignation.index,
        department_resignation.values,
        color=PRIMARY_BLUE,
        height=0.62
    )


    axis.axvline(
        overall_resignation_rate,
        color=ACCENT_ORANGE,
        linestyle="--",
        linewidth=2,
        label=(
            f"Overall rate: "
            f"{overall_resignation_rate:.1f}%"
        )
    )


    axis.set_title(
        "Employee Resignation Rate by Department",
        fontsize=20,
        fontweight="bold",
        pad=20
    )


    axis.text(
        0,
        1.015,
        "Department rates compared with the overall historical rate",
        transform=axis.transAxes,
        fontsize=11,
        color=TEXT_GREY
    )


    axis.set_xlabel(
        "Resignation Rate (%)",
        fontsize=12
    )


    axis.set_ylabel(
        "Department",
        fontsize=12
    )


    prepare_axes(axis)


    for index, bar in enumerate(bars):

        value = (
            department_resignation.iloc[
                index
            ]
        )

        axis.text(
            value + 0.12,
            bar.get_y()
            + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            fontsize=11
        )


    axis.set_xlim(
        0,
        department_resignation.max() + 2
    )


    axis.yaxis.grid(
        visible=False
    )


    axis.xaxis.set_major_formatter(
        PercentFormatter(
            xmax=100
        )
    )


    axis.legend(
        loc="lower right",
        frameon=True
    )


    figure.text(
        0.12,
        0.01,
        (
            f"Highest observed rate: "
            f"{highest_department} "
            f"({highest_rate:.1f}%)."
        ),
        fontsize=10,
        color=TEXT_GREY
    )


    figure.tight_layout(
        rect=(0, 0.04, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/02_resignation_rate_department.png",
        2
    )


    # ========================================================
    # GRAPH 3
    # RESIGNATION RATE BY SATISFACTION
    # ========================================================

    print("\n========================================")
    print("GRAPH 3")
    print("RESIGNATION RATE BY SATISFACTION")
    print("========================================")


    satisfaction_data = (
        visualization_data.copy()
    )


    satisfaction_data[
        "Satisfaction_Level"
    ] = pd.cut(
        satisfaction_data[
            "Employee_Satisfaction_Score"
        ],
        bins=(
            0,
            2.5,
            3.5,
            5
        ),
        labels=(
            "Low (≤ 2.5)",
            "Medium (2.51–3.5)",
            "High (> 3.5)"
        ),
        include_lowest=True
    )


    satisfaction_order = (
        "Low (≤ 2.5)",
        "Medium (2.51–3.5)",
        "High (> 3.5)"
    )


    satisfaction_rate = (
        satisfaction_data
        .groupby(
            "Satisfaction_Level",
            observed=False
        )[
            "Resigned_Flag"
        ]
        .mean()
        .mul(100)
        .reindex(
            satisfaction_order
        )
    )


    satisfaction_counts = (
        satisfaction_data[
            "Satisfaction_Level"
        ]
        .value_counts()
        .reindex(
            satisfaction_order
        )
    )


    figure, axis = plt.subplots(
        figsize=(11, 7)
    )


    bars = axis.bar(
        satisfaction_rate.index,
        satisfaction_rate.values,
        color=(
            RESIGNED_RED,
            PRIMARY_BLUE,
            PRIMARY_BLUE
        ),
        width=0.62
    )


    axis.axhline(
        overall_resignation_rate,
        color=ACCENT_ORANGE,
        linestyle="--",
        linewidth=2,
        label=(
            f"Overall rate: "
            f"{overall_resignation_rate:.1f}%"
        )
    )


    axis.set_title(
        "Resignation Rate by Employee Satisfaction",
        fontsize=20,
        fontweight="bold",
        pad=20
    )


    axis.text(
        0,
        1.015,
        "Low satisfaction is defined as a score of 2.5 or below",
        transform=axis.transAxes,
        fontsize=11,
        color=TEXT_GREY
    )


    axis.set_xlabel(
        "Satisfaction Level",
        fontsize=12
    )


    axis.set_ylabel(
        "Resignation Rate (%)",
        fontsize=12
    )


    prepare_axes(axis)


    for index, bar in enumerate(bars):

        rate = satisfaction_rate.iloc[
            index
        ]

        count = satisfaction_counts.iloc[
            index
        ]

        axis.text(
            bar.get_x()
            + bar.get_width() / 2,
            rate + 1.5,
            f"{rate:.1f}%\n(n={count:,})",
            ha="center",
            fontsize=10,
            fontweight="bold"
        )


    maximum_rate = satisfaction_rate.max()


    axis.set_ylim(
        0,
        maximum_rate + 12
    )


    axis.yaxis.set_major_formatter(
        PercentFormatter(
            xmax=100
        )
    )


    axis.legend(
        loc="upper right"
    )


    low_satisfaction_rate = (
        satisfaction_rate.iloc[0]
    )


    figure.text(
        0.12,
        0.01,
        (
            f"Key finding: low satisfaction employees "
            f"showed a {low_satisfaction_rate:.1f}% resignation rate."
        ),
        fontsize=10,
        color=TEXT_GREY
    )


    figure.tight_layout(
        rect=(0, 0.04, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/03_resignation_rate_satisfaction.png",
        3
    )


    # ========================================================
    # GRAPH 4
    # RESIGNATION RATE BY OVERTIME LEVEL
    # ========================================================

    print("\n========================================")
    print("GRAPH 4")
    print("RESIGNATION RATE BY OVERTIME LEVEL")
    print("========================================")


    overtime_rate = (
        visualization_data
      .groupby(
    "Overtime_Level",
    observed=False
)[
            "Resigned_Flag"
        ]
        .mean()
        .mul(100)
    )


    overtime_counts = (
        visualization_data[
            "Overtime_Level"
        ]
        .value_counts()
    )


    # --------------------------------------------------------
    # Try the expected logical order.
    # If the dataset has different labels,
    # use the labels actually present.
    # --------------------------------------------------------

    expected_order = (
        "Low",
        "Moderate",
        "Medium",
        "High"
    )


    actual_levels = tuple(
        level
        for level in expected_order
        if level in overtime_rate.index
    )


    if len(actual_levels) == 0:

        actual_levels = tuple(
            overtime_rate.index.astype(str)
        )


    overtime_rate = overtime_rate.reindex(
        actual_levels
    )


    overtime_counts = overtime_counts.reindex(
        actual_levels
    )


    # --------------------------------------------------------
    # Create color tuple dynamically.
    # This avoids the Pylance list/tuple error.
    # --------------------------------------------------------

    overtime_colors = tuple(
        RESIGNED_RED
        if str(level) == "High"
        else PRIMARY_BLUE
        for level in overtime_rate.index
    )


    figure, axis = plt.subplots(
        figsize=(11, 7)
    )


    bars = axis.bar(
        overtime_rate.index,
        overtime_rate.values,
        color=overtime_colors,
        width=0.62
    )


    axis.axhline(
        overall_resignation_rate,
        color=ACCENT_ORANGE,
        linestyle="--",
        linewidth=2,
        label=(
            f"Overall rate: "
            f"{overall_resignation_rate:.1f}%"
        )
    )


    axis.set_title(
        "Resignation Rate by Overtime Level",
        fontsize=20,
        fontweight="bold",
        pad=20
    )


    axis.text(
        0,
        1.015,
        "Overtime categories are taken from the preprocessing stage",
        transform=axis.transAxes,
        fontsize=11,
        color=TEXT_GREY
    )


    axis.set_xlabel(
        "Overtime Level",
        fontsize=12
    )


    axis.set_ylabel(
        "Resignation Rate (%)",
        fontsize=12
    )


    prepare_axes(axis)


    for index, bar in enumerate(bars):

        rate = overtime_rate.iloc[
            index
        ]

        count = overtime_counts.iloc[
            index
        ]

        axis.text(
            bar.get_x()
            + bar.get_width() / 2,
            rate + 1.0,
            f"{rate:.1f}%\n(n={count:,})",
            ha="center",
            fontsize=10,
            fontweight="bold"
        )


    axis.set_ylim(
        0,
        overtime_rate.max() + 10
    )


    axis.yaxis.set_major_formatter(
        PercentFormatter(
            xmax=100
        )
    )


    axis.legend(
        loc="upper left"
    )


    figure.text(
        0.12,
        0.01,
        (
            "HR question: Does resignation risk vary "
            "with overtime level?"
        ),
        fontsize=10,
        color=TEXT_GREY
    )


    figure.tight_layout(
        rect=(0, 0.04, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/04_resignation_rate_overtime.png",
        4
    )


    # ========================================================
    # GRAPH 5
    # AVERAGE SATISFACTION
    # RESIGNED VS NOT RESIGNED
    # ========================================================

    print("\n========================================")
    print("GRAPH 5")
    print("AVERAGE SATISFACTION BY RESIGNATION STATUS")
    print("========================================")


    average_satisfaction = (
        visualization_data
        .groupby(
            "Resigned_Flag"
        )[
            "Employee_Satisfaction_Score"
        ]
        .mean()
        .reindex(
            [0, 1]
        )
    )


    status_labels = (
        "Not Resigned",
        "Resigned"
    )


    satisfaction_values = (
        average_satisfaction.values
    )


    figure, axis = plt.subplots(
        figsize=(10, 7)
    )


    bars = axis.bar(
        status_labels,
        satisfaction_values,
        color=(
            STAYED_GREEN,
            RESIGNED_RED
        ),
        width=0.55
    )


    axis.set_title(
        "Average Employee Satisfaction by Resignation Status",
        fontsize=20,
        fontweight="bold",
        pad=20
    )


    axis.text(
        0,
        1.015,
        "Average satisfaction score on a 1–5 scale",
        transform=axis.transAxes,
        fontsize=11,
        color=TEXT_GREY
    )


    axis.set_xlabel(
        "Employee Status",
        fontsize=12
    )


    axis.set_ylabel(
        "Average Satisfaction Score",
        fontsize=12
    )


    prepare_axes(axis)


    for bar in bars:

        value = bar.get_height()

        axis.text(
            bar.get_x()
            + bar.get_width() / 2,
            value + 0.08,
            f"{value:.2f}",
            ha="center",
            fontsize=13,
            fontweight="bold"
        )


    axis.set_ylim(
        0,
        5
    )


    axis.set_yticks(
        (0, 1, 2, 3, 4, 5)
    )


    satisfaction_difference = (
        satisfaction_values[0]
        - satisfaction_values[1]
    )


    figure.text(
        0.12,
        0.01,
        (
            f"Difference in average satisfaction: "
            f"{satisfaction_difference:.2f} points."
        ),
        fontsize=10,
        color=TEXT_GREY
    )


    figure.tight_layout(
        rect=(0, 0.04, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/05_average_satisfaction_resignation_status.png",
        5
    )


    # ========================================================
    # GRAPH 6
    # ACTUAL EMPLOYEE RESIGNATION STATUS
    # ========================================================

    print("\n========================================")
    print("GRAPH 6")
    print("ACTUAL EMPLOYEE RESIGNATION STATUS")
    print("========================================")


    figure, axis = plt.subplots(
        figsize=(10, 8)
    )


    status_values = (
        total_not_resigned,
        total_resigned
    )


    status_labels = (
        "Not Resigned",
        "Resigned"
    )


    # IMPORTANT:
    # Tuple instead of list.
    # This removes the Pylance color type error.

    status_colors = (
        PRIMARY_BLUE,
        RESIGNED_RED
    )


    # ========================================================
    # PROFESSIONAL DONUT
    # ========================================================

    axis.pie(
        status_values,
        startangle=90,
        colors=status_colors,
        wedgeprops={
            "width": 0.38,
            "edgecolor": "white",
            "linewidth": 2
        },
        autopct=lambda percentage:
            f"{percentage:.1f}%",
        pctdistance=0.78,
        textprops={
            "fontsize": 14,
            "fontweight": "bold"
        }
    )


    axis.set_title(
        "Actual Employee Resignation Status",
        fontsize=21,
        fontweight="bold",
        pad=25
    )


    # ========================================================
    # CENTER OF DONUT
    # ========================================================

    axis.text(
        0,
        0.08,
        f"{total_employees:,}",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold"
    )


    axis.text(
        0,
        -0.10,
        "Employees",
        ha="center",
        va="center",
        fontsize=12,
        color=TEXT_GREY
    )


    # ========================================================
    # LEGEND
    # ========================================================

    legend_labels = (
        f"Not Resigned  •  {total_not_resigned:,} employees",
        f"Resigned  •  {total_resigned:,} employees"
    )


    axis.legend(
        legend_labels,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.10),
        frameon=False,
        fontsize=11
    )


    axis.text(
        0.5,
        -0.20,
        (
            f"Actual historical resignation rate: "
            f"{overall_resignation_rate:.1f}%"
        ),
        transform=axis.transAxes,
        ha="center",
        fontsize=11,
        fontweight="bold",
        color=TEXT_GREY
    )


    axis.axis("equal")


    figure.tight_layout(
        rect=(0, 0.08, 1, 1)
    )


    display_and_save(
        figure,
        "graphs/06_actual_employee_resignation_status.png",
        6
    )


    # ========================================================
    # COMPLETION MESSAGE
    # ========================================================

    print("\n========================================")
    print("     DATA VISUALIZATION COMPLETED")
    print("========================================")

    print(
        "\n6 professional HR graphs created."
    )

    print(
        "All graphs saved inside the graphs folder."
    )

    print(
        "The final donut represents the actual "
        "historical resignation status."
    )

    print(
        "\nVisualization stage completed successfully."
    )