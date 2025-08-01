import streamlit as st
import pandas as pd

# 1. Load the cleaned data
@st.cache_data
def load_data():
    return pd.read_csv("data/clean/cleaned_chicago_crime.csv")

df = load_data()

# 2. Page setup
st.set_page_config(page_title="Chicago Crime Dashboard", layout="wide")
st.title("🔍 Chicago Crime & Safety Dashboard")

# 3. Sidebar filters
st.sidebar.header("Filters")
types = st.sidebar.multiselect(
    "Select Crime Types",
    options=df["primary_type"].unique(),
    default=df["primary_type"].unique()
)
hours = st.sidebar.slider(
    "Hour of Day",
    min_value=int(df["hour"].min()),
    max_value=int(df["hour"].max()),
    value=(0, 23),
)

# 4. Apply filters
filtered = df[
    df["primary_type"].isin(types) &
    df["hour"].between(hours[0], hours[1])
]

# 5. Key metrics
st.metric("Total Incidents", len(filtered))
most_common = filtered["primary_type"].value_counts().nlargest(5)
st.bar_chart(most_common)

# 6. Map view
st.subheader("Incident Locations")
st.map(filtered.rename(columns={"latitude":"lat", "longitude":"lon"}))

# 7. Time series
st.subheader("Incidents by Hour")
hourly = filtered.groupby("hour").size().reset_index(name="count")
st.line_chart(hourly.set_index("hour"))

