# Basic data exploration
print('Dataset shape:', df.shape)
print('\nDataset info:')
df.info()

# Check for missing values
print('\nMissing values per column:')
print(df.isnull().sum())

# Handle missing values if any (using median imputation for numeric columns as an example)
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        print(f'Filled missing values in {col} with median value {median_val}')

# A quick check of data types
print('\nData types after cleaning:')
print(df.dtypes)
