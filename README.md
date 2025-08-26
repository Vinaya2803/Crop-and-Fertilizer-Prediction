🌱 AGROGUIDE : Navigating Smarter Farming Solutions

The Crop and Fertilizer Predictor is a machine learning–powered web platform designed to help farmers choose the most suitable crops and fertilizers based on soil nutrients (NPK), pH, rainfall, and city-specific weather conditions.

It provides tailored recommendations that reduce resource wastage, improve crop yield, and promote sustainable farming.

✨ Features

Input soil parameters (Nitrogen, Phosphorous, Potassium, pH)

Predict best-suited crops for given soil & climate

Suggest fertilizers (type & quantity) for selected crop

Real-time Weather API integration

User-friendly web interface built with Flask & Bootstrap

🚀 How to Use

Enter the corresponding nutrient values of your soil, state, and city.

The N-P-K (Nitrogen-Phosphorous-Potassium) values should be entered as their ratios.

When entering the city name, try to use common city names. Remote towns may not be available in the Weather API database (used to fetch humidity & temperature).

💧 Fertilizer Suggestion System

Enter the nutrient contents of your soil and the crop you want to grow.

The algorithm will analyze whether your soil lacks or has excess of nutrients.

Based on this, it will suggest the most suitable fertilizer to use.

⚙️ Installation & Setup

Clone the project

git clone https://github.com/Vinaya2803/Crop-and-Fertilizer-Prediction.git


Or download the ZIP and unzip it.

Make sure you have Git and Anaconda installed on your system.

Create and activate virtual environment
Open Anaconda Prompt in the project folder and run:

conda create -n agroguide python=3.6.12
conda activate agroguide
pip install -r requirements.txt


Here, agroguide is the name of the virtual environment.

Run the project

python app.py


Open in browser
Go to the localhost URL shown after running app.py to use the project locally.
