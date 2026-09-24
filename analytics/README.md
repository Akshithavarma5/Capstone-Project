# Module 2 — Titanic Analytics and Machine Learning Pipeline

## 1. Project Overview

This project builds an end-to-end analytics and machine learning pipeline using the Titanic dataset.

The project covers data profiling, data cleaning, exploratory data analysis (EDA), preprocessing, classification, class imbalance handling, hyperparameter tuning, regression, model evaluation, and deployment-ready pipeline saving.

---

## 2. Dataset

Dataset: Titanic dataset from Seaborn.

- Rows after cleaning: 889
- Original rows: 891
- Original columns: 15
- Columns after cleaning: 14
- Target variable for classification: `survived`
- Regression target: `fare`

The cleaned dataset was saved as:

`titanic.csv`

---

## 3. Data Cleaning

Missing values were analyzed before modeling.

### Missing-value handling

- `age`: median imputation
- `embarked`: rows with missing values removed
- `embark_town`: rows with missing values removed
- `deck`: removed because approximately 77% of its values were missing

After cleaning:

- Missing values remaining: 0
- Final dataset shape: `(889, 14)`

---

## 4. Exploratory Data Analysis

The following analyses were performed:

### Univariate Analysis

- Age histogram
- Age box plot
- Fare histogram
- Fare box plot
- IQR-based outlier analysis
- Mean, median, and mode analysis

Fare was found to be right-skewed because:

- Mean ≈ 32.10
- Median ≈ 14.45
- Mode ≈ 8.05

### Bivariate Analysis

Survival was analyzed by:

- Sex
- Passenger class
- Sex and passenger class

### Correlation Analysis

The strongest correlations were:

- `pclass` and `fare`: approximately `-0.55`
- `sibsp` and `parch`: approximately `0.41`

### Multivariate Analysis

The project analyzed:

- Survival by sex and passenger class
- Survival by age group
- Fare distribution by survival status
- Survival rate by passenger class

---

## 5. Train/Test Split

The classification dataset was split using:

- 80% training data
- 20% testing data
- `random_state=42`
- Stratification based on the target variable

Training set:

- 711 rows

Testing set:

- 178 rows

Stratification preserved the original class distribution.

---

## 6. Preprocessing

A `ColumnTransformer` was used.

### Numerical features

- `pclass`
- `age`
- `sibsp`
- `parch`
- `fare`

Processing:

1. Median imputation
2. StandardScaler

### Categorical features

- `sex`
- `embarked`

Processing:

1. Most-frequent imputation
2. One-hot encoding

The preprocessing was fitted only on training data to prevent data leakage.

---

## 7. Classification Models

The following models were trained:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Balanced Random Forest
5. SMOTE Random Forest
6. Tuned Random Forest

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- AUC

---

## 8. Classification Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.8090 | 0.7833 | 0.6912 | 0.7344 |
| Decision Tree | 0.7697 | 0.6901 | 0.7206 | 0.7050 |
| Random Forest | 0.8202 | 0.7812 | 0.7353 | 0.7576 |
| Balanced Random Forest | 0.8034 | 0.7391 | 0.7500 | 0.7445 |
| SMOTE Random Forest | 0.7921 | 0.7460 | 0.6912 | 0.7176 |
| Tuned Random Forest | 0.8315 | 0.8654 | 0.6618 | 0.7500 |

---

## 9. ROC and AUC

| Model | AUC |
|---|---:|
| Logistic Regression | 0.861 |
| Decision Tree | 0.754 |
| Random Forest | 0.819 |

---

## 10. Class Imbalance Handling

The training data contained:

- Class 0: 439 samples (61.74%)
- Class 1: 272 samples (38.26%)

Two imbalance-handling approaches were evaluated:

### Balanced Random Forest

Used:

`class_weight="balanced"`

### SMOTE

SMOTE was applied only to the training data.

The test data remained unchanged to prevent data leakage.

---

## 11. Random Forest Hyperparameter Tuning

GridSearchCV was used with 5-fold cross-validation.

Parameters tested:

- `n_estimators`: 50, 100, 200
- `max_depth`: None, 5, 10
- `max_features`: sqrt, log2

Best parameters:

```text
n_estimators = 200
max_depth = 5
max_features = sqrt