# Case Study: Social Media Usage Analysis System

## 1. Title
**Analysis of Social Media Usage Patterns Using Python**

## 2. Abstract
This case study demonstrates a small data-analysis workflow for exploring social-media usage, platform preferences, sleep duration, and study hours. A Python program loads a CSV file, validates its fields, calculates descriptive statistics and correlations, categorizes daily usage, and produces visualizations. The included dataset contains 30 synthetic records made for demonstration; therefore, results illustrate how the system works and are not claims about a real population.

## 3. Problem Statement
Social-media usage data can contain multiple variables, making it difficult to compare platform use or inspect possible relationships manually. The project demonstrates how a simple Python-based system can organize a dataset, summarize key measures, and display patterns through charts.

## 4. Objectives
- Load and validate a structured CSV dataset.
- Summarize daily usage, sleep, and study hours.
- Compare average daily usage across platforms.
- Examine descriptive correlations between usage and sleep/study hours.
- Visualize platform counts and usage patterns.
- Generate reproducible outputs using Python.

## 5. Dataset Description
The sample has 30 records and these fields: user ID, age, platform, daily usage hours, sessions per day, notifications per day, sleep hours, study hours, and primary purpose. All records are synthetic demonstration data, not collected from actual participants.

## 6. Tools and Technologies
- Python
- Pandas for loading, validation, grouping, and summary statistics
- Matplotlib for chart generation
- CSV as the input data format

## 7. Methodology
1. Read the CSV file.
2. Check whether required columns exist.
3. Remove duplicate and incomplete rows.
4. Exclude records with implausible values for key numeric fields.
5. Calculate mean values and platform-level usage summaries.
6. Calculate Pearson correlations as descriptive indicators.
7. Create bar charts and a scatter plot.
8. Interpret results cautiously.

## 8. Results
- Records analyzed: **30**
- Average daily social-media usage: **3.37 hours**
- Average sleep duration: **7.01 hours**
- Average study time: **5.17 hours**
- Most frequently recorded platform: **Instagram**
- Platform with the highest average daily usage: **Snapchat**, at **4.93 hours**
- Correlation between daily usage and sleep: **-0.96**
- Correlation between daily usage and study hours: **-0.96**

### Interpretation
The results show how platform summaries and correlations can be calculated from structured records. Correlation values describe the direction and strength of a linear association in this sample; they do not show that social-media use causes a change in sleep or study time. Because the data is synthetic and small, these results are only a demonstration of the method.

## 9. Visualizations
The program creates:
- `outputs/average_usage_by_platform.png`
- `outputs/usage_vs_sleep.png`
- `outputs/platform_counts.png`

## 10. Limitations
- The dataset is synthetic and small.
- No causal conclusions can be drawn.
- Self-reported fields in a real dataset could contain recall errors or inaccurate answers.
- The program is a prototype and does not collect data from social platforms or monitor users.

## 11. Conclusion
The Social Media Usage Analysis System demonstrates a reproducible introductory data-analysis workflow. It combines data validation, descriptive statistics, correlation analysis, usage categories, and visualizations. Future work could use a larger, ethically collected and anonymized real dataset, add interactive filters, and compare results across time periods.

## 12. How to Run
Install dependencies with `pip install -r requirements.txt`, then run `python main.py`.

## 13. Repository
Add the public GitHub repository URL here after creating and uploading the project.
