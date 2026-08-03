# 🌧️ Mumbai Rainfall Storytelling Dashboard
### Week 2 — Advanced Data Visualization & Storytelling with Python
**YuvaIntern | Virtual Data Science with Python Apprentice Internship**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![Seaborn](https://img.shields.io/badge/Seaborn-0.12-teal) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rangeshsha-Rookie/Mumbai-Rainfall-Week2-Storytelling/blob/main/notebooks/mumbai_rainfall_week2.ipynb)

---

## 📖 Project Overview

This project presents a **visual storytelling dashboard** built on Mumbai rainfall data sourced from the **India Meteorological Department (IMD)**. The goal is not just to show charts — it is to guide a non-technical audience through a clear, structured narrative about monsoon patterns, climate trends, and local flood risk in Mumbai.

**Central Question:** *How has Mumbai's rainfall changed over decades, and what does it mean for flood risk and urban planning?*

---

## 📊 The 5-Chart Visual Story

### Figure 1 — Opening Context
![Fig1](visualizations/Mumbai%20receives%20over%202%2C000mm%20every%20year%20%E2%80%94%20almost%20all%20in%20monsoon.png)

### Figure 2 — Seasonal Pattern
![Fig2](visualizations/June%E2%80%93September%20delivers%2080%25%20of%20annual%20rainfall.png)

### Figure 3 — Long-Term Trend
![Fig3](visualizations/Increasing%20variability%20since%20the%201990s.png)

### Figure 4 — Extreme Events
![Fig4](visualizations/Extreme%20days%20(200mm)%20more%20frequent%20since%202005.png)

### Figure 5 — Decade × Month Heatmap
![Fig5](visualizations/September%20rainfall%20intensifying%20%E2%80%94%20monsoon%20delaying.png)

---

## 🗂️ Repository Structure

```
Mumbai-Rainfall-Week2-Storytelling/
│
├── 📓 notebooks/
│   └── mumbai_rainfall_week2.ipynb     ← Full Colab-ready notebook
│
├── 🐍 src/
│   ├── data_loader.py
│   ├── visualizations.py
│   └── __init__.py
│
├── 📊 visualizations/                  ← All 5 PNGs uploaded ✅
│
├── 📁 data/
│   └── README_data.md
│
├── 📁 report/                          ← Upload Week2_Report_Rangesh_Gupta.docx here
│
├── 📄 requirements.txt
└── 📄 .gitattributes
```

---

## 🔑 Key Findings

- **75–80% of Mumbai's annual rainfall falls in just 4 monsoon months** (June–September)
- **Extreme rainfall days (>200mm) have increased** in frequency post-2005
- **The 2005 Mumbai floods** (468mm on July 26) remain the most extreme event on record
- **September rainfall is increasing**, suggesting a delayed monsoon withdrawal pattern
- **Annual rainfall variability** has grown since the 1990s, consistent with climate change signals

---

## 🚀 How to Run

```bash
git clone https://github.com/rangeshsha-Rookie/Mumbai-Rainfall-Week2-Storytelling.git
cd Mumbai-Rainfall-Week2-Storytelling
pip install -r requirements.txt
jupyter notebook notebooks/mumbai_rainfall_week2.ipynb
```

**Or open directly in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rangeshsha-Rookie/Mumbai-Rainfall-Week2-Storytelling/blob/main/notebooks/mumbai_rainfall_week2.ipynb)

---

## 📦 Data Source

| Source | Link | Format |
|--------|------|--------|
| IMD Pune (Official) | [imdpune.gov.in](https://www.imdpune.gov.in) | NetCDF / CSV |
| Kaggle Mirror | [Daily Rainfall India 2009–2024](https://www.kaggle.com/datasets/wydoinn/daily-rainfall-data-india-2009-2024) | CSV |
| OpenCity Mumbai | [data.opencity.in](https://data.opencity.in/dataset/mumbai-rainfall-data) | CSV |

---

## 👤 Author

**Rangesh Gupta** | B.Tech CMPN '29, SLRTCE, Navi Mumbai  
🔗 [GitHub](https://github.com/rangeshsha-Rookie) | 📍 Mumbai, Maharashtra, India

---

*Week 2 Submission — YuvaIntern Virtual Data Science with Python Apprentice Internship*
