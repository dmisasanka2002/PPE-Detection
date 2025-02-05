# PPE Detection System

This project is a Personal Protective Equipment (PPE) detection system that uses a YOLO (You Only Look Once) model to detect various safety items (like helmets, gloves, vests, etc.) worn by individuals in real-time video feeds. The system includes a Tkinter-based GUI that displays detection results and opens an OpenCV imshow window for video visualization.

## Features

- Real-time detection of safety equipment such as helmets, gloves, vests, boots, goggles, and more.
- Easy-to-use GUI built with Tkinter.
- Parallel display of video feed using OpenCV imshow.
- Dynamic updating of detection results in the GUI.
- Resizable OpenCV window.
- Cross-window synchronization: Closing one window closes all related windows.

## Classes Detected

The YOLO model detects the following classes:

- Helmet
- Gloves
- Vest
- Boots
- Goggles
- None
- Person
- No Helmet
- No Goggle
- No Gloves
- No Boots

## Prerequisites

- Python 3.x
- OpenCV
- Tkinter
- PIL (Pillow)
- Ultralytics YOLO

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dmisasanka2002/PPE-Detection.git
   cd ppe-detection
   ```

2. Install the required packages:

   ```bash
   pip install opencv-python-headless tk pillow ultralytics
   ```

3. Ensure your YOLO model file best.pt is placed in the app/models/ directory.

## Usage

To run the PPE detection system, follow these steps:

1. Navigate to the main directory:

   ```bash
   cd app
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. Select the safety items to be detected in the GUI.

4. The second window and an OpenCV imshow window will open. The system will start detecting the selected items in real-time from the video feed.

5. The detection results will be displayed in the second window.

## Handling Window Closures

- Closing the main window will close all related windows.
- Closing the second Tkinter window or the OpenCV window will also close both windows simultaneously.
- To close the OpenCV window using the keyboard, press the 'q' key.

## Code Overview

### Main Script

The main script initializes the Tkinter main window and handles the creation of the second window and the OpenCV video feed.

### Second Window

The second window displays the detection results in a text field and provides options to select which items to detect.

### OpenCV Video Feed

The OpenCV imshow window displays the video feed with bounding boxes and labels for detected items. The window size is set to 500x500 pixels, and it synchronizes with the second Tkinter window for closing events.

### Functions

- create_second_window(selected_items): Initializes the second Tkinter window and sets up the text field for displaying detection results.
- capture_video(selected_items, second_window): Captures video from the webcam, processes each frame using YOLO, displays the frame in an OpenCV window, and updates the detection results in the text field.
- process_frame_with_yolo(frame): Processes the video frame using the YOLO model, draws bounding boxes and labels for detected items, and returns the processed frame and detection results.
- get_result(yolo_result, selected_items): Checks if all selected items are detected for each person and returns the detection status and any missing items.
- group_detections_by_person(yolo_result): Groups detections by person and their associated items.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the developers of YOLO and the open-source community for providing the tools and resources to build this system
