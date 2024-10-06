import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Step 1: Load the data into a pandas DataFrame
url = 'https://drive.google.com/uc?id=1-0RS3gnpIn-3hKPDpHACThgY4lgoC6bk'
df = pd.read_csv(url)

# Check for missing data
print(df.isnull().sum()) # Count the number of missing values in each column
df.dropna(inplace=True) # Drop the rows that contain missing data

# Check for duplicates
print(df.duplicated().sum()) # Count the number of duplicate rows
df.drop_duplicates(inplace=True) # Drop the duplicate rows

# Check for outliers
print(df.describe()) # Compute descriptive statistics
# Apply outlier detection method and remove outliers if necessary

# Check for inconsistent or incorrect data
# Inspect the data and clean it up if necessary

# Standardize or normalize the data if necessary
# Apply scaling or transformation methods as needed


# Step 2: Visualize the data using line plots
plt.figure(figsize=(10,5))
plt.plot(df['Deaths'], label='Deaths')
plt.plot(df['Recovered'], label='Recovered')
if 'No_of_countries_affected' in df.columns:
    plt.plot(df['No_of_countries_affected'], label='No of countries affected')
plt.xlabel('Date')
plt.ylabel('Number of cases')
plt.title('COVID-19 Cases Over Time')
plt.legend()
plt.show()

# Step 3: Perform a regression analysis on the data
if 'No_of_countries_affected' in df.columns:
    X = df[['Recovered', 'No_of_countries_affected']] # independent variables
else:
    X = df[['Recovered']] # independent variable
y = df['Deaths'] # dependent variable
model = LinearRegression()
model.fit(X, y)

# Step 4: Visualize the results of the regression analysis
plt.figure(figsize=(10,5))
sns.regplot(x=X['Recovered'], y=y, ci=None)
plt.xlabel('Number of Recovered Cases')
plt.ylabel('Number of Deaths')
plt.title('Regression Analysis of COVID-19 Deaths and Recoveries')
plt.show()

if 'No_of_countries_affected' in df.columns:
    plt.figure(figsize=(10,5))
    sns.regplot(x=X['No_of_countries_affected'], y=y, ci=None)
    plt.xlabel('Number of Countries Affected')
    plt.ylabel('Number of Deaths')
    plt.title('Regression Analysis of COVID-19 Deaths and Number of Countries Affected')
    plt.show()

# Step 5: Interpret the results of the regression analysis
if 'No_of_countries_affected' in df.columns:
    print('Coefficient for Recovered Cases:', model.coef_[0])
    print('Coefficient for Number of Countries Affected:', model.coef_[1])
else:
    print('Coefficient for Recovered Cases:', model.coef_[0])
print('Intercept:', model.intercept_)
