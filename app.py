import pandas 
import numpy
import sklearn
import pickle
import streamlit as st




import streamlit as st

st.title('ME/CFS, Depression Prediction')

st.write('Fill the details below for diagnosis')

col1, col2 = st.columns(2)

with col1:
  age = st.number_input('Age',18,70,25) # min=18,max=70,default = 25
  gender = st.selectbox('Gender',('Male','Female'))
  sq_index = st.number_input('Sleep Quality Index',1.0,10.0,5.7)
  bf_level = st.number_input('Brain Fog Level',0.0,10.0,2.0)
  pps_score = st.number_input('Physical Pain Score',0.0,10.0,4.2)
  stress_level = st.number_input('Stress Level',0.0,10.0,5.0)
  dep_phq9 = st.number_input('Depression phq9 Score',0.0,27,19)

with col2:
  fs_scale = st.number_input('Fatigue Severity Scale Score',0,10,5.6)
  pem_dur = st.number_input('PEM Duration',0,47,16)
  sleep_hrs = st.number_input('Sleep Hrs',3,10,5.5)
  pem_present = st.selectbox('Is PEM Present',('Yes','No'))
  med = st.selectbox('Meditation/Mindfulness Present',('Yes','No'))
  work_status = st.selectbox('Work Status',('Partially working','Working','Not working'))
  social_level = st.selectbox('Social Activity Level',('Very low','High','Low','Very high','Medium'))
  ex_freq = st.selectbox('Exercise Frequency',('Rarely','Sometimes','Never','Often','Daily'))

if gender=="Male":
  gen_m = 1
  gen_f = 0
else:
  gen_m = 0
  gen_f = 1

if pem_present=="Yes":
  pem_y = 1
  pem_n = 0
else:
  pem_y = 0
  pem_n = 1

if med == "Yes":
  med_y = 1
  med_n = 0
else:
  med_y = 0
  med_n = 1

if work_status == "Partially working":
  ws_pw = 1
  ws_w = 0
  ws_nw = 0
elif work_status == "Working":
  ws_pw = 0
  ws_w = 1
  ws_nw = 0
else:
  ws_pw = 0
  ws_w = 0
  ws_nw = 1

if social_level == "Very low":
  sl_vl = 1
  sl_h = 0
  sl_l = 0
  sl_vh = 0
  sl_m = 0
elif social_level == "High":
  sl_vl = 0
  sl_h = 1
  sl_l = 0
  sl_vh = 0
  sl_m = 0
elif social_level == "Low":
  sl_vl = 0
  sl_h = 0
  sl_l = 1
  sl_vh = 0
  sl_m = 0
elif social_level == "Very high":
  sl_vl = 0
  sl_h = 0
  sl_l = 0
  sl_vh = 1
  sl_m = 0
else:
  sl_vl = 0
  sl_h = 0
  sl_l = 0
  sl_vh = 0
  sl_m = 1


if ex_freq == "Rarely":
  ex_r = 1
  ex_s = 0
  ex_n = 0
  ex_of = 0
  ex_da = 0
elif ex_freq == "Sometimes":
  ex_r = 0
  ex_s = 1
  ex_n = 0
  ex_of = 0
  ex_da = 0
elif ex_freq == "Never":
  ex_r = 0
  ex_s = 0
  ex_n = 1
  ex_of = 0
  ex_da = 0
elif ex_freq == "Often":
  ex_r = 0
  ex_s = 0
  ex_n = 0
  ex_of = 1
  ex_da = 0
else:
  ex_r = 0
  ex_s = 0
  ex_n = 0
  ex_of = 0
  ex_da = 1


test_input= [age,gen_m,]