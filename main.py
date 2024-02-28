import streamlit as st
from PIL import Image

def main():
    st.title("Image Converter")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        convert_format = st.selectbox("Select the output format", ["JPEG", "PNG"])
        if st.button("Convert"):
            converted_image = convert_image(uploaded_file, convert_format)
            st.image(converted_image, caption="Converted Image.", use_column_width=True, format=convert_format.lower())
            st.download_button("Download Converted Image", converted_image_to_bytes(converted_image), f"converted_image.{convert_format.lower()}", key="download_button")

def convert_image(uploaded_file, format):
    original_image = Image.open(uploaded_file)
    converted_image = original_image.convert(format)
    return converted_image

def converted_image_to_bytes(converted_image):
    img_byte_array = BytesIO()
    converted_image.save(img_byte_array, format="PNG")
    return img_byte_array.getvalue()

if __name__ == "__main__":
    main()
