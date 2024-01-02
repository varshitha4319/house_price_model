#import the libraries
import numpy as np
import pickle
import streamlit as st #create account in streamlit
#map our data to give drop-downs and sliders
location_mapping = {
    "Kesarapalli":10,
    "Auto Nagar":12,
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 11,
    "Penamaluru": 7,
    "Payakapuram": 6
}
#in similar way we do for status,facing and property type
status_mapping = {'Ready to move':1,
                  'New':0,'Resale':2,'Under Construction':3}
direction_mapping = {"None": 1,
                     "East": 0,
                     "West":8 ,
                     "NorthEast": 3,
                     "NorthWest":4,
                     "North":2,
                     "South":5,
                     "SouthEast":6,
                     "SouthWest":7}
property_type_mapping = {"Apartment": 0,
                         "Independent Floor": 1,
                         "Independent House": 2,
                         "Residential Plot": 3,
                         "Studio Apartment":4,
                         "Villa" : 5}
#reading pickle file
with open("House_price.pkl",'rb')as f:
    model=pickle.load(f)
#define a function to access the data
def predict(Place,Area,Status,Rooms,Bathrooms,Facing,P_Type):
    """Prdict function to predic the price"""
    selected_location = location_mapping[Place]
    selected_status = status_mapping[Status]
    selected_direction = direction_mapping[Facing]
    selected_property = property_type_mapping[P_Type]
    input_data = np.array([[selected_location,Area,selected_status,
                            Rooms,Bathrooms,selected_direction,selected_property]])
    return model.predict(input_data)[0]
#Streamlit action
if __name__ == "__main__":
    st.header("House Price Prediction Model")
    col1, col2 = st.columns([2, 1])
    Rooms = col1.slider("No.of Bedrooms",max_value=10,min_value=1,
                      value=2)
    Bathrooms = col1.slider("No.of Bathrooms",max_value=10,min_value=0,
                       value=2)
    Place = col1.selectbox("Select a Location",list(location_mapping.keys()))
    Area = col1.number_input("Area",max_value=10000,
                             min_value = 500,value=1000,step=500)
    Status = col1.selectbox("Select the Status",list(status_mapping.keys()))
    Facing = col1.selectbox("Select a Facing",list(direction_mapping.keys()))
    P_Type = col1.selectbox("Select Property Type",
                          list(property_type_mapping.keys()))
    result = predict(Place,Area,Status,Rooms,Bathrooms,Facing,P_Type)
    submit_button = st.button("Submit")
    if submit_button:
        larger_text = f"<h2 style='color: blue;'>The Predicted House Price is : {result} Lakhs</h2>"
        st.markdown(larger_text, unsafe_allow_html=True)
