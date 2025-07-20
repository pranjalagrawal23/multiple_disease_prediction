# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 21:31:29 2025

@author: pranj
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))

heart_model=pickle.load(open('heart_disease_model.sav','rb'))




#sidebar for navigating


with st.sidebar:
    
    selected=option_menu('Multiple diseases system',
                         
                         ['Diabetes Prediction',
                          'Parkinsons Prediction',
                          'Heart Disease Prediction'],
                         
                         icons=['activity','person','heart'],
                         
                         default_index=0)
    
    
#diabetes prediction page

if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting input data from user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnencies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
        
    with col3:
        BloodPressure=st.text_input('BP')
        
    with col1:
        SkinThickness=st.text_input('Skin Thickness')
        
    with col2:
        Insulin=st.text_input('Insulin Level')
        
    with col3:
        BMI=st.text_input('BMI')    
        
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
        
    with col2:
        Age=st.text_input('Age')
        
        
    #code for prediction
    diab_diagnosis=''
    
    #creating a button
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis='The person is Diabetic'
            
        else:
            
            diab_diagnosis='The person is not Diabetic'
    
    st.success(diab_diagnosis)
if(selected=='Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    #getting input data from user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Fo=st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')
        
    with col1:
        Jitter_percent=st.text_input('SMDVP:Jitter(%)')
        
    with col2:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP=st.text_input('MDVP:RAP')
        
    with col1:
        PPQ=st.text_input('MDVP:PPQ')    
        
    with col2:
        Jitter=st.text_input('Jitter:DDP')
        
    with col3:
        Shimmer=st.text_input('MDVP:Shimmer')
        
    with col1:
        ShimmerdB=st.text_input('MDVP:Shimmer(dB)')
        
    with col2:
        APQ3=st.text_input('Shimmer:APQ3')
        
    with col3:
        APQ5=st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ=st.text_input('MDVP:APQ')    
        
    with col2:
        ShimmerDDA=st.text_input('Shimmer:DDA')
        
    with col3:
        NHR=st.text_input('NHR')
        
    with col1:
        HNR=st.text_input('HNR')    
        
    with col2:
        RPDE=st.text_input('RPDE')
        
    with col3:
        DFA=st.text_input('DFA')
        
    with col1:
        spread1=st.text_input('spread1')
        
    with col2:
        spread2=st.text_input('spread2')
        
    with col3:
        D2=st.text_input('D2')
        
    with col1:
        PPE=st.text_input('PPE')    
        
    #code for prediction
    parkinsons_diagnosis=''
    
    #creating a button
    
    if st.button('Parkisons Test Result'):
        parkinsons_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter_percent,Jitter_Abs,RAP,PPQ,Jitter,Shimmer,ShimmerdB,APQ3,APQ5,APQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (parkinsons_prediction[0]==1):
            parkinsons_diagnosis='The person is Diabetic'
            
        else:
            
            parkinsons_diagnosis='The person is not Diabetic'
    
    st.success(parkinsons_diagnosis)
    
if(selected=='Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')

