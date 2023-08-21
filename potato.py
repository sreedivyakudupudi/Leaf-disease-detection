import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
from streamlit_option_menu import option_menu
import webbrowser
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
st.title("Potato Crop Diseases Detection")

upload_file = st.file_uploader("**Upload Effected Leaf**", type=['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")
model = tf.keras.models.load_model(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\potato.h5')


def import_n_pred(image_data, model):
    size = (256, 256)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    reshape = img[np.newaxis, ...]
    pred = model.predict(reshape)
    return pred

dis=""
if generate_pred:
    image = Image.open(upload_file)
    resized_image = image.resize((200, 200))  # Resize the image to a smaller size
    resized_image = np.array(resized_image)  # Convert the resized image to a NumPy array
    # with st.expander('Image', expanded=True):
        # st.image(resized_image, use_column_width=True)

    pred = import_n_pred(image, model)
    labels = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
    st.header("Predicted disease: {}".format(labels[np.argmax(pred)]))
    dis = labels[np.argmax(pred)]
    if dis == 'Potato___Early_blight':
        st.subheader("Why it causes:")
        cau ='<p style="font-size: 20px; font-weight:500;">Early blight of potato is caused by the fungus, Alternaria solani, which can cause disease in potato, tomato, other members of the potato family, and some mustards. This disease, also known as target spot, rarely affects young, vigorously growing plants. It is found on older leaves first. Early blight is favored by warm temperatures and high humidity.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        title ='<p style="font-size: 25px; font-weight:1000;">Remedies:</p>'
        rem = '<p style="font-size: 20px; font-weight:500;">1. Prune or stake plants to improve air circulation and reduce fungal problems.</p><p style="font-size: 20px; font-weight:500;">2. Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.</p><p style="font-size: 20px; font-weight:500;">Keep the soil under plants clean and free of garden debris. Add a layer of organic compost to prevent the spores from splashing back up onto vegetation.</p><p style="font-size: 20px; font-weight:500;">3. Drip irrigation and soaker hoses can be used to help keep the foliage dry.</p><p style="font-size: 20px; font-weight:500;">4. For best control, apply copper-based fungicides early, two weeks before disease normally appears or when weather forecasts predict a long period of wet weather. Alternatively, begin treatment when disease first appears, and repeat every 7-10 days for as long as needed.</p><p style="font-size: 20px; font-weight:500;">5. Containing copper and pyrethrins, Bonide® Garden Dust is a safe, one-step control for many insect attacks and fungal problems. For best results, cover both the tops and undersides of leaves with a thin uniform film or dust. Depending on foliage density, 10 oz will cover 625 sq ft. Repeat applications every 7-10 days, as needed.</p><p style="font-size: 20px; font-weight:500;">6. SERENADE Garden is a broad spectrum, preventative bio-fungicide recommended for the control or suppression of many important plant diseases. For best results, treat prior to foliar disease development or at the first sign of infection. Repeat at 7-day intervals or as needed.</p><p style="font-size: 20px; font-weight:500;">7. Remove and destroy all garden debris after harvest and practice crop rotation the following year.</p><p style="font-size: 20px; font-weight:500;">8.Burn or bag infected plant parts. Do NOT compost.</p>'
        st.markdown(title, unsafe_allow_html=True)
        st.markdown(rem, unsafe_allow_html=True)
        prec = '<p style="font-size: 25px; font-weight:1000;">Precautions:</p>'
        precau = '<p style="font-size: 20px; font-weight:500;">Early blight can be minimized by maintaining optimum growing conditions, including proper fertilization, irrigation, and management of other pests. Grow later maturing, longer season varieties. Fungicide application is justified only when the disease is initiated early enough to cause economic loss.</p>'
        st.markdown(prec, unsafe_allow_html=True)
        st.markdown(precau, unsafe_allow_html=True)

        pro = '<p style="font-size: 25px; font-weight:1000;">Recommended Products:</p>'
        st.markdown(pro, unsafe_allow_html=True)
        
        col3,col1,col2 = st.columns(3)
        with col3:
            st.markdown("![Foo](https://www.planetnatural.com/wp-content/uploads/2013/03/liquid-copper-spray-195x215.jpg)")
            st.write('**Copper Liquid Spary**')
            link = '[**BUY NOW**](https://www.amazon.com/BONIDE-PRODUCTS-775-Fungicide-32-Ounce/dp/B016IVIJLG/ref=as_li_ss_tl?keywords=Liquid+Copper+Spray&qid=1573678911&sr=8-2&linkCode=sl1&tag=planetnatur03-20&linkId=dd3de186832f49f2d228be1726fee688)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\liquid-copper-concentrate-removebg-preview.png')
            st.image(image, caption=None,width=130)
            st.write('**Copper Liquid**')
            st.write("[**BUY NOW**](https://www.amazon.in/Liqui-Cop-Copper-Fungicide-Spray-Conc/dp/B000UGQ4MW/ref=sr_1_11?crid=2K0TB9AIDHFX3&keywords=copper+liquid+spray&qid=1692292589&sprefix=copper+liquid+spray%2Caps%2C386&sr=8-11)")
        
        c3,c1,c2 = st.columns(3)
        with c3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\seranade.png')
            st.image(image, caption=None,width=115)
            st.write('**Serenade Garden**')
            link = '[**BUY NOW**](https://www.amazon.in/Serenade-Garden-Disease-Control-Fungicide/dp/B01N0T7CBY)'
            st.markdown(link, unsafe_allow_html=True)
            
        with c2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\garden dust.png')
            st.image(image,width=125)
            st.write('**Garden Dust**')
            st.write("[**BUY NOW**](https://www.amazon.com/Bonide-Chemical-933-Number-4-Garden/dp/B000OW9474/ref=as_li_ss_tl?keywords=Bonide+Garden+Dust&qid=1573780720&sr=8-5&linkCode=sl1&tag=planetnatur03-20&linkId=51a09b0c66a69766048831a1c570907d)")
            
    if dis == 'Potato___Late_blight':
        st.subheader("Why it causes:")
        cau ='<p style="font-size: 20px; font-weight:500;">Late blight is a disease which is common in solanaceous plants like potatoes, tomatoes, etc. It is caused by an oomycete pathogen, i.e., Phytophthora infestans. Late blight in a potato is a lethal disease which can have the potential to devastate the crop. It can attack the crop at any stage and can infect the foliage and tubers.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">1. Plant resistant cultivars when available.</p><p style="font-size: 20px; font-weight:500;">2. Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation.</p><p style="font-size: 20px; font-weight:500;">3. Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day — avoid overhead irrigation.</p><p style="font-size: 20px; font-weight:500;">4. Destroy all tomato and potato debris after harvest (see Fall Garden Cleanup).</p><p style="font-size: 20px; font-weight:500;">5.Apply a copper based fungicide (2 oz/ gallon of water) every 7 days or less, following heavy rain or when the amount of disease is increasing rapidly. If possible, time applications so that at least 12 hours of dry weather follows application.</p><p style="font-size: 20px; font-weight:500;">6. Used as a foliar spray, Organocide® Plant Doctor will work its way through the entire plant to prevent fungal problems from occurring and attack existing many problems. Mix 2 tsp/ gallon of water and spray at transplant or when direct seeded crops are at 2-4 true leaf, then at 1-2 week intervals as required to control disease.</p><p style="font-size: 20px; font-weight:500;">7. Safely treat fungal problems with SERENADE Garden. This broad spectrum bio-fungicide uses a patented strain of Bacillus subtilis and is approved for organic use. Best of all, SERENADE is completely non-toxic to honey bees and beneficial insects.</p><p style="font-size: 20px; font-weight:500;">8. Monterey® All Natural Disease Control is a ready-to-use blend of naturally occurring ingredients that control most plant foliar diseases. All stages of the disease is controlled, but applying before infestation gives the best results.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:500;">Late blight is controlled by eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices, and applying fungicides when necessary. Air drainage to facilitate the drying of foliage each day is important. Under marginal conditions, overhead sprinkler irrigation can favor late blight; in Tule Lake under solid set sprinklers, conditions conducive to late blight development are enhanced by day time irrigation but not night time irrigation.</p>'
        st.markdown(precau, unsafe_allow_html=True)

        st.subheader("Recommended Products:")
        
        
        col3,col1,col2 = st.columns(3)
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\seranade.png')
            st.image(image, caption=None,width=115)
            st.write('**Serenade Garden**')
            link = '[**BUY NOW**](https://www.amazon.in/Serenade-Garden-Disease-Control-Fungicide/dp/B01N0T7CBY)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\liquid-copper-concentrate-removebg-preview.png')
            st.image(image, caption=None,width=130)
            st.write('**Copper Liquid**')
            st.write("[**BUY NOW**](https://www.amazon.in/Liqui-Cop-Copper-Fungicide-Spray-Conc/dp/B000UGQ4MW/ref=sr_1_11?crid=2K0TB9AIDHFX3&keywords=copper+liquid+spray&qid=1692292589&sprefix=copper+liquid+spray%2Caps%2C386&sr=8-11)")
       

    if dis == 'Potato___healthy':            
        st.header("No worries!!:blush:")
        st.header("Potato is Healthy :white_check_mark:")
        #st.title(":blush:")
        

