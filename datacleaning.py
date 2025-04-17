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

Output:-
Dataset shape: (506, 14)

Dataset info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   CRIM    500 non-null    float64
 1   ZN      506 non-null    float64
 2   INDUS   506 non-null    float64
 3   CHAS    506 non-null    float64
 4   NOX     506 non-null    float64
 5   RM      506 non-null    float64
 6   AGE     500 non-null    float64
 7   DIS     506 non-null    float64
 8   RAD     506 non-null    float64
 9   TAX     506 non-null    float64
 10  PTRATIO 506 non-null    float64
 11  B       506 non-null    float64
 12  LSTAT   506 non-null    float64
 13  PRICE   506 non-null    float64
dtypes: float64(14)
memory usage: 55.5 KB

Missing values per column:
CRIM      6
ZN        0
INDUS     0
CHAS      0
NOX       0
RM        0
AGE       6
DIS       0
RAD       0
TAX       0
PTRATIO   0
B         0
LSTAT     0
PRICE     0
dtype: int64

Filled missing values in CRIM with median value 0.25651
Filled missing values in AGE with median value 77.5

Data types after cleaning:
CRIM       float64
ZN         float64
INDUS      float64
CHAS       float64
NOX        float64
RM         float64
AGE        float64
DIS        float64
RAD        float64
TAX        float64
PTRATIO    float

