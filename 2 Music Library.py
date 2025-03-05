import streamlit as st
from raag_data import raags
st.set_page_config(layout="wide")
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
