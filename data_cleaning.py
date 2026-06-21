import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv(r"C:\Users\mythi\Downloads\data_cleaning_project\scripts\cleaned_coffee_sales.csv")

print("First 5 rows:\n", df.head())

print("\nDataset Info:\n")
print(df.info())

print("\nSummary Statistics:\n", df.describe())

print("\nMissing Values:\n", df.isnull().sum())

for col in df.select_dtypes(include=['float64', 'int64']):
    df[col] = df[col].fillna(df[col].mean())

df.select_dtypes(include=['object', 'string'])
df[col] = df[col].fillna(df[col].mean())


df.drop_duplicates(inplace=True)


for col in df.columns:
    if "date" in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')


df.to_csv("cleaned_coffee_sales.csv", index=False)

print("\n Data cleaned and saved!")


num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object', 'string']).columns


if len(num_cols) > 0:
    plt.figure()
    sns.histplot(df[num_cols[0]], kde=True)
    plt.title(f"Distribution of {num_cols[0]}")
    plt.show()


if len(cat_cols) > 0:
    plt.figure()
    df[cat_cols[0]].value_counts().head(10).plot(kind='bar')
    plt.title(f"Top Categories: {cat_cols[0]}")
    plt.xticks(rotation=45)
    plt.show()


if len(num_cols) > 1:
    plt.figure()
    sns.heatmap(df[num_cols].corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()


if len(num_cols) > 1:
    plt.figure()
    sns.scatterplot(x=df[num_cols[0]], y=df[num_cols[1]])
    plt.title(f"{num_cols[0]} vs {num_cols[1]}")
    plt.show()


date_cols = [col for col in df.columns if "date" in col.lower()]

if len(date_cols) > 0 and len(num_cols) > 0:
    plt.figure()
    df.groupby(date_cols[0])[num_cols[0]].sum().plot()
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

print("\n All charts generated successfully!")