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
st.title("Paddy Crop Diseases Detection")

upload_file = st.file_uploader("**Upload Effected Leaf**", type=['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")
model = tf.keras.models.load_model(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\rice.h5')


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

    pred = import_n_pred(image, model)
    labels = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']
    st.title("Predicted disease: {}".format(labels[np.argmax(pred)]))

    if labels[np.argmax(pred)] == 'Leaf smut':
        st.subheader("Why it causes:")
        cau ='<p style="font-size: 20px; font-weight:500;">Paddy leaf smut is caused by the fungal pathogen Ustilaginoidea virens. The disease typically starts in the early stages of rice development and becomes more noticeable during the heading and flowering stages. The fungus infects the rice panicle (inflorescence) and develops within the grain, causing it to swell and form characteristic smut balls. These smut balls replace the rice grains, resulting in yield loss.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        title ='<p style="font-size: 25px; font-weight:1000;">Remedies:</p>'
        rem = '<p style="font-size: 20px; font-weight:500;">Managing paddy leaf smut involves a combination of preventive measures and cultural practices:</p><p style="font-size: 20px; font-weight:500;"><b> Resistant Varieties:</b> Choose tomato varieties that are resistant to Tomato Mosaic Virus when available.</p><p style="font-size: 20px; font-weight:500;"> <b>Field Hygiene: </b> Keep the field clean by removing plant debris and weeds that can harbor the pathogen.</p><p style="font-size: 20px; font-weight:500;"> <b>Early Planting:</b>  Plant rice early to avoid peak disease conditions.</p><p style="font-size: 20px; font-weight:500;"><b>Seed Treatment:</b> Treating seeds with fungicides before planting can help reduce the incidence of leaf smut.</p><p style="font-size: 20px; font-weight:500;"> <b>Proper Fertilization: </b> Balanced and proper fertilization can enhance the plants resistance to disease.</p><p style="font-size: 20px; font-weight:500;"> <b>Sanitation: </b>  Remove and destroy smut balls to reduce the spread of the pathogen.</p>'

        st.markdown(title, unsafe_allow_html=True)
        st.markdown(rem, unsafe_allow_html=True)
        prec = '<p style="font-size: 25px; font-weight:1000;">Precautions:</p>'
        precau = '<p style="font-size: 20px; font-weight:500;">To prevent and manage paddy leaf smut, consider these precautions:</p><p style="font-size: 20px; font-weight:500;"><b> Sanitize Equipment:</b> Clean and sanitize equipment and tools used in the field to prevent the spread of spores.</p><p style="font-size: 20px; font-weight:500;"> <b>Avoid Waterlogged Conditions: </b> Proper water management is important to prevent waterlogging, which can favor disease development.</p><p style="font-size: 20px; font-weight:500;"> <b>Quarantine New Plants:</b>   Isolate new plants before introducing them to your field to prevent the introduction of pathogens.</p>'
        st.markdown(prec, unsafe_allow_html=True)
        st.markdown(precau, unsafe_allow_html=True)

        pro = '<p style="font-size: 25px; font-weight:1000;">Recommended Products:</p>'
        st.markdown(pro, unsafe_allow_html=True)
        
        col3,col1,col2 = st.columns(3)
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\Tebuconazole.png')
            st.image(image, caption=None,width=130)
            st.write('**Tebuconazole**')
            link = '[**BUY NOW**](https://www.amazon.in/Fascure-Tebuconazole-25-9-Systemic-Fungicide/dp/B09RKKLW26?th=1)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\Trifloxystrobin.png')
            st.image(image, caption=None,width=130)
            st.write('**Trifloxystrobin**')
            st.write("[**BUY NOW**](https://www.kissanghar.pk/product-details?name=Nativo-75%wg-75gm-Tebuconazole-50%-+-Trifloxystrobin-25%-65gm-Bayer&c=160)")
        

    if labels[np.argmax(pred)] == 'Bacterial leaf blight':
        st.subheader("Why it causes:")
        cau ='<p style="font-size: 20px; font-weight:500;">Paddy bacterial leaf blight is caused by the bacterium Xanthomonas oryzae pv. oryzae. The bacterium enters the plant through natural openings like stomata or wounds, leading to infection. Warm and humid conditions are favorable for the spread of the disease. Rainwater or irrigation can facilitate the movement of bacteria between plants, causing further infection.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        title ='<p style="font-size: 25px; font-weight:1000;">Remedies:</p>'
        rem = '<p style="font-size: 20px; font-weight:500;">  While complete eradication of bacterial leaf blight can be challenging, management strategies can help mitigate its impact:</p><p style="font-size: 20px; font-weight:500;"><b> Resistant Varieties:</b> Planting rice varieties with genetic resistance to bacterial leaf blight can significantly reduce the risk of infection.</p><p style="font-size: 20px; font-weight:500;"> <b>Healthy Seeds:  </b> Use certified disease-free seeds from reputable sources to minimize the introduction of the pathogen.</p><p style="font-size: 20px; font-weight:500;"> <b>Proper Spacing:</b> Adequate spacing between rice plants allows for better air circulation and reduces humidity around plants.</p><p style="font-size: 20px; font-weight:500;"><b>Crop Rotation: </b> Rotate rice with non-host crops to break the disease cycle and reduce pathogen populations in the soil.</p><p style="font-size: 20px; font-weight:500;"> <b>Aerobic Rice Cultivation: </b>   Practicing aerobic (non-flooded) rice cultivation can reduce disease severity, as bacterial leaf blight thrives in standing water.</p><p style="font-size: 20px; font-weight:500;"> <b>Copper-based Sprays: </b>Copper-based bactericides can be used as a preventive measure, but their effectiveness may vary.</p>'

        st.markdown(title, unsafe_allow_html=True)
        st.markdown(rem, unsafe_allow_html=True)
        prec = '<p style="font-size: 25px; font-weight:1000;">Precautions:</p>'
        precau = '<p style="font-size: 20px; font-weight:500;">To prevent and manage paddy brown spot,consider these precautions:</p><p style="font-size: 20px; font-weight:500;"><b> Healthy Seeds:</b> Use certified disease-free seeds from reputable sources.</p><p style="font-size: 20px; font-weight:500;"> <b>Water Management:</b> Maintain proper water management to avoid waterlogged conditions that promote disease development.</p><p style="font-size: 20px; font-weight:500;"> <b>Field Hygiene:</b>  Keep the field clean by removing infected plant debris and weeds that can harbor bacteria.</p><p style="font-size: 20px; font-weight:500;"> <b>Timely Planting:</b>Plant rice early to avoid peak disease conditions.</p>'
        st.markdown(prec, unsafe_allow_html=True)
        st.markdown(precau, unsafe_allow_html=True)

        pro = '<p style="font-size: 25px; font-weight:1000;">Recommended Products:</p>'
        st.markdown(pro, unsafe_allow_html=True)
        
        col3,col1,col2 = st.columns(3)
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\terramycin 17.png')
            st.image(image, caption=None,width=100)
            st.write('**Terramycin 17**')
            link = '[**BUY NOW**](https://americanhistory.si.edu/collections/search/object/nmah_714840)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\agrimycin.png')
            st.image(image, caption=None,width=150)
            st.write('**Agri-Mycin 50**')
            link = '[**BUY NOW**](https://www.amazon.com/Nufarm-Agri-Mycin-50-3/dp/B07G1JRFJ1)'
            st.markdown(link, unsafe_allow_html=True)
        


    if labels[np.argmax(pred)] == 'Brown spot':
        st.subheader("Why it causes:")
        cau ='<p style="font-size: 20px; font-weight:500;">Paddy brown spot is caused by the fungal pathogen Bipolaris oryzae. The disease develops in warm and humid conditions, often during periods of heavy rain or extended leaf wetness. The fungus infects rice leaves through wounds or natural openings and produces characteristic brown lesions.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        title ='<p style="font-size: 25px; font-weight:1000;">Remedies:</p>'
        rem = '<p style="font-size: 20px; font-weight:500;"> Effective management of paddy brown spot involves a combination of preventive measures and cultural practices:</p><p style="font-size: 20px; font-weight:500;"><b> Resistant Varieties:</b> Choose tomato varieties that are resistant to Tomato Mosaic Virus when available.</p><p style="font-size: 20px; font-weight:500;"> <b>Healthy Seeds:  </b> Use certified disease-free seeds from reputable sources to minimize the introduction of the pathogen.</p><p style="font-size: 20px; font-weight:500;"> <b>Proper Spacing:</b>  Plant rice early to avoid peak disease conditions.</p><p style="font-size: 20px; font-weight:500;"><b>Crop Rotation: </b> Rotate rice with non-host crops to break the disease cycle and reduce pathogen populations in the soil.</p><p style="font-size: 20px; font-weight:500;"> <b>Timely Planting: </b>  Plant rice early to avoid peak disease conditions.</p><p style="font-size: 20px; font-weight:500;"> <b>Leaf Removal: </b>  Remove and destroy heavily infected leaves to reduce the spread of the disease.</p>'

        st.markdown(title, unsafe_allow_html=True)
        st.markdown(rem, unsafe_allow_html=True)
        prec = '<p style="font-size: 25px; font-weight:1000;">Precautions:</p>'
        precau = '<p style="font-size: 20px; font-weight:500;">To prevent and manage paddy brown spot,consider these precautions:</p><p style="font-size: 20px; font-weight:500;"><b> Sanitation:</b> CRemove and destroy infected plant debris to reduce the overwintering of the fungus.</p><p style="font-size: 20px; font-weight:500;"> <b>Avoid Waterlogged Conditions: </b> Proper water management is important to prevent waterlogging, which can favor disease development.</p><p style="font-size: 20px; font-weight:500;"> <b>Field Hygiene:</b>  Maintain a clean field environment by removing weeds and crop residues that can harbor the pathogen.</p>'
        st.markdown(prec, unsafe_allow_html=True)
        st.markdown(precau, unsafe_allow_html=True)

        pro = '<p style="font-size: 25px; font-weight:1000;">Recommended Products:</p>'
        st.markdown(pro, unsafe_allow_html=True)
        
        col3,col1,col2 = st.columns(3)
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\iprodione.png')
            st.image(image, caption=None,width=80)
            st.write('**Iprodione**')
            link = '[**BUY NOW**](https://www.kissanghar.pk/product-details?name=Rovral-%C3%82%C2%AE-500sc-Iprodione-200ml-Fmc-Fungicide&c=361)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\Trifloxystrobin.png')
            st.image(image, caption=None,width=130)
            st.write('**Trifloxystrobin**')
            st.write("[**BUY NOW**](https://www.kissanghar.pk/product-details?name=Nativo-75%wg-75gm-Tebuconazole-50%-+-Trifloxystrobin-25%-65gm-Bayer&c=160)")
        
