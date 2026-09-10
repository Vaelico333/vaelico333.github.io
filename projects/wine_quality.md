---
layout: default
title: Wine Quality Prediction
---

<div class="project-page" markdown="1">

<p class="project-kicker">MACHINE LEARNING PROJECT · PYTHON · DATA ANALYSIS</p>

# Wine Quality Prediction

### An end-to-end regression analysis exploring how physicochemical properties can be used to predict wine quality

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Wine-Quality-Study">View on GitHub</a>
<a class="project-button secondary" href="{{ '/gl/prueba_mod7_DZG.html' | relative_url }}" target="_blank" rel="noopener noreferrer">View HTML export</a>
</p>

<span class="project-tech-tags">
<span class="project-tech-tag"><a href="/tags/tech/python.html">Python</a></span>
<span class="project-tech-tag"><a href="/tags/tech/jupyter.html">Jupyter</a></span>
<span class="project-tech-tag"><a href="/tags/tech/pandas.html">Pandas</a></span>
<span class="project-tech-tag"><a href="/tags/tech/numpy.html">NumPy</a></span>
<span class="project-tech-tag"><a href="/tags/tech/scikit-learn.html">Scikit-learn</a></span>
<span class="project-tech-tag"><a href="/tags/tech/statsmodels.html">Statsmodels</a></span>
<span class="project-tech-tag"><a href="/tags/tech/matplotlib.html">Matplotlib</a></span>
<span class="project-tech-tag"><a href="/tags/tech/seaborn.html">Seaborn</a></span>
</span>

<img class="project-hero-image" src="{{ '/images/calidad_vino.png' | relative_url }}" alt="Wine quality prediction project">

---

## Overview

This project investigates whether the physicochemical properties of red wine can be used to predict its quality score.

I explored the dataset, analysed relationships between variables, evaluated multicollinearity and compared several regression approaches. The objective was not simply to train a model, but to understand how different preprocessing and feature-selection strategies affected predictive performance.

The complete workflow was:

**Data retrieval → Exploratory Data Analysis → Preprocessing → Feature Selection → Model Training → Evaluation → Residual Analysis**

The analysis was developed in Jupyter Notebook, combining Python, statistical analysis and data visualisation.

---

## Dataset

The project uses the **Red Wine Quality** dataset from the UCI Machine Learning Repository.

The dataset contains:

- **1,599 observations**
- **11 physicochemical features**
- **1 target variable: wine quality**
- All variables are numerical
- Quality scores range from **3 to 8**
- Mean quality score: **5.64**

The predictor variables describe properties such as fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, sulphur dioxide, density, pH, sulphates and alcohol.

The dataset contains no missing values, and all 12 columns are numeric. 
---

## Exploratory Data Analysis

The initial analysis focused on understanding the structure and relationships within the data before training the models.

### Feature relationships

A correlation matrix revealed several notable relationships between physicochemical variables.

Fixed acidity showed a correlation of approximately **0.67 with density** and **0.67 with citric acid**, while free and total sulphur dioxide were also strongly correlated. The strongest negative relationship highlighted in the analysis was between **pH and fixed acidity (-0.68)**.

These relationships suggested that multicollinearity could affect a linear regression model and motivated a dedicated feature-selection analysis.

### Data quality

The dataset contained **no missing values**, and the predictors were entirely numerical, so no categorical encoding or missing-value imputation was required.

---

## Data Preparation

I separated the predictors from the `quality` target and used an **80/20 train-test split**, keeping `random_state=17` to make the experiments reproducible.

Because the features have very different scales, I also evaluated standardized versions of the data using `StandardScaler`.

An important finding was that **standardization did not improve the Linear Regression model**: both the scaled and unscaled versions produced the same MSE and R².

---

## Feature Selection

### Variance Inflation Factor (VIF)

The correlation analysis indicated substantial multicollinearity, so I used **Variance Inflation Factor (VIF)** to investigate it more systematically.

Several variables showed extremely high VIF values:

| Feature | VIF |
| --- | ---: |
| Density | 1528.15 |
| pH | 1078.17 |
| Alcohol | 147.62 |
| Fixed acidity | 74.46 |
| Sulphates | 22.46 |
| Volatile acidity | 17.96 |

The analysis showed that `density`, `pH` and `fixed acidity` were particularly affected by multicollinearity.

I removed **pH, density and fixed acidity** and retrained the model.

An interesting result was that removing `alcohol`, despite its high VIF, actually reduced predictive performance. I therefore retained it because the experiments suggested that it contained useful information for predicting wine quality.

The VIF-based feature selection produced a small improvement in predictive performance.

---

## Principal Component Analysis

I also evaluated **Principal Component Analysis (PCA)** as an alternative dimensionality-reduction strategy.

After standardizing the predictors, I calculated the explained variance of the principal components. The first **8 components explained 94.68%** of the variance, while the first **9 components reached 97.81%**. The model therefore used the first 9 components to retain at least 95% of the variance. 
A Linear Regression model was then trained using these reduced features.

PCA produced the best overall performance among the approaches tested.

---

## Machine Learning

### Linear Regression

Linear Regression was used as the baseline regression model.

The baseline provided a useful reference for evaluating whether scaling, feature selection or dimensionality reduction actually improved the predictions.

### Standardized Linear Regression

The predictors were standardized before training.

The result was effectively identical to the unscaled model:

**MSE: 0.400 · R²: 0.413**

This showed that, for this particular Linear Regression experiment, scaling the predictors did not provide a measurable predictive benefit.

### VIF-based Linear Regression

After removing `pH`, `density` and `fixed acidity`, the model achieved:

**MSE: 0.395 · R²: 0.421**

This was a modest improvement over the baseline.

### PCA + Linear Regression

The PCA approach produced the strongest result:

**MSE: 0.393 · R²: 0.423**

The improvement over the original model was small, but PCA achieved both the lowest MSE and the highest R² among the final models compared.

### Polynomial Regression

I also tested polynomial regression with degrees from 1 to 4 to investigate whether a non-linear relationship could improve the model.

The degree-2 model performed best within this polynomial experiment, while higher degrees degraded performance substantially. Degree 4, for example, produced a negative R², indicating that it performed worse than a simple baseline based on the target mean.

The final degree-2 polynomial model used in the overall comparison achieved:

**MSE: 0.640 · R²: 0.388**

It therefore did not outperform the PCA-based Linear Regression model.

---

## Decision Tree Regression

As a final alternative, I tested a `DecisionTreeRegressor` using:

- `max_depth=6`
- `max_features=8`
- `splitter='random'`
- `criterion='squared_error'`
- `random_state=17`

The resulting model achieved:

**MSE: 0.433 · R²: 0.365**

The Decision Tree therefore performed worse than the Linear Regression approaches, particularly the PCA-based model.

---

## Model Comparison

| Model | MSE | R² |
| --- | ---: | ---: |
| Unscaled Linear Regression | 0.400 | 0.413 |
| Standardized Linear Regression | 0.400 | 0.413 |
| VIF Linear Regression | 0.395 | 0.421 |
| **PCA Linear Regression** | **0.393** | **0.423** |
| Polynomial Regression — Degree 2 | 0.640 | 0.388 |
| Decision Tree Regression | 0.433 | 0.365 |

### Best model

The **PCA + Linear Regression** approach achieved the best performance in the final comparison, with an MSE of **0.393** and an R² of **0.423**.

The improvement is relatively small, which is itself an important finding: the experiments suggest that the available physicochemical variables contain useful predictive information, but they do not explain most of the variation in the wine quality score.

---

## Residual Analysis

Model evaluation was not limited to MSE and R².

I analysed the residuals using histograms and Q-Q plots to investigate their distribution and identify potential anomalies.

For the baseline Linear Regression model, the residuals were approximately normally distributed and centred around zero, although a small number of observations deviated from the expected distribution, particularly in the left tail.

This provided an additional diagnostic perspective beyond the aggregate performance metrics.

---

## Key Findings

- **Standardization did not improve Linear Regression** for this dataset.
- The dataset contains substantial **multicollinearity**, particularly involving density, pH and fixed acidity.
- **VIF-based feature selection** produced a modest improvement.
- `alcohol` showed high multicollinearity but removing it reduced predictive performance, demonstrating that statistical diagnostics need to be considered alongside model performance.
- **PCA provided the best final result**, although the improvement over the baseline was small.
- Polynomial regression did not provide a meaningful improvement and became considerably worse at higher degrees.
- The Decision Tree performed worse than the linear approaches tested.
- Residual analysis suggested that the baseline model's errors were approximately normally distributed, with a few notable deviations.

---

## Limitations

The results should be interpreted in the context of this dataset and experimental setup.

The model explains only around **42% of the variance** in wine quality, so the physicochemical variables included here are not sufficient to accurately predict the complete quality score.

Wine quality is also inherently subjective, and the dataset does not capture every factor that could influence the target. A stronger model would therefore require further investigation of additional variables, alternative modelling approaches and potentially more advanced validation and hyperparameter optimisation.

The purpose of this project is consequently not to produce a production-ready wine-quality predictor, but to demonstrate a complete process of **data exploration, statistical diagnosis, feature selection, model comparison and evaluation**.

---

## Technologies

**Python · Pandas · NumPy · Scikit-learn · Statsmodels · Matplotlib · Seaborn · Jupyter Notebook**

---

## What I learned

This project strengthened my understanding of the complete regression workflow, from exploratory analysis through to model evaluation.

In particular, I gained practical experience with:

- **Exploratory Data Analysis**
- **Correlation analysis**
- **Multicollinearity and VIF**
- **Feature selection**
- **Standardization**
- **Principal Component Analysis**
- **Polynomial regression**
- **Decision Tree regression**
- **MSE and R² evaluation**
- **Residual analysis and Q-Q plots**

More importantly, the project reinforced the importance of **comparing approaches rather than assuming that a more complex model will necessarily perform better**.

---

## Source code

The complete Jupyter project and HTML export are available on GitHub.

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Wine-Quality-Study">View source code</a>
</p>

<p><a href="{{ '/' | relative_url }}">← Back to portfolio</a></p>

</div>