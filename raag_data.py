raags = [
  {
    'name':'Bhairavi',
    'intro':'bhairavi was introduced in...',
    'avarahana':'P G M',
    'arohana':'P G M',
    'mussical structure':'',
  },
  {
    'name':'Bhairavi',
    'intro':'bhairavi was introduced in...',
    'avarahana':'P G M',
    'arohana':'P G M',
  },
]

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
r = {}
for raag in raags:
  if raag.name == option:
    r = raag
    break;
raag = raag[2]
st.write(r.name)
st.write(r.intro)
