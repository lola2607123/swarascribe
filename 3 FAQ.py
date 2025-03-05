import streamlit as st
st.set_page_config(layout="wide")
def main():
    st.title("FAQ - Carnatic Music Ragam Detection")
    st.write("Find answers to common questions about our ragam detection tool.")
    
    with st.expander("How does the ragam detection work?"):
        st.write("Our tool analyzes the frequency patterns and swaras in the uploaded audio file to identify the closest matching ragam.")
    
    with st.expander("What types of audio files are supported?"):
        st.write("We support MP3, WAV, and FLAC formats for ragam detection.")
    
    with st.expander("Is the detection 100% accurate?"):
        st.write("While our model is highly accurate, results may vary based on audio quality, background noise, and clarity of singing.")
    
    with st.expander("Can I use instrumental music for ragam detection?"):
        st.write("Yes, but vocal recordings generally yield more accurate results compared to instrumental music.")
    
    with st.expander("How long does the detection process take?"):
        st.write("It typically takes a few seconds, but processing time may vary based on file size and server load.")
    
    with st.expander("Do I need an internet connection to use this tool?"):
        st.write("Yes, since the detection runs on our cloud-based servers, an internet connection is required.")
    
    with st.expander("Can I get notations for the detected ragam?"):
        st.write("Yes! Once a ragam is detected, we provide notations for some popular compositions in that ragam.")
    
    with st.expander("Who can use this tool?"):
        st.write("Anyone interested in Carnatic music, from beginners to experts, can use our ragam detection tool to enhance their learning and practice.")
        st.write("\n## General Carnatic Music FAQs")
    
    with st.expander("What is Carnatic music?"):
        st.write("Carnatic music is a classical music system from South India, known for its intricate melodies, rhythmic structures, and deep devotional themes.")
    
    with st.expander("What are the basic elements of Carnatic music?"):
        st.write("Carnatic music consists of three primary elements: Sruti (pitch), Raga (melodic framework), and Tala (rhythmic cycle).")
    
    with st.expander("What is a Ragam?"):
        st.write("A Ragam is a melodic framework in Carnatic music that consists of specific swaras (notes) and characteristic phrases, forming the basis for improvisation and compositions.")
    
    with st.expander("What is a Kriti?"):
        st.write("A Kriti is a structured composition in Carnatic music that includes Pallavi (opening section), Anupallavi (middle section), and Charanam (concluding section).")
    
    with st.expander("Who are some famous Carnatic musicians?"):
        st.write("Some renowned Carnatic musicians include Tyagaraja, Muthuswami Dikshitar, Syama Sastri, MS Subbulakshmi, and Balamuralikrishna.")
    
if __name__ == "__main__":
    main()