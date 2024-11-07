from flask import Flask, request, jsonify, render_template
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load your saved model
model = load_model('Yoga_Pose_Classification_Model.h5')

def preprocess_image(image):
    # Resize the image to the size expected by the model (300x300)
    resized_image = cv2.resize(image, (300, 300))
    
    # Normalize the image
    resized_image = resized_image / 255.0
    
    # Expand dimensions to fit model input shape (1, 300, 300, 3)
    resized_image = np.expand_dims(resized_image, axis=0)
    
    return resized_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('file')
    
    if file is None or file.filename == '':
        return jsonify({'error': 'No file uploaded'}), 400

    # Save the image temporarily
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'pose.jpg')
    file.save(filepath)

    # Read the image and preprocess it for prediction
    image = cv2.imread(filepath)
    preprocessed_image = preprocess_image(image)

    # Predict using the model
    prediction = model.predict(preprocessed_image)
    
    # Define your pose classes here
    pose_classes = ['downdog', 'goddess', 'tree', 'warrior2']  # Replace with actual pose names
    predicted_pose = pose_classes[np.argmax(prediction)]

    # Return the prediction result
    return jsonify({'predicted_pose': predicted_pose})

if __name__ == '__main__':
    app.run(debug=True)
