# **AI Job Analysis Using Python**


# **IMPORTING LIBRARIES**


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# **1. LOAD DATASET**


dataset_name = "AI Job Impact Dataset"
dataset_source = "CSV file (Kaggle dataset)"

df = pd.read_csv("ai_job_impact.csv")

# **2. DATASET INFORMATION**


rows, cols = df.shape

print("Dataset Name:", dataset_name)
print("Dataset Source:", dataset_source)
print("Number of Rows:", rows)
print("Number of Columns:", cols)
print("\nAttributes (Columns):\n", list(df.columns))


# **3. BASIC DATA CHECKING**


print("\nFirst 5 rows:\n", df.head())

print("\nDataset Info:\n")
df.info()

print("\nMissing Values:\n", df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# **4. USING NUMPY and Basic Stats**


print("\nNumPy Statistics:")

salary_before = np.array(df['Salary_Before_AI'])
salary_after = np.array(df['Salary_After_AI'])

print("Average Salary Before AI:", np.mean(salary_before))
print("Average Salary After AI:", np.mean(salary_after))
print("Max Salary After AI:", np.max(salary_after))
print("Min Salary Before AI:", np.min(salary_before))

# **PERCENTAGE CHANGE IN SALARY**

print("\nPercentage Change in Salary:\n")

df['Salary_Percent_Change'] = ((df['Salary_After_AI'] - df['Salary_Before_AI']) 
                               / df['Salary_Before_AI']) * 100

print("First 5 Percentage Changes:\n", df['Salary_Percent_Change'].head())

avg_percent_change = df['Salary_Percent_Change'].mean()
print(f"\nAverage Percentage Change in Salary: {avg_percent_change:.2f}%")

if avg_percent_change > 0:
    print("→ Overall salaries increased after AI.\n")
else:
    print("→ Overall salaries decreased after AI.\n")

# **5. BAR GRAPH (Industry vs AI Adoption)**


industry_adoption = df.groupby('Industry')['AI_Adoption_Level'].value_counts().unstack()

industry_adoption.plot(kind='bar', title='Industry vs AI Adoption Level')
plt.xlabel('Industry')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()

# **6. PIE CHART (Education Level)**


category_sums = df['Education_Level'].value_counts()

# Calculate percentages
percentage_labels = [f"{cat}\n{percent:.1f}%" for cat, percent in zip(category_sums.index, category_sums / category_sums.sum() * 100)]

# Plotting the pie chart with percentages and column names outside the slices
plt.pie(category_sums, labels=None, autopct='%1.1f%%', startangle=90, pctdistance=1.1)

# Adding legend outside the pie chart
plt.legend(percentage_labels, loc='center left', bbox_to_anchor=(1, 0.5))

plt.title('Education Level Distribution')
plt.show()

# **7. HISTOGRAM (Salary Distribution)**


df['Salary_Before_AI'].plot(kind='hist', bins=10, color='green', edgecolor='black', title='Distribution of Salary Before AI', rwidth=0.85)
plt.xlabel('Salary Before AI')
plt.ylabel('Frequency')
plt.show()

# **8. LINE PLOT (Experience vs Average Salary After AI)**


exp_salary = df.groupby('Years_Experience')['Salary_After_AI'].mean().reset_index()

exp_salary.plot(x='Years_Experience', y='Salary_After_AI', kind='line', marker='o', title='Experience vs Avg Salary After AI')
plt.xlabel('Years of Experience')
plt.ylabel('Avg Salary After AI')
plt.show()


# **9. BOXPLOT OF SALARY AFTER AI**

df.boxplot(column='Salary_After_AI')
plt.title('Boxplot of Salary After AI')
plt.show()

# **10. CORRELATION**
correlation = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation)

# **11. TOP 5 SALARIES AFTER AI**

top5 = df[['Job_Role', 'Salary_After_AI']]\
        .sort_values(by='Salary_After_AI', ascending=False)\
        .head()

print("\nTop 5 Highest Paying Jobs After AI:\n", top5)


# **12. OBSERVATIONS**



print("\n===== OBSERVATIONS =====\n")

# 1. Average Salary Change
avg_before = np.mean(df['Salary_Before_AI'])
avg_after = np.mean(df['Salary_After_AI'])

print(f"1. Average salary before AI: {avg_before:.2f}")
print(f"   Average salary after AI: {avg_after:.2f}")

if avg_after > avg_before:
    print("   → Salaries have increased after AI adoption.\n")
else:
    print("   → Salaries have decreased after AI adoption.\n")

# 2. Most Common Education Level
top_edu = df['Education_Level'].value_counts().idxmax()
print(f"2. Most common education level: {top_edu}\n")

# 3. Most Common Industry
top_industry = df['Industry'].value_counts().idxmax()
print(f"3. Industry with highest participation: {top_industry}\n")

# 4. AI Adoption Trend
top_ai = df['AI_Adoption_Level'].value_counts().idxmax()
print(f"4. Most common AI adoption level: {top_ai}\n")

# 5. Experience vs Salary Insight
corr_val = df.corr(numeric_only=True).loc['Years_Experience', 'Salary_After_AI']
print(f"5. Correlation between experience and salary after AI: {corr_val:.2f}")

if corr_val > 0:
    print("   → More experience generally leads to higher salary.\n")
else:
    print("   → Experience does not strongly increase salary.\n")



# **13. LIMITATIONS**


print("\n===== LIMITATIONS =====\n")

print("1. Dataset Size: The dataset contains only 2000 records.")
print("   A larger dataset would produce more reliable and generalised results.\n")

print("2. No Time Dimension: The dataset does not include time-based data.")
print("   So trends over years (e.g., salary change year-by-year) cannot be studied.\n")

print("3. Self-Reported Data: If the dataset is survey-based, responses may be biased.")
print("   Actual salaries and job statuses may differ from reported values.\n")

print("4. Limited Features: Factors like company size, location, and skillset")
print("   are not included, which limits the depth of analysis.\n")

print("5. No Causality: Correlation found in analysis does not imply causation.")
print("   For example, higher AI adoption may not directly cause salary changes.\n")


# **14. CONCLUSION**


# -----------------------------
# CONCLUSION
# -----------------------------
print("===== CONCLUSION =====\n")

print("This analysis shows the impact of AI on jobs and salaries.")
print("AI adoption influences salary trends across industries.")
print("Higher experience and education levels tend to affect salary positively.")
print("Different industries adopt AI at different levels, creating variation in job impact.")
