from flask import Flask, request, jsonify, render_template
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load the pre-trained model
model = load_model('Yoga_Pose_Classification_Model.h5')

# Dictionary of pose suggestions
pose_suggestions = {
    "downdog": {
        "incorrect": "Ensure your hands and feet are firmly planted, hips lifted high, and back straight. Avoid letting your head drop too low.",
        "correct": "Great job! Your Downward Dog is looking solid."
    },
    "goddess": {
        "incorrect": "Widen your stance and bend your knees more deeply. Keep your chest open and arms in a strong 'goalpost' position.",
        "correct": "Excellent Goddess pose! Maintain that strong stance."
    },
    "tree": {
        "incorrect": "Focus on balancing by pressing your foot into your inner thigh, keep your hands at heart center, and gaze forward.",
        "correct": "Well done! Your Tree pose is balanced and steady."
    },
    "warrior2": {
        "incorrect": "Extend your arms fully, bend your front knee over your ankle, and turn your head to look over your front hand.",
        "correct": "Great Warrior II! Keep your stance strong and aligned."
    }
}

def preprocess_image(image):
    resized_image = cv2.resize(image, (300, 300))
    resized_image = resized_image / 255.0
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

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'pose.jpg')
    file.save(filepath)

    image = cv2.imread(filepath)
    preprocessed_image = preprocess_image(image)

    prediction = model.predict(preprocessed_image)
    pose_classes = ['downdog', 'goddess', 'tree', 'warrior2']
    predicted_pose = pose_classes[np.argmax(prediction)]

    # Convert confidence to Python float
    confidence = float(np.max(prediction))

    # Simple logic to determine if pose is "incorrect" (e.g., confidence < 0.7)
    feedback_type = "incorrect" if confidence < 0.7 else "correct"
    suggestion = pose_suggestions[predicted_pose][feedback_type]

    return jsonify({
        'predicted_pose': predicted_pose,
        'confidence': confidence,
        'suggestion': suggestion
    })

if __name__ == '__main__':
    app.run(debug=True)