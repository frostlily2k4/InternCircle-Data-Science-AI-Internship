\# Titanic Dataset – Exploratory Data Analysis (EDA)



\## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic passenger dataset using Python and Pandas.



The objective is to identify patterns in passenger survival based on gender, passenger class, and age group.



\## Technologies Used

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Google Colab



\## Dataset Information

\- Dataset: Titanic

\- Original records: 891

\- Original columns: 15

\- Records after cleaning: 891

\- Columns after cleaning: 13



\## Project Objectives

1\. Analyze survival rates by gender.

2\. Analyze survival rates by passenger class.

3\. Analyze survival rates by age group.

4\. Handle missing values and inspect duplicate records.

5\. Visualize important statistical findings.



\## Data Cleaning

\- Filled missing age values using median age grouped by passenger class and sex.

\- Filled missing embarked values using the mode.

\- Removed the deck column due to excessive missing values.

\- Removed the redundant embark\_town column.

\- Identified 118 identical rows and retained them because unique passenger identities could not be confirmed.



\## Key Findings



| Analysis | Result |

|---|---|

| Female survival rate | 74.20% |

| Male survival rate | 18.89% |

| First-class survival rate | 62.96% |

| Second-class survival rate | 47.28% |

| Third-class survival rate | 24.24% |

| Child survival rate | 57.97% |

| Senior survival rate | 22.73% |



\## Project Structure



```text

Titanic-EDA-Project-01/

├── Titanic\_EDA\_Project\_01.ipynb

├── README.md

└── screenshots/

&#x20;   ├── dataset\_preview.png

&#x20;   ├── gender\_survival.png

&#x20;   ├── class\_survival.png

&#x20;   └── age\_survival.png

```



\## Conclusion

The analysis identified differences in survival rates across gender, passenger class, and age groups. Female passengers, first-class passengers, and children had comparatively higher survival rates in this dataset.



This project demonstrates practical skills in data cleaning, statistical analysis, grouping, aggregation, and data visualization using Python.



\## Author

Jothi A



\## Project Type

Data Science \& AI Internship – Project 01



