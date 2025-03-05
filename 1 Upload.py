import streamlit as st
from predict import predict_audio_class
st.set_page_config(layout="wide")
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