---

layout: default
title: Machine Learning Desktop Application
---

<div class="project-page" markdown="1">

<p class="project-kicker">FEATURED PROJECT · MACHINE LEARNING · PYTHON</p>

# Machine Learning Desktop Application

### An end-to-end machine learning workflow built as a Python desktop application

A desktop application built with **Python and PyQt5** that takes the user through the complete machine learning workflow — from synthetic data generation and cleaning to exploratory analysis, model training, evaluation and model persistence.

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Proyecto-final-machine-learning-en-Deusto">View on GitHub</a>
<a class="project-button secondary" href="https://drive.usercontent.google.com/download?id=1YWJ2tx1j1lj6hpa0lUCA7CevUgd51wPF&export=download&authuser=0">Download / Demo</a>
</p>

<span class="project-tech-tags">
<span class="project-tech-tag"><a href="/tags/tech/python.html">Python</a></span>
<span class="project-tech-tag"><a href="/tags/tech/pyqt5.html">PyQt5</a></span>
<span class="project-tech-tag"><a href="/tags/tech/pandas.html">Pandas</a></span>
<span class="project-tech-tag"><a href="/tags/tech/numpy.html">Numpy</a></span>
<span class="project-tech-tag"><a href="/tags/tech/scikit-learn.html">Scikit-learn</a></span>
<span class="project-tech-tag"><a href="/tags/tech/xgboost.html">XGBoost</a></span>
<span class="project-tech-tag"><a href="/tags/tech/matplotlib.html">Matplotlib</a></span>
<span class="project-tech-tag"><a href="/tags/tech/seaborn.html">Seaborn</a></span>
<span class="project-tech-tag"><a href="/tags/tech/github.html">GitHub</a></span>
</span>

<img class="project-hero-image" src="{{ '/images/app_hospitalizacion_gif.gif' | relative_url }}" alt="Machine learning desktop application">

---

## Overview

The application was developed around a synthetic patient-hospitalisation classification problem.

Rather than starting with a perfectly clean dataset, the application generates data containing controlled inconsistencies and then provides tools to prepare, analyse and model it.

The complete workflow is:

**Data generation → Data cleaning → EDA → Model training → Evaluation → Model export**

The project combines **data science, machine learning and Python application development** in a single desktop application.

---

## The application

Users can:

* Generate configurable synthetic datasets.
* Introduce controlled data inconsistencies.
* Clean and transform the resulting data.
* Perform exploratory data analysis.
* Visualise relevant variables and relationships.
* Train and compare classification models.
* Search for suitable hyperparameters.
* Evaluate models using several metrics.
* Export trained models together with their metadata.

The application also handles model training in the background so that long-running operations do not block the graphical interface.

---

## Machine Learning

Three classification algorithms are implemented.

### Logistic Regression

A `StandardScaler` + `LogisticRegression` pipeline is used so that preprocessing remains part of the model workflow and is correctly handled during cross-validation.

Hyperparameters are explored using `HalvingGridSearchCV`.

### Random Forest

A Random Forest classifier is used to explore the effect of parameters such as:

* number of estimators;
* tree depth;
* minimum samples per split;
* feature selection.

### XGBoost

XGBoost is trained using a dedicated validation set for early stopping while keeping the test set reserved for final evaluation.

---

## Results

The repository includes three trained example models together with their JSON metadata.

| Model               |   Accuracy |  Precision |     Recall |         F1 |
| ------------------- | ---------: | ---------: | ---------: | ---------: |
| Logistic Regression |     92.24% |     94.75% |     89.44% |     92.02% |
| **Random Forest**   | **97.68%** | **98.85%** | **96.48%** | **97.65%** |
| **XGBoost**         | **97.68%** | **98.85%** | **96.48%** | **97.65%** |

The example results show a clear performance improvement from Logistic Regression to the tree-based models on this dataset.

Because the dataset is synthetic, these figures demonstrate the modelling workflow rather than representing expected performance on real clinical data.

---

## Engineering

### Responsive GUI

Training and hyperparameter searches can be computationally expensive.

The application uses Qt's background execution mechanisms and signals to keep the GUI responsive while reporting progress back to the interface.

### Model persistence

Each trained model is stored in its own result directory together with a JSON metadata file.

The metadata preserves information about the experiment, including model configuration, evaluation metrics, dataset characteristics and software versions.

### Reproducibility

Random states are controlled throughout the main machine learning workflow, while the exported metadata preserves relevant information about each training run.

### Modular architecture

The application separates the graphical interface from:

* data generation;
* data analysis;
* visualisation;
* model training;
* background execution;
* model persistence.

---

## Architecture

```text
                       PyQt5 GUI
                           │
             ┌─────────────┼─────────────┐
             │             │             │
        Data & EDA    Model Training   Workers
             │             │             │
             └─────────────┼─────────────┘
                           │
                       Evaluation
                           │
                  Model Persistence
                           │
                  Results + Metadata
```

---

## Technologies

**Python · PyQt5 · Pandas · NumPy · Scikit-learn · XGBoost · Matplotlib · Seaborn · Joblib**

---

## What I learned

The main challenge was not simply training the models, but building the application around them.

The project gave me practical experience combining **data preparation, exploratory analysis, machine learning, GUI development, background execution and model persistence** into a complete Python application.

It also helped me move from working primarily with notebooks and isolated experiments towards building a reusable software project.

---

## Source code

The complete source code, example models, metadata and documentation are available on GitHub.

<p class="project-links">
<a class="project-button" href="https://github.com/Vaelico333/Proyecto-final-machine-learning-en-Deusto">View source code</a>
</p>

<p><a href="{{ '/' | relative_url }}">← Back to portfolio</a></p>

</div>
