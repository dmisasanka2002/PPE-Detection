import tkinter as tk
import cv2
from tkinter import font
import threading

from predictions.result import get_result
from predictions.detection import process_frame_with_yolo

def create_second_window(selected_items):
    """Creates the second window with output text field and OpenCV video."""
    second_window = tk.Toplevel()
    second_window.title("Processing Results")
    
    def on_closing():
        """Handles the window close event to release OpenCV resources."""
        cap.release()
        cv2.destroyAllWindows()
        second_window.destroy()

    second_window.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Output Text Field (dark background, light green text)
    global output_text
    output_text = tk.Text(second_window, height=5, width=50, font=('Arial', 16), wrap='word', bd=2, relief='solid', bg='black', fg='lightgreen')
    output_text.tag_configure("center", justify='center')
    output_text.insert(tk.END, "CHECKING.....", "center")
    output_text.pack(pady=10)
    
    # Display selected checkbox items
    selected_label = tk.Label(second_window, text=f"Selected Features: {', '.join(selected_items)}", font=('Arial', 12))
    selected_label.pack(pady=10)

    # OpenCV video stream (for example, using the webcam)
    thread = threading.Thread(target=capture_video, args=(selected_items, second_window))
    thread.daemon = True
    thread.start()
    
    second_window.mainloop()

def capture_video(selected_items, second_window):
    """Capture video from the webcam and display it in the Opencv window."""
    global cap
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(r"C:\Users\User\Desktop\Programming\Web development\HTML CSS JS\Projects\File Share\V 1.0.3\uploads\6474391-uhd_1440_2560_25fps.mp4")
    
    new_width = 400

    while True:
        ret, frame = cap.read()
        if ret:
            # Process the frame using YOLO for object detection
            frame, result = process_frame_with_yolo(frame)

            # Resizing
            original_height, orginal_width, _ = frame.shape

            ratio = new_width / float(orginal_width)
            new_dims = (new_width, int(original_height * ratio))


            resized_frame = cv2.resize(frame, new_dims)
            cv2.imshow("LIVE VIDEO", resized_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Update the text based on the get_result function
            detection_status, missing_items = get_result(result, selected_items)
            result_text = f"Detection Status: {detection_status}\nMissing Items: {', '.join(missing_items) if missing_items else 'None'}"
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, result_text, "center")
        
        if not second_window.winfo_exists():
            break

    cap.release()
    cv2.destroyAllWindows()

    if second_window.winfo_exists():
        second_window.destroy()
