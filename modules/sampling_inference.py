import numpy as np


def perform_sampling_inference(data):
    """
    Take a random sample from the employee dataset
    and estimate the resignation rate of the population.
    """

    print("\n========================================")
    print("        SAMPLING & INFERENCE")
    print("========================================")

    # ----------------------------------------
    # 1. Population information
    # ----------------------------------------

    population_size = len(data)

    population_resignation_rate = (
        data["Resigned_Flag"].mean()
    )

    print("\n1. Population")

    print(
        "Population size:",
        population_size
    )

    print(
        "Population resignation rate:",
        round(
            population_resignation_rate * 100,
            2
        ),
        "%"
    )

    # ----------------------------------------
    # 2. Select random sample
    # ----------------------------------------

    sample_size = 1000

    sample = data.sample(
        n=sample_size,
        random_state=42
    )

    print("\n2. Random Sample")

    print(
        "Sample size:",
        len(sample)
    )

    # ----------------------------------------
    # 3. Calculate sample resignation rate
    # ----------------------------------------

    sample_resignation_rate = (
        sample["Resigned_Flag"].mean()
    )

    print(
        "Sample resignation rate:",
        round(
            sample_resignation_rate * 100,
            2
        ),
        "%"
    )

    # ----------------------------------------
    # 4. Calculate standard error
    # ----------------------------------------

    standard_error = np.sqrt(
        (
            sample_resignation_rate *
            (1 - sample_resignation_rate)
        )
        / sample_size
    )

    # ----------------------------------------
    # 5. Calculate 95% confidence interval
    # ----------------------------------------

    confidence_level = 0.95

    z_value = 1.96

    margin_of_error = (
        z_value *
        standard_error
    )

    lower_limit = (
        sample_resignation_rate -
        margin_of_error
    )

    upper_limit = (
        sample_resignation_rate +
        margin_of_error
    )

    # Keep limits between 0 and 1
    lower_limit = max(
        0,
        lower_limit
    )

    upper_limit = min(
        1,
        upper_limit
    )

    # ----------------------------------------
    # 6. Display confidence interval
    # ----------------------------------------

    print("\n3. 95% Confidence Interval")

    print(
        "Lower limit:",
        round(
            lower_limit * 100,
            2
        ),
        "%"
    )

    print(
        "Upper limit:",
        round(
            upper_limit * 100,
            2
        ),
        "%"
    )

    print(
        "Confidence interval:",
        f"{lower_limit * 100:.2f}%"
        f" to "
        f"{upper_limit * 100:.2f}%"
    )

    # ----------------------------------------
    # 7. Compare sample with population
    # ----------------------------------------

    print("\n4. Sample vs Population")

    difference = (
        sample_resignation_rate -
        population_resignation_rate
    )

    print(
        "Difference:",
        round(
            difference * 100,
            2
        ),
        "percentage points"
    )

    # ----------------------------------------
    # 8. Interpretation
    # ----------------------------------------

    print("\n5. Interpretation")

    print(
        "The sample was used to estimate the "
        "population resignation rate."
    )

    print(
        "The 95% confidence interval gives a "
        "range of plausible values for the "
        "population resignation rate based "
        "on the sample."
    )

    print("\n========================================")
    print("    SAMPLING & INFERENCE COMPLETED")
    print("========================================")