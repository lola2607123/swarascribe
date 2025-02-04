import streamlit as st
from PIL import Image
from predict import predict_audio_class

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
raags = [
  {
    'name': 'Kanakangi',
    'intro': 'Kanakangi is the first raga in the Melakarta system, marking the beginning of the 72 parent ragas in Carnatic music. It is a Sampurna raga, meaning it contains all seven notes in both ascending (Arohana) and descending (Avarohana) sequences. The raga is rarely performed in concerts but is highly significant for learners and musicologists.',
    'arohana': 'S R₁ G₁ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₁ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Kanakangi conveys purity, simplicity, and devotion, often evoking a serene and meditative mood. The use of Shuddha Rishabham (R₁) and Shuddha Gandharam (G₁) creates a soft and delicate tonal quality, making the raga sound gentle yet profound.',
    'associated_deity_emotion': 'This raga is associated with Lord Vishnu and is believed to invoke tranquility, divine grace, and deep introspection. It is often linked to themes of devotion and prayer, making it a preferred choice for temple and early morning performances.',
    'musical_structure': 'Kanakangi follows the basic Sampurna scale structure without any vakra (zig-zag) patterns or special gamakas. Its notes are placed in their natural order, making it an essential raga for understanding the foundation of Carnatic melody.',
    'popular_compositions': [
      'Rama Nannu Brovara - Tyagaraja',
      'Sri Vighneswaraya - Muthuswami Dikshitar'
    ],
    'history': 'Kanakangi was classified as the first Melakarta raga by the musicologist Venkatamakhi in the 17th century and later reinforced by Govindacharya in the Katapayadi system. Although it is not widely used in compositions, its theoretical significance is immense, as it serves as a model for other ragas. Many later ragas borrow swaras from Kanakangi to create derived (janya) ragas.',
    'cultural_significance': 'Kanakangi is highly respected as a fundamental raga in Carnatic music. While it is not commonly used in performances, its pure and unornamented scale makes it a key raga for students learning the Melakarta system. It is also believed to have a calming effect on the mind, making it suitable for meditation and devotional music.'
  },
  {
    'name': 'Ratnangi',
    'intro': 'Ratnangi is the second raga in the Melakarta system and serves as a natural progression from Kanakangi. It is a Sampurna raga, meaning it contains all seven notes in both ascending (Arohana) and descending (Avarohana) sequences. It blends sharp and natural notes, giving it a bright yet refined quality.',
    'arohana': 'S R₂ G₁ M₁ P D₂ N₁ S',
    'avarohana': 'S N₁ D₂ P M₁ G₁ R₂ S',
    'time_of_day': 'Early Morning',
    'character': 'Ratnangi is a graceful and elegant raga, known for its smooth melodic flow and gentle optimism. The combination of Chatushruti Rishabham (R₂) and Chatushruti Dhaivatam (D₂) gives it a lively yet refined feel, making it ideal for expressing beauty, admiration, and devotion.',
    'associated_deity_emotion': 'The raga is associated with Goddess Lakshmi and is believed to evoke emotions of grace, beauty, and spiritual wealth. It is often performed in a devotional setting to invoke divine blessings and harmony.',
    'musical_structure': 'Ratnangi follows a Sampurna scale structure without complex gamakas or vakra (zig-zag) patterns. The straight progression of swaras makes it smooth and melodious, suitable for both light and classical compositions.',
    'popular_compositions': [
      'Sri Vighneswaraya - Muthuswami Dikshitar'
    ],
    'history': 'Ratnangi was classified as the second Melakarta raga by Venkatamakhi and later reinforced in the Katapayadi system. It was likely codified during the 18th or 19th century, a period of intense raga classification. While there is limited historical documentation of its use in early classical texts, Ratnangi gained prominence through its inclusion in the Melakarta framework and its suitability for morning performances.',
    'cultural_significance': 'Ratnangi is deeply associated with devotion and spiritual renewal. It is often performed in temple settings and early morning concerts, aligning with the time of divine worship. The raga’s ability to balance sweetness and energy makes it popular in both classical and semi-classical forms of Carnatic music.'
  },
  {
    'name': 'Shankarabharanam',
    'intro': 'Shankarabharanam is the 29th Melakarta raga and one of the most foundational scales in Carnatic music. It is equivalent to the Western major scale and serves as a basis for many janya ragas.',
    'arohana': 'S R₂ G₃ M₁ P D₂ N₃ S',
    'avarohana': 'S N₃ D₂ P M₁ G₃ R₂ S',
    'time_of_day': 'Evening',
    'character': 'Shankarabharanam is uplifting, majestic, and grand. It conveys a sense of completeness, joy, and devotion, making it one of the most versatile ragas in Carnatic music.',
    'associated_deity_emotion': 'Associated with Lord Shiva, this raga is believed to evoke spiritual wisdom and cosmic harmony.',
    'musical_structure': 'This raga follows a completely linear scale and allows for extensive improvisation in both kalpana swaras and manodharma.',
    'popular_compositions': [
      'Endaro Mahanubhavulu - Tyagaraja',
      'Swara Raga Sudha - Tyagaraja'
    ],
    'history': 'One of the oldest and most fundamental ragas in Indian classical music, Shankarabharanam has been extensively used in both Carnatic and Hindustani traditions.',
    'cultural_significance': 'Shankarabharanam’s universal appeal makes it an essential raga in concerts and learning.'
  },
  {
    'name': 'Vanaspati',
    'intro': 'Vanaspati is the fourth Melakarta raga and has a mysterious yet melodious quality. It is known for its unique swara combinations.',
    'arohana': 'S R₁ G₂ M₁ P D₁ N₂ S',
    'avarohana': 'S N₂ D₁ P M₁ G₂ R₁ S',
    'time_of_day': 'Late Morning',
    'character': 'Vanaspati has a slightly introspective and emotional feel. It blends melancholy with hope.',
    'associated_deity_emotion': 'Linked to nature and growth, Vanaspati is associated with renewal and change.',
    'musical_structure': 'A linear Melakarta raga with characteristic phrase combinations that define its uniqueness.',
    'popular_compositions': [
      'Varashikivahana - Tyagaraja'
    ],
    'history': 'Vanaspati was classified in the 17th century as part of the Melakarta system.',
    'cultural_significance': 'It is rarely performed but has a strong theoretical significance in Carnatic music.'
  },
  {
    'name': 'Manavati',
    'intro': 'Manavati is the fifth Melakarta raga, known for its light yet slightly unconventional character.',
    'arohana': 'S R₁ G₂ M₁ P D₂ N₂ S',
    'avarohana': 'S N₂ D₂ P M₁ G₂ R₁ S',
    'time_of_day': 'Afternoon',
    'character': 'Manavati has a delicate yet intriguing quality, evoking a sense of curiosity and subtle emotions.',
    'associated_deity_emotion': 'Associated with hidden wisdom and depth, this raga invokes a sense of mystery.',
    'musical_structure': 'Manavati follows a Sampurna scale but allows for slight deviations in gamakas.',
    'popular_compositions': [
      'Pahi Pahi Gajanana - Muthuswami Dikshitar'
    ],
    'history': 'A relatively lesser-known raga, Manavati has been part of the Melakarta scheme for centuries.',
    'cultural_significance': 'Used in scholarly compositions, Manavati is significant for its experimental nature in Carnatic music.'
  }
  {
    'name': 'Ganamurthi',
    'intro': 'Ganamurthi is the third raga in the Melakarta system and is known for its structured, solemn, and introspective nature. It is a Sampurna raga, meaning it contains all seven notes in both ascending (Arohana) and descending (Avarohana) sequences. The raga has a stately quality that lends itself to devotional and philosophical themes.',
    'arohana': 'S R₁ G₃ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₃ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Ganamurthi carries an air of dignity and nobility, with a serious and contemplative tone. The presence of Antara Gandharam (G₃) and Shuddha Madhyamam (M₁) gives it a distinct blend of serenity and power. It is ideal for expressing reverence, devotion, and introspection, making it well-suited for spiritual or meditative compositions.',
    'associated_deity_emotion': 'Ganamurthi is linked to Lord Ganesha, symbolizing wisdom, clarity, and the removal of obstacles. The raga evokes feelings of devotion, peace, and intellectual depth, often serving as an invocation for success and divine guidance.',
    'musical_structure': 'Ganamurthi adheres to a structured Sampurna scale with a balanced arrangement of notes. The absence of vakra patterns gives it a straightforward and steady melodic progression, allowing for deep emotional exploration in both slow and medium-paced compositions.',
    'popular_compositions': [
      'Ganapati Bappa (popular devotional pieces)'
    ],
    'history': 'Ganamurthi was formalized as the third Melakarta raga by Venkatamakhi and gained recognition in the early modern period. While it lacks an extensive historical record in ancient compositions, it became more prominent through its classification in the Melakarta system. The name "Ganamurthi" itself, meaning "embodiment of music," reflects its significance in Carnatic tradition. The raga was favored by Muthuswami Dikshitar for its structured, philosophical essence.',
    'cultural_significance': 'Ganamurthi is closely associated with Lord Ganesha and is often performed at the beginning of concerts and religious ceremonies. Given its solemn and introspective nature, it is widely used in invocatory pieces and devotional music. The raga’s balance of depth and structure makes it an important choice for both classical performances and spiritual settings.'
  }
  {
    'name': 'Senavati',
    'intro': 'Senavati is a Sampurna raga in the Melakarta system known for its harmonious and balanced tone. It features a combination of both sharp and natural notes, creating a melody that is both rich and serene. Senavati is a versatile raga, suitable for both light and classical compositions, and is often performed during the late morning or early afternoon hours.',
    'arohana': 'S R₂ G₃ M₁ P D₂ N₁ S',
    'avarohana': 'S N₁ D₂ P M₁ G₃ R₂ S',
    'time_of_day': 'Late Morning to Early Afternoon',
    'character': 'Senavati conveys a feeling of serenity, balance, and subtle elegance. The use of Chatushruti Rishabham (R₂) and Chatushruti Dhaivatam (D₂) along with Antara Gandharam (G₃) brings out a majestic yet calm flavor, making it ideal for both reflective and grand expressions. It is a raga of moderate intensity, which allows for a range of emotional expressions from devotion to contemplation.',
    'associated_deity_emotion': 'Senavati is associated with Lord Shiva and is believed to evoke feelings of devotion, strength, and stability. It is often performed to invoke blessings for health, well-being, and inner peace.',
    'musical_structure': 'Senavati follows the Sampurna scale structure without any vakra (zig-zag) patterns. Its smooth melodic flow allows for both slow, meditative renditions as well as faster, more energetic compositions. The arrangement of notes is balanced and orderly, making it an essential raga for understanding the interrelations of notes in the Melakarta system.',
    'popular_compositions': [
      'Sree Ganeshwara - Muthuswami Dikshitar',
      'Senavathi Varnam - Unknown Composer'
    ],
    'history': 'Senavati was classified as the 59th Melakarta raga in the 72 Melakarta system by Venkatamakhi. While its use in ancient compositions is not as prominent as some other ragas, Senavati gained recognition in the 18th and 19th centuries, especially through its association with devotional and philosophical themes. The raga’s formal structure and balanced tone make it a staple in both classical and devotional music.',
    'cultural_significance': 'Senavati is widely regarded for its spiritual and emotional depth. It is often performed in temple settings, particularly during religious ceremonies and festivals. The raga’s association with Lord Shiva and its calm yet grand nature makes it a popular choice for invoking a sense of inner peace and spiritual connection during worship and meditation.'
 }
 {
    'name': 'Hanumatodi',
    'arohana': 'S R₁ G₂ M₁ P D₁ N₂ Ṡ',
    'avarohana': 'Ṡ N₂ D₁ P M₁ G₂ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Hanumatodi is a powerful, devotional raga with a serious, bold character. It is known for its preference for lower notes, giving it a deep and gravitas-laden tone. The raga is full of emotional depth and is often associated with strength, courage, and reverence.',
    'associated_deity_emotion': 'Hanumatodi is associated with Lord Hanuman and is used to evoke feelings of strength, devotion, and protection. It is a raga that inspires reverence and deep devotion to the deity.',
    'popular_compositions': [
        'Era Na Pai - Patnam Subramania Iyer',
        'Thāye Yashoda - Oottukkadu Venkata Kavi',
        'Daani Samajendra - Swathi Thirunal',
        'Shri Krishnam Bhajamaanasa - Muthuswami Dikshitar',
        'Kādhanu vāriki - Thyagaraja',
        'Raave Himagiri Kumari - Syama Sastri'
    ],
    'history': 'Hanumatodi is the 8th melakarta raga in the 72 melakarta system, and it is a complex and challenging raga due to its intricate phrasing and intonation. It was classified by Venkatamakhi in the 17th century and has been used in several devotional compositions. The raga has a distinct connection to Lord Hanuman and has gained popularity in the Carnatic tradition over time, especially in the works of composers like Thyagaraja, Muthuswami Dikshitar, and Syama Sastri.',
    'cultural_significance': 'Hanumatodi, while not as widely performed as some other ragas, holds significant cultural value in Carnatic music, particularly in temple settings and devotional concerts. The raga is strongly associated with Lord Hanuman, symbolizing strength and protection, making it a popular choice for invoking blessings in devotional and spiritual contexts.'
 }
 {
    'name': 'Dhenuka',
    'arohana': 'S R₁ G₃ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₃ R₁ S',
    'time_of_day': 'Night',
    'character': 'Dhenuka is a serene and meditative raga, known for its deep, contemplative nature. It creates a mood of calmness and solemnity, making it perfect for introspection and spiritual reflection. The combination of Shuddha Rishabham (R₁) and Antara Gandharam (G₃) gives it a soft yet profound tonal quality.',
    'associated_deity_emotion': 'Dhenuka is associated with Lord Shiva and is believed to evoke feelings of reverence, peace, and spiritual awareness. It is used to express devotion and introspection, invoking a sense of connection with the divine.',
    'popular_compositions': [
        'Dhenuka Varnam - Muthuswami Dikshitar'
    ],
    'history': 'Dhenuka is part of the Melakarta system and was classified by Venkatamakhi in the 17th century. It is considered one of the more peaceful ragas in the system, though its usage in compositions is not as widespread as some other ragas. The raga has a calming influence and is often chosen for slow, devotional pieces.',
    'cultural_significance': 'Dhenuka is a raga often associated with spiritual practices and is performed in temple settings or during devotional concerts. Its meditative quality makes it suitable for creating a tranquil atmosphere, and it is used to invoke a deep sense of peace and divine presence.'
 }
 {
  "name": "Natakapriya",
  "arohana": "S R₁ G₂ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₂ R₁ S",
  "time_of_day": "Morning",
  "character": "Natakapriya is known for its dramatic and evocative quality, which makes it suitable for compositions that convey devotion or deep emotion. The combination of Shuddha Rishabham (R₁) and Sadharana Gandharam (G₂) gives it a somber yet soothing feel, while Chatusruti Dhaivatam (D₂) adds brightness to its overall character.",
  "associated_deity_emotion": "Natakapriya is associated with Lord Vishnu and is believed to evoke feelings of devotion, peace, and reverence. It is often used to express divine connection and a sense of profound emotional depth in compositions.",
  "popular_compositions": [
    "Sri Venkatesa Girisam - Muthuswami Dikshitar",
    "Jagadeesha Guruguha - Muthuswami Dikshitar"
  ],
  "history": "Natakapriya is part of the Melakarta system, classified by Venkatamakhin in the 17th century. It is one of the ragas used in both classical and devotional compositions. Although not as commonly performed as some other ragas, its emotional depth makes it highly revered in Carnatic music.",
  "cultural_significance": "Natakapriya is often performed in temple settings and devotional concerts, where its dramatic and emotional qualities help to convey devotion and spiritual reverence. Its ability to evoke strong emotional connections makes it suitable for compositions in praise of deities, especially in the classical tradition."
 }
 {
  "name": "Bhairavi",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Early Morning or Late Evening",
  "character": "Bhairavi is associated with deep devotion, pathos, and longing. The use of Shuddha Madhyamam (M₁) and Shatsruti Rishabham (R₁) contributes to its somber and devotional feel. The raga evokes feelings of introspection, surrender, and melancholy, often performed in slow tempos to allow for deep emotional expression.",
  "associated_deity_emotion": "Bhairavi is traditionally associated with intense devotion, spiritual release, and divine yearning. It expresses themes of separation and longing, often used in compositions to convey deep emotional connection with the divine.",
  "popular_compositions": [
    "Madhava Mamava - Muthuswami Dikshitar",
    "Bhavayami Gopalabalam - Annamacharya",
    "Enna Thavam Seithanai - Muthuswami Dikshitar",
    "Jagadananda Karaka - Tyagaraja",
    "Rama Nannu Brovara - Tyagaraja"
  ],
  "history": "Bhairavi is an ancient raga, mentioned in early texts of Indian classical music, and has been a prominent part of both Carnatic and Hindustani music for centuries. In the Carnatic tradition, Bhairavi is a Melakarta raga and has long been used in devotional and classical music. It is believed to have deep cultural roots, originating from spiritual and devotional themes.",
  "cultural_significance": "Bhairavi has significant cultural importance, especially in temple and devotional settings, where its emotional depth is used to evoke devotion and a connection to the divine. It plays a major role in classical concerts, especially during early morning or evening renditions, where its reflective and emotional qualities create a deeply meditative atmosphere."
 }
 {
  "name": "Kalyani",
  "arohana": "S R₂ G₃ M₂ P D₂ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Kalyani is known for its regal and uplifting nature, with a combination of both brightness and depth. The use of Prati Madhyamam (M₂) and Antara Gandharam (G₃) imparts a sense of grandeur and elegance. The raga evokes feelings of devotion, serenity, and joy, often used to convey both the emotional depth and beauty of the divine.",
  "associated_deity_emotion": "Kalyani is associated with the Goddess Lakshmi and is believed to evoke feelings of devotion, grace, and prosperity. It is often used in compositions that express admiration, reverence, and the search for divine blessings.",
  "popular_compositions": [
    "Achyutam Keshavam - Annamacharya",
    "Jagadodharana - Purandara Dasa",
    "Kalyani Varnam - W. V. Srinivasa Ayyangar",
    "Sundara Viharini - Muthuswami Dikshitar"
  ],
  "history": "Kalyani is one of the most revered ragas in the Carnatic music tradition, often regarded as the quintessential raga for expressing devotion and grandeur. It is a melakarta raga and has been widely used in both classical compositions and performances, representing the culmination of emotional expression. Its origin dates back to the works of early composers like Muthuswami Dikshitar and Tyagaraja, who wrote some of their most popular pieces in this raga.",
  "cultural_significance": "Kalyani holds great cultural significance, particularly in classical Carnatic music and temple performances. Its ability to evoke feelings of beauty and reverence makes it a favorite in both light and classical music. It is performed in various settings, from concerts to festivals, symbolizing divine grace, wealth, and happiness."
 }
 {
  "name": "Kambhoji",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Kambhoji is a majestic and grand raga, known for its deep, serious, and emotionally stirring character. The combination of Shuddha Rishabham (R₁) and Shuddha Madhyamam (M₁) with Kakali Nishadam (N₃) creates a raga of profound beauty and intensity. It evokes a sense of devotion, reverence, and intense emotion, often used to express the grandeur of divine presence.",
  "associated_deity_emotion": "Kambhoji is associated with Lord Shiva and is believed to evoke feelings of devotion, awe, and deep contemplation. It is often used in compositions dedicated to Lord Shiva, conveying a sense of grandeur, solemnity, and spiritual intensity.",
  "popular_compositions": [
    "Rama Nannu Brovara - Tyagaraja",
    "Bho Shambo - Muthuswami Dikshitar",
    "Vishnu Sahasranama Stotra - Muthuswami Dikshitar",
    "Dundubhi - Shyama Sastri"
  ],
  "history": "Kambhoji is one of the prominent ragas in Carnatic music and has been widely used by many legendary composers, including Tyagaraja, Muthuswami Dikshitar, and Shyama Sastri. It has a rich history and has been a central part of Carnatic music for centuries. The raga's profound emotional depth makes it a staple in both classical and devotional music.",
  "cultural_significance": "Kambhoji holds significant cultural importance in both the classical Carnatic music tradition and temple music. It is often performed during important religious ceremonies and festivals, especially in the evening and night. The raga's ability to convey intense emotion and reverence makes it a favorite in devotional concerts and spiritual gatherings."
 }
 {
  "name": "Kharaharapriya",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Late Evening",
  "character": "Kharaharapriya is a raga that exudes a feeling of devotion, serenity, and emotional intensity. The combination of Shuddha Rishabham (R₁) and Antara Gandharam (G₃) gives it a smooth, contemplative quality, while Shuddha Madhyamam (M₁) and Kakali Nishadam (N₃) add richness to its sound. It is often used to express a sense of longing and deep emotional connection.",
  "associated_deity_emotion": "Kharaharapriya is associated with Lord Rama and is believed to evoke feelings of devotion, surrender, and reverence. It is often used in compositions that express the devotee's intense longing for the divine and their deep emotional connection with God.",
  "popular_compositions": [
    "Narayana Ninna Namada - Purandara Dasa",
    "Rama Ni Samanamevaru - Tyagaraja",
    "Kshamasva - Muthuswami Dikshitar"
  ],
  "history": "Kharaharapriya is an ancient raga in the Carnatic music tradition and is part of the 28th melakarta raga in the system. It has been used in many compositions, especially in the classical devotional music repertoire. The raga has been an essential part of Carnatic music and has been passed down through generations of composers and performers.",
  "cultural_significance": "Kharaharapriya holds an important place in the devotional music tradition, especially in compositions dedicated to Lord Rama. It is often performed in the late evening, creating a tranquil and reflective atmosphere. The raga is particularly significant during religious festivals and ceremonies, helping to convey the emotions of devotion and spiritual longing."
 }
 {
  "name": "Todi",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Todi is a raga that is known for its intense and serious emotional depth. The raga conveys a sense of devotion, longing, and melancholy, evoking feelings of introspection and a connection to the divine. The use of Shuddha Rishabham (R₁), Antara Gandharam (G₃), and Kakali Nishadam (N₃) gives it a rich, resonant quality, while Shuddha Madhyamam (M₁) adds gravitas.",
  "associated_deity_emotion": "Todi is often associated with Lord Shiva, evoking feelings of reverence, surrender, and devotion. It is believed to be a raga that expresses intense longing and devotion to the divine, often used in compositions that reflect spiritual yearning and deep emotional connection.",
  "popular_compositions": [
    "Vathapi Ganapathim - Muthuswami Dikshitar",
    "Rama Nannu Brovara - Tyagaraja",
    "Todi Varnam - Various Composers"
  ],
  "history": "Todi is an ancient and highly revered raga in Carnatic music. It is one of the melakarta ragas in the 72 melakarta system and has been a significant part of classical music for centuries. Its serious emotional depth and intricate structure have made it a favorite of both composers and performers, particularly in compositions that involve devotional themes.",
  "cultural_significance": "Todi is considered one of the most important ragas in Carnatic music, frequently performed in both solo and group concerts. It is particularly significant in temple settings, where its emotional weight adds to the atmosphere of devotion and spirituality. Todi is used to express feelings of longing and devotion, especially in compositions that praise deities or explore themes of devotion."
 }







]



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
	

		    	
if option=="Shankarabharanam" or option=="Dheerasankarabaranam":
	
	hi1, hi2 = st.columns(2)

	with hi1:
	    st.title(option)
	    st.write('''
	    **Shankarabharanam** is a major raga in Carnatic music, known for its auspicious and uplifting quality.  
	    It corresponds to the Western major scale and serves as a **Melakarta raga** (29th in the system), meaning it is a parent raga from which other ragas are derived.  
	
	    **Arohana**: S R₂ G₃ M₁ P D₂ N₃ Ṡ  
	    **Avarohana**: Ṡ N₃ D₂ P M₁ G₃ R₂ S  
	
	    **Musical Structure**:  
	    - Shankarabharanam is a **Sampurna raga**, containing all seven notes in both ascending (arohana) and descending (avarohana) scales.  
	    - The notes used are Shadjam (**S**), Chatushruti Rishabham (**R₂**), Antara Gandharam (**G₃**), Shuddha Madhyamam (**M₁**), Paṅchamam (**P**), Chatushruti Dhaivatam (**D₂**), and Kakali Nishadam (**N₃**).  
	    - It is the **Shuddha Madhyamam equivalent** of the 65th Melakarta raga, Kaḷyāṇi.  
	    - In Hindustani music, Shankarabharanam corresponds to **Bilaval**, while in Western music, it aligns with the **major scale**, making it widely recognized across musical traditions.  
	    ''')
	
	    st.markdown("""
	    **Popular Songs**:  
	    - "Endaro Mahanubhavulu" by Saint Tyagaraja  
	
	    **Janya Ragas**:  
	    Shankarabharanam has given rise to many Janya (derived) ragas, each bringing out different moods and interpretations.  
	    - **Arabhi**
	    - **Atana**
	    - **Bilahari**
	    - **Devagaandhaari**
	    - **Jana Ranjani**
	    - **Hamsadhvani**
	    - **Kadanakutuhalam**
	    - **Niroshta**
	    - **Shuddha Sāveri**
	    - **Pahādi**  
	    These Janya ragas add richness to the raga's expression, allowing for diverse musical exploration within the framework of Shankarabharanam.
	    """)
	
	    st.title("CHALAMELA")
	    st.markdown('''
	    **Ragam**: Durbar (22nd Mela Janyam)  
	    **Talam**: Adi  
	
	    **Arohanam**: S R₂ M₁ P D₂ N₂ S  
	    **Avarohanam**: S N₂ D₂ P M₁ R₂ G₂ G₂ R₂ S  
	
	    **Composer**: Thiruvotriyur Thyagaiyyer  
	    **Notation Courtesy**: Apoorva Raghunandan  
	
	    **Pallavi**:  
	    ChalamEla jEsEvurA chAla nammina nApai  
	
	    **Anupallavi**:  
	    Valachiyunna nAthO vAdEla VEnu gOpAla dEva  
	
	    **Charanam**:  
	    Palukumu nAthO  
	
	    **Meaning**:  
	    Lord Venugopala, why do you wreak a grudge on me? Please shower your Grace upon this one who has ardently believed in you.  
	    ''')
	
	with hi2:
	    st.image("spec.png")
	    
	    st.title("Fun Facts About Shankarabharanam")
	    st.markdown("""
	    - **🧑‍🎤 King of Ragas**: Revered for its grandeur in Carnatic music.  
	    - **🎵 Melakarta Raga**: 29th in the 72 Melakarta system, under the Indu Chakra.  
	    - **🔢 Sampurna Scale**: Utilizes all seven notes in both ascending and descending orders.  
	    - **🎶 Vadi and Samvadi**: Vadi is P (Paṅchamam); Samvadi is S (Shadjam).  
	    - **🌅 Time of Performance**: Typically performed in the early evening.  
	    - **🎤 Famous Compositions**: Includes 'Vatapi Ganapatim' by Muthuswami Dikshitar.  
	    - **💎 Name Meaning**: Translates to 'the ornament of Shankara' (Lord Shiva).  
	    - **🎶 Hindustani Equivalent**: Yaman, sharing similar moods and structures.  
	    - **🩷 Emotional Range**: Expresses devotion, grandeur, and peace.  
	    - **🎻 Vocal and Instrumental**: Equally popular in both vocal and instrumental performances.
	    """)


with tab3:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image("upload.png")
    uploaded_file = st.file_uploader("Choose a file")
    if st.button("Analyze"):
        prediction = predict_audio_class(uploaded_file)
        st.write(prediction)

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
        with st.form("my_form"):
            st.write("Feedback - Was I Right?")
            sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
            selected = st.feedback("thumbs")
            if selected is not None:
                st.markdown(f"You selected: {sentiment_mapping[selected]}")
            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")   
    
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
