#!/usr/bin/env python3
"""
Clean Chicago crime data for dashboarding:
- Drops unused columns
- Filters out records without geo
- Parses dates and extracts year, month, hour, weekday
- Standardizes text fields
- Writes cleaned CSV to data/clean/
"""

import os
import pandas as pd

# 1. Ensure output folder exists
os.makedirs("data/clean", exist_ok=True)

# 2. Load raw data
raw_path = "data/raw/chicago_crime_data.csv"
df = pd.read_csv(raw_path)

# 3. Drop columns we don't need
drop_cols = [
    "case_number", "id", "ward", "community_area",
    "updated_on", 
] + [c for c in df.columns if c.startswith("@computed_region_")] + ["x_coordinate", "y_coordinate"]
df.drop(columns=drop_cols, errors="ignore", inplace=True)

# 4. Parse datetime & extract parts
df["date"] = pd.to_datetime(df["date"])
df["year"]    = df["date"].dt.year
df["month"]   = df["date"].dt.month
df["hour"]    = df["date"].dt.hour
df["weekday"] = df["date"].dt.day_name()

# 5. Remove rows missing both latitude & longitude
df.dropna(subset=["latitude", "longitude"], how="all", inplace=True)

# 6. Clean up text fields
df["primary_type"] = df["primary_type"].str.strip().str.title()
df["location_description"] = (
    df["location_description"]
      .fillna("Unknown")
      .str.strip()
      .str.title()
)

# 7. Select only the columns we need for the dashboard
keep_cols = [
    "date", "year", "month", "hour", "weekday",
    "primary_type", "location_description",
    "latitude", "longitude"
]
df_clean = df[keep_cols]

# 8. Save cleaned data
out_path = "data/clean/cleaned_chicago_crime.csv"
df_clean.to_csv(out_path, index=False)
print(f"✅ Cleaned data saved to {out_path}")
