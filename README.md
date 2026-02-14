

## Introduction

Mashup Studio is a Python-based web project that generates custom music mashups automatically. The application takes a singer name, downloads multiple related audio tracks from YouTube, trims a fixed duration from each one, and merges them together into a single combined mashup file.

The backend is built using Flask and handles downloading, audio processing, merging, and file generation. The frontend provides a simple interface where users can enter the required details and receive their final mashup as a downloadable ZIP file.

---

## How It Works

The user enters a singer name, number of videos, and duration per clip through the web interface. The system then searches YouTube for related content, downloads the audio streams, cuts the specified portion from each track, and merges them into one continuous mashup. The final output is packaged as a ZIP file for easy download.

---

## How to Use

Install the required dependencies by running:

pip install -r requirements.txt

Start the application using:

python app.py

Once the server starts, open a browser and visit:

http://127.0.0.1:5000

Enter the required details and click **Create Mashup** to generate and download your mashup.

---

## Technologies Used

Python, Flask, yt-dlp, Pydub, FFmpeg, HTML, and CSS are used to build and run this project.

---

## Author

Pallika Malhotra

---

## Note

This project is developed for academic learning and practical demonstration of Python automation and web application development.
