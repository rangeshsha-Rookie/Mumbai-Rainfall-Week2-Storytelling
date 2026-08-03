"""
data_loader.py
Load and clean Mumbai rainfall data from CSV.
Source: IMD Pune / Kaggle mirror
"""

import pandas as pd
import numpy as np


def load_mumbai_rainfall(filepath: str) -> pd.DataFrame:
    """
    Load Mumbai daily rainfall CSV and return a cleaned DataFrame.
    Expected columns: date (or year/month), rainfall_mm
    """
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df


def clean_rainfall(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean rainfall data:
    - Replace IMD missing value code -999 with NaN
    - Forward-fill short gaps (max 3 days)
    - Remove physically impossible negatives
    - Cap extreme outliers at 500mm (above = sensor error)
    - Add temporal feature columns
    """
    df = df.copy()

    # Replace IMD missing value sentinel
    df['rainfall_mm'] = df['rainfall_mm'].replace(-999, np.nan)

    # Forward-fill short gaps only (monsoon is temporally correlated)
    df['rainfall_mm'] = df['rainfall_mm'].fillna(method='ffill', limit=3)

    # Remove negatives (data entry errors)
    df = df[df['rainfall_mm'] >= 0].copy()

    # Cap sensor error outliers
    df = df[df['rainfall_mm'] <= 500].copy()

    # Add temporal features
    df['year']    = df['date'].dt.year
    df['month']   = df['date'].dt.month
    df['decade']  = (df['year'] // 10) * 10
    df['monsoon'] = df['month'].isin([6, 7, 8, 9])

    return df


def annual_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return annual total and max daily rainfall."""
    return df.groupby('year').agg(
        total_mm=('rainfall_mm', 'sum'),
        max_day_mm=('rainfall_mm', 'max'),
        extreme_days=('rainfall_mm', lambda x: (x > 200).sum())
    ).reset_index()


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return average monthly rainfall."""
    return df.groupby('month')['rainfall_mm'].mean().reset_index()


def decade_month_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """Return pivot table for heatmap: decades x months."""
    return df.pivot_table(
        values='rainfall_mm',
        index='decade',
        columns='month',
        aggfunc='mean'
    )
