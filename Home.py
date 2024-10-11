import streamlit as st
from PIL import Image
st.set_page_config(layout="wide")

st.markdown("""
<style>

	.stTabs [data-baseweb="tab"] {
		background-color: #77a380;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #fad07d;
	}

</style>""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Learn More", "Upload","About Me"])

import base64
#home
with tab1:
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
    set_png_as_page_bg('background.png')

    #split homescreen into two column add images, add about me image, upload page (file uploader widget)-steps to guide


    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("swara.png")

    st.markdown("<h2 style=' color: ""#fad07d"";'>Introdution to Carnatic Music</h2>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
    st.write("Carnatic music is a classical tradition from South India, characterized by its complex melodies and rhythms. It features vocal performances, often accompanied by instruments like the violin and mridangam. With a strong emphasis on improvisation and expression, Carnatic music reflects deep cultural and spiritual roots. It invites listeners to explore a rich tapestry of sound and emotion. Being able to appriciate Carnatic music is no easy feat. It takes time and constant listening to develop a liking for such heavy rich music.")
    st.markdown("<h2 style=' color: ""#fad07d"";'>Music Theory</h2>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
    st.write("Carnatic music theory is built around key ideas like ragas (melodic frameworks) and talas (rhythmic cycles). Each raga has specific notes (swaras) and rules for how they can be used, creating different moods and feelings. Talas provide the rhythmic structure, often featuring complex patterns that enhance the music. Melakarta ragas are the main ragas with a set scale of seven notes used in both ascending and descending order, forming the basis for many others. Janya ragas come from Melakarta ragas and can leave out some notes for more flexibility and emotional expression. The theory also includes concepts like gamakas (ornamentation) and alapana (improvisation), which allow musicians to explore melodies within a structured framework. This foundation supports the improvisational nature of the music, enabling artists to create unique interpretations while following traditional forms.")
    st.markdown("<h2 style=' color: ""#fad07d"";'>Famous Composers</h2>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
    st.write("Carnatic music features several famous composers who have shaped the tradition. Thyagaraja (1767-1847) is celebrated for his devotional songs dedicated to Lord Rama, and the Thyagaraja Aradhana festival honors his contributions. Muthuswami Dikshitar (1775-1835), a contemporary of Thyagaraja, is known for his complex compositions in Sanskrit, often reflecting philosophical ideas. He traveled widely in South India, gathering musical influences. Syama Sastri (1762-1827) is recognized for his emotive songs that express devotion, many of which he composed while serving the Tanjore court. These composers have left a lasting impact, and their music continues to inspire many today.")
    st.markdown("<h2 style=' color: ""#fad07d"";'>Performing</h2>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
    st.write("Carnatic music is usually performed in concerts called kacheris. A kacheri typically starts with a varnam, which showcases the raga and the musician's skills. This is followed by several kritis, which are composed pieces expressing different emotions. Performers often include improvisational sections, like alapana (freeform exploration of the raga) and neraval (improvisation on a line from a kriti). Accompaniment usually features instruments like the mridangam (drum) and violin, creating a rich interaction between the vocalist and the musicians. The concert ends with a lively tani avartanam, where the percussionist improvises rhythmically, inviting the audience to engage and appreciate the music.")
    st.markdown("<h2 style=' color: ""#fad07d"";'>RanjaniGayathri</h2>", unsafe_allow_html=True)
    st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
    col1,col2 = st.columns(2)

    with col1:
        st.video("https://youtu.be/44HUgWxBFX4?si=PhVh2Mb7OETMC9yi",)



with tab2:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("learn.png")

with tab3:
    st.header("Upload")


#about me
with tab4:
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
