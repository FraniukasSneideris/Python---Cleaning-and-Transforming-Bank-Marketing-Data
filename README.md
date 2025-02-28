# Python---Cleaning-and-Transforming-Bank-Marketing-Data

## Project Overview

This project focuses on cleaning and transforming data from a bank's marketing campaign. The data was collected to help the bank understand the effectiveness of their marketing efforts in attracting customers to take out personal loans. The data contains various columns such as client information, campaign statistics, and economic indicators.

The goal is to clean, reformat, and split the data into three separate CSV files so the bank can store and use them for future campaigns in a PostgreSQL database. 

### Data Overview

The raw data, `bank_marketing.csv`, contains information on clients, previous marketing campaigns, and economic indicators. The task is to clean and preprocess the data into three CSV files based on the specified structure:

1. **client.csv** - Contains client demographic data:
   - `client_id` (integer)
   - `age` (integer)
   - `job` (string)
   - `marital` (string)
   - `education` (string)
   - `credit_default` (boolean)
   - `mortgage` (boolean)

2. **campaign.csv** - Contains campaign-specific data:
   - `client_id` (integer)
   - `number_contacts` (integer)
   - `contact_duration` (integer)
   - `previous_campaign_contacts` (integer)
   - `previous_outcome` (boolean)
   - `campaign_outcome` (boolean)
   - `last_contact_date` (datetime)

3. **economics.csv** - Contains economic indicators:
   - `client_id` (integer)
   - `cons_price_idx` (float)
   - `euribor_three_months` (float)

### Cleaning Requirements

- Replace any periods (`.`) with underscores (`_`) in job and education columns.
- Convert `unknown` values in the education column to NaN.
- Convert categorical columns like `credit_default`, `mortgage`, and `campaign_outcome` to boolean values (`1` for "yes", `0` for "no").
- Convert the `previous_outcome` column to boolean values (`1` for "success", `0` for others).
- Create a `last_contact_date` column from the `year`, `month`, and `day` columns.
- Output the cleaned data into three CSV files: `client.csv`, `campaign.csv`, and `economics.csv`.

### Code
First of all, we need to import both pandas and numpy, as we'll need both libraries.
```python
import pandas as pd
import numpy as np
```
#### Reading the data
```python
df = pd.read_csv("bank_marketing.csv")
```
The script starts by loading the dataset into a Pandas DataFrame named df.
#### Cleaning the job and education Columns
```python
for column in ["job", "education"]:
    df[column] = df[column].str.replace(".", "_")
```
The script loops through the job and education columns, replacing any period (.) characters with an underscore (_). This standardizes the text values in these columns.
#### Handling Missing Data in the education Column
```python
df["education"] = df["education"].replace("unknown", np.nan) 
```
The value "unknown" in the education column is replaced with NaN (Not a Number), which is a common way to represent missing or undefined data.
#### Converting Categorical Columns to Boolean
```python
for column in ["credit_default", "mortgage", "campaign_outcome"]:
    replace = {
        "yes": 1, "no": 0, "unknown": 0
    }
    df[column] = df[column].map(replace).astype(bool)
```
The credit_default, mortgage, and campaign_outcome columns are transformed to boolean values:
- "yes" becomes 1
- "no" becomes 0
- "unknown" becomes 0
The astype(bool) method ensures that the columns are explicitly converted to boolean data types.
#### Converting previous_outcome to Boolean
```python
to_replace = {
    "success": 1, "nonexistent": 0, "failure": 0
}
df["previous_outcome"] = df["previous_outcome"].map(to_replace).astype(bool)
```
The previous_outcome column is similarly transformed:
- "success" becomes 1
- "nonexistent" becomes 0
- "failure" becomes 0
This conversion also ensures the column has a boolean type.
#### Creating the last_contact_date Column
```python
df["year"] = "2022"
parts = df["year"] + "-" + df["month"] + "-" + df["day"].astype(str)
df["last_contact_date"] = pd.to_datetime(parts, format="%Y-%b-%d")
```
The script creates a new column called last_contact_date by combining the year (2022), month, and day columns. These are then combined into a string and converted to a datetime object using pd.to_datetime(), ensuring the proper date format is used.
#### Defining New DataFrames
```python
client = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]
campaign = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "last_contact_date"]]
economics = df[["client_id", "cons_price_idx", "euribor_three_months"]]
```
After cleaning the data, the script splits the DataFrame into three smaller DataFrames:
- client: Contains client-specific information such as ID, age, job, marital status, education, and financial status (credit_default, mortgage).
- campaign: Contains campaign-specific information like number of contacts, duration, previous campaign interactions, and outcome.
- economics: Contains economic indicators like the consumer price index and Euribor rates.
#### Saving Cleaned DataFrames to CSV
```python
dataframes = [client, campaign, economics]
filenames = ["client.csv", "campaign.csv", "economics.csv"]
for df, filename in zip(dataframes, filenames):
    df.to_csv(filename, index=False)
```
Finally, the three cleaned DataFrames are saved as CSV files (client.csv, campaign.csv, and economics.csv). The index=False argument ensures that the DataFrame index is not included in the saved file.
