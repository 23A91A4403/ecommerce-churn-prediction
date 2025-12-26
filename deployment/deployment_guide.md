# Deployment Guide

## Platform
Streamlit Community Cloud (Free)

## Prerequisites
- Public GitHub repository
- `requirements.txt` file present in the root directory
- Streamlit application entry file located at `app/streamlit_app.py`
- Trained model and scaler files available in the `models/` directory

## Deployment Steps
1. Push the latest project code to the GitHub repository.
2. Open https://share.streamlit.io in a web browser.
3. Click on **New App**.
4. Select the GitHub repository `ecommerce-churn-prediction`.
5. Choose the **main** branch.
6. Set the main file path as:
   ```
   app/streamlit_app.py
   ```
7. Click **Deploy** and wait for the application to build and launch.

## Post-Deployment Verification
After deployment, verify the following:
- The application loads successfully without runtime errors.
- Single customer churn prediction works correctly.
- Batch prediction functionality (if implemented) executes properly.
- Dashboard visualizations and charts load without issues.
- Model predictions are returned correctly for valid inputs.

## Live Application URL
https://ecommerce-churn-prediction-3nwr22bnvx9mwus6wcp562.streamlit.app/

## Reproducibility Note
Docker configuration files (`Dockerfile` and `docker-compose.yml`) are included in the project root to ensure reproducible evaluation in a containerized environment.
