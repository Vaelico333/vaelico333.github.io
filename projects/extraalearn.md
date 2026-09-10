---
layout: default
title: Lead Conversion Prediction
---

<div class="project-page" markdown="1">

<p class="project-kicker">DATA ANALYTICS & MACHINE LEARNING · PYTHON · BUSINESS INSIGHTS</p>

# Lead Conversion Prediction

<p class="project-subtitle">
Using customer behaviour data to identify high-potential leads, understand conversion drivers, and support more targeted marketing decisions.
</p>

<div class="project-buttons">
<a href="https\\:vaelico333.github.io" class="project-button">GitHub</a>
<a href="{{ '/gl/Learner2B-2BCode2B-2BCustomers%2BPrediction.html' | relative_url }}" class="project-button">HTML Report</a>
</div>

<div class="tech-tags">
<span>Python</span>
<span>Pandas</span>
<span>NumPy</span>
<span>Scikit-learn</span>
<span>Matplotlib</span>
<span>Seaborn</span>
<span>Machine Learning</span>
<span>Data Analysis</span>
</div>

<img class="project-hero-image" src="{{ '/images/extraalearn_front.png' | relative_url }}" alt="Lead Conversion Prediction">

---

## Overview

ExtraaLearn is an EdTech company that generates a large number of leads through digital channels such as its website, mobile application, social media and other marketing activities.

The business challenge is not simply generating leads, but identifying **which leads are more likely to become paying customers** so that sales and marketing resources can be allocated more effectively.

This project combines exploratory data analysis, feature engineering and classification models to:

- Identify leads with a higher probability of conversion.
- Understand the factors associated with successful conversion.
- Build a predictive classification model.
- Translate the analysis into actionable business recommendations.
- Define a profile of leads with a higher likelihood of becoming customers.

The project therefore goes beyond model training: the goal is to connect **data → prediction → business decision**.

---

## The Business Problem

When a company receives a large volume of leads, treating every lead in exactly the same way can result in inefficient use of sales resources.

ExtraaLearn needed to answer three practical questions:

1. **Which leads are most likely to convert?**
2. **What behaviours and characteristics are associated with conversion?**
3. **How can these insights be used to improve marketing and lead-nurturing strategies?**

The target variable, `status`, indicates whether a lead ultimately subscribed to a program.

This makes the problem a **binary classification task**, while the exploratory analysis provides the business context needed to interpret the predictions.

---

## Dataset

The dataset contains **4,612 leads** and **15 features** describing demographic characteristics, acquisition channels and interactions with ExtraaLearn.

Examples of the available variables include:

| Feature | Description |
|---|---|
| `age` | Age of the lead |
| `current_occupation` | Professional, unemployed or student |
| `first_interaction` | Website or mobile app |
| `profile_completed` | Level of profile completion |
| `website_visits` | Number of website visits |
| `time_spent_on_website` | Total time spent on the website |
| `page_views_per_visit` | Average pages viewed per visit |
| `last_activity` | Most recent interaction with ExtraaLearn |
| `print_media_type1` | Newspaper advertising exposure |
| `print_media_type2` | Magazine advertising exposure |
| `digital_media` | Digital advertising exposure |
| `educational_channels` | Exposure through educational channels |
| `referral` | Whether the lead came through a referral |
| `status` | Conversion target |

The dataset contained **no missing values**, while categorical variables had relatively low cardinality, making them suitable for categorical encoding.

### Conversion Distribution

Approximately **29.85% of leads converted**, while **70.15% did not**.

This class imbalance is important when evaluating the models: accuracy alone does not provide a complete picture of how well the model identifies potential customers.

---

## Exploratory Data Analysis

The exploratory analysis focused on understanding both the structure of the lead population and the relationship between customer behaviour and conversion.

Several patterns emerged.

### Lead Profile

Around **57% of leads were working professionals**, 31% were unemployed and 12% were students.

This suggests that the company's offering attracted a substantial proportion of people who were already working and potentially interested in upskilling or reskilling.

The first interaction was relatively balanced:

- 55% through the website.
- 45% through the mobile application.

Profile completion was concentrated among leads with more developed profiles, with approximately 49% having highly completed profiles and 48.5% having partially completed profiles.

### Recent Activity

Email was the most common form of recent interaction, accounting for approximately 49% of activity.

Website activity represented around 24%, while phone calls and SMS accounted for approximately 27%.

### Marketing Channels

The analysis also showed relatively limited exposure to several advertising channels:

- Newspaper: approximately 11%.
- Magazine: approximately 5%.
- Digital media: approximately 11%.
- Educational channels: approximately 15%.

These distributions provided useful context for evaluating the relative importance of the different acquisition channels.

---

## Profile Completion and Conversion

One of the clearest relationships identified during the analysis was the connection between **profile completeness and conversion**.

| Profile completion | Subscribed | Not subscribed |
|---|---:|---:|
| Low | 7.48% | 92.52% |
| Medium | 18.88% | 81.12% |
| High | 41.78% | 58.22% |

The conversion rate increases substantially as the lead's profile becomes more complete.

This makes profile completion a potentially useful behavioural signal when prioritising leads.

---

## Feature Engineering & Data Preparation

The dataset contained both numerical and categorical variables.

Categorical variables were transformed using one-hot encoding, allowing the classification algorithms to work with the categorical information while avoiding an artificial numerical ordering between categories.

The original `time_spent_on_website` variable was also transformed into a categorical/binary feature based on a threshold identified during the analysis.

This allowed the analysis to distinguish between leads with lower and higher levels of website engagement.

The resulting dataset was then prepared for model training and evaluation.

---

## Machine Learning

The project approached lead conversion as a supervised binary classification problem.

### Decision Tree

A Decision Tree was first explored as an interpretable model capable of capturing non-linear relationships between lead characteristics and conversion.

A simple tree based only on `time_spent_on_website` provided limited predictive performance, demonstrating that a single behavioural variable was not sufficient to accurately identify subscribers.

The more complete Decision Tree model performed considerably better by combining multiple lead characteristics.

### Random Forest

A Random Forest model was then used to combine multiple decision trees and improve predictive performance.

The final model achieved:

- **87% test accuracy**
- **76% F1-score for converted leads**
- **73% recall for converted leads**
- **80% precision for converted leads**

The model was evaluated on **1,384 test observations**, including 413 actual converted leads.

| Metric | Not Converted | Converted |
|---|---:|---:|
| Precision | 0.89 | 0.80 |
| Recall | 0.92 | 0.73 |
| F1-score | 0.91 | 0.76 |

The Random Forest performed slightly better than the Decision Tree, particularly in its overall balance between precision and recall.

---

## Model Comparison

The comparison highlighted the advantage of combining multiple decision trees rather than relying on a single tree.

| Model | Accuracy | Positive-class F1 |
|---|---:|---:|
| Decision Tree | 86% | 0.75 |
| Random Forest | **87%** | **0.76** |

The difference is relatively small, but the Random Forest provided the strongest overall performance in the analysis.

More importantly, the model demonstrated that lead conversion can be predicted using a combination of behavioural, acquisition and demographic characteristics rather than relying on a single variable.

---

## Model Interpretation

One of the most valuable parts of the project was not simply predicting conversion, but understanding **which variables contributed most to the predictions**.

The feature-importance analysis identified the following factors as particularly relevant.

### Strongest factors

**Time spent on the website**

Website engagement was the most important factor identified by the model. Leads spending more time exploring the website were more likely to convert.

**First interaction through the website**

Leads whose first interaction occurred through the website showed a stronger association with conversion than those whose first interaction was through the mobile application.

### Moderate factors

Other variables with a meaningful influence included:

- Profile completeness.
- Pages viewed per visit.
- Age.

These findings provided a bridge between the machine-learning model and practical marketing decisions.

---

## The Ideal Lead Profile

Combining the exploratory analysis and model interpretation produced a practical profile of a higher-potential lead.

The strongest profile identified in the analysis was a lead who:

- Discovered ExtraaLearn through a **referral**.
- First interacted with the company through the **website**.
- Has completed **50–100% of their profile**.
- Spends a **significant amount of time on the website**.
- Views a **high number of pages per visit**.

This profile is not intended to define an individual customer with certainty. Instead, it provides a practical framework for identifying leads with characteristics associated with a higher probability of conversion.

---

## Business Recommendations

The analysis suggests several ways the company could use these findings operationally.

### 1. Strengthen referral strategies

Referral was identified as the most impactful publicity channel in the analysis.

A **refer-a-friend programme** could therefore be tested as a way to generate more leads with characteristics associated with higher conversion rates.

### 2. Improve website visibility

Because website interaction was strongly associated with conversion, increasing the visibility of the website through **SEO** could help attract more relevant prospects.

### 3. Increase website engagement

The strong relationship between time spent on the website and conversion suggests that improving the website experience could be valuable.

Content, navigation and calls to action could be designed to encourage interested leads to explore the platform for longer and interact with more pages.

### 4. Target working professionals

Working professionals represented the largest segment of leads in the dataset.

A targeted campaign aimed at **middle-aged working professionals**, including campaigns through LinkedIn, could therefore be explored.

---

## From Data to Business Decision

One of the main objectives of this project was to avoid treating machine learning as an isolated modelling exercise.

The analytical process followed a complete path:

```text
Lead Data
    ↓
Exploratory Data Analysis
    ↓
Behaviour & Conversion Patterns
    ↓
Feature Engineering
    ↓
Classification Models
    ↓
Model Evaluation
    ↓
Feature Importance
    ↓
Lead Profile
    ↓
Marketing Recommendations
```

This approach demonstrates how Python and machine learning can be used not only to build predictive models, but also to transform raw customer data into information that can support business decisions.

---

## Key Findings

### Conversion is strongly linked to engagement

Time spent on the website was the most important factor identified by the model.

### Profile completion matters

Leads with more complete profiles showed substantially higher conversion rates.

### Website interaction is particularly relevant

The website played an important role both in initial interaction and in subsequent engagement.

### Referrals were a valuable acquisition channel

Referral leads were associated with the strongest conversion potential among the analysed publicity channels.

### Predictive modelling can support lead prioritisation

The Random Forest achieved **87% accuracy** and a **0.76 F1-score for converted leads**, providing a useful basis for prioritising leads while recognising the limitations of the dataset and evaluation.

---

## Limitations

The analysis also highlights several limitations that would need to be addressed before deploying such a system in a real business environment.

### Class imbalance

Only around 30% of leads converted, meaning that performance on the positive class is particularly important.

For this reason, precision, recall and F1-score should be considered alongside accuracy.

### Predictive performance is not perfect

Although the Random Forest achieved good overall performance, its recall for converted leads was 73%.

This means that a meaningful proportion of actual potential customers were still classified incorrectly.

### Association is not causation

The feature-importance analysis identifies variables associated with model predictions. It does not prove that changing one of these variables will directly cause conversion.

For example, increasing website time artificially would not necessarily increase the probability of conversion.

### Further validation would be required

Before using the model operationally, it would need to be validated on newer data and evaluated according to the actual costs of false positives and false negatives.

---

## Technologies

**Programming & Analysis**

- Python
- Pandas
- NumPy

**Data Visualization**

- Matplotlib
- Seaborn

**Machine Learning**

- Scikit-learn
- Decision Trees
- Random Forest

**Methods**

- Exploratory Data Analysis
- Categorical Encoding
- Feature Engineering
- Classification
- Model Evaluation
- Feature Importance
- Business-oriented Data Interpretation

---

## What I Learned

This project strengthened my ability to connect technical analysis with practical business questions.

### Data analysis

I learned to move from individual variables and distributions towards identifying patterns that could answer a specific business problem.

### Feature engineering

Transforming raw variables into useful model features showed how data preparation can influence both model performance and interpretability.

### Classification

The project provided practical experience with binary classification, Decision Trees and Random Forests, including the importance of evaluating the positive class rather than relying exclusively on accuracy.

### Model interpretation

Feature importance made it possible to move beyond prediction and understand which characteristics were most influential in the model.

### Business thinking

The most valuable part of the project was translating model outputs into a concrete lead profile and a set of potential marketing strategies.

---

## Source Code

The complete analysis, including the exploratory work, data preparation, modelling and evaluation, is available in the project repository.

<a href="https\\:vaelico333.github.io" class="project-button">View source code on GitHub →</a>

</div>