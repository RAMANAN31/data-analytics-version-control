Data Analytics Version Control – BMW Sales Data Cleaning Project
Course Information

Course Code: CSE3505
Course Name: Fundamentals of Data Analytics (FDA)
Register Number: 22MIA1150
Student Name: Ramanan G
Institution: VIT Chennai

Project Overview

This project demonstrates how version control using Git and GitHub can be effectively integrated into a data analytics workflow.
The dataset used is BMW Sales Data (2010–2024), and the focus of this project is to perform data cleaning using Python and document the workflow using version control practices.

The project highlights how version control enables traceability, collaboration, and reproducibility in data analytics tasks.

Objectives

To understand and implement Git version control in a data analytics project

To perform data cleaning using Python (Pandas)

To maintain a reproducible and organized workflow using GitHub

Data Cleaning Script

File: data_cleaning.py

Features of the Script

Loads the raw dataset (BMW sales data (2010–2024).csv)

Handles missing values and removes duplicates

Removes outliers using the Interquartile Range (IQR) method

Standardizes column names for consistency

Converts data types where necessary

Saves a cleaned version of the dataset as cleaned_bmw_sales.csv

Sample Code
import pandas as pd

# Load dataset
df = pd.read_csv("BMW sales data (2010-2024) (1).csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna({
    "Color": "Unknown",
    "Fuel_Type": "Unknown",
    "Transmission": "Unknown"
})

# Handle outliers using IQR
Q1 = df["Mileage_KM"].quantile(0.25)
Q3 = df["Mileage_KM"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["Mileage_KM"] >= (Q1 - 1.5 * IQR)) & (df["Mileage_KM"] <= (Q3 + 1.5 * IQR))]

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Save cleaned data
df.to_csv("cleaned_bmw_sales.csv", index=False)

Git and GitHub Workflow
Task 1: Set Up Git

Installed Git and configured username and email

Verified configuration using:

git config --list

Task 2: Create a Local Repository

Created a folder named data-analytics-version-control

Initialized it as a Git repository

Added files: data_cleaning.py, dataset, and README.md

Made the first commit:

git add .
git commit -m "Initial commit - added data cleaning script and dataset"

Task 3: Push to GitHub

Created a new GitHub repository with the same name

Linked it to the local repository and pushed files:

git remote add origin https://github.com/RAMANAN31/data-analytics-version-control.git
git branch -M main
git push -u origin main

Repository Structure
<img width="476" height="175" alt="image" src="https://github.com/user-attachments/assets/b013fe83-af96-44a2-8d7a-886d711c6785" />


Reflection Summary

Version control significantly enhanced this project by ensuring organization, collaboration, and traceability.
Git’s commit history maintained a detailed record of code evolution, while GitHub served as a reliable backup and collaboration platform.

Overall, the integration of version control made the workflow structured, reproducible, and professional.

GitHub Repository

https://github.com/RAMANAN31/data-analytics-version-control
