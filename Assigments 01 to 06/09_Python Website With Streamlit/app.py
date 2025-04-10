import streamlit as st
from deep_translator import GoogleTranslator

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Arial', sans-serif;
        }

        .stTitle {
            color: #2e8b57;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }

        .stTextArea textarea {
            border: 2px solid #4CAF50;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            width: 100%;
            margin-bottom: 20px;
        }

        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #45a049;
        }

        .stSelectbox select {
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
            margin-bottom: 20px;
        }

        .stSuccess {
            color: #4CAF50;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
        }

        .stWarning {
            color: #ff6347;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }

        .stText {
            font-size: 18px;
            font-weight: normal;
            color: #333;
            line-height: 1.5;
        }

        .stDownloadButton button {
            background-color: #ff9900;
            color: white;
            font-size: 16px;
            padding: 10px 15px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }

        .stDownloadButton button:hover {
            background-color: #ff7f00;
        }
        
        .stBalloons {
            display: block;
            text-align: center;
            padding: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Set up the title for the web app with custom styling
st.title("🌍 Translator App")

# Input text area for the user to enter text they want to translate
text = st.text_area("Enter text to translate:")

# Create a translator instance for determining supported languages
translator_instance = GoogleTranslator(source='auto', target='english')

# Get the list of supported languages for translation
languages = translator_instance.get_supported_languages()

# Language selection dropdowns for source and destination languages
src_lang = st.selectbox("Translate from:", languages, index=languages.index("english"))
dest_lang = st.selectbox("Translate to:", languages, index=languages.index("urdu"))

# Trigger translation when the "Translate" button is clicked
if st.button("Translate"):
    # Check if the input text is empty and display a warning if true
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Perform the translation using the selected languages
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        
        # Display the translated text with a success message
        st.success(f"Translated text ({dest_lang}):")
        st.write(f"**{translated}**")
        
        # Provide a download button for the user to download the translated text as a .txt file
        st.download_button("Download Translation", translated, file_name="translation.txt", mime="text/plain")
        
        # Trigger celebration balloons after successful translation
        st.balloons()
        
        # Display a success message confirming the translation was successful
        st.success("Translation successful!")
