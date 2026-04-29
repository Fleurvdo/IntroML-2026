import pandas as pd
import matplotlib as plot

train_df = pd.read_parquet(r'C:\Users\Admin\Documents\GitHub\IntroML-2026\Projet\train.parquet')
test_df = pd.read_parquet(r'C:\Users\Admin\Documents\GitHub\IntroML-2026\Projet\test.parquet')
sensors_df = pd.read_parquet(r'C:\Users\Admin\Documents\GitHub\IntroML-2026\Projet\sensors.parquet')

# Merge extra information about sensors 
train_df = train_df.merge(sensors_df, on='sensor', how='left')

# Sort by time and sensor 
train_df = train_df.sort_values(['sensor', 'time'])
print(train_df.head())

# The head of the training data at time t=0.0 has 3 profiles (from the 3 experiences)
# Identify 3 experiences through plotting
