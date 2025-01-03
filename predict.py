import joblib
import cv2
import numpy as np
import librosa
import onnxruntime as ort

# Feature Extraction Function
def features_extractor(file):
    audio, sample_rate = librosa.load(file, res_type='kaiser_fast')
    mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sample_rate)
    mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)
    return mel_spectrogram

# Preprocess Input Data
def preprocess_audio(audio_file):
    scaler = joblib.load('saved_models/scaler.pkl')
    pca = joblib.load('saved_models/pca.pkl')
    features = features_extractor(audio_file)
    features_resized = cv2.resize(features, (224, 224))
    features_flat = features_resized.flatten().reshape(1, -1)
    features_scaled = scaler.transform(features_flat)
    features_pca = pca.transform(features_scaled)
    return features_pca

# Predict Audio Class
def predict_audio_class(audio_file):
    labelencoder = joblib.load('saved_models/label_encoder.pkl')
    # Load the ONNX model
    session = ort.InferenceSession("saved_models/audio_classification_model.onnx")

    # Preprocess the input audio file
    input_data = preprocess_audio(audio_file)

    # Get the input name for the ONNX model
    input_name = session.get_inputs()[0].name

    # Perform inference
    outputs = session.run(None, {input_name: input_data})

    # Decode the predicted class
    predicted_label = np.argmax(outputs[0], axis=1)
    prediction_class = labelencoder.inverse_transform(predicted_label)

    return prediction_class[0]