"""
visualizations.py
All 5 storytelling chart functions for the Mumbai Rainfall Week 2 dashboard.
Each function saves a PNG and returns the figure.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd
import numpy as np

SNS_PALETTE = 'Blues_r'
FIG_DPI = 150


def fig1_annual_overview(annual_df: pd.DataFrame, save_path='viz1_annual_overview.png'):
    """
    Figure 1: Annual rainfall bar chart with mean line.
    Story role: Opening context — how much rain does Mumbai get?
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    colors = ['#2166ac' if v >= annual_df['total_mm'].mean() else '#92c5de'
              for v in annual_df['total_mm']]
    ax.bar(annual_df['year'], annual_df['total_mm'], color=colors, width=0.8)
    mean_val = annual_df['total_mm'].mean()
    ax.axhline(mean_val, color='red', linestyle='--', linewidth=1.5,
               label=f'Long-term mean: {mean_val:.0f} mm')
    ax.set_title('Mumbai receives over 2,000 mm of rain every year — almost all in monsoon season',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Total Annual Rainfall (mm)', fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    sns.despine()
    plt.tight_layout()
    plt.savefig(save_path, dpi=FIG_DPI)
    plt.show()
    return fig


def fig2_monthly_pattern(monthly_df: pd.DataFrame, save_path='viz2_monthly_pattern.png'):
    """
    Figure 2: Monthly average rainfall bar chart.
    Story role: Seasonal pattern — when does rain arrive?
    """
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    colors = ['#2166ac' if m in [6,7,8,9] else '#d1e5f0' for m in monthly_df['month']]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(months, monthly_df['rainfall_mm'], color=colors)
    monsoon_patch = mpatches.Patch(color='#2166ac', label='Monsoon months (Jun–Sep)')
    dry_patch     = mpatches.Patch(color='#d1e5f0', label='Non-monsoon months')
    ax.legend(handles=[monsoon_patch, dry_patch], fontsize=10)
    ax.set_title('June to September delivers nearly 80% of Mumbai's annual rainfall',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Month', fontsize=11)
    ax.set_ylabel('Average Daily Rainfall (mm)', fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    sns.despine()
    plt.tight_layout()
    plt.savefig(save_path, dpi=FIG_DPI)
    plt.show()
    return fig


def fig3_trend_over_time(annual_df: pd.DataFrame, save_path='viz3_trend.png'):
    """
    Figure 3: Annual rainfall trend line with polynomial fit.
    Story role: Has rainfall changed over decades?
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(annual_df['year'], annual_df['total_mm'],
            color='#4393c3', linewidth=1.5, alpha=0.8, label='Annual rainfall')
    z = np.polyfit(annual_df['year'], annual_df['total_mm'], 1)
    p = np.poly1d(z)
    ax.plot(annual_df['year'], p(annual_df['year']),
            color='red', linestyle='--', linewidth=2,
            label=f'Trend ({z[0]:+.1f} mm/year)')
    ax.set_title('Mumbai's annual rainfall shows increasing variability since the 1990s',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Total Rainfall (mm)', fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    sns.despine()
    plt.tight_layout()
    plt.savefig(save_path, dpi=FIG_DPI)
    plt.show()
    return fig


def fig4_extreme_events(annual_df: pd.DataFrame, save_path='viz4_extreme_events.png'):
    """
    Figure 4: Extreme rainfall days per year (days > 200mm), annotated.
    Story role: Local impact — when do flood-risk events happen?
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    colors = ['#d73027' if v > annual_df['extreme_days'].mean() * 1.5 else '#fc8d59'
              for v in annual_df['extreme_days']]
    ax.bar(annual_df['year'], annual_df['extreme_days'], color=colors)
    mean_ex = annual_df['extreme_days'].mean()
    ax.axhline(mean_ex, color='navy', linestyle='--', linewidth=1.5,
               label=f'Mean ({mean_ex:.1f} days/year)')
    # Annotate 2005 flood
    if 2005 in annual_df['year'].values:
        val_2005 = annual_df.loc[annual_df['year'] == 2005, 'extreme_days'].values[0]
        ax.annotate('2005 Mumbai Floods\n468mm in 12 hrs',
                    xy=(2005, val_2005), xytext=(2005 - 5, val_2005 + 1.5),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    fontsize=9, color='darkred')
    ax.set_title('Extreme rainfall days (>200mm) have become more frequent since 2005',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Days with >200mm Rainfall', fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    sns.despine()
    plt.tight_layout()
    plt.savefig(save_path, dpi=FIG_DPI)
    plt.show()
    return fig


def fig5_heatmap(pivot_df: pd.DataFrame, save_path='viz5_heatmap.png'):
    """
    Figure 5: Decade x Month heatmap of average monthly rainfall.
    Story role: Climax — which months in which decades are getting wetter?
    """
    month_labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fig, ax = plt.subplots(figsize=(13, 6))
    sns.heatmap(pivot_df, cmap='Blues', annot=True, fmt='.0f',
                linewidths=0.5, ax=ax,
                cbar_kws={'label': 'Average Rainfall (mm)'})
    ax.set_xticklabels(month_labels, rotation=0, fontsize=10)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
    ax.set_title('September rainfall has intensified since 2000 — monsoon withdrawal is delaying',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Month', fontsize=11)
    ax.set_ylabel('Decade', fontsize=11)
    plt.tight_layout()
    plt.savefig(save_path, dpi=FIG_DPI)
    plt.show()
    return fig
