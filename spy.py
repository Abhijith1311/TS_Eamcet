import numpy as np
import pandas as pd
import streamlit as st
st.title("Hello")
df=pd.read_csv('original.csv')
df.head()
gender=st.radio('Select The Gender',('M','F'))
rank=st
rank=st.number_input('Enter Your Rank')
caste=st.radio('Select The caste',('OC','BC_B'))
branch_code=st.radio('Select your Required branch',('CSE','INF','ECE'))


if branch_code=='None':
	val=df[df['rank']>=rank]
	val_x=val[val['gender']==gender]
	val_y=val_x[val_x['caste']==caste]
		
	temp=val_y
else:
	val=df[df['rank']>=rank]
	val_x=val[val['gender']==gender]
	val_y=val_x[val_x['caste']==caste]
	val_z=val_y[val_y['branch_code']==branch_code]
		
	temp=val_z
y=temp.sort_values(by='rank', ascending = True)
z=y.drop_duplicates(subset = ["college","branch_code"],keep='last')
z.sort_values(by=['rank'],inplace=True)
st.write(z.head())
