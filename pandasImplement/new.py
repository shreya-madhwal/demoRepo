import pandas as pd
df=pd.read_csv('file1.csv')
df.loc[df['GxpPresent'] != 'False', 'GxpPresent'] = 'True'
df.rename(columns = {'GxP/NON-GxP/Server_y':'GxP/NON-GxP/Server'}, inplace = True) 
df.to_csv('updated_file.csv')
