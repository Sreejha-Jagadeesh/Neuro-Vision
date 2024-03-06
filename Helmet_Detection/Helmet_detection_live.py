import cv2
from ultralytics import YOLO

# Create a YOLO model
model = YOLO(model="C:\\Users\\hp\\Downloads\\Helmet-Detection-Model-main\\Helmet-Detection-Model-main\\best.pt")

# Specify the camera as the source
source = 0  # Change this if your camera has a different source index

# Open the camera
cap = cv2.VideoCapture(source)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Perform inference with the YOLO model
    results = model(frame)

    # Get the first result (assuming we only want to display the first detection)
    result = results[0]

    # Draw the bounding boxes and labels on the frame
    boxes = result.boxes.data.tolist()
    labels = result.names
    for box in boxes:
        x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, labels[int(box[5])], (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("YOLO Object Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
