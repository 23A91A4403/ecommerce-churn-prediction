# Deployment Guide

## Platform
Streamlit Community Cloud (Free)

## Prerequisites
- Public GitHub repository
- requirements.txt present
- streamlit_app.py inside app/

## Steps

1. Push latest code to GitHub
2. Go to https://share.streamlit.io
3. Click "New App"
4. Select repository
5. Branch: main
6. Main file path: app/streamlit_app.py
7. Click Deploy

## Post Deployment
- Test single prediction
- Test batch upload
- Verify charts load

## Live Application URL
[PASTE YOUR STREAMLIT URL HERE]

## Folder Structure

your-repo/
├── app/
│   ├── streamlit_app.py
│   └── predict.py
├── models/
│   ├── gradient_boosting.pkl
│   └── scaler.pkl
├── deployment/
│   └── deployment_guide.md
├── requirements.txt
└── README.md
