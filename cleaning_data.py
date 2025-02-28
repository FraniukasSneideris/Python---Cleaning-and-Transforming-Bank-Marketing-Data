import pandas as pd
import numpy as np

df = pd.read_csv("bank_marketing.csv")

# Converting . to _ in job and education 
for column in ["job", "education"]:
    df[column] = df[column].str.replace(".", "_")

# Converting unknown to NaN in education
df["education"] = df["education"].replace("unknown", np.nan)    

# Converting credit_default, mortgage and campaign_outcome to bool and 1 if yes, else 0
for column in ["credit_default", "mortgage", "campaign_outcome"]:
    replace = {
        "yes": 1, "no": 0, "unknown": 0
    }
    df[column] = df[column].map(replace).astype(bool)

# Converting previous_outcome to bool and 1 if success, else 0
to_replace = {
    "success": 1, "nonexistent": 0, "failure": 0
}
df["previous_outcome"] = df["previous_outcome"].map(to_replace).astype(bool)

# Creating last_contact_date column
df["year"] = "2022"
parts = df["year"] + "-" + df["month"] + "-" + df["day"].astype(str)
df["last_contact_date"] = pd.to_datetime(parts, format="%Y-%b-%d")

# Defining the new dataframes
client = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]
campaign = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "last_contact_date"]]
economics = df[["client_id", "cons_price_idx", "euribor_three_months"]]

# Saving new dataframes as csv
dataframes = [client, campaign, economics]
filenames = ["client.csv", "campaign.csv", "economics.csv"]
for df, filename in zip(dataframes, filenames):
    df.to_csv(filename, index=False)
