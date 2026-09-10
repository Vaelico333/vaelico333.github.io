---
layout: default
title: Python Flask Web Application
---

<div class="project-page" markdown="1">

<p class="project-kicker">PYTHON WEB DEVELOPMENT · FLASK · DATABASES · DATA VISUALIZATION</p>

# Python Web Application

<p class="project-subtitle">
A modular Flask web application combining user authentication, database management, contact management, and interactive data analysis.
</p>

<div class="project-buttons">
<a href="https://github.com/Vaelico333/Proyecto-final-python-en-Deusto" class="project-button">GitHub</a>
</div>

<span class="project-tech-tags">
<span class="tech-tag"><a href="/tags/tech/python.html">Python</a></span>
<span class="tech-tag"><a href="/tags/tech/flask.html">Flask</a></span>
<span class="tech-tag"><a href="/tags/tech/sql.html">SQLAlchemy</a></span>
<span class="tech-tag"><a href="/tags/tech/sql.html">SQLite</a></span>
<span class="tech-tag"><a href="/tags/tech/flask.html">Flask-Login</a></span>
<span class="tech-tag"><a href="/tags/tech/pandas.html">Pandas</a></span>
<span class="tech-tag"><a href="/tags/tech/matplotlib.html">Matplotlib</a></span>
<span class="tech-tag"><a href="/tags/tech/seaborn.html">Seaborn</a></span>
</span>

<img class="project-hero-image" src="{{ '/images/flask_web_front.png' | relative_url }}" alt="Machine learning desktop application">


---

## Overview

This project is a multi-purpose web application built with **Python and Flask**, combining several independent features inside a single modular application.

Rather than building a single-purpose website, I designed the project around three different functional areas:

- A **contact management system** with full CRUD operations.
- A **user administration system** with authentication and account management.
- A **data analysis dashboard** for exploring COVID-19 data through interactive visualizations.

The application uses a relational database through SQLAlchemy, separates functionality into Flask blueprints, and processes analytical data using Pandas and visualization libraries.

The project therefore combines several areas of Python development in one application:

```text
Web Application
      │
      ├── User Management
      │     ├── Registration
      │     ├── Login
      │     ├── Authentication
      │     ├── Editing
      │     └── Deletion
      │
      ├── Contact Management
      │     ├── Create
      │     ├── Read
      │     ├── Update
      │     └── Delete
      │
      └── Data Analysis
            ├── Data processing
            ├── Aggregation
            ├── Bar charts
            └── Pie charts
```

---

## The Application

The application is structured around a central Flask application with separate blueprints for its main areas of functionality.

This keeps the different features isolated while allowing them to operate as part of the same web application.

The main modules are:

### User Management

<img class="project-hero-image" src="{{ '/images/flask_web_access.png' | relative_url}}" alt="Login page">

A user administration system providing:

- User registration.
- Login and logout.
- Password verification.
- User editing.
- User deletion.
- Authentication-protected pages.
- Persistent user information stored in the database.

### Contact Management

<img class="project-hero-image" src="{{ '/images/flask_web_address.png' | relative_url}}" alt="Address book managing page">

An agenda system allowing authenticated users to:

- Create contacts.
- Search for contacts.
- View contact details.
- Edit contacts.
- Delete contacts.
- Display contacts associated with the current user.

### Data Analysis

<img class="project-hero-image" src="{{ '/images/flask_web_analysis.png' | relative_url}}" alt="Frontpage of the Analysis part">

A data analysis dashboard that processes a COVID-19 dataset and allows the user to explore different indicators through visualizations.

The dashboard supports:

- Deaths.
- New cases.
- Hospitalizations.
- ICU admissions.

The data can be visualized by **day of the week** and by **province**.

---

## Application Architecture

The project uses Flask's **Blueprint** architecture to separate the application's functionality.

```text
Flask Application
│
├── Main application
│
├── Agenda Blueprint
│   ├── Routes
│   ├── Forms
│   ├── Models
│   └── Templates
│
├── Users Blueprint
│   ├── Authentication
│   ├── Forms
│   └── Templates
│
└── Analysis Blueprint
    ├── Routes
    ├── Forms
    ├── Services
    └── Templates
```

The main application registers the three blueprints independently, allowing each area to maintain its own routes and templates.

This structure makes the codebase easier to navigate and provides a foundation for extending the application with additional modules.

---

## Database & ORM

The application uses **SQLAlchemy** to interact with a SQLite database.

The database contains a user model with fields including:

- ID.
- Email.
- Name.
- Surname.
- Phone number.
- Age.
- Password hash.

The application uses SQLAlchemy's ORM functionality rather than handling SQL queries directly throughout the application.

For example, user records can be retrieved, updated and deleted through model/database operations while keeping database interaction separated from the presentation layer.

---

## Authentication & Security

User authentication is implemented using **Flask-Login**.

Protected routes use authentication checks so that functionality such as the user administration and contact management sections is restricted to authenticated users.

The application also avoids storing plain-text passwords.

Passwords are converted into hashes using Werkzeug before being stored in the database:

```python
user.set_password(form.contraseña.data)
```

Authentication then verifies the supplied password against the stored hash rather than comparing plain-text credentials.

This project therefore provided practical experience with:

- Login sessions.
- Protected routes.
- User authentication.
- Password hashing.
- User-specific data access.

---

## Contact Management — CRUD

The agenda module implements the four fundamental CRUD operations:

```text
CREATE
   ↓
Create a new contact

READ
   ↓
List / search / view contacts

UPDATE
   ↓
Edit an existing contact

DELETE
   ↓
Remove a contact
```

Contacts contain information such as:

- Name.
- Telephone number.
- Email address.
- Associated user.

The application also restricts the contact list according to the authenticated user, while providing broader access for the administrator account.

This part of the project demonstrates the connection between:

**HTTP request → Flask route → form → database operation → rendered template**

---

## Forms & Input Validation

The application uses Flask form classes to handle user input.

Separate forms are used for operations such as:

- User registration.
- User login.
- User editing.
- User deletion.
- Password confirmation.
- Contact creation.
- Contact search.

This provides a structured way of validating and processing information submitted through the web interface.

The contact management system, for example, validates the submitted form before creating or updating database records.

---

## Data Analysis Dashboard

The third component of the application turns the project into a small data-analysis platform.

The dashboard works with a COVID-19 dataset containing information organised by date and province.

The user can select different indicators:

- Deaths.
- New cases.
- Hospitalizations.
- ICU admissions.

The application then processes the data and generates visualizations dynamically.

---

## Data Processing Pipeline

The analysis module follows a simple data pipeline:

```text
COVID-19 CSV
     ↓
Data ingestion
     ↓
JSON-based local data store
     ↓
Pandas DataFrame
     ↓
Data transformation
     ↓
Aggregation
     ↓
Visualization
     ↓
Flask web interface
```

The application initially reads the CSV data and stores it in a local JSON-formatted text file.

The analysis service then loads this data into a Pandas DataFrame for processing.

This separation means that the visualization layer does not need to deal directly with the original CSV file.

---

## Data Analysis by Day of the Week

The analysis module converts the original date field into a day-of-week variable.

The data is then grouped by:

- Province.
- Day of the week.
- Selected indicator.

This allows the application to generate bar charts showing how deaths, cases, hospitalizations or ICU admissions are distributed across the days of the week.

The implementation also allows the user to focus on the provinces with the highest number of occurrences.

---

## Data Analysis by Province

The second visualization provides a provincial breakdown using pie charts.

The application:

1. Groups the selected metric by province.
2. Removes provinces with zero occurrences.
3. Sorts provinces by the selected metric.
4. Allows the analysis to focus on the top provinces.
5. Generates the resulting chart dynamically.

This provides a second perspective on the same dataset:

**Temporal perspective**

> How does the selected indicator vary by day of the week?

**Geographical perspective**

> How is the selected indicator distributed across provinces?

---

## Visualization

The analysis module uses **Matplotlib and Seaborn** to generate charts.

The charts are rendered server-side and converted into Base64 data URIs before being passed to the HTML templates.

This allows the generated visualizations to be displayed directly within the web application without requiring a separate chart server.

The analysis service also configures Matplotlib to use a non-interactive backend, which is appropriate for generating images from a web application rather than displaying them through a desktop interface.  
  
There are two kinds of charts, depending on the way we want to categorize the data:


### Total cases per province and day of the week - Bar Chart

We can view the whole dataset:
<img class="project-hero-image" src="{{ '/images/flask_web_barchart_all.png' | relative_url}}" alt="Bar chart of the whole dataset by province and day of the week">
  
Or just the 10 most prominent ones:
<img class="project-hero-image" src="{{ '/images/flask_web_barchart_ten.png' | relative_url}}" alt="Bar chart of the ten highest by province and day of the week">

### Percentage of ocurrence per province - Pie Chart

We can view the whole dataset:
<img class="project-hero-image" src="{{ '/images/flask_web_piechart_all.png' | relative_url}}" alt="Pie chart of the whole dataset by province">
  
Or just the 10 most prominent ones:
<img class="project-hero-image" src="{{ '/images/flask_web_piechart_ten.png' | relative_url}}" alt="Pie chart of the ten highest by province">

---

## Backend Flow

A typical analysis request follows this process:

```text
User selects metric
        ↓
Flask receives request
        ↓
Analysis route processes selection
        ↓
Service loads data
        ↓
Pandas transforms & aggregates data
        ↓
Matplotlib / Seaborn creates chart
        ↓
Chart converted to image data
        ↓
Flask renders template
        ↓
User sees visualization
```

This was an important part of the project because it required connecting **web development and data analysis inside the same Python application**.

---

## Project Structure

The repository is organised into a modular Flask application:

```text
proyecto-triple/
│
├── app/
│   ├── agenda/
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── routes.py
│   │
│   ├── analisis/
│   │   ├── forms.py
│   │   ├── routes.py
│   │   └── services.py
│   │
│   ├── templates/
│   │   ├── agenda/
│   │   ├── analisis/
│   │   └── usuarios/
│   │
│   ├── static/
│   │   └── css/
│   │
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
│
├── config.py
└── data/
```

The separation between routes, forms, models, services, templates and static resources makes the application considerably more maintainable than placing all functionality into a single Python file.

---

## Technologies

### Backend

- Python
- Flask
- Flask Blueprints
- Flask-Login
- SQLAlchemy

### Database

- SQLite
- SQLAlchemy ORM

### Data Analysis

- Pandas
- Matplotlib
- Seaborn

### Frontend

- HTML
- CSS
- Jinja templates

### Development Concepts

- MVC-style separation
- CRUD operations
- Authentication
- Form handling
- Database modelling
- Data transformation
- Server-side visualization
- Modular application architecture

---

## What I Learned

This project was particularly valuable because it brought together several areas of Python development that are often learned separately.

### Building a Flask application

I gained practical experience structuring a Python web application using Flask, routes, templates and blueprints.

### Working with databases

Using SQLAlchemy provided practical experience modelling data and connecting a Python application to a relational database.

### Authentication

Implementing registration, login, protected routes and password hashing helped me understand how user authentication fits into a web application.

### CRUD architecture

The contact-management component provided practical experience implementing the complete lifecycle of database records.

### Combining Python and data visualization

The analysis module allowed me to integrate Pandas, Matplotlib and Seaborn directly into a Flask application.

### Modular software design

Separating the application into blueprints, routes, forms, models, services and templates made the code easier to understand and maintain.

---

## Why This Project Matters

This project demonstrates a different side of my Python skills from my machine-learning work.

While my ML projects focus on **data analysis, predictive modelling and statistical reasoning**, this application demonstrates my ability to use Python to build a complete software product around a web interface.

It brings together:

```text
Python
  +
Web Development
  +
Databases
  +
Authentication
  +
Data Analysis
  +
Data Visualization
```

For a Python-focused role, this combination demonstrates that I can work beyond isolated scripts or notebooks and build applications where different technical components have to work together.

---

## Limitations & Possible Improvements

The project provides a solid foundation, but several aspects could be developed further.

### Deployment

The application could be deployed to a production hosting environment with environment-specific configuration.

### Database scalability

SQLite is appropriate for a lightweight application, but a production deployment with multiple concurrent users could benefit from a server-based relational database.

### Testing

A larger automated test suite could be added to validate routes, forms, database operations and analysis functions.

### API layer

The analytical functionality could be separated into a REST API, allowing other applications or frontend clients to consume the processed data.

### Interactive visualization

The current charts are generated as images. A future version could use a browser-based visualization library to provide interactive filtering, tooltips and dynamic exploration.

### Deployment security

Production deployment would require stronger secret management and configuration practices than the development-oriented setup currently used.

---

## Source Code

The complete source code is available on GitHub.

<a href="https://github.com/Vaelico333/Proyecto-final-python-en-Deusto" class="project-button">View source code on GitHub →</a>

</div>