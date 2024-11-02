import DataFrameProcessing as DFP
import DB_Commands as DBC


conn = DBC.db_init('test3.db')

meres_df = DFP.df_processor(DFP.df_init('Hűtőpanelek.csv'))

adag_df = DFP.df_init('Adagok.csv')

adag_df['Kezdet_DATUM'] =  DFP.date_to_right_format(adag_df['Kezdet_DATUM'])
adag_df['Vege_DATUM'] = DFP.date_to_right_format(adag_df['Vege_DATUM'])
adag_df['KezdetIdo'] = adag_df.apply(lambda row: f"{row['Kezdet_DATUM']} {row['Kezdet_IDO']}", axis=1)
adag_df['VegeIdo'] = adag_df.apply(lambda row: f"{row['Vege_DATUM']} {row['Vege_IDO']}", axis=1)
adag_df = adag_df.drop(['Kezdet_DATUM', 'Vege_DATUM', 'Kezdet_IDO', 'Vege_IDO', 'ADAGKOZI IDO', 'ADAGIDO'], axis=1)

DFP.df_cleaner(meres_df)

print(adag_df)
#print(adag_df['VegeIdo'])


#DBC.db_export(conn, meres_df, adag_df)





