import streamlit as st
import malaya
import re

# Load the transliteration model
model = malaya.jawi_rumi.transformer()


# Function to check if the text contains only Jawi characters
def is_jawi_text(text):
    jawi_pattern = re.compile(r"^[\u0600-\u06FF\s]+$")
    return bool(jawi_pattern.match(text))


def transliterate(input_text):
    result = model.greedy_decoder([input_text])
    return result[0]


# Add your logo
logo_url = "https://static.wixstatic.com/media/a82f81_ee5d3c423b80433eaac59bb71b2bba16~mv2.png"  # Replace with the URL of your logo
st.image(logo_url, width=100)  # Adjust width as needed
# Streamlit app
st.title("Deep Learning for Classical Malay Text Transliteration")

# Input text box
input_text = st.text_input("Enter Jawi Text:")

# Transliteration button
if st.button("Transliterasi"):
    if not input_text:
        st.warning("Sila masukkan teks untuk transliterasi.")
    # elif not is_jawi_text(input_text):
    #     st.warning("Sila masukkan teks Jawi sahaja.")
    else:
        translation = transliterate(input_text)
        st.success(f"Hasil Transliterasi:  {translation}")

st.subheader("Contoh Teks")
st.write("ادوهاي")
st.write("بركروت داهيڽ")
st.write("امڤون توانكو ڤوتري")
st.write("دي سوده ترچدرا تروق")
st.write("مات راتو سيتي بانون ممبولت")
st.write("لقسامان كستوري كيت تيدق اكن داڤت برتاهن لبيه لاما جک برتروسن بڬيني")
