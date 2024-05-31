# Face-Recognition-Based-Attendance-System
## Overview 
The Face Recognition Based Attendance System is a Python-based project that leverages facial recognition technology to automate the process of attendance marking. This system captures real-time images using a webcam, detects faces, recognizes known individuals, and logs their attendance with the date and time in a CSV file. It provides a robust and efficient way to track attendance, reducing manual effort and potential errors.

## Features
- **Real-time Face Recognition:** Uses the webcam to capture and process images in real-time.
- **Automated Attendance Logging:** Marks attendance with a timestamp in Attendance.csv file.
- **Multiple Person Recognition:** Capable of recognizing multiple individuals.
-**Robust Face Encoding:** Utilizes the face_recognition library for accurate face encoding and matching.

## Setup and Installation
### Prerequisites
Ensure you have Python 3.7 or higher installed. The project relies on the following Python libraries:
- OpenCV
- Numpy
- face_recognition

### Installation
1. Clone the Repository
    ```sh
   git clone https://github.com/yourusername/Face-Recognition-Based-Attendance-System.git
   cd Face-Recognition-Based-Attendance-System
   ```

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare Images**

   Place the images of individuals to be recognized in the `Images_Attendance` directory. Ensure each image file is named with the person's name (e.g., `john_doe.jpg`).

4. **Run the System**

   Execute the main script to start the attendance system.

   ```sh
   python main.py
   ```

## Usage

1. **Starting the System**

   Run `main.py` to start the webcam and initialize the face recognition process. The system will continuously monitor the video feed for faces.

2. **Recognizing Faces**

   When a known face is detected, the system will draw a rectangle around the face and display the person's name. The attendance record will be automatically added to `Attendance.csv` with the current date and time.

3. **Stopping the System**

   Press the `Enter` key to stop the webcam and terminate the script.

## Troubleshooting

If you encounter issues with face recognition or encoding, ensure the images in `Images_Attendance` are clear and well-lit. The script `test.py` can be used to debug and test individual components of the system.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the existing style and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

