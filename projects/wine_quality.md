---
layout: default
title: Extraalearn analysis
---

<div class="project-page" markdown="1">

<p class="project-kicker"> MACHINE LEARNING PROJECT · PYTHON · JUPYTER</p>

# Machine Learning Desktop Application

### 

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Wine-Quality-Study">View on GitHub</a>
<a class="project-button secondary" href="{{ '/projects/wine_quality.html' | relative_url }}" target="_blank" rel="noopener noreferrer">View HTML export</a>
</p>

<span class="project-tech-tags">
<span class="project-tech-tag"><a href="/tags/tech/python.html">Python</a></span>
<span class="project-tech-tag"><a href="/tags/tech/jupyter.html">Jupyter</a></span>
<span class="project-tech-tag"><a href="/tags/tech/seaborn.html">Seaborn</a></span>
<span class="project-tech-tag"><a href="/tags/tech/matplotlib.html">Matplotlib</a></span>
<span class="project-tech-tag"><a href="/tags/tech/numpy.html">Numpy</a></span>
<span class="project-tech-tag"><a href="/tags/tech/pandas.html">Pandas</a></span>
<span class="project-tech-tag"><a href="/tags/tech/scikit-learn.html">Scikit-learn</a></span>
</span>

<img class="project-hero-image" src="{{ '/images/app_hospitalizacion_gif.gif' | relative_url }}" alt="Machine learning desktop application">

---

## Overview

This is an education project where I created a model capable of predicting the quality of a given wine, based on its characteristics (e.g., citric acid, chlorides, density, pH...).  
It's written in `Jupyter Notebook` format, due to its simplicity and effectiveness in documenting both the process and the results via data visualization.

---

## Process

The complete workflow is:
**Data retrieval → EDA → Preprocessing → Model Training → Model Evaluation → Visualization**  
At first, I trained a `Linear Regression` model with standardization, and another one without it, to have something to compare with, but I saw that the results were suboptimal, so I went for feature selection, and added a bonus `Decision Tree Classifier` for flavour.

---

## Machine Learning

For a problem like this one, where we want to predict a number (quality) based on a series of features, the ideal model is a linear one, like `Linear Regression`.

---

### Linear Regression

I chose `Linear Regression` for its effectiveness at predicting numeric outcomes.

---

#### Unstandardized Model

In order to compare the effectiveness of the standardization and to have a first glance at the problem, I created a `Linear Regression` model with the raw data.

---

#### Standardized Model

Standardization didn´t make a difference, but it was worth a shot.

---

#### VIF Selected Features

Given the mediocre performance of the `Linear Regression` model, I used `VIF` (Variance Inflation Factor) to discard the features that make the model worse. The model's performance improved slightly.

---

#### PCA Selected Features

Using `PCA` (Principal Components Analysis), I achieved a slight improvement from the original model.

---

#### Polynomial Lineal Regression

I created a function that iterates through `Linear Regression` models with polynomial features, from grade 1 to 5, in order to compare them and select the best.  
The model's performance was quite weak, even a bit worse than the previous attempts.

---

### Bonus: Decision Tree

I decided to try a `Decision Tree Regressor` model, but the results were worse than any other.

---

## Results

| Model | MSE | R² |
| ------ | ---: | --: |
| Unscaled Linear Regression | 0.400 | 0.413 |
| Standardized Linear Regression | 0.400 | 0.413 |
| VIF Linear Regression | 0.395 | 0.421 |
| PCA Linear Regression | 0.393 | 0.423 |
| Decision Tree Regressor | 0.422 | 0.380 |

The best model was `Linear Regression` with `PCA` selected features.

---

## Technologies

**Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn**

---

## What I learned

The main challenge was to improve the model's performance, which I achieved to some point.  
I mainly learned how to **select features**, **build a polynomial model** and appraise a model's performance.

---

## Source code

The complete source code in Jupyter and the HTML export are available on Github.

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Wine-Quality-Study">View source code</a>
</p>

<p><a href="{{ '/' | relative_url }}">← Back to portfolio</a></p>

</div>
