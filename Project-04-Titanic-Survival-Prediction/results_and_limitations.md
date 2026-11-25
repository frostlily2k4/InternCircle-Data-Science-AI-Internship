# Project 04: Results and Limitations

## 1. Project Summary

This project involved building a Decision Tree Classifier to predict Titanic passenger survival using Scikit-Learn.

The model used four features:
- Passenger class
- Sex
- Age
- Ticket fare

The target variable was `survived`, where 0 represents passengers who did not survive and 1 represents passengers who survived.

## 2. Model Performance

The dataset was divided into:
- Training set: 712 records (80%)
- Testing set: 179 records (20%)

A baseline model was created by always predicting the most common outcome (did not survive).

| Evaluation Metric | Result |
|---|---:|
| Baseline Accuracy | 61.45% |
| Decision Tree Accuracy | 77.65% |
| Mean Squared Error | 0.2235 |

The Decision Tree improved accuracy by 16.20 percentage points compared with the baseline.

## 3. Confusion Matrix Analysis

The confusion matrix was:

```text
[[105   5]
 [ 35  34]]
```

Interpretation:

- True Negative: 105 passengers were correctly predicted not to have survived.
- False Positive: 5 passengers were predicted to have survived but did not.
- False Negative: 35 passengers were predicted not to have survived but did.
- True Positive: 34 passengers were correctly predicted to have survived.

The model performed better at identifying passengers who did not survive than passengers who survived.

## 4. Overfitting Analysis

Different Decision Tree depths from 1 to 12 were tested.

The results showed:
- Training accuracy generally increased with tree depth.
- Testing accuracy fluctuated across different depths.
- At depth 12, training accuracy reached 93.68%, while testing accuracy was 81.01%.

This indicates that deeper trees can fit training data more closely without consistently improving performance on unseen data.

## 5. Feature Importance

The feature importance analysis produced the following results:

| Feature | Importance |
|---|---:|
| Sex | 0.598570 |
| Passenger Class | 0.208209 |
| Fare | 0.098815 |
| Age | 0.094407 |

Sex was the most influential feature in the trained model, followed by passenger class.

These values describe the model's use of features and do not establish causation.

## 6. Limitations

1. **Small Dataset:** The Titanic dataset contains only 891 passenger records, so the evaluation results may vary with a different data split.
2. **Missing Values:** Missing age values were replaced using the median, which may not represent every passenger accurately.
3. **Limited Features:** Only four features were used. Other passenger information might provide additional predictive value.
4. **Model Generalization:** The results come from one train/test split and may not represent performance on every unseen dataset.
5. **Class Imbalance:** Accuracy alone does not fully describe performance across survival classes.
6. **Feature Importance:** Feature importance indicates how the model uses features, not whether they caused survival.

## 7. What I Learned

Through this project, I gained practical experience in:

- Preparing data for Machine Learning.
- Handling missing values and encoding categorical variables.
- Splitting data into training and testing sets.
- Training a Decision Tree Classifier using Scikit-Learn.
- Establishing and comparing a baseline.
- Evaluating a model using accuracy, confusion matrix, and MSE.
- Understanding overfitting through tree depth experiments.
- Identifying important features.

## 8. Final Conclusion

The Decision Tree Classifier achieved 77.65% accuracy on the test dataset, outperforming the 61.45% baseline.

This project helped me understand the fundamentals of supervised Machine Learning, model evaluation, and the importance of testing models on unseen data.

**Project:** InternCircle Data Science & AI Internship – Project 04

**Author:** Jothi A