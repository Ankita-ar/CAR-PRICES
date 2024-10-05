import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle

with open ('final_model_gbm.pkl', 'rb') as file:
    model = pickle.load(file)

def prediction(input_data):
    input_data = np.array(input_data, dtype='object')

    pred = model.predict(input_data)[0]
    
    if pred>0.5:
        return f' The price of car is more likely to be high : Price = {round(pred)}'
    else:
        return f' The price of car is less likely to be high : Price = {round(pred)}'

def main():
    st.title('Car Prices')

    sym = st.slider('What is the insurance risk rating?', min_value=-3, max_value=3, step=1)
    ft = (lambda x: 1 if x=='diesel' else 0)(st.selectbox('Enter the type of fuel', ['diesel', 'gas']))
    asp = (lambda x: 1 if x=='turbo' else 0)(st.selectbox('Enter the type of aspiration', ['turbo', 'std']))
    door = st.selectbox('Enter the number of doors in the car.', [2,4])
    cb_lambda = (lambda x: 0 if x=='convertible' else 1 if x=='hatchback' else 2 if x=='sedan' else 3 if x=='wagon' else 4)
    cb = cb_lambda(st.selectbox('What is the body type of car?'['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop']))
    dw_lambda = (lambda x : 0 if x=='rwd' else 1 if x=='fwd' else 2)
    dw = dw_lambda(st.selectbox('Which kind of drivewheel is it?'['rwd', 'fwd', '4wd']))
    el = (lambda x: 1 if x=='front' else 0)(st.selectbox('What is the engine location?', ['front', 'rear']))
    wl = st.text_input('What is the wheelbase?')
    cl = st.text_input('What is the length of the car?')
    cw = st.text_input('What is the width of the car?')
    ch = st.text_input('What is the height of the car?')
    curbw = st.text_input('What is the curbweight of the car?')
    et_lambda = (lambda x: 0 if x=='ohc' else 1 if x=='ohcf' else 2 if x=='ohcv' else 3 if x=='dohc' else 4 if x=='l' else 5 if x=='rotor' else 6)
    et = et_lambda(st.selectbox('What is the engine type of the car?'['ohc', 'ohcf', 'ohcv', 'dohc', 'l', 'rotor', 'dohcv']))
    cn_lambda = (lambda x: 0 if x=='four' else 1 if x=='six' else 2 if x=='five' else 3 if x=='eight' else 4 if x=='two' else 5 if x=='three' else 6)
    cn = cn_lambda(st.selectboc('How many cylinders are there in car?'['four', 'six', 'five', 'eight', 'two', 'three', 'twelve']))
    es = st.text_input('What is the engine size?')
    fs_lambda = (lambda x: 0 if x=='mpfi' else 1 if x=='2bbl' else 2 if x=='idi' else 3 if x=='1bbl' else 4 if x=='spdi' else 5 if x=='4bbl' else 6 if x=='mfi' else x)
    fs = fs_lambda(st.selectbox('What is the fuel system of the car?', ['mpfi', '2bbl', 'idi', '1bbl', 'spdi', '4bbl', 'mfi', 'spfi']))
    br = st.text_input('What is the bore ratio of the car?')
    stroke = st.text_input('How much is the stroke or volume inside the engine?')
    cr = st.text_input('What is the compression ratio of the car?')
    hp = st.text_input('What is the horsepower of the car?')
    rpm = st.text_input('What is the car peak rpm?')
    cmpg = st.slider('How much is the mileage of car in city?', min_value = 14, max_value = 49, step=1)
    hpmg = st.slider('How much is the mileage of car on highway?', min_value = 16, max_value = 54, step=1)

    input_list = [[sym, ft, asp, door, cb, dw, el, wl, cl, cw, ch, curbw, et, cn, es, fs, br, stroke, cr, hp, rpm, cmpg, hpmg]]

    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)


if __name__=='__main__':
    main()                           
                   
                   
                   
                   
                   
