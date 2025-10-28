# 🌾 AGROGUIDE : Navigating Smarter Farming Solutions

The **Crop and Fertilizer Predictor** is a machine learning–powered web platform designed to help farmers choose the most suitable crops and fertilizers based on **soil nutrients (NPK), pH, rainfall, and city-specific weather conditions.**  
It provides tailored recommendations that reduce resource wastage, improve crop yield, and promote sustainable farming.  

---

## ✨ Features

- Input soil parameters (**Nitrogen, Phosphorous, Potassium, pH**).  
- Predict best-suited crops for given soil & climate.  
- Suggest fertilizers (**type & quantity**) for selected crop.  
- Real-time **weather API integration**.  
- User-friendly web interface built with **Flask & Bootstrap**.  

---

## 🚀 How to Use

### Enter the corresponding **nutrient values of your soil, state and city**.  
- The **N-P-K** (Nitrogen-Phosphorous-Potassium) values should be entered as their ratio.  
- When entering the **city name**, make sure it is a **common city** (remote towns may not be available in the Weather API).  

### Fertilizer Suggestion System  
- Enter the **nutrient contents of your soil** and the **crop you want to grow**.  
- The algorithm will detect nutrient **deficiency/excess** and recommend suitable fertilizers accordingly.  

---

## ⚙️ Installation & Setup

1. Clone the project:  
   ```bash
   git clone https://github.com/Vinaya2803/Crop-and-Fertilizer-Prediction.git

Or download the code and unzip it.

2. Make sure you have [Git](https://git-scm.com/downloads) and [Anaconda](https://www.anaconda.com/) installed.

3. Open Anaconda Prompt in the project directory and run:
   ```bash
    conda create -n agroguide python=3.6.12
    conda activate agroguide
    pip install -r requirements.txt    
  agroguide is the name of the virtual environment.

4.Run the project:
   ```bash
    python app.py
