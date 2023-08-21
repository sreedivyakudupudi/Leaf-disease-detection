import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Baloo+Bhai+2&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Baloo Bhai 2','Times New Roman';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

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
st.title("Corn Crop Diseases Detection")

upload_file = st.file_uploader("Upload Effected Leaf", type=['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")
model = tf.keras.models.load_model(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\corn.h5')


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
    labels = ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']
    st.title("Predicted disease: {}".format(labels[np.argmax(pred)]))

    if labels[np.argmax(pred)] == 'Blight':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nLeaf smut, caused by the fungus Entyloma oryzae, is a widely distributed but somewhat minor disease.\nIt can be eradicated by:\n1. Cleaning up debris at the end of each growing season can prevent the spread of leaf smut.\n2. Keeping a good nutrient balance is also important.\n3. Treat seed with a fungicide.\n4. Avoid late planting.\n5. Apply recommended rates of nitrogen.")

    if labels[np.argmax(pred)] == 'Common_Rust':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nBacterial leaf blight is a deadly bacterial disease that is among the most destructive afflictions of cultivated rice.\nThis disease is caused by the Gram-negative bacterium Xanthomonas oryzae pv.\nIt can be eradicated by:\n1. Soak the seeds with a solution of plantomycin 10gms or streptocyclin 1.5gms and copper oxychloride 25gms in 10 litres of water.\n2. Spray the affected crop with the same chemicals at 500 litres/ha at 7-10 days intervals 2-3 times on a need basis.\n3. Remove weed hosts and plow under rice stubble, straw, rice ratoons, and volunteer seedlings which can serve as hosts of bacteria.")

    if labels[np.argmax(pred)] == 'Gray_Leaf_Spot':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nBrown spot is a fungal disease that infects the coleoptile, leaves, and leaf sheath.\nBrown spot iscaused by the fungus Cochliobolus miyabeanus.\nIt can be eradicated by:\n1. Application of edifenphos, chitosan, iprodione, or carbendazim in the field is also advisable.\n2. Use fungicides (e.g., iprodione, propiconazole, azoxystrobin, trifloxystrobin, and carbendazim) as seed treatments.\n3. Treat seeds with hot water (53−54°C) for 10−12 minutes before planting.")
    
    if labels[np.argmax(pred)] == 'Healthy':
        st.header("No worries!!:blush:")
        st.header("Your crop is Healthy :white_check_mark:")