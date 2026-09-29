# Smart HR Analytics & Employee Attrition Prediction System

## Project Overview

Smart HR Analytics & Employee Attrition Prediction System is a Python-based HR analytics project developed to analyze employee data and identify patterns related to employee resignation.

The project uses Python and data science techniques such as data preprocessing, statistical analysis, probability, sampling and inference, hypothesis testing, data visualization, and machine learning.

The project also demonstrates CRUD operations, web scraping, exception handling, file handling, custom modules, and an interactive Streamlit dashboard.

---

## Objectives

- Analyze employee data and HR-related factors.
- Identify patterns related to employee resignation.
- Perform data cleaning and preprocessing.
- Perform statistical and probability analysis.
- Apply sampling and inference techniques.
- Perform hypothesis testing.
- Create meaningful HR data visualizations.
- Build a machine learning model for employee resignation prediction.
- Implement CRUD operations with permanent data storage.
- Demonstrate web scraping using HR-related information.
- Demonstrate exception handling for different runtime errors.
- Develop an interactive Streamlit dashboard.

---

## Dataset

The project uses an employee dataset containing 100,000 employee records and 20 original attributes.

The dataset includes:

- Employee ID
- Department
- Gender
- Age
- Job Title
- Hire Date
- Years at Company
- Education Level
- Performance Score
- Monthly Salary
- Work Hours per Week
- Projects Handled
- Overtime Hours
- Sick Days
- Remote Work Frequency
- Team Size
- Training Hours
- Promotions
- Employee Satisfaction Score
- Resigned

---

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Scikit-learn
- Requests
- BeautifulSoup
- Certifi
- Streamlit
- Plotly

---

## Project Modules

### 1. Dataset Loading

Loads the employee dataset from a CSV file using Pandas.

### 2. Data Exploration

Explores the dataset structure, columns, data types, records, and basic information.

### 3. Data Cleaning

Checks the dataset for missing values, duplicate records, and data consistency.

### 4. Data Preprocessing

Prepares the dataset for analysis and machine learning.

Feature engineering is also performed by creating:

- Age Group
- Experience Level
- Salary Category
- Satisfaction Level
- Overtime Category

### 5. Statistical Analysis

Performs statistical calculations such as:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation
- Correlation analysis

### 6. Probability Analysis

Calculates probabilities related to employee resignation and HR conditions.

Examples include:

- Probability of resignation
- Probability of promotion
- Conditional resignation probabilities

### 7. Sampling and Inference

A sample of employees is selected from the dataset and used to estimate the resignation rate.

A 95% confidence interval is also calculated for the sample resignation rate.

### 8. Hypothesis Testing

An independent two-sample t-test is performed to compare employee satisfaction scores between employees who resigned and employees who stayed.

The analysis uses SciPy.

### 9. Data Visualization

The project contains visualizations for:

- Workforce distribution by department
- Resignation rate by department
- Resignation rate by satisfaction level
- Resignation rate by overtime level
- Average satisfaction by resignation status
- Actual employee resignation status

### 10. Machine Learning

Logistic Regression is used to predict whether an employee is likely to resign.

The machine learning pipeline includes:

- Train-Test Split
- One-Hot Encoding
- StandardScaler
- Logistic Regression
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The dataset is divided into 80% training data and 20% testing data.

### 11. CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

The project demonstrates adding, viewing, updating, and deleting employee records.

CRUD records are stored separately in:

```text
output/hr_employee_records.csv