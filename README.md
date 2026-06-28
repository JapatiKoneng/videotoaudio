# Video2MP3

Video2MP3 is a desktop application for converting video files to MP3 audio **offline**. It provides a fast and simple way to extract audio from your videos without requiring an internet connection.

## How to Run the Application

1. Open the **dist** folder.
2. Double-click **Video2MP3.exe** to start the application.

<img width="498" height="333" alt="Video2MP3 Screenshot" src="https://github.com/user-attachments/assets/38efc1b6-7d31-4ccd-abd3-ec45669a51ba" />

## Running the Project from Source

If you want to run or modify the application in Visual Studio Code, follow these steps:

### Requirements

* Python 3.x installed
* FFmpeg (`ffmpeg.exe`) in the project folder

### Installation

1. Install the required package:

```bash
py -m pip install customtkinter
```

### Run the Application

```bash
py main.py
```

### Build the Executable

Use the following command to generate the executable file:

```bash
pyinstaller --onefile --windowed --add-binary "ffmpeg.exe;." --name "Video2MP3" main.py
```
