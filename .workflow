name: Automated Data Preprocessing

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  preprocessing:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Preprocessing Script
        run: |
          python preprocessing/automate_Al.py

      - name: Commit Preprocessed Data
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "github-actions@github.com"
          git add preprocessing/student_score_clean.csv
          git commit -m "Update preprocessed dataset" || echo "No changes"
          git push
