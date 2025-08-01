Chicago Crime Dashboard

A minimal dashboard for exploring Chicago crime data with Streamlit.

Prerequisites:

Python 3.8+ installed

Git installed

Setup:

Clone the repository:
git clone git@github.com:NickstaK/crime_dash.git
cd crime_dash

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Usage:

Fetch raw data:
python data/scripts/api_pull.py

Clean and prepare data:
python data/scripts/cleaning_data.py

Launch the Streamlit dashboard:
streamlit run data/scripts/app.py

The dashboard will be available at http://localhost:8501.
