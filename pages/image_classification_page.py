from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st

st.title('카메라 입력을 사용한 이미지 분류기')
img_file_buffer = st.camera_input("카메라를 통해 이미지를 캡처하세요.")

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_preprocessed = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    predictions = model.predict(img_preprocessed)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0]
    st.write(f"예측 결과: {decoded_predictions[1]} ({decoded_predictions[2] * 100:.2f}%)")
