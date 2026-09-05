# Logistics Driver Workforce Analysis

## Overview

This project presents the strategic planning and exploratory data analysis phase of a logistics analytics project focused on driver workforce management.

The analysis uses a dataset containing 150 driver records and examines driver availability, employment status, years of experience, CDL class, license state, and home terminal distribution. The objective is to demonstrate how Python and data analysis can support logistics workforce planning and resource allocation.

## Objectives

The main objectives of this project are to:

* Analyze the structure and quality of the driver dataset.
* Calculate key workforce performance indicators (KPIs).
* Examine driver distribution across home terminals.
* Analyze years of driver experience.
* Identify workforce patterns that may support resource allocation.
* Propose a roadmap for future clustering, predictive analytics, and optimization.

## Dataset

The dataset contains **150 driver records** with the following variables:

| Column              | Description                        |
| ------------------- | ---------------------------------- |
| `driver_id`         | Unique driver identifier           |
| `first_name`        | Driver first name                  |
| `last_name`         | Driver last name                   |
| `hire_date`         | Date of hire                       |
| `termination_date`  | Date of termination, if applicable |
| `license_number`    | Driver license number              |
| `license_state`     | License issuing state              |
| `date_of_birth`     | Driver date of birth               |
| `home_terminal`     | Driver's assigned terminal         |
| `employment_status` | Current employment status          |
| `cdl_class`         | Commercial Driver's License class  |
| `years_experience`  | Years of driving experience        |

## Key Performance Indicators

The analysis focuses on the following KPIs:

* Total number of drivers.
* Active driver rate.
* Average years of driving experience.
* Median years of driving experience.
* Number of drivers by home terminal.
* CDL class distribution.

## Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Visual Studio Code

## Analysis Workflow

```text
Data Collection
      ↓
Data Validation
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
KPI Calculation
      ↓
Terminal and Experience Analysis
      ↓
Driver Segmentation (Proposed)
      ↓
Resource Allocation Insights
      ↓
Business Recommendations
```

## Visualizations

The project includes the following charts:

* Number of Drivers by Home Terminal
* Distribution of Driver Experience
* Driver Employment Status
* Average Driver Experience by Home Terminal

## Key Findings

* The dataset contains **150 drivers**.
* **124 drivers are active**.
* The average driver experience is approximately **13.49 years**.
* The driver workforce is distributed across multiple home terminals.
* Driver experience varies between terminals, which may provide useful information for workforce planning and future resource allocation decisions.

## Future Scope

The current dataset focuses on driver workforce information. Future analysis could integrate additional logistics data such as:

* Vehicle information
* Delivery routes
* Shipment records
* Distance traveled
* Fuel consumption
* Traffic conditions
* Customer demand

With these additional datasets, the project could be extended to include:

* Driver clustering
* Workforce forecasting
* Delivery delay prediction
* Driver-to-route allocation
* Route and transportation optimization

## Files

* `drivers.csv` - Driver workforce dataset.
* `logistics_analysis.py` - Python analysis script.
* `Week_1_Strategic_Planning_Logistics_Report.docx` - Complete Week 1 strategic planning report.
* `*.png` - Visualizations generated during exploratory data analysis.

## Conclusion

This project establishes a data-driven approach to analyzing a logistics driver workforce using Python. The analysis provides baseline workforce insights and a strategic roadmap for future predictive analytics and optimization, supporting better workforce planning and logistics resource allocation.
