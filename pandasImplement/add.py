import pandas as pd
df=pd.read_csv('GXP_DATA_-_GXP_NON_GXP.csv')

df1=pd.read_csv('Detail_INFO_-_Distinct_Host_Detection_Count.csv')

filtered=df[df["GxP/NON-GxP/Server"].str.contains("GxP")]
#print(filtered)

 
new_df = df1.assign(GxpPresent='True') 
#print(new_df)

s1 = pd.merge(df1, df, how='left', on=['AgentID'])



s1['GxpPresent'] = s1['AgentID'].apply(s1['GxP/NON-GxP/Server_y'].str.find('GxP')==0 , other='False')

print(s1)

s1.to_csv('file1.csv')
