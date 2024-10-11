import pandas as pd

url_nassau = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=10000'
url_suffolk = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Suffolk&$limit=10000'

nassau_df = pd.read_csv(url_nassau)
len(nassau_df)

suffolk_df = pd.read_csv(url_suffolk)
len(suffolk_df)

# Merged data
merged = pd.concat([nassau_df, suffolk_df])
len(merged)
print("Number of rows in merged DataFrame:", len(merged))

# Specifying columns
df = pd.read_csv(url, usecols=['race','ethnicity','age_group', 'gender', 'length_of_stay', 'total_charges', 'total_costs', 'type_of_admission'])
print(df)
# Describing columns
print(df[['length_of_stay', 'total_charges', 'total_costs']].describe())

# Descriptive Stats for 'length_of_stay', 'total_charges', 'total_costs'
value_counts = merged['length_of_stay'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['age_group'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['gender'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_charges'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_costs'].value_counts() 
print("Value Counts:\n", value_counts)
value_counts = merged['type_of_admission'].value_counts()
print("Value Counts:\n", value_counts)

length_of_stay = np.array([74085, 66479, 49343, 33418, 23726])
total_charges = np.array([9203.04, 15082.10, 17690.10, 14587.88, 15611.25])
total_costs = np.array([2384.85, 1743.66, 1924.39, 4825.86, 3011.89])

def calculate_statistics(data, label):
    print(f"Statistics for {label}:")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    print(f"25th Percentile: {np.percentile(data, 25)}")
    print(f"50th Percentile (Median): {np.percentile(data, 50)}")
    print(f"75th Percentile: {np.percentile(data, 75)}")
    print(f"Quartiles: {np.percentile(data, [25, 50, 75])}")
    print("\n")

calculate_statistics(length_of_stay, "Length of Stay")
calculate_statistics(total_charges, "Total Charges")
calculate_statistics(total_costs, "Total Costs")

# Exploring Categorical Variables**:
 
    # Count distribution for Age Group, Gender, and Type of Admission
age_group_counts = merged['age_group'].value_counts()
gender_counts = merged['gender'].value_counts()
admission_type_counts = merged['type_of_admission'].value_counts()

print("Age Group Distribution:\n", age_group_counts)
print("\nGender Distribution:\n", gender_counts)
print("\nType of Admission Distribution:\n", admission_type_counts)

# Create a bar plot for Age Group, Gender, and Type of Admission
import matplotlib.pyplot as plt
age_count = df['age_group'].value_counts()
print(age_count)
ax = age_count.plot.bar(rot=0, title='Age Group Distribution')
ax.set_ylabel('Count')
plt.show()

sex_count = df['gender'].value_counts()
print(sex_count)
sx = sex_count.plot.bar(rot=0, title = 'Sex Count')
sx.set_ylabel('Count')
plt.show()

adm_typ = df['type_of_admission']
print(adm_typ)
admx = adm_typ.plot.bar(rot=0, title = 'Type of Admission')
admx.set_ylabel('Count')
plt.show()

# Visualizations**:
 # Create at least 3 visualizations to summarize the dataset:
 #  Histogram of Length of Stay
plt.figure(figsize=(8, 6))
sns.histplot(merged['length_of_stay'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay')
plt.ylabel('Frequency')
plt.show()

# Sample 10% of the data
sampled_data = merged['total_charges'].dropna().sample(frac=0.1, random_state=42)

# Plot boxplot for the sampled data
plt.figure(figsize=(8, 6))
sns.boxplot(x=sampled_data, color='green')
plt.title('Boxplot of Total Charges (Sampled Data)')
plt.xlabel('Total Charges')
plt.show()

# Apply log transformation to reduce the range of values
plt.figure(figsize=(8, 6))
sns.boxplot(x=np.log1p(merged['total_charges'].dropna()), color='green')
plt.title('Log-transformed Boxplot of Total Charges')
plt.xlabel('Log of Total Charges')
plt.show()

# Use the existing counts for type of admission
plt.figure(figsize=(8, 6))
sns.barplot(x=admission_type_counts.index, y=admission_type_counts.values, palette='coolwarm')
plt.title('Type of Admission Analysis')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Handling missing data

# Handling missing values in the dataset

### Handling Missing Data 
data = {
    'Length of Stay': [74085, 66479, 49343, 33418, 23726],
    'Total Charges': [9203.04, 15082.10, 17690.10, 14587.88, 15611.25],
    'Type of Admission': ['Emergency', 'Elective', 'Newborn', 'Urgent', 'Trauma', 'Not Available']
}

df = pd.DataFrame(data)

# Check for missing data
print("Missing data in each column:")
print(df.isnull().sum())

# Drop rows with missing data
df_dropped = df.dropna()
print("\nData after dropping rows with missing data:")
print(df_dropped)
