# COVID-19 Data Analysis and Regression

This project involves analyzing COVID-19 data and performing regression analysis to predict the number of deaths based on the number of recoveries and the number of countries affected. The data is visualized using line plots and regression plots to understand the relationship between the variables.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Data Preprocessing](#data-preprocessing)
4. [Data Visualization](#data-visualization)
5. [Regression Analysis](#regression-analysis)
6. [Results Interpretation](#results-interpretation)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Future Improvements](#future-improvements)

## Project Overview

The goal of this project is to:
- Clean and preprocess the COVID-19 dataset.
- Visualize the data to observe trends in deaths, recoveries, and affected countries.
- Perform regression analysis to determine the relationship between the number of recoveries and deaths, and also the number of countries affected if available.

## Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Data Preprocessing

The data is loaded from a CSV file hosted on Google Drive. The following preprocessing steps are applied:

1. **Handling missing data**: Rows containing missing values are dropped.
2. **Duplicate removal**: Duplicate rows are identified and removed.
3. **Outlier detection**: Descriptive statistics are generated to detect potential outliers. Further steps can be applied if necessary to handle outliers.
4. **Inconsistent or incorrect data**: Data is inspected for inconsistencies and cleaned as needed.

## Data Visualization

The data is visualized using line plots to show the number of deaths, recoveries, and affected countries over time. This helps in understanding trends and the progression of the pandemic.

## Regression Analysis

A linear regression model is created using the `LinearRegression` class from the `sklearn` library. The independent variables used in the model are the number of recovered cases and the number of affected countries (if available). The dependent variable is the number of deaths.

### Regression Plots

The regression plots visualize the relationship between the dependent and independent variables:

- **Deaths vs Recovered Cases**
- **Deaths vs Number of Countries Affected** (if the column is present)

## Results Interpretation

The coefficients of the linear regression model are printed to provide insights into the relationship between the variables.

- **Coefficient for Recovered Cases**: Represents the change in the number of deaths for a unit increase in recovered cases.
- **Coefficient for Number of Countries Affected**: (if available) Represents the change in the number of deaths for each additional country affected.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/eshmehar/covid19-analysis.git
    ```
2. Install the required Python packages:
    ```bash
    pip install pandas matplotlib seaborn scikit-learn
    ```

## Usage

1. Load the data by replacing the Google Drive URL with your own CSV file link (if necessary).
2. Run the script to clean the data, visualize the trends, and perform the regression analysis.
3. Observe the regression coefficients to interpret the impact of the independent variables on the number of deaths.

## Future Improvements

- Implement more sophisticated outlier detection and handling techniques.
- Explore non-linear regression models or other machine learning algorithms.
- Add time-series analysis to predict future trends in COVID-19 cases.
