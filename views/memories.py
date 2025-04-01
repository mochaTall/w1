import streamlit as st
import os
from PIL import Image

# Set up page title
st.title("Upload and View Shared Images")

# Create an "uploads" directory if it doesn't exist
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Save the uploaded image
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded {uploaded_file.name} successfully!")

# Display all uploaded images
st.subheader("Shared Image Gallery")

image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(("png", "jpg", "jpeg"))]

if image_files:
    cols = st.columns(3)  # Arrange images in 3 columns
    for idx, image_name in enumerate(image_files):
        image_path = os.path.join(UPLOAD_DIR, image_name)
        img = Image.open(image_path)
        with cols[idx % 3]:  # Cycle through columns
            st.image(img, caption=image_name, use_container_width=True)

else:
    st.write("No images uploaded yet. Be the first to upload one! 📸")
