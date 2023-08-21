import streamlit as st
import tensorflow as tf
import numpy as np
import subprocess
# from st_functions import st_button
from PIL import Image, ImageOps
from streamlit_option_menu import option_menu
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Baloo+Bhai+2&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Baloo Bhai 2','Times New Roman';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

selected = option_menu(menu_title=None,options=["Home", "Prediction","Contact"], 
        icons=['house', 'lightbulb-fill','envelope'], default_index=0,
    orientation="horizontal",
    # styles = {
    #     "container": {"padding": "0!important"},
    #     # "nav-link": {
    #     #     "font-size": "25px",   
    #     #     "margin":"0px",
    #     #     "font-family": "Baloo Bhai 2",
    #     # },
    # }   ,  
    )

if(selected=="Home"):
    st.title("Welcome\n")
    col3,col1,col2 = st.columns(3)

    # this will put a button in the middle column
    with col3:
        image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\potato_pic.png')
        st.image(image, caption=None,width=250)
        b1=st.button("Potato")
        if(b1):
            subprocess.Popen(["streamlit","run","potato.py"])
            st.experimental_rerun()
    with col2:
        image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\rice_pic.png')
        st.image(image, caption=None,width=250)
        b2=st.button("Paddy")
        if(b2):
            subprocess.Popen(["streamlit","run","paddy.py"])
            st.experimental_rerun()

    c1,c2,c3 = st.columns(3)
    with c1:
        image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\tomato_pic-removebg-preview.png')
        st.image(image, caption=None,width=250)
        bt1=st.button("Tomato")
        if(bt1):
            subprocess.Popen(["streamlit","run","tomato.py"])
            st.experimental_rerun()
    with c3:
        image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\corn_pic.png')
        st.image(image, caption=None,width=250)
        bt2=st.button("Maize")
        if(bt2):
            subprocess.Popen(["streamlit","run","corn.py"])
            st.experimental_rerun()


   
if(selected=="Contact"):
    Name = st.text_input('Name',placeholder="Enter your Name")
    Email = st.text_input('Email',placeholder="Enter your Email")
    Sub = st.text_input('Subject',placeholder="Enter Subject")
    msg =st.text_area('Message 👇',placeholder="Enter Message",height=150)
    st.markdown(
    """
    <style>
   
    input {
        # font-size: 3rem !important;
        border: 2px solid black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
          width: 750px;
          border: 2px solid black;
          border-radius: 8px;
        }
    </style>
    '''
    tabs_font_css = """
    <style>
        div[class*="stTextArea"] label p {
          font-size: 20px;
          font-weight:bold;
        #   color: red;
        }

        div[class*="stTextInput"] label p {
          font-size: 20px;
          font-weight:bold;
        }

    </style>
    """
    st.markdown(tabs_font_css, unsafe_allow_html=True)
    st.markdown(custom_css, unsafe_allow_html=True)
  
    col1,col2 = st.columns(2)

    # this will put a button in the middle column
    with col2:
        btn=st.button("send")
    if(btn):
        st.success("Message Sent")

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://image.shutterstock.com/image-photo/blur-background-sunset-260nw-740181883.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )



add_bg_from_url()

if(selected=="Prediction"):

    st.title("Crop Diseases Detection")

    upload_file = st.file_uploader("Upload Effected Leaf", type=['jpg', 'png', 'jpeg'])


    generate_pred = st.button("Predict")
    model = tf.keras.models.load_model(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\potato.h5')


    def import_n_pred(image_data, model):
        size = (256, 256)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        reshape = img[np.newaxis, ...]
        pred = model.predict(reshape)
        return pred


    if generate_pred:
        image = Image.open(upload_file)
        resized_image = image.resize((200, 200))  # Resize the image to a smaller size
        resized_image = np.array(resized_image)  # Convert the resized image to a NumPy array
        # with st.expander('Image', expanded=True):
            # st.image(resized_image, use_column_width=True)

        pred = import_n_pred(image, model)
        labels = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
        st.title("Predicted disease: {}".format(labels[np.argmax(pred)]))

        if labels[np.argmax(pred)] == 'Potato___Early_blight':
            st.markdown(
                "Don't Worry!!\nWe Are Here To Help You.\nPotato___Early_blight, caused by the fungus Entyloma oryzae, is a widely distributed but somewhat minor disease.\nIt can be eradicated by:\n1. Cleaning up debris at the end of each growing season can prevent the spread of leaf smut.\n2. Keeping a good nutrient balance is also important.\n3. Treat seed with a fungicide.\n4. Avoid late planting.\n5. Apply recommended rates of nitrogen.")

        if labels[np.argmax(pred)] == 'Potato___Late_blight':
            st.markdown(
                "Don't Worry!!\nWe Are Here To Help You.\nPotato___Late_blight is a deadly bacterial disease that is among the most destructive afflictions of cultivated rice.\nThis disease is caused by the Gram-negative bacterium Xanthomonas oryzae pv.\nIt can be eradicated by:\n1. Soak the seeds with a solution of plantomycin 10gms or streptocyclin 1.5gms and copper oxychloride 25gms in 10 litres of water.\n2. Spray the affected crop with the same chemicals at 500 litres/ha at 7-10 days intervals 2-3 times on a need basis.\n3. Remove weed hosts and plow under rice stubble, straw, rice ratoons, and volunteer seedlings which can serve as hosts of bacteria.")

        if labels[np.argmax(pred)] == 'Potato___healthy':
            st.markdown(
                "Don't Worry!!\nWe Are Here To Help You.\nPotato___healthy is a fungal disease that infects the coleoptile, leaves, and leaf sheath.\nBrown spot iscaused by the fungus Cochliobolus miyabeanus.\nIt can be eradicated by:\n1. Application of edifenphos, chitosan, iprodione, or carbendazim in the field is also advisable.\n2. Use fungicides (e.g., iprodione, propiconazole, azoxystrobin, trifloxystrobin, and carbendazim) as seed treatments.\n3. Treat seeds with hot water (53−54°C) for 10−12 minutes before planting.")
            

