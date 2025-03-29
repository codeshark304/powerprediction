# Power Prediction using LSTM

## Overview
This project implements three power prediction models using **XGBoost, LSTM, and GRU**. The trained models are deployed using **Flask** with a dropdown for model selection and real-time predictions. The web application is hosted using **Docker**, and the UI is improved with HTML.

## Features
- Three trained models: **XGBoost, LSTM, and GRU**.
- Web-based interface for user-friendly interaction.
- Real-time power prediction with dynamic model selection.
- Dockerized Flask deployment for portability.

## Installation
### Prerequisites
Ensure you have the following installed:
```sh
# Required Dependencies
Python 3.8+
Flask
TensorFlow
XGBoost
Docker
```

### Clone the Repository
```sh
git clone https://github.com/yourusername/power-prediction.git
cd power-prediction
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### Run Flask Application
```sh
python app.py
```
The web app will be available at `http://localhost:5000`

### Run with Docker
Build the Docker image:
```sh
docker build -t power-prediction .
```
Run the container:
```sh
docker run -p 5000:5000 power-prediction
```

## Project Structure
```sh
power-prediction/
│── models/               # Trained models
│── static/               # CSS, JS, images
│── templates/            # HTML templates
│── app.py                # Flask backend
│── requirements.txt      # Dependencies
│── Dockerfile            # Docker configuration
└── README.md             # Project documentation
```

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.
