# Social Media Usage Analysis System

A Python-based mini project that explores social-media usage patterns using a CSV dataset, descriptive statistics, simple validation, correlation analysis, and charts.

## Important data note
The included 30-row dataset is **synthetic sample data created for demonstration and coursework**. It is not a survey of real people and must not be presented as real-world evidence.

## Features
- Loads and validates a CSV dataset
- Checks required columns and removes duplicate/incomplete/invalid records
- Calculates average daily usage, sleep hours, and study hours
- Compares average usage by platform
- Calculates descriptive correlations between usage, sleep, and study hours
- Groups records into transparent usage bands
- Generates three chart images

## Requirements
- Python 3.10 or newer
- pandas
- matplotlib

## Run
```bash
pip install -r requirements.txt
python main.py
```

## Project structure
```text
social_media_usage_analysis_system/
├── main.py
├── requirements.txt
├── README.md
├── CASE_STUDY.md
├── data/
│   └── social_media_usage_sample.csv
└── outputs/
    ├── average_usage_by_platform.png
    ├── usage_vs_sleep.png
    └── platform_counts.png
```

## Sample findings
- Records analyzed: 30
- Mean daily usage: 3.37 hours
- Mean sleep: 7.01 hours
- Mean study time: 5.17 hours
- Platform with highest mean daily usage: Snapchat (4.93 hours)
- Correlation between daily usage and sleep: -0.96
- Correlation between daily usage and study hours: -0.96

These are findings from this synthetic sample only. Correlation does not prove causation, and the small synthetic dataset cannot support broad population claims.
