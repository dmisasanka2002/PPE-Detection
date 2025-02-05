from ultralytics import YOLO
import cv2

from utils.colors import colors


def process_frame_with_yolo(frame):
    """Process the frame using YOLO for object detection and draw bounding boxes."""

    model = YOLO(r'../app\models\best.pt')
    class_names = model.names
    
    # Perform inference on the frame
    results = model(frame)

    # Draw detections on the frame
    for detection in results[0].boxes.data:
        x1, y1, x2, y2, confidence, class_id = detection[:6]
        class_id = int(class_id)
        label = f"{class_names[class_id]}: {confidence:.2f}"

        # Draw the bounding box
        color = colors.get(class_id, [0, 255, 0])  # Default to green if class_id not found
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

        # Draw the label above the bounding box
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return frame,results
