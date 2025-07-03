# Vision in Motion: Revolutionizing Sports with Pose Detection Technology



## Project Overview
"Vision in Motion" is a real-time yoga pose classification project designed to help users refine their yoga postures through pose detection technology. The project captures video frames, processes them using OpenCV, and classifies the yoga pose with a machine learning model to provide instant feedback on pose accuracy.

## Table of Contents
- [System Architecture](#system-architecture)
- [Model Training and Testing](#model-training-and-testing)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## System Architecture

The following system architecture illustrates the flow of data and key components used in the project:

1. **User**  
   Input: Live video captured via a webcam.

2. **Frontend**  
   Technologies: HTML, CSS, JavaScript, WebRTC.  
   Functionality: Captures real-time video feed from the user and sends it to the Flask backend.

3. **Flask Server (Backend)**  
   Technologies: Flask (Python).  
   Functionality: Receives video frames, processes requests, and manages communication between the frontend and the model.

4. **Preprocessing Module**  
   Technology: OpenCV.  
   Functionality: Processes video frames (resizing, normalization) to prepare them for the model.

5. **Pose Detection Model**  
   Model: `Yoga_Pose_Classification_Model.h5`  
   Technology: TensorFlow/Keras.  
   Functionality: Classifies each frame into one of the predefined categories (downdog, goddess, tree, warrior2).

6. **Pose Classification Output**  
   Output: Classification result.  
   Feedback: Displays the pose result (correct/incorrect) on the webpage or through audio.

## Model Training and Testing

### 1. Data Collection and Preprocessing
The model is trained on a labeled dataset of yoga pose images. Images are preprocessed by resizing, normalizing pixel values, and applying data augmentation techniques.

### 2. Model Architecture
The model is based on a Convolutional Neural Network (CNN) or a pre-trained network like MobileNetV2 or ResNet for efficient pose classification.

### 3. Model Training
The model is trained using categorical cross-entropy as the loss function, and the Adam optimizer, with fine-tuning for batch size, learning rate, and epochs.

### 4. Saving the Model
The trained model is saved in H5 format (`Yoga_Pose_Classification_Model.h5`) for easy loading and deployment.

### 5. Real-Time Prediction
Video frames are passed through the model to detect and classify yoga poses, providing feedback to the user.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, WebRTC
- **Backend**: Flask (Python)
- **Pose Detection Model**: TensorFlow/Keras, MobileNetV2 or ResNet
- **Image Processing**: OpenCV

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Vision-in-Motion.git
    cd Vision-in-Motion
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Download or save the pre-trained model (`Yoga_Pose_Classification_Model.h5`) in the project's root directory.

4. Run the Flask server:
    ```bash
    python app.py
    ```

## Usage

1. **Start the Flask server**:
   Open your web browser and go to `http://127.0.0.1:5000`.

2. **Capture Pose**:
   Use the “Capture Pose” button to start capturing poses from the webcam.

3. **Get Feedback**:
   The app will classify the pose and display the result on the screen in real-time, providing feedback on the pose accuracy.

## Output

Sample output:

![Yoga Pose Classification](https://github.com/bhuvanesh2235/Yoga-Pose-Classification/blob/main/Output%20Image.png)

- The system displays the classified yoga pose with feedback on the webpage.
- Predicted Pose: downdog.
- The model classifies poses like downdog, goddess, tree, warrior2, etc.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and open a pull request. For major changes, open an issue to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.
