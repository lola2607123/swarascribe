import streamlit as st
import base64
st.set_page_config(layout="wide")
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg('treclef.png')

col1, col2, col3 = st.columns(3)

with col2:
    st.image("aboutme.png")

col3,col4= st.columns(2)

with col4:
    st.write('''Hi! My name is Sri Gupta, and I am currently a student at North London Collegiate School Dubai with a strong passion for Carnatic music. I’ve been learning and exploring this traditional form of South Indian classical music for 7 years and have fallen completely in love with it. My goal is to deepen my understanding of its rich history, techniques, and melodies, while sharing my journey with others who appreciate the beauty of Carnatic music. My passion for Carnatic music started when I first listened to a young girl named Sooryagayathri. At the time, she was 3 years older than me, and I wanted to be just like her. My motivation for making this website was to share my interest in this historic art form with those who are also captivated by the intricate rhythms and deep emotional expression in Carnatic compositions. I find joy in learning new ragas and perfecting my skills in vocal or instrumental performances. Whether it’s through my practice, research, or performances, I’m constantly inspired by the complexity and beauty of this art form.''')

with col3:
    st.image("man.png")

st.write("This website is dedicated to my love for Carnatic music. Here, I showcase what I’ve learnt, share insights about different ragas, talas, and composers, and provide a scanner to identify ragas of any composition you may upload. Whether you’re new to Carnatic music or a fellow enthusiast, I hope this site serves as a platform for learning and appreciating the depth of this classical art form. Thank you for visiting, and feel free to reach out if you'd like to discuss music or collaborate!")