import cv2
from ultralytics import YOLO


if __name__ == "__main__":

    # Load a model
    model = YOLO("best.pt")

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Webcam frame settings
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while cap.isOpened():

        # Capture frame
        ret, frame = cap.read()

        # Make detections
        results = model(frame)

        # Plot detections
        cv2.imshow('YOLO', results[0].plot())

        # If we press the exit-buttom 'q' we end the webcam caption
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close everything in the end
    cap.release()
    cv2.destroyAllWindows()
