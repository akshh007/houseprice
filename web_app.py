import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('cost_predictor.sav','rb'))

def house_price_prediction(input_data):

    #changing input data as numpy array
    input_data_numpy = np.asarray(input_data)

    #reshaping the array because if we don't the model thinks we will provide 543 data but we are provided only 1 and so we need to reshape for one instance.
    input_data_numpy_reshape = input_data_numpy.reshape(1,-1)

    prediction1 = loaded_model.predict(input_data_numpy_reshape)
    return prediction1[0]

district_data = {
    "Ariyalur": 2000,
    "Chengalpattu": 2145,
    "Chennai": 16200,
    "Coimbatore": 2135,
    "Cuddalore": 2400,
    "Dharmapuri": 2400,
    "Dindigul": 1836,
    "Erode": 1700,
    "Kallakurichi": 2430,
    "Kanchipuram": 2400,
    "Kanniyakumari": 2430,
    "Karur": 2430,
    "Krishnagiri": 1836,
    "Madurai": 2135,
    "Mayiladuthurai": 1836,
    "Nagapattinam": 2430,
    "Namakkal": 2400,
    "Nilgiris": 2400,
    "Perambalur": 2430,
    "Pudukkottai": 1836,
    "Ramanathapuram": 2430,
    "Ranipet": 1836,
    "Salem": 2000,
    "Sivagangai": 2400,
    "Tenkasi": 2430,
    "Thanjavur": 2430,
    "Theni": 2400,
    "Thoothukudi": 1836,
    "Tiruchirappalli": 2430,
    "Tirunelveli": 2430,
    "Tirupathur": 2400,
    "Tiruppur": 1836,
    "Tiruvallur": 2430,
    "Tiruvannamalai": 2400,
    "Tiruvarur": 2430,
    "Vellore": 2430,
    "Viluppuram": 2400,
    "Virudhunagar": 1836,
    "Bangalore": 1905
}


def hidden_price_prediction(input_data):
    finalPrice = sum(input_data)
    return finalPrice

def main():
    #giving a title to the page
    st.title('House Price Prediction System')

    #getting the input data from the user
    											
    # Getting the input data from the user
    district = st.selectbox("Select a District", list(district_data.keys()))
    if district:
        area = district_data[district]
        st.write(f"The area code of {district} is {area}")

    area = st.text_input('Area code of the house')
    bedrooms = st.text_input('Number of Bedrooms')
    bathrooms = st.text_input('Number of Bathrooms')
    stories = st.text_input('Number of Storey')
    mainroad = st.text_input('Is there a Mainroad? (0 or 1)')
    guestroom = st.text_input('Is there a Guestroom? (0 or 1)')
    basement = st.text_input('Is there a Basement? (0 or 1)')
    hotwaterheating = st.text_input('Is there hot water heating? (0 or 1)')
    airconditioning = st.text_input('Is there air conditioning? (0 or 1)')
    parking = st.text_input('Number of parking spaces')
    prefarea = st.text_input('Is there a preferred area? (0 or 1)')
    
    sclarea = st.text_input('School / College nearby (0 or 1)')
    furnishingstatus = st.text_input('Furnishing status (unfurnished-0, semi-furnished-1, or furnished-2)')
    
    # Initialize session state for price and hiddenPrice
    if 'price' not in st.session_state:
        st.session_state.price = 0
    if 'hiddenPrice' not in st.session_state:
        st.session_state.hiddenPrice = 0

    #creating a button
    if st.button('Predict the price of the house'):
        try:
            area = int(area)
            bedrooms = int(bedrooms)
            bathrooms = int(bathrooms)
            stories = int(stories)
            mainroad = int(mainroad)
            guestroom = int(guestroom)
            basement = int(basement)
            hotwaterheating = int(hotwaterheating)
            airconditioning = int(airconditioning)
            parking = int(parking)
            prefarea = int(prefarea)
            furnishingstatus = int(furnishingstatus)
            st.session_state.price = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])
            st.success(f'The price of the house is: {st.session_state.price}')
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")

    st.divider()

    st.subheader('Hidden Costs while buying the house')
    transferFee = st.text_input(" 1 Society Transfer Fee (Cost that goes to society fund)")
    maintainance = st.text_input(" 2 Maintainance Cost (per year)")
    homeInsurance = st.text_input(" 3 Home Insurance (Basic - 3000, Comprehensive - 5000, Premium - 10000")
    propertyTax = st.text_input(" 4 Property Tax (Enter 20.4 for residential & 34.68 for Commercial)")
    brokerFee = st.text_input(" 5 Brokerage")
    st.text(" 6 Sales Deed (Price * 0.06)")

    hiddenPrice = 0

    if st.button('Calculate the hidden costs'):
        try:
            transferFee = int(transferFee)
            maintainance = int(maintainance)
            homeInsurance = int(homeInsurance)
            st.session_state.price = house_price_prediction([area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])
            salesDeed = st.session_state.price * 0.06
            propertyTax = float(propertyTax)
            propertyTax = float(area) * propertyTax
            brokerFee = int(brokerFee)
            st.session_state.hiddenPrice = hidden_price_prediction([transferFee,maintainance,homeInsurance,salesDeed,propertyTax,brokerFee,st.session_state.price])
            st.success(f'The initial cost of the house: {st.session_state.price}')
            st.success(f'The final cost of the house in a year is: {st.session_state.hiddenPrice}')
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")
    


if __name__ == '__main__':
    main()
