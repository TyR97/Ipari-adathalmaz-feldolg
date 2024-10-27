import DataFrameProcessing as DFP

meres_df = DFP.df_init('Hűtőpanelek.csv')
new_df = DFP.df_processor(meres_df)


print(new_df)




