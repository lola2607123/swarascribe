import streamlit as st


st.set_page_config(layout="wide")

st.markdown("""
<style>

	.stTabs [data-baseweb="tab"] {
		background-color: #77a380;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #77a380;
	}

</style>""", unsafe_allow_html=True)

import base64
#home

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
c, c1 = st.columns(2)
with c:
    st.write("Carnatic music is a classical tradition from South India, characterized by its complex melodies and rhythms. It features vocal performances, often accompanied by instruments like the violin and mridangam. With a strong emphasis on improvisation and expression, Carnatic music reflects deep cultural and spiritual roots. It invites listeners to explore a rich tapestry of sound and emotion. Being able to appriciate Carnatic music is no easy feat. It takes time and constant listening to develop a liking for such heavy rich music.")
with c1:
    st.image("https://www.bella-entertainment.com/wp-content/uploads/2023/01/monis-yousafzai-QuuaCzjXOYk-unsplash.jpg", width=500)


st.markdown("<h2 style=' color: ""#fad07d"";'>Music Theory</h2>", unsafe_allow_html=True)
st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
c2, c3 = st.columns(2)
with c3:
    st.write("Carnatic music theory is built around key ideas like ragas (melodic frameworks) and talas (rhythmic cycles). Each raga has specific notes (swaras) and rules for how they can be used, creating different moods and feelings. Talas provide the rhythmic structure, often featuring complex patterns that enhance the music. Melakarta ragas are the main ragas with a set scale of seven notes used in both ascending and descending order, forming the basis for many others. Janya ragas come from Melakarta ragas and can leave out some notes for more flexibility and emotional expression. The theory also includes concepts like gamakas (ornamentation) and alapana (improvisation), which allow musicians to explore melodies within a structured framework. This foundation supports the improvisational nature of the music, enabling artists to create unique interpretations while following traditional forms.")
with c2:
    st.image("https://i0.wp.com/math.ucr.edu/home/baez/cultural/melakarta_ragas.png", width=450)
st.markdown("<h2 style=' color: ""#fad07d"";'>Famous Composers</h2>", unsafe_allow_html=True)
st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
c4, c5 = st.columns(2)
with c4:
    st.write("Carnatic music features several famous composers who have shaped the tradition. Thyagaraja (1767-1847) is celebrated for his devotional songs dedicated to Lord Rama, and the Thyagaraja Aradhana festival honors his contributions. Muthuswami Dikshitar (1775-1835), a contemporary of Thyagaraja, is known for his complex compositions in Sanskrit, often reflecting philosophical ideas. He traveled widely in South India, gathering musical influences. Syama Sastri (1762-1827) is recognized for his emotive songs that express devotion, many of which he composed while serving the Tanjore court. These composers have left a lasting impact, and their music continues to inspire many today.")
with c5:
    st.image("https://hinduismtoday.b-cdn.net/wp-content/uploads/2000/02/music2000-2.jpg")
st.markdown("<h2 style=' color: ""#fad07d"";'>Performing</h2>", unsafe_allow_html=True)
st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)
c6, c7 = st.columns(2)
with c7:
    st.write("Carnatic music is usually performed in concerts called kacheris. A kacheri typically starts with a varnam, which showcases the raga and the musician's skills. This is followed by several kritis, which are composed pieces expressing different emotions. Performers often include improvisational sections, like alapana (freeform exploration of the raga) and neraval (improvisation on a line from a kriti). Accompaniment usually features instruments like the mridangam (drum) and violin, creating a rich interaction between the vocalist and the musicians. The concert ends with a lively tani avartanam, where the percussionist improvises rhythmically, inviting the audience to engage and appreciate the music.")
with c6:
    st.image("https://th-i.thgim.com/public/incoming/9d7apv/article66320572.ece/alternates/FREE_1200/Concert_4.jpg", width=450)
st.markdown("<h2 style=' color: ""#fad07d"";'>RanjaniGayathri</h2>", unsafe_allow_html=True)
st.markdown("""<hr style="height:4px;border:none;color:#fad07d;background-color:#fad07d;" /> """, unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns([1,1,8,1,1])
with c3:
    st.video("https://youtu.be/44HUgWxBFX4?si=PhVh2Mb7OETMC9yi",)

