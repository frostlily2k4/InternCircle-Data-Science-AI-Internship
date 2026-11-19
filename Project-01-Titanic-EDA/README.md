# Titanic Dataset – Exploratory Data Analysis (EDA)

## Project Overview
This project focuses on analyzing the Titanic passenger dataset using Python. The goal is to understand passenger survival patterns based on gender, passenger class, and age group.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Dataset Information
- Dataset: Titanic
- Original records: 891
- Original columns: 15
- Records after cleaning: 891
- Columns after cleaning: 13

## Research Questions
1. Did female passengers survive more than male passengers?
2. Did passenger class affect survival rates?
3. Was age related to survival?

## Data Cleaning
- Filled missing age values using the median based on passenger class and sex.
- Filled missing embarked values using the mode.
- Removed the deck column because it had many missing values.
- Removed the redundant embark_town column.
- Identified 118 identical rows and retained them because they could represent different passengers.

## Key Findings

| Analysis | Survival Rate |
|---|---:|
| Female passengers | 74.20% |
| Male passengers | 18.89% |
| First-class passengers | 62.96% |
| Second-class passengers | 47.28% |
| Third-class passengers | 24.24% |
| Children | 57.97% |
| Senior passengers | 22.73% |

## Conclusion
The analysis showed that female passengers, first-class passengers, and children had comparatively higher survival rates. This project helped me understand data cleaning, statistical analysis, grouping, aggregation, and data visualization using Python.

## Project Structure

```text
Project-01-Titanic-EDA/
├── Titanic_EDA_Project_01.ipynb
├── README.md
└── screenshots/
    ├── dataset_preview.png
    ├── gender_survival.png
    ├── class_survival.png
    └── age_survival.png
```

## Author
Jothi A

## Internship
InternCircle – Data Science & AI Internship

Project 01: Exploratory Data Analysis (EDA) on Titanic
