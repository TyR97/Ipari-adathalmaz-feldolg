import pandas as pd
import sqlite3

try:
    meres_df = pd.read_csv('Hűtőpanelek.csv', sep=';', engine='python')
    adag_df = pd.read_csv("Adagok.csv", sep=';', engine='python')
    print('CSVs successfully loaded')
except Exception as err:
    print('Error:', err)

new_df = pd.DataFrame(columns = ['MeresID', 'Panel', 'Ido', 'Homerseklet'])



for i in range(1, 16):
    time_col = f'Panel hőfok {i} [°C] Time'
    temp_col = f'Panel hőfok {i} [°C] ValueY'

    if temp_col in meres_df.columns and time_col in meres_df.columns:
        temp_df = pd.DataFrame({
            'MeresID': meres_df.index + 1,
            'Panel': i,
            'Ido': meres_df[time_col],
            'Homerseklet': meres_df[temp_col]
        })
        new_df = pd.concat([new_df, temp_df])


print(new_df)
new_df.to_csv('feck.csv', index = False)
new_df.to_csv('feck2.csv', index = False)



