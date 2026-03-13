# Sleep-Analysis-Project
This project investigates the question: What factors most influence sleep quality? Using real-world sleep data exported from the Sleep Cycle app, the analysis applies exploratory data analysis (EDA) and statistical methods to uncover patterns in sleep behavior. Multiple variables were examined in this project..
# 😴 Sleep Quality Analysis

A personal data science project analyzing sleep patterns using self-tracked data from the **Sleep Cycle** app. The analysis explores how lifestyle factors — including caffeine consumption, physical activity, and sleep duration — influence sleep quality.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Limitations](#limitations)
- [References](#references)

---

## Overview

This project investigates the question: **What factors most influence sleep quality?**

Using real-world sleep data exported from the Sleep Cycle app, the analysis applies exploratory data analysis (EDA) and statistical methods to uncover patterns in sleep behavior. Variables examined include caffeine intake (tea and coffee), physical activity, time in bed, heart rate, mood upon waking, and day of the week.

---

## Dataset

The dataset (`sleepdata.csv`) was collected via the [Sleep Cycle app](https://www.sleepcycle.com/) and sourced from [Kaggle](https://www.kaggle.com/danagerous/sleep-data). It contains individual sleep session records from December 2014 onward.

| Column | Description |
|---|---|
| `Start` | Sleep session start timestamp |
| `End` | Sleep session end timestamp |
| `Sleep quality` | Subjective sleep quality (0–100%) |
| `Time in bed` | Total time spent in bed (HH:MM) |
| `Wake up` | Mood upon waking (`:)` Happy, `:|` Moderate) |
| `Sleep Notes` | Freetext lifestyle notes (e.g. *Drank coffee*, *Worked out*) |
| `Heart rate` | Resting heart rate (BPM) |
| `Activity (steps)` | Daily step count |

### Data Cleaning

The raw data was cleaned through several steps:
- Sleep Notes parsed into binary feature columns: `Drank tea`, `Drank coffee`, `Worked out`, `Ate late`, `Stressful day`
- Sleep quality converted from percentage string to numeric float
- Time in bed converted from `HH:MM` format to decimal hours
- Start/End columns parsed as datetime objects; `Month` and `Day of week` derived
- Rows with outlier sleep durations (>24 hours) removed

---

## Project Structure

```
sleep-quality-analysis/
│
├── sleepdata.csv             # Raw dataset from Sleep Cycle app
├── sleepquality.py           # Main analysis script
└── Sleep_quality_analysis.pdf  # Full written report
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/sleep-quality-analysis.git
   cd sleep-quality-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install pandas seaborn matplotlib
   ```

---

## Usage

Run the analysis script:

```bash
python sleepquality.py
```

This will generate the following outputs:
- Bar chart: Effect of working out on sleep quality and duration
- Heatmap: Correlation matrix of numeric variables
- Count plots: Workout, coffee, and tea consumption by day of week
- Console output: Average sleep scores by caffeine intake

---

## Key Findings

### 1. Sleep Duration is the Strongest Predictor of Sleep Quality
A strong positive correlation (~0.71) was found between time in bed and sleep quality. Longer sleep consistently produced higher quality scores, reinforcing the recommended 7–9 hours per night.

### 2. Caffeine Consumption Was Associated with Better Sleep
Counterintuitively, days with caffeine intake showed *higher* average sleep quality (~77%) compared to caffeine-free days (~70%). Time in bed was also slightly longer on caffeine days (~7.8 hrs vs ~7.3 hrs). This may reflect that caffeine tends to be consumed on more active, structured days.

| Drank Tea | Drank Coffee | Sleep Quality (%) | Time in Bed (Hours) |
|---|---|---|---|
| No | No | 70.52 | 7.30 |
| No | Yes | 74.85 | 7.80 |
| Yes | No | 77.37 | 7.96 |
| Yes | Yes | 77.11 | 7.64 |

### 3. Working Out Had a Minor Positive Effect
Sleep quality was marginally higher on workout days (~75%) versus non-workout days (~74%). Time in bed remained unchanged (~7.6 hrs), suggesting exercise improves *perceived* sleep quality without affecting duration.

### 4. Heart Rate Showed No Significant Correlation
Heart rate had near-zero correlation with all other variables, suggesting it was not a meaningful predictor of sleep quality in this individual dataset.

---

## Visualizations

The script produces the following charts:

- **Correlation Matrix Heatmap** — shows relationships between all numeric variables
- **Workout Effect Bar Chart** — compares sleep quality and duration on workout vs. non-workout days
- **Weekday Count Plots** — frequency of workouts, coffee, and tea consumption by day of week

---

## Limitations

- **Single-user dataset** — findings reflect one individual's patterns and cannot be generalized
- **Subjective data** — sleep quality is self-reported by the app's algorithm, not measured physiologically
- **Confounding variables** — caffeine and workout days may correlate with other unmeasured lifestyle factors
- **Environmental factors** — weather and air pressure data were not included in this analysis

---

## References

- Walker, M. (2017). *Why We Sleep*. Simon & Schuster.
- Blunden, S., & Galland, B. (2014). The complexities of defining optimal sleep. *Sleep Medicine Reviews*, 18(5), 371–378.
- Hirshkowitz, M. et al. (2015). National Sleep Foundation's sleep time duration recommendations. *Sleep Health*, 1(1), 40–43.
- Kumar, S., Nilsen, W. et al. (2017). Mobile health: Revolutionizing healthcare through transdisciplinary research. *Annual Review of Biomedical Engineering*, 19, 109–127.
- Northcube (2018). Sleep Cycle app data. [Kaggle](https://www.kaggle.com/danagerous/sleep-data).
