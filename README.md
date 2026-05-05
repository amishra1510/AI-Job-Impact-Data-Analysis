🤖 AI Job Impact Analysis
A data analysis project exploring how Artificial Intelligence adoption affects job roles, salaries, and workforce trends across industries — built using core Python data science libraries.

📁 Dataset

Name: AI Job Impact Dataset
Source: Kaggle
Size: 2000 records
Format: CSV


🔍 What This Project Covers

Loading and inspecting the dataset (shape, nulls, duplicates)
NumPy-based salary statistics (mean, min, max)
Salary percentage change calculation before vs after AI adoption
5 visualizations across bar, pie, histogram, line, and boxplot chart types
Correlation matrix across numeric features
Top 5 highest-paying job roles after AI
Printed observations, limitations, and conclusion


📊 Visualizations

Bar Chart — Industry vs AI Adoption Level
Pie Chart — Education Level Distribution
Histogram — Salary Before AI Distribution
Line Plot — Years of Experience vs Avg Salary After AI
Boxplot — Salary After AI spread

🛠️ Tech Stack

Python — Core language
Pandas — Data loading & manipulation
NumPy — Statistical computations
Matplotlib — Visualizations

## 🚀 How to Run

```
# 1. Clone the repo
git clone https://github.com/amishra1510/ai-job-impact-analysis.git
cd ai-job-impact-analysis

# 2. Install dependencies
pip install pandas numpy matplotlib

# 3. Place the dataset in the same folder
# (ai_job_impact.csv from Kaggle)

# 4. Run the script
python 1025250008.py
```


📌 Key Findings

Average salary before vs after AI adoption is compared and interpreted
Experience positively correlates with salary after AI in most cases
Education level distribution reveals the most common qualification in the workforce
AI adoption level varies significantly across industries


⚠️ Limitations

Only 2000 records — larger data would improve reliability
No time-series dimension (year-by-year trends unavailable)
Possible self-reporting bias if survey-based
Missing features: company size, location, skillset
Correlation ≠ causation

