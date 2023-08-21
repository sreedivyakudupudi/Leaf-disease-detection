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
st.title("Tomato Crop Diseases Detection")

upload_file = st.file_uploader("**Upload Effected Leaf**", type=['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")
model = tf.keras.models.load_model(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\tomato.h5')


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
    labels = ['Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']
    st.header("Predicted disease: {}".format(labels[np.argmax(pred)]))

    if labels[np.argmax(pred)] == 'Tomato_Bacterial_spot':
        st.subheader("Why it causes? :")
        cau ='<p style="font-size: 20px; font-weight:500;">Tomato bacterial spot is caused by the bacterium Xanthomonas campestris pv. vesicatoria. The bacteria enter the plant through natural openings like stomata, wounds, or cracks in the plant tissues. Warm and humid conditions facilitate the spread and development of the disease. It can also be spread through contaminated tools, equipment, or hands.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">Unfortunately, once a plant is infected with bacterial spot, there is no cure. The primary focus is on preventing the spread of the disease to healthy plants. Here are some management strategies:</p><p style="font-size: 20px; font-weight:500;"><b>Resistant Varieties:</b> Planting resistant tomato varieties can significantly reduce the risk of infection.</p><p style="font-size: 20px; font-weight:500;"><b>Crop Rotation:</b> Rotate tomatoes with non-host crops to reduce the buildup of the pathogen in the soil.</p><p style="font-size: 20px; font-weight:500;"><b>Sanitation:</b> Regularly remove and destroy infected plant debris to prevent overwintering of the bacteria.</p><p style="font-size: 20px; font-weight:500;"><b>Spacing:</b> Proper plant spacing allows for better air circulation and helps reduce humidity around plants.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:500;"><b>Start with Disease-Free Plants:</b> Purchase plants from reputable sources to minimize the risk of introducing the disease.</p><p style="font-size: 20px; font-weight:500;"><b>Practice Good Hygiene:</b> Clean tools and equipment regularly to prevent the transfer of bacteria.</p><p style="font-size: 20px; font-weight:500;"><b>Monitor Your Plants:</b> Regularly inspect your tomato plants for symptoms and take action if you notice any signs of infection.</p><p style="font-size: 20px; font-weight:500;"><b>Quarantine New Plants:</b> If you introduce new plants to your garden, isolate them for a period to ensure they are disease-free before planting them with your established plants.</p>'
        st.markdown(precau, unsafe_allow_html=True)

        st.subheader("Recommended Products:")
        
        
        col3,col1,col2 = st.columns(3)
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\agrimycin.png')
            st.image(image, caption=None,width=150)
            st.write('**Agri-Mycin 50**')
            link = '[**BUY NOW**](https://www.amazon.com/Nufarm-Agri-Mycin-50-3/dp/B07G1JRFJ1)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\liquid-copper-spray-400x440-removebg-preview.png')
            st.image(image, caption=None,width=145)
            st.write('**Copper Liquid**')
            st.write("[**BUY NOW**](https://www.amazon.in/Liqui-Cop-Copper-Fungicide-Spray-Conc/dp/B000UGQ4MW/ref=sr_1_11?crid=2K0TB9AIDHFX3&keywords=copper+liquid+spray&qid=1692292589&sprefix=copper+liquid+spray%2Caps%2C386&sr=8-11)")
        

    if labels[np.argmax(pred)] == 'Tomato_Early_blight':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nBacterial leaf blight is a deadly bacterial disease that is among the most destructive afflictions of cultivated rice.\nThis disease is caused by the Gram-negative bacterium Xanthomonas oryzae pv.\nIt can be eradicated by:\n1. Soak the seeds with a solution of plantomycin 10gms or streptocyclin 1.5gms and copper oxychloride 25gms in 10 litres of water.\n2. Spray the affected crop with the same chemicals at 500 litres/ha at 7-10 days intervals 2-3 times on a need basis.\n3. Remove weed hosts and plow under rice stubble, straw, rice ratoons, and volunteer seedlings which can serve as hosts of bacteria.")

    if labels[np.argmax(pred)] == 'Tomato_Late_blight':
        st.subheader("Why it causes? :")
        cau ='<p style="font-size: 20px; font-weight:500;">Tomato late blight is caused by the pathogen Phytophthora infestans. It thrives in cool and moist conditions. Spores are spread by wind, rain, or irrigation water. Once spores land on susceptible plant parts, they germinate and infect the plant tissues, leading to rapid disease progression.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">While its challenging to completely eradicate late blight once it has infected plants, there are measures to manage its impact:</p><p style="font-size: 20px; font-weight:500;"><b>Resistant Varieties:</b> Planting resistant tomato varieties can significantly reduce the risk of infection.</p><p style="font-size: 20px; font-weight:500;"><b>Cultural Practices:</b> Proper plant spacing, pruning, and staking promote air circulation and reduce humidity, which can slow down disease development.</p><p style="font-size: 20px; font-weight:500;"><b>Fungicides:</b> Copper-based fungicides and other fungicides labeled for late blight management can help reduce disease spread. Apply them preventively and according to the label instructions. Fungicides are most effective when used in a rotation to prevent the development of resistant strains.</p><p style="font-size: 20px; font-weight:500;"><b>Organic Solutions:</b> Some organic solutions like copper-based sprays, neem oil, and biological control agents can also help manage late blight to some extent.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:500;"><b>Proper Plant Spacing:</b> Adequate spacing between plants allows for better air circulation, reducing humidity and the spread of the disease.</p><p style="font-size: 20px; font-weight:500;"><b>Avoid Overhead Watering:</b>  Watering at the base of plants helps keep foliage dry and reduces conditions favorable for disease development.</p><p style="font-size: 20px; font-weight:500;"><b>Timely Harvest:</b> Harvest mature fruits promptly to prevent disease spread within the plant canopy.</p><p style="font-size: 20px; font-weight:500;"><b>Sanitation:</b> Remove and destroy infected plant debris to prevent overwintering of the pathogen.</p><p style="font-size: 20px; font-weight:500;"><b>Crop Rotation: </b> Rotate tomatoes and potatoes with unrelated crops to prevent the buildup of the pathogen in the soil.</p>'
        st.markdown(precau, unsafe_allow_html=True)

        st.subheader("Recommended Products:")
        
        
        col3,col1,col2 = st.columns(3)
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\Presidio.png')
            st.image(image, caption=None,width=150)
            st.write('**Presidio 4FL**')
            link = '[**BUY NOW**](https://www.domyown.com/presidio-fungicide-p-21758.html)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\orondis opti.png')
            st.image(image, caption=None,width=95)
            st.write('**Orondis Opti**')
            st.write("[**BUY NOW**](https://www.agcareproducts.com/products/orondis-opti-2-5-gal)")
        

        
    if labels[np.argmax(pred)] == 'Tomato_Leaf_Mold':
        st.subheader("Why it causes? :")
        cau ='<p style="font-size: 20px; font-weight:500;">Tomato leaf mold is caused by the fungus Fulvia fulva. It thrives in warm and humid conditions, often developing on the underside of tomato leaves. The disease spreads through spores produced by the fungus, and it can be introduced into your garden through infected seeds, transplants, or contaminated tools.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">Although there is no cure for leaf mold once a plant is infected, management strategies can help reduce its impact:</p><p style="font-size: 20px; font-weight:500;"><b>Improve Air Circulation:</b> Proper spacing and pruning promote better air circulation, reducing humidity and the conditions conducive to fungal growth.</p><p style="font-size: 20px; font-weight:500;"><b>Mulching: </b> Applying mulch around plants can help prevent soil splashing onto leaves, which can contribute to disease spread.Resistant Varieties: Some tomato varieties are resistant to leaf mold. Choosing resistant varieties can greatly reduce the risk of infection.</p><p style="font-size: 20px; font-weight:500;"><b>Fungicides:</b> Fungicides labeled for leaf mold control can be used preventively. Products containing chlorothalonil, mancozeb, or other recommended fungicides can help reduce disease severity. Follow the instructions on the label for proper application.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:500;"><b>Healthy Transplants: </b>  Purchase or raise healthy tomato transplants from reputable sources to reduce the risk of introducing the disease.</p><p style="font-size: 20px; font-weight:500;"><b>Avoid Overhead Watering:</b>  Watering at the base of plants helps keep foliage dry and reduces conditions favorable for disease development.</p><p style="font-size: 20px; font-weight:500;"><b>Monitor Regularly: </b>  Regularly inspect your tomato plants for signs of leaf mold, especially on the undersides of leaves.</p><p style="font-size: 20px; font-weight:500;"><b>Sanitation:</b> Remove and destroy infected plant material to reduce the chances of spores overwintering and spreading.</p>'
        st.markdown(precau, unsafe_allow_html=True)

        st.subheader("Recommended Products:")
        
        
        col3,col1,col2 = st.columns(3)
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\mancozeb.png')
            st.image(image, caption=None,width=115)
            st.write('**Mancozeb**')
            link = '[**BUY NOW**](https://www.amazon.in/Bonide-Chemical-862-Mancozeb-Fungicide/dp/B000BWZ9JO)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\dithane.png')
            st.image(image, caption=None,width=150)
            st.write('**Dithane**')
            st.write("[**BUY NOW**](https://www.meesho.com/dithane-m-45-fungicide-500-gm/p/23bgvo)") 
    
    
    if labels[np.argmax(pred)] == 'Tomato_Septoria_leaf_spot':
        st.subheader("Why it causes?:")
        cau ='<p style="font-size: 20px; font-weight:500;">Tomato septoria leaf spot is caused by the fungus Septoria lycopersici. The disease spreads through spores produced by the fungus. Warm and humid conditions, along with overhead watering or rain, create an environment conducive to spore germination and disease development. The fungus typically overwinters on infected plant debris and can survive in the soil.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">While its difficult to completely eradicate septoria leaf spot once its established, several strategies can help manage its impact:</p><p style="font-size: 20px; font-weight:500;"><b>Improve Air Circulation:</b> Proper spacing and pruning promote better air circulation, reducing humidity and the conditions conducive to fungal growth.</p><p style="font-size: 20px; font-weight:500;"><b>Resistant Varieties:  </b><p style="font-size: 20px; font-weight:500;">While its difficult to completely eradicate septoria leaf spot once its established, several strategies can help manage its impact:</p><p style="font-size: 20px; font-weight:500;"><b>Proper Plant Spacing:</b> Adequate spacing between plants promotes air circulation, reducing humidity and the spread of the disease.</p><p style="font-size: 20px; font-weight:500;"><b>Resistant Varieties:  </b> Applying mulch around plants can help prevent soil splashing onto leaves, which can contribute to disease spread.Resistant Varieties: Some tomato varieties are resistant to leaf mold. Choosing resistant varieties can greatly reduce the risk of infection.</p><p style="font-size: 20px; font-weight:500;"><b>Prune Lower Leaves: </b> Remove and destroy lower leaves that show symptoms to reduce disease spread.</p><p style="font-size: 20px; font-weight:500;"><b>Crop Rotation: </b> Rotate tomato plants with unrelated crops to break the disease cycle and reduce the buildup of the pathogen in the soil.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:500;"><b> Sanitation:</b> Remove and destroy infected plant debris and fallen leaves to reduce the overwintering of the fungus.</p><p style="font-size: 20px; font-weight:500;"> <b>Water Management: </b>Avoid overhead watering, as wet foliage encourages spore germination and disease spread. Water at the base of the plants.</p><p style="font-size: 20px; font-weight:500;">6. <b>Avoid Crowding:</b> Avoid overcrowding plants, as this can lead to poor air circulation and higher humidity levels.</p><p style="font-size: 20px; font-weight:500;">7.<b> Quarantine New Plants:</b>  Isolate new plants before introducing them to your garden to prevent the introduction of the disease.</p>'
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
    if labels[np.argmax(pred)] == 'Tomato_Spider_mites_Two_spotted_spider_mite':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nLeaf smut, caused by the fungus Entyloma oryzae, is a widely distributed but somewhat minor disease.\nIt can be eradicated by:\n1. Cleaning up debris at the end of each growing season can prevent the spread of leaf smut.\n2. Keeping a good nutrient balance is also important.\n3. Treat seed with a fungicide.\n4. Avoid late planting.\n5. Apply recommended rates of nitrogen.")

    if labels[np.argmax(pred)] == 'Tomato__Target_Spot':
        st.markdown(
            "Don't Worry!!\nWe Are Here To Help You.\nBacterial leaf blight is a deadly bacterial disease that is among the most destructive afflictions of cultivated rice.\nThis disease is caused by the Gram-negative bacterium Xanthomonas oryzae pv.\nIt can be eradicated by:\n1. Soak the seeds with a solution of plantomycin 10gms or streptocyclin 1.5gms and copper oxychloride 25gms in 10 litres of water.\n2. Spray the affected crop with the same chemicals at 500 litres/ha at 7-10 days intervals 2-3 times on a need basis.\n3. Remove weed hosts and plow under rice stubble, straw, rice ratoons, and volunteer seedlings which can serve as hosts of bacteria.")

    if labels[np.argmax(pred)] == 'Tomato__Tomato_YellowLeaf__Curl_Virus':
        st.subheader("Why it causes?:")
        cau ='<p style="font-size: 20px; font-weight:500;">TYLCV is caused by a virus from the genus Begomovirus, specifically transmitted by the sweet potato whitefly (Bemisia tabaci). The virus is non-circulative, meaning it does not multiply within the whitefly vector but is retained in its body and can be transmitted to healthy plants during feeding. Once infected, the virus disrupts the plants normal physiological processes, leading to the characteristic symptoms of yellowing, curling, stunting, and other abnormalities.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">1. Do not move infected or host plants or seedlings, or infected SLW</p><p style="font-size: 20px; font-weight:500;">2. Maintain a high standard of weed control within and around crops to reduce hosts of both the virus and silverleaf whitefly.</p><p style="font-size: 20px; font-weight:500;">3. Plant new crops as far away as practicable from existing crops which may harbour the virus and its carrier, silverleaf whitefly</p><p style="font-size: 20px; font-weight:500;">4.Planting resistant varieties of tomatoes.</p><p style="font-size: 20px; font-weight:500;">5control silverleaf whiteflies using appropriate chemicals, application methods and IPM strategies</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:1000;">Prevention of ToMV infection in tomatoes:</p><p style="font-size: 20px; font-weight:500;">The best way to prevent ToMV infection in tomatoes is to plant resistant varieties of tomatoes.</p><p style="font-size: 20px; font-weight:500;">1. Use resistent or tolerant variaties.</p><p style="font-size: 20px; font-weight:500;">2. Disinfecting tools and equipment after working with tomatoes.</p><p style="font-size: 20px; font-weight:500;">3. Avoiding contact with infected plants.</p><p style="font-size: 20px; font-weight:500;">4.<b> Resistant Varieties:</b> Choose tomato varieties that are resistant to Tomato Mosaic Virus when available.</p><p style="font-size: 20px; font-weight:500;">5. <b>Crop Rotation: </b> Rotate tomato crops with non-susceptible plants to reduce the buildup of the virus in the soil.</p><p style="font-size: 20px; font-weight:500;">6. <b>Use Disease-Free Seeds and Plants:</b> Start with certified disease-free seeds or seedlings from reputable sources.</p><p style="font-size: 20px; font-weight:500;">7.<b> Insect Control:</b> Manage insect vectors like aphids and whiteflies through appropriate pest management methods to reduce the risk of virus transmission.</p>'
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
       
        
    if labels[np.argmax(pred)] == 'Tomato__Tomato_mosaic_virus':
        st.subheader("Why it causes? :")
        cau ='<p style="font-size: 20px; font-weight:500;">Tomato Mosaic Virus is caused by the Tomato mosaic virus (ToMV) and the Tobacco mosaic virus (TMV), which belong to the Tobamovirus genus. These viruses are highly stable and can survive in infected plant debris and soil for extended periods. The virus is primarily transmitted through direct contact with infected plants, either mechanically or via insect vectors such as aphids and whiteflies. Humans can also inadvertently spread the virus by handling infected plants and then healthy ones without proper sanitation.</p>'
        st.markdown(cau, unsafe_allow_html=True)
        st.subheader("Remedies:")
        rem = '<p style="font-size: 20px; font-weight:500;">1. Removing and destroying infected plants and plant debris</p><p style="font-size: 20px; font-weight:500;">2. Watering plants at the base to avoid wetting the leaves.</p><p style="font-size: 20px; font-weight:500;">3. Providing good air circulation around plants.</p><p style="font-size: 20px; font-weight:500;">4.Planting resistant varieties of tomatoes.</p><p style="font-size: 20px; font-weight:500;">5.Using insect control measures to reduce the number of insects that can transmit the virus.</p>'
        st.markdown(rem, unsafe_allow_html=True)
        st.subheader("Precautions:")
        precau = '<p style="font-size: 20px; font-weight:1000;">Prevention of ToMV infection in tomatoes:</p><p style="font-size: 20px; font-weight:500;">The best way to prevent ToMV infection in tomatoes is to plant resistant varieties of tomatoes.</p><p style="font-size: 20px; font-weight:500;">1. Buying transplants from reputable sources.</p><p style="font-size: 20px; font-weight:500;">2. Disinfecting tools and equipment after working with tomatoes.</p><p style="font-size: 20px; font-weight:500;">3. Avoiding contact with infected plants.</p><p style="font-size: 20px; font-weight:500;">4.<b> Resistant Varieties:</b> Choose tomato varieties that are resistant to Tomato Mosaic Virus when available.</p><p style="font-size: 20px; font-weight:500;">5. <b>Crop Rotation: </b> Rotate tomato crops with non-susceptible plants to reduce the buildup of the virus in the soil.</p><p style="font-size: 20px; font-weight:500;">6. <b>Use Disease-Free Seeds and Plants:</b> Start with certified disease-free seeds or seedlings from reputable sources.</p><p style="font-size: 20px; font-weight:500;">7.<b> Insect Control:</b> Manage insect vectors like aphids and whiteflies through appropriate pest management methods to reduce the risk of virus transmission.</p>'
        st.markdown(precau, unsafe_allow_html=True)

        st.subheader("Recommended Products:")
        c3,c1,c2 = st.columns(3)
        with c3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\safer soap.png')
            st.image(image, caption=None,width=100)
            st.write('**Safer Soap**')
            link = '[**BUY NOW**](https://www.amazon.in/32-Ounce-Safer-Brand-Insect-Killing/dp/B000BQL8UY)'
            st.markdown(link, unsafe_allow_html=True)
            
        with c2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\bon neem.png')
            st.image(image, caption=None,width=85)
            st.write('**Bon-Neem II**')
            st.write("[**BUY NOW**](https://www.amazon.com/Bonide-Bon-Neem-Insecticidal-Soap-Rtu/dp/B001D10EQA?th=1)")
        
        
        col3,col1,col2 = st.columns(3)
        with col3:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\harvest.png')
            st.image(image, caption=None,width=115)
            st.write('**Harvest Guard**')
            link = '[**BUY NOW**](https://www.amazon.in/Gardeneer-Harvest-Guard-Germination-Garden-Protection/dp/B01N4GCEG7)'
            st.markdown(link, unsafe_allow_html=True)
            
        with col2:
            image = Image.open(r'C:\Users\SREE DIVYA\Documents\Code\potato_disease\training\products\alldown.png')
            st.image(image, caption=None,width=115)
            st.write('**AllDown**')
            st.write("[**BUY NOW**](https://www.amazon.com/gp/product/B00JMI4ZU2/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=planetnatur03-20&linkId=2c16cc09090d3b74b36dd983747e5ea8&language=en_US)")

        
       
    if labels[np.argmax(pred)] == 'Tomato_healthy':
        st.header("No worries!!:blush:")
        st.header("Tomato is Healthy :white_check_mark:")