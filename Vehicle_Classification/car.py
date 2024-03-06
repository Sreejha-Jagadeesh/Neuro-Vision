import cv2

# Load the pre-trained Haar Cascade model for vehicles
vehicle_cascade = cv2.CascadeClassifier('C:\\Users\\hp\\Downloads\\vehicle_detection_haarcascades-master\\vehicle_detection_haarcascades-master\\cars.xml')

# Open the default camera (change the index if you have multiple cameras)
cap = cv2.VideoCapture(0)

# Set a threshold size for classification (you may need to adjust this based on your requirements)
threshold_size = 5000

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the frame
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))

    # Classify each detected vehicle
    for (x, y, w, h) in vehicles:
        # Extract the region of interest (ROI) for each detected vehicle
        roi = gray[y:y+h, x:x+w]

        # Your classification logic here (e.g., use a pre-trained classifier or deep learning model)
        # For a simple example, let's assume we classify based on size
        vehicle_size = w * h

        # Print the classification result
        if vehicle_size > threshold_size:
            classification_result = "Vehicle"
        else:
            classification_result = "Not a Vehicle"

        # Draw rectangles around the detected vehicles
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the classification result
        cv2.putText(frame, classification_result, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with vehicle detections and classifications
    cv2.imshow('Vehicle Classification', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
