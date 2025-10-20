import cv2
import csv

# Load the pre-trained face detector from OpenCV
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
CAMERA_PORT = 0  # Const variable, do not change

# Open the default camera (index 0)
cap = cv2.VideoCapture(CAMERA_PORT)


# Function to read the latest happiness percentage from the CSV file
def read_latest_happiness_percentage():
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) >= 2:
            return round(
                float(rows[-1][-1]) * 10, 2
            )  # Last row, last column (happiness percentage)
    return "N/A"  # Return "N/A" if no data is available


# Function to detect faces and draw rectangles in a live video feed
def detect_faces_live():
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Get the latest happiness percentage
        happiness_percentage = read_latest_happiness_percentage()

        # Loop through each detected face
        for x, y, w, h in faces:
            # Draw a blue rectangle around the face with increased thickness
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

            # Display text above the square with the latest happiness percentage
            text = f"Happiness: {happiness_percentage}%"
            cv2.putText(
                frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2
            )

        # Display the frame with rectangles around faces
        cv2.imshow("Live Video Feed", frame)

        # Capture an image when 'p' is pressed
        if cv2.waitKey(1) & 0xFF == ord("p"):
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured successfully.")

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Call the function to start face detection from the live video feed
    detect_faces_live()
    happiness_percentage = read_latest_happiness_percentage()
