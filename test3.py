import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
import librosa
import librosa.display
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, TensorBoard
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, precision_recall_fscore_support
from sklearn.decomposition import PCA
import joblib
from concurrent.futures import ThreadPoolExecutor
from sklearn.utils.class_weight import compute_class_weight
import datetime
import cv2
import tf2onnx

warnings.filterwarnings('ignore')

# Loading audio files from dataset directory
base_directory = "C:/Scholars/Sri/SwaraScribe/balanced_carnatic_raag_300/"
audio_files = []
labels = []

for raga_folder in os.listdir(base_directory):
    raga_folder_path = os.path.join(base_directory, raga_folder)
    if os.path.isdir(raga_folder_path):
        for file in os.listdir(raga_folder_path):
            if file.endswith(".wav"):
                audio_files.append(os.path.join(raga_folder_path, file))
                labels.append(raga_folder)

# Feature Extraction Function
def features_extractor(file):
    audio, sample_rate = librosa.load(file, res_type='kaiser_fast')
    mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sample_rate)
    mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)
    return mel_spectrogram

# Extract features in parallel
def parallel_feature_extraction(audio_files):
    with ThreadPoolExecutor() as executor:
        features = list(executor.map(lambda file: features_extractor(file), audio_files))
    return features

# Extract features and labels
features = parallel_feature_extraction(audio_files)
X = np.array([cv2.resize(feature, (224, 224)) for feature in features])  # Resize to 224x224
X_flat = X.reshape(X.shape[0], -1)  # Flatten the images for PCA
y = np.array(labels)

# Standardize Features
scaler = StandardScaler()
X_flat = scaler.fit_transform(X_flat)

# Apply PCA to Reduce Dimensionality
pca = PCA(n_components=0.95)  # Retain 95% of the variance
X_pca = pca.fit_transform(X_flat)

# Encode Labels
labelencoder = LabelEncoder()
y = to_categorical(labelencoder.fit_transform(y))

# Model Architecture Enhancement (Dense-based Model after PCA)
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
fold_no = 1

for train_idx, val_idx in skfold.split(X_pca, np.argmax(y, axis=1)):
    X_train, X_val = X_pca[train_idx], X_pca[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

    model = Sequential()
    model.add(Dense(512, input_shape=(X_train.shape[1],), activation='relu', kernel_regularizer='l2'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu', kernel_regularizer='l2'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(y.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    model.summary()

    # Class Weights for Handling Class Imbalance
    class_weights = compute_class_weight('balanced', classes=np.unique(np.argmax(y, axis=1)), y=np.argmax(y, axis=1))
    class_weights = dict(enumerate(class_weights))

    # Callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.001)
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

    # Training
    model.fit(X_train, y_train, batch_size=32, epochs=100, validation_data=(X_val, y_val),
              callbacks=[early_stopping, reduce_lr, tensorboard_callback], class_weight=class_weights, verbose=1)

    # Evaluate the Model
    y_pred = model.predict(X_val)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_val, axis=1)

    # Confusion Matrix
    conf_matrix = confusion_matrix(y_true, y_pred_classes)
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')
    plt.title(f'Confusion Matrix for Fold {fold_no}')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.show()

    # Classification Report
    print(f'Classification Report for Fold {fold_no}')
    print(classification_report(y_true, y_pred_classes))

    # Additional Metrics: Precision, Recall, F1-Score
    precision, recall, f1_score, _ = precision_recall_fscore_support(y_true, y_pred_classes, average='weighted')
    print(f'Precision: {precision:.2f}, Recall: {recall:.2f}, F1-Score: {f1_score:.2f}')

    # ROC and AUC Curve
    fpr, tpr, _ = roc_curve(y_true, y_pred[:, 1], pos_label=1)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, color='blue', label=f'ROC curve (area = {roc_auc:.2f})')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Receiver Operating Characteristic (ROC) for Fold {fold_no}')
    plt.legend(loc="lower right")
    plt.show()

    fold_no += 1

# Save the model
model.save('saved_models/audio_classification_model.h5')

# Save the label encoder, scaler, and PCA
joblib.dump(labelencoder, 'saved_models/label_encoder.pkl')
joblib.dump(scaler, 'saved_models/scaler.pkl')
joblib.dump(pca, 'saved_models/pca.pkl')

# Convert the Keras model to ONNX format
onnx_model, _ = tf2onnx.convert.from_keras(model, opset=13)

# Save the ONNX model to file
with open("saved_models/audio_classification_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())