import pandas as pd

df1 = pd.read_csv('./data/public-transport-quantity-final.csv')
df2 = pd.read_csv('./archive/city_population.csv')
region_replacements = {
    'Zhambyl Region': 'Jambyl Region',
    'Zhetysu Region': 'Jetisu Region',
    'Abay Region': 'Abai Region',
    'Turkestan Region': 'Turkistan Region',
    'Туркестанская ':'Turkistan Region',
    'The Republic of Kazakhstan': 'The Republic Of Kazakhstan',
    'Shymkent City': 'Shymkent city',
    'Almaty City': 'Almaty city',
    'Astana City': 'Astana city',
    'The Republic Kazakhstan': 'The Republic Of Kazakhstan',
    'Область Абай': 'Abai Region',
    'Ulytau Region Region': 'Ulytau Region',
    'Актюбинская ': 'Aktobe Region',
    'Zhetisu Region': 'Jetisu Region',
    'Karagandy Region': 'Karaganda Region',
    'Astana city Region': 'Astana city'
}

df2['Region'] = df2['Region'].replace(region_replacements)
df1['Region'] = df1['Region'].replace(region_replacements)

df2 = df2.drop(df2.columns[2:], axis=1)
df2.rename(columns={'Total': 'Population'}, inplace=True)

df1.rename(columns={'Value': 'Transport-quanity'}, inplace=True)
df1 = df1.drop(df1.columns[2:], axis=1)

df3=pd.merge(df1,df2,on='Region', how='outer')

df3['Transport-quanity-rate'] = ((df3['Transport-quanity']*1000)/df3['Population'])

df3.to_csv('./data/public-transport-quanity-rate.csv', index=False)
print(df3)