import pandas as pd

# Load dataset into a pandas DataFrame
df = pd.read_csv('D:\keerthana java\Projects\Neelem\datasetofhospitals')

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle outliers in numerical columns (e.g., using Z-score or IQR)
z_threshold = 3
z_scores = np.abs((df['Numerical_Column'] - df['Numerical_Column'].mean()) / df['Numerical_Column'].std())
outliers = df[z_scores > z_threshold]
# Encode categorical variables (e.g., using one-hot encoding)
encoded_df = pd.get_dummies(df, columns=['Facility.Type'])
encoded_df.to_csv('encoded_dataset.csv', index=False)

# Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
