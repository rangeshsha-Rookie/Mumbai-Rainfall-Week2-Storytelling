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

## 🗂️ Repository Structure

```
Mumbai-Rainfall-Week2-Storytelling/
│
├── 📓 notebooks/
│   └── mumbai_rainfall_week2.ipynb     ← Full Colab-ready notebook (5 charts)
│
├── 🐍 src/
│   ├── data_loader.py                  ← Load & clean rainfall data
│   ├── visualizations.py               ← All 5 chart functions
│   └── __init__.py
│
├── 📊 visualizations/
│   └── README.md                       ← Chart index (upload PNGs here after running)
│
├── 📁 data/
│   └── README_data.md                  ← Dataset download guide (IMD + Kaggle)
│
├── 📁 report/
│   └── README.md                       ← Upload Week2_Report_Rangesh_Gupta.docx here
│
├── 📄 requirements.txt
├── 📄 .gitattributes
└── 📄 README.md
```

---

## 📊 The 5-Chart Visual Story

| Figure | Chart Type | Question Answered | Story Role |
|--------|-----------|-------------------|------------|
| Fig 1 | Bar chart | How much rain does Mumbai get each year? | Opening context |
| Fig 2 | Bar/Pie chart | Which months receive the most rain? | Seasonal pattern |
| Fig 3 | Line chart + trend | Has rainfall changed over decades? | Trend & climate |
| Fig 4 | Bar chart (annotated) | When do extreme rainfall events occur? | Local impact |
| Fig 5 | Heatmap (Year × Month) | Which months in which decades are getting wetter? | Climax insight |

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
# 1. Clone the repo
git clone https://github.com/rangeshsha-Rookie/Mumbai-Rainfall-Week2-Storytelling.git
cd Mumbai-Rainfall-Week2-Storytelling

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run notebook in Colab or Jupyter
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
