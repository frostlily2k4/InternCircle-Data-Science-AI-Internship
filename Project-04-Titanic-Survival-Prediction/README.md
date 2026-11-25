# Project 04: First Machine Learning Classifier

## Titanic Survival Prediction using Decision Tree Classifier

**Internship:** InternCircle Data Science & AI Internship

## 1. Project Overview

This project focuses on building a supervised Machine Learning classification model to predict whether a Titanic passenger survived or did not survive.

A Decision Tree Classifier from Scikit-Learn is used to train the model using passenger information such as passenger class, sex, age, and ticket fare.

The model is evaluated using an independent test dataset to understand its prediction performance.

## 2. Objective

To predict whether a passenger survived the Titanic disaster based on the following features:

- Passenger class (`pclass`)
- Sex (`sex`)
- Age (`age`)
- Ticket fare (`fare`)

**Target variable:** `survived`

- 0 – Did not survive
- 1 – Survived

## 3. Dataset Information

- **Dataset:** Titanic
- **Source:** Seaborn built-in dataset
- **Total records:** 891
- **Selected columns:** 5
- **Missing values:** 177 in the age column, handled using median imputation.

## 4. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Google Colab

## 5. Machine Learning Workflow

1. Loaded the Titanic dataset.
2. Selected the required features and target variable.
3. Handled missing age values using median imputation.
4. Converted sex into numerical values (male = 0, female = 1).
5. Split the dataset into 80% training and 20% testing data.
6. Calculated baseline accuracy.
7. Trained a Decision Tree Classifier with `max_depth=4`.
8. Evaluated predictions using accuracy, confusion matrix, and Mean Squared Error.
9. Tested different tree depths to investigate overfitting.
10. Analysed feature importance.

## 6. Model Evaluation Results

| Metric | Result |
|---|---:|
| Baseline Accuracy | 61.45% |
| Decision Tree Accuracy | 77.65% |
| Mean Squared Error | 0.2235 |
| Correct Predictions | 139 |
| Incorrect Predictions | 40 |

### Confusion Matrix

```text
[[105   5]
 [ 35  34]]
```

- True Negative: 105
- False Positive: 5
- False Negative: 35
- True Positive: 34

The Decision Tree achieved 77.65% accuracy, outperforming the baseline by 16.20 percentage points.

## 7. Overfitting Analysis

Different maximum tree depths from 1 to 12 were tested.

- Training accuracy generally increased as tree depth increased.
- Testing accuracy fluctuated between different depths.
- At depth 12, training accuracy reached 93.68%, while testing accuracy was 81.01%.

This demonstrates that increasing model complexity does not always guarantee better performance on unseen data.

## 8. Feature Importance

| Feature | Importance |
|---|---:|
| Sex | 0.598570 |
| Passenger Class | 0.208209 |
| Fare | 0.098815 |
| Age | 0.094407 |

Sex was the most influential feature in the trained Decision Tree, followed by passenger class.

## 9. Limitations

1. The dataset contains only 891 passenger records.
2. Missing age values were replaced with the median.
3. Only four input features were considered.
4. Results depend on the selected train/test split.
5. Feature importance does not establish causation.
6. Accuracy alone does not fully explain classification performance.

## 10. Conclusion

This project provided practical experience with a supervised Machine Learning pipeline using Scikit-Learn.

The Decision Tree Classifier achieved 77.65% test accuracy and performed better than the baseline model.

The project also demonstrated the importance of testing on unseen data, understanding confusion matrices, evaluating different tree depths, and identifying important features.

## Author

**Jothi A**

InternCircle Data Science & AI Internship

## Project Files

- `First_Machine_Learning_Classifier_Project_04.ipynb` – Complete Python notebook.
- `results_and_limitations.md` – Summary of model results and limitations.
