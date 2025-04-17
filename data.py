# Import and setup libraries
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Necessary backend setting
import matplotlib.pyplot as plt
plt.switch_backend('Agg')  # switch backend if only plt imported

import seaborn as sns
sns.set(style='whitegrid', palette='muted', color_codes=True)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Ensure inline plotting (Kaggle specific)
%matplotlib inline

# Set a random seed for reproducibility
RANDOM_STATE = 42

print('Libraries imported and backend configured.')
     
