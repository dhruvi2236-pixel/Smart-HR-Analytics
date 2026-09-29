# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# MAIN PROGRAM
# ============================================================

from modules.data_loader import load_data
from modules.data_exploration import explore_data
from modules.data_cleaning import clean_data
from modules.data_preprocessing import preprocess_data
from modules.statistical_analysis import perform_statistical_analysis
from modules.probability_analysis import perform_probability_analysis
from modules.sampling_inference import perform_sampling_inference
from modules.hypothesis_testing import perform_hypothesis_testing
from modules.data_visualization import create_visualizations
from modules.machine_learning import perform_machine_learning
from modules.crud_operations import demonstrate_crud
from modules.web_scraping import scrape_hr_information
from modules.exception_handling import demonstrate_exception_handling


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    print("\n")
    print("=" * 60)
    print("       SMART HR ANALYTICS & EMPLOYEE ATTRITION")
    print("=" * 60)


    # ========================================================
    # STEP 1: DATA LOADING
    # ========================================================

    print("\n\nSTEP 1: DATA LOADING")

    data = load_data(
        "dataset/employee_data.csv"
    )


    # ========================================================
    # STEP 2: DATA EXPLORATION
    # ========================================================

    print("\n\nSTEP 2: DATA EXPLORATION")

    explore_data(data)


    # ========================================================
    # STEP 3: DATA CLEANING
    # ========================================================

    print("\n\nSTEP 3: DATA CLEANING")

    cleaned_data = clean_data(data)


    # ========================================================
    # STEP 4: DATA PREPROCESSING
    # ========================================================

    print("\n\nSTEP 4: DATA PREPROCESSING")

    processed_data = preprocess_data(
        cleaned_data
    )


    # ========================================================
    # STEP 5: STATISTICAL ANALYSIS
    # ========================================================

    print("\n\nSTEP 5: STATISTICAL ANALYSIS")

    perform_statistical_analysis(
        processed_data
    )


    # ========================================================
    # STEP 6: PROBABILITY
    # ========================================================

    print("\n\nSTEP 6: PROBABILITY ANALYSIS")

    perform_probability_analysis(
        processed_data
    )


    # ========================================================
    # STEP 7: SAMPLING & INFERENCE
    # ========================================================

    print("\n\nSTEP 7: SAMPLING & INFERENCE")

    perform_sampling_inference(
        processed_data
    )


    # ========================================================
    # STEP 8: HYPOTHESIS TESTING
    # ========================================================

    print("\n\nSTEP 8: HYPOTHESIS TESTING")

    perform_hypothesis_testing(
        processed_data
    )


    # ========================================================
    # STEP 9: DATA VISUALIZATION
    # ========================================================

    print("\n\nSTEP 9: DATA VISUALIZATION")

    create_visualizations(
        processed_data
    )


    # ========================================================
    # STEP 10: MACHINE LEARNING
    # ========================================================

    print("\n\nSTEP 10: MACHINE LEARNING")

    ml_results = perform_machine_learning(
        processed_data
    )


    # ========================================================
    # STEP 11: CRUD OPERATIONS
    # ========================================================

    print("\n\nSTEP 11: CRUD OPERATIONS")

    demonstrate_crud()


    # ========================================================
    # STEP 12: WEB SCRAPING
    # ========================================================

    print("\n\nSTEP 12: WEB SCRAPING")

    scrape_hr_information()


    # ========================================================
    # STEP 13: EXCEPTION HANDLING
    # ========================================================

    print("\n\nSTEP 13: EXCEPTION HANDLING")

    demonstrate_exception_handling()


    # ========================================================
    # FINAL SUMMARY
    # ========================================================

    print("\n\n")
    print("=" * 60)
    print("              CIPAT PROJECT COMPLETED")
    print("=" * 60)

    print("\nPython for Data Science Concepts Implemented:")

    concepts = [
        "1. Python Core Concepts",
        "2. Data Structures",
        "3. Python Libraries",
        "4. Custom Modules",
        "5. Exception Handling",
        "6. Web Scraping",
        "7. File Handling",
        "8. CRUD Operations",
        "9. NumPy",
        "10. SciPy",
        "11. Pandas",
        "12. Data Preprocessing",
        "13. Data Visualization",
        "14. Statistical Analysis",
        "15. Probability",
        "16. Sampling & Inference",
        "17. Hypothesis Testing",
        "18. Machine Learning"
    ]

    for concept in concepts:
        print("✓", concept)


    # ========================================================
    # MACHINE LEARNING RESULTS
    # ========================================================

    if ml_results is not None:

        print("\n")
        print("=" * 60)
        print("              MACHINE LEARNING RESULTS")
        print("=" * 60)

        print(
            f"Accuracy  : {ml_results['accuracy']:.2%}"
        )

        print(
            f"Precision : {ml_results['precision']:.2%}"
        )

        print(
            f"Recall    : {ml_results['recall']:.2%}"
        )

        print(
            f"F1-Score  : {ml_results['f1_score']:.2%}"
        )


    # ========================================================
    # PROJECT COMPLETION
    # ========================================================

    print("\n")
    print("=" * 60)
    print("        ALL MODULES EXECUTED SUCCESSFULLY")
    print("=" * 60)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()