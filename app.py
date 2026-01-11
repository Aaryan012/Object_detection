import streamlit as st
import os
from utils import obj_detect,load_model
# Loading model 
model=load_model()
# creating streamlit UI
st.title("Object Detection..")
# upload image
file= st.file_uploader("Upload the image where you want to do object detection.",type=['jpg','png','jpeg'])
if file is not None:
    st.image(file)
    file_name=f"upload_photo.{file.name.split('.')[-1]}"
    if st.button('Detect'):
        with open(file_name,'wb') as f:
            f.write(file.read())
        with st.spinner("Detecting..."):
            img=obj_detect(file_name)
        st.image(img,width="content")
        os.remove(file_name)



