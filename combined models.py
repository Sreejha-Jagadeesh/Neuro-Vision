from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Load Haar cascade classifier for vehicle classification
vehicle_cascade = cv2.CascadeClassifier('C:\\Users\\hp\\Downloads\\vehicle_detection_haarcascades-master\\vehicle_detection_haarcascades-master\\cars.xml')

# Load Haar cascade classifier for license plate detection
plate_cascade = cv2.CascadeClassifier('C:\\Users\\hp\\Downloads\\Car-Number-Plates-Detection-main\\Car-Number-Plates-Detection-main\\model\\number plate.xml')

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Perform vehicle classification using Haar cascade
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))

        # Perform license plate detection using Haar cascade
        plates = plate_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))

        # Draw bounding boxes for vehicle classification
        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Draw bounding boxes for license plate detection
        for (x, y, w, h) in plates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Convert the frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')  # You need to create an HTML template for this

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
