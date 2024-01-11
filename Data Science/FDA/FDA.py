import numpy as np
import pandas as pd 

cin = pd.read_csv(r'C:\Users\turalrif\OneDrive - Crayon Group\Python-learning-\Data Science\FDA\faa_ai_prelim.csv')
# print(cin.dtypes)

# print(cin[:5])
# print(cin.columns)

cols = ['ACFT_MAKE_NAME', 'ACFT_MODEL_NAME', 'LOC_STATE_NAME', 'RMK_TEXT', 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG']
extract  = cin[cols]
# print(extract)
print(extract.dtypes)
