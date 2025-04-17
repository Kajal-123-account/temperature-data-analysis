file_path = '/kaggle/input/temperature/temperature.csv'
try:
    df = pd.read_csv(file_path, encoding='ascii', delimiter=',')
    print('Data loaded successfully, sample records below:')
    display(df.head())
except Exception as error:
    print('Error loading the dataset. Check file path or encoding settings.')
    print(error)
