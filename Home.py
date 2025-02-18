import streamlit as st
from PIL import Image
from predict import predict_audio_class
from raag_data import raags

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



with tab2:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("library.png")

        st.subheader("Select one of the 72 Melakartha ragams plus a few more!")
        option = st.selectbox(
	    "",
	("Kanakangi", "Ratnangi", "Ganamurti", "Vanaspati", "Manavati",  
"Tanarupi", "Senavati", "Hanumatodi", "Dhenuka", "Natakapriya",  
"Kokilapriya", "Rupavati", "Gayakapriya", "Vakulabharanam", "Mayamalavagowla",  
"Chakravakam", "Suryakantam", "Hatakambari", "Jhankaradhwani", "Natabhairavi",  
"Keeravani", "Kharaharapriya", "Gourimanohari", "Varunapriya", "Mararanjani",  
"Charukesi", "Sarasangi", "Harikambhoji", "Dheerasankarabaranam", "Naganandini",  
"Yagapriya", "Ragavardhini", "Gangeyabhushani", "Vagadheeswari", "Shulini",  
"Chalanata", "Salagam", "Jalarnavam", "Jhalavarali", "Navaneetam",  
"Pavani", "Raghupriya", "Gavambhodi", "Bhavapriya", "Shubhapantuvarali",  
"Shadvidamargini", "Suvarnangi", "Divyamani", "Dhavalambari", "Namanarayani",  
"Kamavardhini", "Ramapriya", "Gamanashrama", "Vishwambari", "Shamalangi",  
"Shanmukhapriya", "Simhendramadhyamam", "Hemavati", "Dharmavati", "Neetimati",  
"Kantamani", "Rishabhapriya", "Latangi", "Vachaspati", "Mechakalyani",  
"Chitrambari", "Sucharitra", "Jyoti swarupini", "Dhatuvardani", "Nasikabhushini",  
"Kosalam", "Rasikapriya", "Suddha Dhanyasi", "Revati", "Hamsadhwani",  
"Mohanam", "Kalyani", "Todi", "Bhairavi", "Shankarabharanam",  
"Karaharapriya", "Kambhoji", "Saveri", "Kaanada", "Darbar",  
"Bilahari", "Begada", "Poorvikalyani", "Madhyamavati", "Yamunakalyani",  
"Abhogi", "Shree", "Arabhi", "Anandabhairavi", "Nattai",  
"Varali", "Sahana", "Amritavarshini", "Hindolam", "Pantuvarali",  
"Janaranjani", "Manirangu", "Vasantha", "Surutti", "Desh",  
"Harikambhoji", "Mukhari", "Ranjani", "Kapi", "Simhavahini"  
))

    #loop through raags.name and if option==raags.name, get raag
    raag = None
    for r in raags:
        if option==r["name"]:
            raag = r

    if raag is not None:
        hi1, hi2 = st.columns(2)

        with hi1:
            st.title(raag["name"])
            st.write('**Arohana**: ' + raag["arohana"])
            st.write('**Avarohana**: ' + raag["avarohana"])
            st.write('**Time of Day**: ' + raag["time_of_day"])
            st.write('**Character**: ' + raag["character"])
        with hi2:
            st.write('**Associated Deity**: ' + raag["associated_deity_emotion"])
            st.write('**Popular Compositions**: ')
            for comp in raag["popular_compositions"]:
                st.write(comp)
            st.write('**History**: ' + raag["history"])
            st.write('**Cultural Significance**: ' + raag["cultural_significance"])



with tab3:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("upload.png")
    uploaded_file = st.file_uploader("Choose a file")
    if st.button("Analyze"):
        prediction = predict_audio_class(uploaded_file)
        st.write(prediction)
    if prediction=="Shankharabharanam":
        
        hi1, hi2 = st.columns(2)
        with hi1:
            st.title("This song is in the ragam: Shankharabharanam")
            
            
            st.write(''' **Arohana**: S R₂ G₃ M₁ P D₂ N₃ Ṡ   
            **Avarohana**: Ṡ N₃ D₂ P M₁ G₃ R₂ S''')
                    
            st.markdown("""
            **Notes of Shankarabharanam:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₃** (Antara Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₃** (Kakali Nishadam)
            """)
            # Title of the page
            st.title("Janya Ragas of Shankarabharanam")
            
            # Display text with bullet points and emojis
            st.markdown("""
            Shankarabharanam has given rise to many Janya (derived) ragas, each bringing out different moods and interpretations. 
            Some well-known Janya ragas include:
            - 🎶 **Arabhi**
            - 🎶 **Atana**
            - 🎶 **Bilahari**
            - 🎶 **Devagaandhaari**
            - 🎶 **Jana Ranjani**
            - 🎶 **Hamsadhvani**
            - 🎶 **Kadanakutuhalam**
            - 🎶 **Niroshta**
            - 🎶 **Shuddha Sāveri**
            - 🎶 **Pahādi**
            
            These Janya ragas add richness to the raga's expression, allowing for diverse musical exploration within the framework of Shankarabharanam.
            """)
            #with st.form("my_form"):
                #st.write("Feedback - Was I Right?")
                #sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                #selected = st.feedback("thumbs")
                #if selected is not None:
                    #st.markdown(f"You selected: {sentiment_mapping[selected]}")
                #submitted = st.form_submit_button("Submit")   
            
            with hi2:
                st.image("spec.png")
        
                st.title('Fun Facts About Shankarabharanam')
        
                # Add an introductory text
                st.markdown("""
                Shankarabharanam is a majestic raga in Carnatic music, known for its grandeur and versatility. Here are some interesting facts about this raga:
                """)
                
                # List of facts
                facts = [
                        ("🧑‍🎤 **King of Ragas**", "Shankarabharanam is considered one of the most majestic and revered ragas in Carnatic music."),
                        ("🎵 **Melakarta Raga**", "It is the 29th raga in the 72 Melakarta system and falls under the Indu Chakra."),
                        ("🔢 **Sampurna Scale**", "Shankarabharanam uses all seven notes in both ascending and descending scales: S, R₂, G₃, M₁, P, D₂, N₃."),
                        ("🎶 **Vadi and Samvadi**", "The Vadi (most important note) is P (Paṅchamam), and the Samvadi is S (Shadjam)."),
                        ("🌅 **Time of Performance**", "Typically performed in the early evening, evoking serenity and devotion."),
                        ("🎤 **Famous Compositions**", "Known for iconic compositions like 'Vatapi Ganapatim' by Muthuswami Dikshitar."),
                        ("💎 **Name Meaning**", "Shankarabharanam translates to 'the ornament of Shankara' (Lord Shiva)."),
                        ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Yaman, with a similar mood and structure."),
                        ("🩷 **Emotional Range**", "Shankarabharanam expresses devotion, grandeur, and peacefulness, making it versatile for performances."),
                        ("🎻 **Vocal and Instrumental**", "Popular in both vocal and instrumental renditions, especially in classical concerts.")
                ]
                
                # Loop through the list and present each fact
                for fact in facts:
                        st.markdown(f"**{fact[0]}**: {fact[1]}")
                
                st.header("CHALAMELA")
                
                st.markdown('''Ragam: Durbar (22nd Mela Janyam)
                Talam: Adi
                    
                    Arohanam:          S R2 M1 P D2 N2 S            	||
                    Avarohanam:  	S N2 D2 P M1 R2 G2 G2 R2 S    	||
                    
                    Composer:           Thiruvotriyur Thyagaiyyer
                    Notation Courtesy: Apoorva Raghunandan
                    
                    Pallavi: ChalamEla jEsEvurA chAla nammina nApai
                    
                    Anupallavi: Valachiyunna nAthO vAdEla VEnu gOpAla dEva
                    
                    Charanam: Palukumu nAthO
                    
                    Meaning: Lord Venugopala, why do you wreak a grudge on me? Please shower your Grace upon this one who has ardently believed in you.''')
                    
                    
                st.subheader("Pallavi:")
                    
                st.markdown('''P &nbsp; &nbsp; M &nbsp; &nbsp; R &nbsp; &nbsp;,  &nbsp; &nbsp;    G &nbsp; &nbsp; , &nbsp; &nbsp;  G &nbsp; &nbsp; , &nbsp; &nbsp;       R &nbsp; &nbsp; S &nbsp; &nbsp; R &nbsp; &nbsp; , &nbsp; &nbsp;        N &nbsp; &nbsp; R &nbsp; &nbsp; S  &nbsp; &nbsp; N &nbsp; &nbsp; | D &nbsp; &nbsp; P &nbsp; &nbsp; D &nbsp; &nbsp; N &nbsp; &nbsp;  	S &nbsp; &nbsp; R &nbsp; &nbsp; S &nbsp; &nbsp; R  &nbsp; &nbsp; ||&nbsp; &nbsp;	P &nbsp; &nbsp; , &nbsp; &nbsp; M &nbsp; &nbsp; R  &nbsp; &nbsp;  	G &nbsp; &nbsp; R &nbsp; &nbsp; S &nbsp; &nbsp; R &nbsp; &nbsp; ||''')
                                    
                st.markdown('''Cha- &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;la - &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 	 &nbsp; &nbsp;     me-  &nbsp; &nbsp;   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 	la -    &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; 	je &nbsp; &nbsp;-  &nbsp; &nbsp;-  &nbsp; &nbsp; - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;se&nbsp; &nbsp; -    &nbsp; &nbsp;	- &nbsp; &nbsp; - &nbsp; &nbsp; - &nbsp; &nbsp; -  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;    	vu &nbsp; &nbsp; -&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;- &nbsp; &nbsp;ra &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;    	- &nbsp; &nbsp; - &nbsp; &nbsp; - &nbsp; &nbsp; -&nbsp; &nbsp;|\n\n''')
                    
                    
                st.markdown('''P &nbsp; &nbsp; M  &nbsp; &nbsp; R &nbsp; &nbsp;G  &nbsp; &nbsp;	R &nbsp; &nbsp;S &nbsp; &nbsp;R&nbsp; &nbsp; M &nbsp; &nbsp; || &nbsp; &nbsp;  P &nbsp; &nbsp;M&nbsp; &nbsp; , &nbsp; &nbsp;P  &nbsp; &nbsp;   	D&nbsp; &nbsp; N&nbsp; &nbsp; S&nbsp; &nbsp; R &nbsp; &nbsp;|| &nbsp; &nbsp;N&nbsp; &nbsp; N &nbsp; &nbsp;, &nbsp; &nbsp; D  &nbsp; &nbsp; 	D&nbsp; &nbsp; P &nbsp; &nbsp;D&nbsp; &nbsp; N &nbsp; &nbsp; | &nbsp; &nbsp; P &nbsp; &nbsp; M &nbsp; &nbsp;R &nbsp; &nbsp;G   &nbsp; &nbsp; 	G &nbsp; &nbsp;R &nbsp; &nbsp;S &nbsp; &nbsp;R &nbsp; &nbsp;||\n\n''')
                st.markdown('''Cha  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;- -  &nbsp; &nbsp;&nbsp; &nbsp; -   	-   &nbsp; &nbsp;&nbsp; &nbsp;- la -   &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;      - nam - -    &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;	-  -   -  -| &nbsp; &nbsp;&nbsp; &nbsp;Mi -  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;- na    &nbsp; &nbsp;&nbsp; &nbsp;	- &nbsp; &nbsp;&nbsp; &nbsp;  -  na -  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; 	-  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; -  -  -      	pai  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;- - - &nbsp; &nbsp;&nbsp; &nbsp;|\n\n''')
                    
                st.subheader("Anupallavi:")
                    
                    
                st.markdown('''D&nbsp; &nbsp; N&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp;   	M&nbsp; &nbsp; P&nbsp; &nbsp; R&nbsp; &nbsp; M&nbsp; &nbsp;  	R&nbsp; &nbsp; P&nbsp; &nbsp; M&nbsp; &nbsp; R&nbsp; &nbsp;   	G &nbsp; &nbsp;G &nbsp; &nbsp;R&nbsp; &nbsp; S&nbsp; &nbsp; ||&nbsp; &nbsp;M&nbsp; &nbsp; M&nbsp; &nbsp; R&nbsp; &nbsp; P&nbsp; &nbsp;   	P&nbsp; &nbsp; M&nbsp; &nbsp; D&nbsp; &nbsp; D&nbsp; &nbsp;   |  &nbsp; &nbsp; P&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp;    	N &nbsp; &nbsp;N &nbsp; &nbsp;S&nbsp; &nbsp;  , &nbsp; &nbsp;||\n\n''')
                st.markdown('''Va- &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;-   -     	-  -  &nbsp; &nbsp;&nbsp; &nbsp;  la -    &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;	-   -  -  -    	chi - &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; -   -|  &nbsp; &nbsp;&nbsp; &nbsp;yu -  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  -   -   	-   &nbsp; &nbsp;&nbsp; &nbsp; -  na -  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  	-  na -  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  -     	 &nbsp; &nbsp;&nbsp; &nbsp;tho -  &nbsp; &nbsp;&nbsp; &nbsp;- &nbsp; &nbsp;&nbsp; &nbsp; - &nbsp; &nbsp;&nbsp; &nbsp;|\n\n''')
                    
                st.markdown('''P&nbsp; &nbsp; D&nbsp; &nbsp; P&nbsp; &nbsp; S&nbsp; &nbsp;          N&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; S&nbsp; &nbsp;   	R &nbsp; &nbsp;G&nbsp; &nbsp; G&nbsp; &nbsp; R&nbsp; &nbsp;    	S&nbsp; &nbsp; N&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; ||&nbsp; &nbsp;S &nbsp; &nbsp; ,&nbsp; &nbsp;   ,&nbsp; &nbsp;   P&nbsp; &nbsp;     	, &nbsp; &nbsp;  , &nbsp; &nbsp;  D&nbsp; &nbsp; N&nbsp; &nbsp;  |   &nbsp; &nbsp;P&nbsp; &nbsp; M&nbsp; &nbsp; R&nbsp; &nbsp; G&nbsp; &nbsp;    	G&nbsp; &nbsp; R&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; ||\n\n''')
                st.markdown('''Va &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; -  pa  &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;  	-    -   la -   &nbsp; &nbsp;&nbsp; &nbsp; 	-    -  &nbsp; &nbsp;&nbsp; &nbsp; de -   &nbsp; &nbsp;&nbsp; &nbsp;   	- va  &nbsp; &nbsp;&nbsp; &nbsp;-  - &nbsp; &nbsp;&nbsp; &nbsp;|\n\n''')
                    
                st.subheader("Mukthayi Swaram:")
                    
                    
                st.markdown('''P &nbsp; &nbsp;M&nbsp; &nbsp; R&nbsp; &nbsp; G&nbsp; &nbsp;    	R &nbsp; &nbsp;S&nbsp; &nbsp; N&nbsp; &nbsp; R&nbsp; &nbsp;  	 S&nbsp; &nbsp; R&nbsp; &nbsp; N&nbsp; &nbsp; S&nbsp; &nbsp;  	  D &nbsp; &nbsp;P&nbsp; &nbsp; D&nbsp; &nbsp; N&nbsp; &nbsp; ||\n\n S&nbsp; &nbsp; R&nbsp; &nbsp; S&nbsp; &nbsp; M&nbsp; &nbsp;      	R &nbsp; &nbsp;P&nbsp; &nbsp; M&nbsp; &nbsp; D&nbsp; &nbsp;  |	&nbsp; &nbsp;P &nbsp; &nbsp;D&nbsp; &nbsp; M&nbsp; &nbsp; &nbsp; &nbsp;P&nbsp; &nbsp;   	D N S ,  ||\n\n''')
                    
                    
                st.markdown('''D&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; N&nbsp; &nbsp;       S &nbsp; &nbsp; ,&nbsp; &nbsp;  R&nbsp; &nbsp; S&nbsp; &nbsp;   	R&nbsp; &nbsp; G&nbsp; &nbsp; G&nbsp; &nbsp; R&nbsp; &nbsp;  	S&nbsp; &nbsp; R&nbsp; &nbsp; N&nbsp; &nbsp; ,&nbsp; &nbsp;  ||\n\n D&nbsp; &nbsp;  P&nbsp; &nbsp;   S&nbsp; &nbsp;  S&nbsp; &nbsp;        	&nbsp; &nbsp; , &nbsp; &nbsp;  P &nbsp; &nbsp;  P&nbsp; &nbsp;   ,&nbsp; &nbsp;    |&nbsp; &nbsp; 	D&nbsp; &nbsp;  P &nbsp; &nbsp; M &nbsp; &nbsp; R&nbsp; &nbsp;    	G&nbsp; &nbsp;  R&nbsp; &nbsp;  S&nbsp; &nbsp;  R&nbsp; &nbsp;   || (Cha)|\n\n''')
                    
                    
                    
                    
                st.subheader("Charanam:")
                    
                st.markdown('''P&nbsp; &nbsp;  ,&nbsp; &nbsp;   P&nbsp; &nbsp; ,&nbsp; &nbsp;     	,&nbsp; &nbsp;  D&nbsp; &nbsp; P &nbsp; &nbsp;M&nbsp; &nbsp;       	P&nbsp; &nbsp; D&nbsp; &nbsp; ,&nbsp; &nbsp;  P&nbsp; &nbsp;   	D&nbsp; &nbsp; ,&nbsp; &nbsp;  D&nbsp; &nbsp; R&nbsp; &nbsp;  ||&nbsp; &nbsp;N &nbsp; &nbsp; ,&nbsp; &nbsp; N&nbsp; &nbsp;  ,&nbsp; &nbsp;     	D&nbsp; &nbsp; ,&nbsp; &nbsp;   P&nbsp; &nbsp;  ,&nbsp; &nbsp;    |   	&nbsp; &nbsp;M &nbsp; &nbsp;R &nbsp; &nbsp;G &nbsp; &nbsp;, &nbsp; &nbsp;  	R&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; M&nbsp; &nbsp; ||   |\n\n''')
                st.markdown('''Pa -&nbsp;&nbsp;&nbsp; &nbsp;  &nbsp;  lu -  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 	&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;- &nbsp;&nbsp; ku - &nbsp;&nbsp;&nbsp; -   &nbsp;&nbsp;     &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;	-  &nbsp;&nbsp;&nbsp; -  -&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; -    &nbsp;&nbsp;&nbsp;&nbsp;	&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;-  -   -  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;-&nbsp;&nbsp;|&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;Mu -&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - -  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;    &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;	- &nbsp;&nbsp; - &nbsp;  -  -  &nbsp;&nbsp;      &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;	na - &nbsp;&nbsp; - &nbsp;&nbsp; -   &nbsp;&nbsp;&nbsp;	tho&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; -&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;- &nbsp; -&nbsp;&nbsp;|\n\n''')
                    
                st.subheader("Chittai Swaram:")
                    
                st.markdown('''1.  P &nbsp; &nbsp; ,&nbsp; &nbsp;   ,&nbsp; &nbsp;  ,&nbsp; &nbsp;  	  ,&nbsp; &nbsp;   ,&nbsp; &nbsp;   D &nbsp; &nbsp;, &nbsp; &nbsp; 	,&nbsp; &nbsp;   , &nbsp; &nbsp; P&nbsp; &nbsp;  ,&nbsp; &nbsp;      M &nbsp; &nbsp; , &nbsp; &nbsp; R &nbsp; &nbsp; ,&nbsp; &nbsp; || &nbsp; &nbsp;G  &nbsp; &nbsp; , &nbsp; &nbsp;   , &nbsp; &nbsp;   , &nbsp; &nbsp;  	R &nbsp; &nbsp;   , &nbsp; &nbsp;  , &nbsp; &nbsp;   , &nbsp; &nbsp;  |	 &nbsp; &nbsp;S  &nbsp; &nbsp; , &nbsp; &nbsp;   ,  &nbsp; &nbsp;  , &nbsp; &nbsp;  	R &nbsp; &nbsp; ,  &nbsp; &nbsp; M &nbsp; &nbsp; , &nbsp; &nbsp; ||  (Palu)|\n\n \n\n \n\n
                    
                    
                    2. P  &nbsp; &nbsp; ,  &nbsp; &nbsp; D  &nbsp; &nbsp; D &nbsp; &nbsp;   	P &nbsp; &nbsp; M &nbsp; &nbsp; P &nbsp; &nbsp;  , &nbsp; &nbsp;   	P &nbsp; &nbsp; M &nbsp; &nbsp; R &nbsp; &nbsp; G &nbsp; &nbsp;	,  &nbsp; &nbsp;R  &nbsp; &nbsp;S &nbsp; &nbsp; R &nbsp; &nbsp;   || &nbsp; &nbsp;N &nbsp; &nbsp;R&nbsp; &nbsp; S&nbsp; &nbsp; N&nbsp; &nbsp;    	,&nbsp; &nbsp;  S&nbsp; &nbsp; D&nbsp; &nbsp;  ,&nbsp; &nbsp;    |	&nbsp; &nbsp;,&nbsp; &nbsp; N&nbsp; &nbsp;  ,&nbsp; &nbsp; S&nbsp; &nbsp;   	,&nbsp; &nbsp; R&nbsp; &nbsp; ,&nbsp; &nbsp;  M&nbsp; &nbsp;  ||  (Palu)|\n\n \n\n \n\n
                    
                    
                    3. D&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; M&nbsp; &nbsp;  	P&nbsp; &nbsp; R&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp;   	S &nbsp; &nbsp;R&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp; 	M&nbsp; &nbsp; R&nbsp; &nbsp; G&nbsp; &nbsp; R&nbsp; &nbsp; || &nbsp; &nbsp;S&nbsp; &nbsp; R&nbsp; &nbsp; N &nbsp; &nbsp;S &nbsp; &nbsp;   	D&nbsp; &nbsp; N&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp;   |	&nbsp; &nbsp;P&nbsp; &nbsp; D&nbsp; &nbsp; N&nbsp; &nbsp; S&nbsp; &nbsp; 	R&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; ||\n\n
                    
                    S&nbsp; &nbsp; R&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp;   	D &nbsp; &nbsp;M&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp;  	N &nbsp; &nbsp;S &nbsp; &nbsp;P&nbsp; &nbsp; D&nbsp; &nbsp; 	N&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; N&nbsp; &nbsp;  | &nbsp; &nbsp;G&nbsp; &nbsp; R&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp;   	N &nbsp; &nbsp;R&nbsp; &nbsp; S&nbsp; &nbsp; N&nbsp; &nbsp;   |	&nbsp; &nbsp;S&nbsp; &nbsp; D&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; 	M&nbsp; &nbsp; P&nbsp; &nbsp; R&nbsp; &nbsp; M&nbsp; &nbsp; ||   (Palu)|\n\n \n\n \n\n
                    
                    
                    4. D &nbsp; &nbsp;N&nbsp; &nbsp; S&nbsp; &nbsp; P&nbsp; &nbsp;          , &nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; P&nbsp; &nbsp;     	M&nbsp; &nbsp; R&nbsp; &nbsp; G&nbsp; &nbsp; G&nbsp; &nbsp;      R&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp; N&nbsp; &nbsp; || &nbsp; &nbsp;S &nbsp; &nbsp;, &nbsp; &nbsp;  , &nbsp; &nbsp; D &nbsp; &nbsp;     	D&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp; N&nbsp; &nbsp;   |	 &nbsp; &nbsp;S &nbsp; &nbsp;N&nbsp; &nbsp; ,&nbsp; &nbsp; S&nbsp; &nbsp;   	  R&nbsp; &nbsp; ,&nbsp; &nbsp; M&nbsp; &nbsp; P&nbsp; &nbsp;   ||\n\n
                    
                    D &nbsp; &nbsp;,&nbsp; &nbsp;  N&nbsp; &nbsp;  S&nbsp; &nbsp;     	R&nbsp; &nbsp; S&nbsp; &nbsp; N&nbsp; &nbsp;  ,&nbsp; &nbsp;     	,&nbsp; &nbsp;  S&nbsp; &nbsp; D&nbsp; &nbsp; P&nbsp; &nbsp; 	   M&nbsp; &nbsp; D&nbsp; &nbsp; P&nbsp; &nbsp; M&nbsp; &nbsp; ||&nbsp; &nbsp;G  &nbsp; &nbsp;,&nbsp; &nbsp;  R&nbsp; &nbsp; R&nbsp; &nbsp;      	S&nbsp; &nbsp;  ,&nbsp; &nbsp;  N&nbsp; &nbsp; S&nbsp; &nbsp;    |	&nbsp; &nbsp;R &nbsp; &nbsp;M &nbsp; &nbsp;P&nbsp; &nbsp;M &nbsp; &nbsp;     &nbsp; &nbsp;P&nbsp; &nbsp;  ,&nbsp; &nbsp;  ,&nbsp; &nbsp;   ,&nbsp; &nbsp;   ||\n\n
                    
                    D&nbsp; &nbsp; P&nbsp; &nbsp; M&nbsp; &nbsp; R&nbsp; &nbsp;      	G &nbsp; &nbsp;R&nbsp; &nbsp; S&nbsp; &nbsp;  ,&nbsp; &nbsp;    	R &nbsp; &nbsp;M&nbsp; &nbsp; P&nbsp; &nbsp; R&nbsp; &nbsp;   	,&nbsp; &nbsp;  M&nbsp; &nbsp; P&nbsp; &nbsp; D&nbsp; &nbsp;  || &nbsp; &nbsp; M &nbsp; &nbsp; ,&nbsp; &nbsp;  P&nbsp; &nbsp; D &nbsp; &nbsp;     	N&nbsp; &nbsp; S&nbsp; &nbsp; P&nbsp; &nbsp;  ,&nbsp; &nbsp;   | 	D&nbsp; &nbsp; N&nbsp; &nbsp;  S&nbsp; &nbsp; R&nbsp; &nbsp;      N&nbsp; &nbsp;  ,&nbsp; &nbsp;  S&nbsp; &nbsp; R&nbsp; &nbsp;  ||\n\n
                    
                    G &nbsp; &nbsp; ,&nbsp; &nbsp;   G&nbsp; &nbsp; ,&nbsp; &nbsp;      	R&nbsp; &nbsp; S&nbsp; &nbsp; N&nbsp; &nbsp;  ,&nbsp; &nbsp;    	N&nbsp; &nbsp;  ,&nbsp; &nbsp;   D &nbsp; &nbsp;P &nbsp; &nbsp; 	D&nbsp; &nbsp; N&nbsp; &nbsp; S&nbsp; &nbsp; R&nbsp; &nbsp;  ||   &nbsp; &nbsp;N &nbsp; &nbsp; ,&nbsp; &nbsp;  S&nbsp; &nbsp; P&nbsp; &nbsp;       	, &nbsp; &nbsp; D &nbsp; &nbsp;M &nbsp; &nbsp;, &nbsp; &nbsp;  | 	&nbsp; &nbsp;P &nbsp; &nbsp;R &nbsp; &nbsp;, &nbsp; &nbsp; M&nbsp; &nbsp;    	S &nbsp; &nbsp; ,&nbsp; &nbsp;  R&nbsp; &nbsp; M&nbsp; &nbsp; |  (Palu)''')

    elif prediction=="Kalyani":

        k1, k2 = st.columns(2)

        with k1:
            st.title("This song is in the ragam: Kalyani")

            st.write(''' **Arohana**: S R₂ G₃ M₂ P D₂ N₃ Ṡ  
                        **Avarohana**: Ṡ N₃ D₂ P M₂ G₃ R₂ S''')
            
            st.markdown("""
            **Notes of Kalyani:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₃** (Antara Gandharam)
            - **M₂** (Prati Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₃** (Kakali Nishadam)
            """)

            # Title of the page
            st.title("Janya Ragas of Kalyani")

            # Display text with bullet points and emojis
            st.markdown("""
            Kalyani has given rise to numerous Janya (derived) ragas, each bringing unique flavors to Carnatic music. 
            Some popular Janya ragas include:
            - 🎶 **Hamir Kalyani**
            - 🎶 **Yamunakalyani**
            - 🎶 **Saranga**
            - 🎶 **Mohana Kalyani**
            - 🎶 **Sunadavinodini**
            - 🎶 **Pantuvarali**
            - 🎶 **Hamsanadam**
            - 🎶 **Valsala**
            
            These ragas reflect the versatility of Kalyani and its melodic richness.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")

        with k2:
            st.image("spec.png")

            st.title('Fun Facts About Kalyani')

            # Add an introductory text
            st.markdown("""
            Kalyani is one of the most celebrated ragas in Carnatic music, renowned for its elegance and grandeur. Here are some interesting facts about this raga:
            """)

            # List of facts
            facts = [
                ("🎵 **Melakarta Raga**", "It is the 65th raga in the 72 Melakarta system and belongs to the Prathi Madhyama group."),
                ("🔢 **Sampurna Scale**", "Kalyani employs all seven notes in both ascending and descending scales: S, R₂, G₃, M₂, P, D₂, N₃."),
                ("🎶 **Vadi and Samvadi**", "The Vadi (most important note) is G₃ (Antara Gandharam), and the Samvadi is N₃ (Kakali Nishadam)."),
                ("🌅 **Time of Performance**", "Typically performed in the evening, evoking devotion and joy."),
                ("🎤 **Famous Compositions**", "Kalyani is known for iconic compositions like 'Nidhi Chala Sukhama' by Tyagaraja."),
                ("💎 **Name Meaning**", "Kalyani translates to 'auspicious' or 'beneficent.'"),
                ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Yaman."),
                ("🩷 **Emotional Range**", "Kalyani conveys grandeur, devotion, and serenity."),
                ("🎻 **Vocal and Instrumental**", "Popular in both vocal and instrumental renditions, showcasing its adaptability."),
            ]

            # Loop through the list and present each fact
            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")
    elif prediction=="Bhairavi":

        j1, j2 = st.columns(2)

        with j1:
            st.title("This song is in the ragam: Bhairavi")

            st.write(''' **Arohana**: S R₂ G₂ M₁ P D₂ N₂ Ṡ  
                        **Avarohana**: Ṡ N₂ D₂ P M₁ G₂ R₂ S''')

            st.markdown("""
            **Notes of Bhairavi:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₂** (Sadharana Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₂** (Kaishiki Nishadam)
            """)

            # Title of the page
            st.title("Janya Ragas of Bhairavi")

            # Display text with bullet points and emojis
            st.markdown("""
            Bhairavi has given rise to numerous Janya (derived) ragas, each showcasing its emotive beauty. 
            Some popular Janya ragas include:
            - 🎶 **Manji**
            - 🎶 **Mukhari**
            - 🎶 **Huseni**
            - 🎶 **Owdava Bhairavi**
            - 🎶 **Sindhubhairavi**

            These ragas highlight Bhairavi's adaptability and emotional depth.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")

        with j2:
            st.image("spec.png")

            st.title('Fun Facts About Bhairavi')

            # Add an introductory text
            st.markdown("""
            Bhairavi is one of the most expressive and versatile ragas in Carnatic music, embodying deep emotion and devotion. Here are some interesting facts about this raga:
            """)

            # List of facts
            facts = [
                ("🎵 **Melakarta Raga**", "Bhairavi is not a Melakarta but a Bhashanga raga, incorporating both anya swaras and traditional Carnatic notes."),
                ("🔢 **Sampurna Scale**", "It employs all seven notes in its scale but can incorporate anya swaras like Suddha Dhaivatam in certain compositions."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is M₁ (Shuddha Madhyamam), and the Samvadi is S (Shadjam)."),
                ("🌅 **Time of Performance**", "Typically performed in the morning or early evening, evoking devotion and pathos."),
                ("🎤 **Famous Compositions**", "Iconic compositions include 'Upacharamulanu' by Tyagaraja and 'Viriboni' by Pacchimiriam Adiyappa."),
                ("💎 **Name Meaning**", "Bhairavi signifies 'fierce goddess,' often associated with intense devotion."),
                ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Bhairavi (though it differs in scale usage)."),
                ("🩷 **Emotional Range**", "Bhairavi conveys devotion, pathos, and introspection."),
                ("🎻 **Vocal and Instrumental**", "Highly favored in both vocal and instrumental renditions, emphasizing its versatility."),
            ]

            # Loop through the list and present each fact
            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")

    elif prediction=="Kharaharapriya":


        b1, b2 = st.columns(2)

        with b1:
            st.title("This song is in the ragam: Kharaharapriya")

            st.write(''' **Arohana**: S R₂ G₂ M₁ P D₂ N₂ Ṡ  
                        **Avarohana**: Ṡ N₂ D₂ P M₁ G₂ R₂ S''')

            st.markdown("""
            **Notes of Kharaharapriya:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₂** (Sadharana Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₂** (Kaishiki Nishadam)
            """)

            # Title of the page
            st.title("Janya Ragas of Kharaharapriya")

            # Display text with bullet points and emojis
            st.markdown("""
            Kharaharapriya has given rise to numerous Janya (derived) ragas, each showcasing its melodic richness. 
            Some popular Janya ragas include:
            - 🎶 **Abhogi**
            - 🎶 **Shuddha Dhanyasi**
            - 🎶 **Dhenuka**
            - 🎶 **Kanada**
            - 🎶 **Kapi**

            These ragas highlight Kharaharapriya's adaptability and emotive depth.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")

        with b2:
            st.image("spec.png")

            st.title('Fun Facts About Kharaharapriya')

            # Add an introductory text
            st.markdown("""
            Kharaharapriya is one of the most melodically rich and expressive ragas in Carnatic music. Here are some interesting facts about this raga:
            """)

            # List of facts
            facts = [
                ("🎵 **Melakarta Raga**", "Kharaharapriya is the 22nd raga in the 72 Melakarta system."),
                ("🔢 **Sampurna Scale**", "It employs all seven notes in both ascending and descending scales."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is G₂ (Sadharana Gandharam), and the Samvadi is N₂ (Kaishiki Nishadam)."),
                ("🌅 **Time of Performance**", "Typically performed in the evening, evoking peace and introspection."),
                ("🎤 **Famous Compositions**", "Iconic compositions include 'Chakkani Raja' by Tyagaraja and 'Rama Nee Samana' by Tyagaraja."),
                ("💎 **Name Meaning**", "Kharaharapriya translates to 'The beloved of Kharahara.'"),
                ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Kafi."),
                ("🩷 **Emotional Range**", "Kharaharapriya conveys peace, devotion, and introspection."),
                ("🎻 **Vocal and Instrumental**", "Equally popular in vocal and instrumental renditions, emphasizing its versatility."),
            ]

            # Loop through the list and present each fact
            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")

    elif prediction=="Todi"():
        a1, a2 = st.columns(2)

        with a1:
            st.title("This song is in the ragam: Todi")

            st.write(''' **Arohana**: S R₁ G₂ M₁ P D₁ N₂ Ṡ  
                        **Avarohana**: Ṡ N₂ D₁ P M₁ G₂ R₁ S''')

            st.markdown("""
            **Notes of Todi:**
            - **S** (Shadjam)
            - **R₁** (Shuddha Rishabham)
            - **G₂** (Sadharana Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₁** (Shuddha Dhaivatam)
            - **N₂** (Kaishiki Nishadam)
            """)

            # Title of the page
            st.title("Janya Ragas of Todi")

            # Display text with bullet points and emojis
            st.markdown("""
            Todi has given rise to numerous Janya (derived) ragas, each enriching the tapestry of Carnatic music. 
            Some popular Janya ragas include:
            - 🎶 **Subhapantuvarali**
            - 🎶 **Jayamanohari**
            - 🎶 **Deshkar**
            - 🎶 **Bhairavi**
            - 🎶 **Dhanyasi**

            These ragas demonstrate Todi's deep emotional and melodic versatility.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")

        with a2:
            st.image("spec.png")

            st.title('Fun Facts About Todi')

            # Add an introductory text
            st.markdown("""
            Todi is one of the most profound and evocative ragas in Carnatic music. Here are some interesting facts about this raga:
            """)

            # List of facts
            facts = [
                ("🎵 **Melakarta Raga**", "Todi is the 8th raga in the 72 Melakarta system."),
                ("🔢 **Sampurna Scale**", "It employs all seven notes in both ascending and descending scales."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is G₂ (Sadharana Gandharam), and the Samvadi is D₁ (Shuddha Dhaivatam)."),
                ("🌅 **Time of Performance**", "Traditionally performed in the morning, evoking devotion and seriousness."),
                ("🎤 **Famous Compositions**", "Iconic compositions include 'Kaddanu Variki' by Tyagaraja and 'Gajavadana Sammodita' by Muthuswami Dikshitar."),
                ("💎 **Name Meaning**", "Todi translates to 'to invoke' or 'to call out.'"),
                ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Bhairav."),
                ("🩷 **Emotional Range**", "Todi conveys devotion, seriousness, and intensity."),
                ("🎻 **Vocal and Instrumental**", "Renowned for its use in both vocal and instrumental renditions, emphasizing its expressive power."),
            ]

            # Loop through the list and present each fact
            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")

    else:
        i1, i2 = st.columns(2)

        with i1:
            st.title("This song is in the ragam: Khamboji")

            st.write(''' **Arohana**: S R₂ G₃ M₁ P D₂ S  
                        **Avarohana**: S N₂ D₂ P M₁ G₃ R₂ S''')

            st.markdown("""
            **Notes of Khamboji:**
            - **S** (Shadjam)
            - **R₂** (Chatushruti Rishabham)
            - **G₃** (Antara Gandharam)
            - **M₁** (Shuddha Madhyamam)
            - **P** (Paṅchamam)
            - **D₂** (Chatushruti Dhaivatam)
            - **N₂** (Kaishiki Nishadam)
            """)

            # Title of the page
            st.title("Janya Ragas of Khamboji")

            # Display text with bullet points and emojis
            st.markdown("""
            Khamboji has given rise to numerous Janya (derived) ragas, each bringing unique textures to Carnatic music. 
            Some popular Janya ragas include:
            - 🎶 **Harikambhoji**
            - 🎶 **Natakuranji**
            - 🎶 **Kedaragaula**
            - 🎶 **Surati**
            - 🎶 **Mohana**

            These ragas highlight Khamboji's adaptability and melodic richness.
            """)

            with st.form("my_form"):
                st.write("Feedback - Was I Right?")
                sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
                selected = st.feedback("thumbs")
                if selected is not None:
                    st.markdown(f"You selected: {sentiment_mapping[selected]}")
                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")

        with i2:
            st.image("spec.png")

            st.title('Fun Facts About Khamboji')

            # Add an introductory text
            st.markdown("""
            Khamboji is a vibrant and versatile raga in Carnatic music. Here are some interesting facts about this raga:
            """)

            # List of facts
            facts = [
                ("🎵 **Melakarta Raga**", "Khamboji is a Janya raga of the 28th Melakarta, Harikambhoji."),
                ("🔢 **Vakra Scale**", "The avarohana has a vakra (zigzag) structure, adding to its charm."),
                ("🎶 **Vadi and Samvadi**", "The Vadi is G₃ (Antara Gandharam), and the Samvadi is N₂ (Kaishiki Nishadam)."),
                ("🌅 **Time of Performance**", "Typically performed in the evening, evoking a mood of devotion and grandeur."),
                ("🎤 **Famous Compositions**", "Famous compositions include 'O Ranga Sai' by Tyagaraja and 'Marubari' by Muthuswami Dikshitar."),
                ("💎 **Name Meaning**", "Khamboji translates to 'a beautiful garland' in Sanskrit."),
                ("🎶 **Hindustani Equivalent**", "The raga's counterpart in Hindustani music is Kafi."),
                ("🩷 **Emotional Range**", "Khamboji conveys joy, grandeur, and devotion."),
                ("🎻 **Vocal and Instrumental**", "Widely used in both vocal and instrumental forms, showcasing its majestic appeal."),
            ]

            # Loop through the list and present each fact
            for fact in facts:
                st.markdown(f"**{fact[0]}**: {fact[1]}")


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
