"""
Social Media Usage Analysis System
Academic demonstration using a synthetic sample dataset.
Run: python main.py
Dependencies: pandas, matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "social_media_usage_sample.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

REQUIRED_COLUMNS = [
    "user_id", "age", "platform", "daily_usage_hours", "sessions_per_day",
    "notifications_per_day", "sleep_hours", "study_hours", "primary_purpose"
]

def load_and_validate_data(path):
    """Load CSV, check required columns, remove duplicates, and handle missing rows."""
    data = pd.read_csv(path)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    initial_rows = len(data)
    data = data.drop_duplicates()
    data = data.dropna(subset=REQUIRED_COLUMNS)
    data = data[
        data["age"].between(10, 100)
        & data["daily_usage_hours"].between(0, 24)
        & data["sleep_hours"].between(0, 24)
        & data["study_hours"].between(0, 24)
        & data["sessions_per_day"].ge(0)
        & data["notifications_per_day"].ge(0)
    ].copy()
    print(f"Rows loaded: {initial_rows}")
    print(f"Rows after validation: {len(data)}")
    print(f"Rows removed during validation: {initial_rows - len(data)}")
    return data

def analyze_data(data):
    """Print summary statistics, platform comparisons, and correlations."""
    print("\n=== SOCIAL MEDIA USAGE ANALYSIS ===")
    print(f"Number of records: {len(data)}")
    print(f"Average daily usage: {data['daily_usage_hours'].mean():.2f} hours")
    print(f"Average sleep: {data['sleep_hours'].mean():.2f} hours")
    print(f"Average study time: {data['study_hours'].mean():.2f} hours")
    print(f"Most frequently recorded platform: {data['platform'].mode().iat[0]}")
    platform_means = data.groupby("platform")["daily_usage_hours"].mean().sort_values(ascending=False)
    print("\nAverage daily usage by platform:")
    print(platform_means.round(2).to_string())
    print("\nCorrelation with daily usage (descriptive only):")
    print(f"Usage vs sleep: {data['daily_usage_hours'].corr(data['sleep_hours']):.3f}")
    print(f"Usage vs study: {data['daily_usage_hours'].corr(data['study_hours']):.3f}")

    bins = [-0.01, 2, 4, 6, 24]
    labels = ["Light (≤2h)", "Moderate (>2–4h)", "High (>4–6h)", "Very high (>6h)"]
    data["usage_category"] = pd.cut(data["daily_usage_hours"], bins=bins, labels=labels)
    print("\nRecords by usage category:")
    print(data["usage_category"].value_counts().reindex(labels, fill_value=0).to_string())
    return platform_means

def create_visualizations(data):
    """Create chart images for the report and case study."""
    platform_means = data.groupby("platform")["daily_usage_hours"].mean().sort_values(ascending=False)

    ax = platform_means.plot(kind="bar", figsize=(8, 5), title="Average Daily Social Media Usage by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Average daily usage (hours)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "average_usage_by_platform.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(data["daily_usage_hours"], data["sleep_hours"])
    plt.title("Daily Social Media Usage vs Sleep Hours")
    plt.xlabel("Daily usage (hours)")
    plt.ylabel("Sleep (hours)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "usage_vs_sleep.png", dpi=160)
    plt.close()

    ax = data["platform"].value_counts().plot(kind="bar", figsize=(8, 5), title="Number of Records by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Number of records")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "platform_counts.png", dpi=160)
    plt.close()
    print(f"\nCharts saved in: {OUTPUT_DIR}")

def main():
    data = load_and_validate_data(DATA_PATH)
    analyze_data(data)
    create_visualizations(data)
    print("\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()
