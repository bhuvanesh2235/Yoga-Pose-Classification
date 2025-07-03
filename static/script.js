// Ensure the video stream is captured from the webcam
const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const resultElement = document.getElementById('prediction-result');
const chatbotElement = document.getElementById('chatbot');

// Start the webcam feed
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    })
    .catch(err => {
        console.error("Error accessing webcam: ", err);
    });

// Capture the current video frame when the button is clicked
captureButton.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw the video frame to the canvas
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert the canvas to a Blob and send it to the Flask server
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'pose.jpg');

        // Send the frame to the Flask server for prediction
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultElement.textContent = `Predicted Pose: ${data.predicted_pose} (Confidence: ${data.confidence.toFixed(2)})`;
            chatbotElement.innerHTML = `<p>${data.suggestion}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, 'image/jpeg');
});