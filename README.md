# Face-Recognition-Based-Attendance-System

The Face Recognition Based Attendance System is a Python 3 project that utilizes computer vision and facial recognition technology to automate attendance tracking. This system is designed to work with standard webcams and provides a user-friendly interface for administrators and users.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Face Recognition:** Automatically recognizes individuals based on facial features.
- **Real-time Monitoring:** Supports real-time attendance tracking for both individual and group sessions.
- **Attendance Logging:** Records attendance data with timestamps and stores it securely.
- **User-Friendly Interface:** An intuitive and easy-to-use interface for administrators and users.
- **Customization:** Easily adapt the system to your specific use case and customize recognition parameters.
- **Cross-Platform:** Compatible with Windows, macOS, and Linux.

## Requirements

To run the Face Recognition Based Attendance System, you will need the following:

- Python 3.x
- OpenCV (cv2)
- NumPy
- face_recognition
- OS
- Datetime

You can install these requirements using the provided `requirements.txt` file:

```shell
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/Hafsa1000/Face-Recognition-Based-Attendance-System.git
   cd Face-Recognition-Based-Attendance-System
   ```

2. Install the required Python libraries if not already installed:

   ```shell
   pip install -r requirements.txt
   ```

3. Configure the system settings and recognition parameters to meet your needs.

4. Run the system:

   ```shell
   python main.py
   ```

## Usage

1. Add images of individuals to the "Images_Attendance" directory for recognition.

2. Execute the system to capture and recognize faces in real-time.

3. Attendance records are stored in the "Attendance.csv" file with timestamps.

## Contributing

Contributions are welcome! Feel free to open issues, create pull requests, or suggest new features and improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [NumPy](https://numpy.org/)
