# 📦 Data Sources — Mumbai Rainfall

## Primary Source: IMD Pune (Official Government Data)
- **URL:** https://www.imdpune.gov.in/cmpg/Griddata/Rainfall_25_NetCDF.html
- **Format:** NetCDF (0.25° × 0.25° grid, 1901–2024)
- **Mumbai coordinates:** 72.75°E, 19.0°N
- **How to load:** Use `xarray` to extract grid point and convert to CSV

## Secondary Source: Kaggle Mirror (Easier CSV)
- **URL:** https://www.kaggle.com/datasets/wydoinn/daily-rainfall-data-india-2009-2024
- **Format:** CSV — state-wise daily rainfall 2009–2024
- **Recommended for:** Quick Colab runs without NetCDF setup

## Additional Reference: OpenCity Mumbai
- **URL:** https://data.opencity.in/dataset/mumbai-rainfall-data
- **Format:** CSV — station-level rainfall data
- **Best for:** Colaba and Santacruz station comparison

## Loading Code (Colab)
```python
# Kaggle CSV
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/...')  # replace with actual URL

# IMD NetCDF
import xarray as xr
ds = xr.open_dataset('rainfall_0.25x0.25_daily_1901-2024.nc')
mumbai_rain = ds.sel(lon=72.75, lat=19.0, method='nearest')
df = mumbai_rain.to_dataframe().reset_index()
```
