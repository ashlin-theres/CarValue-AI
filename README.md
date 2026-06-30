# 🚗 CarValue AI – Used Car Resale Price Prediction (India)

CarValue AI is a Machine Learning-powered web application that predicts the resale value of used cars in India.  
It provides an interactive interface to analyze car price trends and get instant predictions based on vehicle features.

The app is built using Streamlit and deployed as a full-stack ML web application.

---

## 🌐 Live Demo
👉 https://carvalue-ai-2feuldgd8v9wlrjwre2tjp.streamlit.app/

---

## 📌 Project Overview

Buying or selling used cars in India often involves uncertain pricing.  
This project solves that problem using a trained regression model to estimate fair market value.

The system takes inputs such as:
- Car brand and model  
- Year of manufacture  
- Fuel type  
- Transmission type  
- Mileage  

and predicts the expected resale price.

---

## 📱 App Pages

### 🏠 Home Page
- Introduction to the application  
- Overview of project purpose  
- Navigation to other pages  

### 📊 Prediction Page
- Input form for car details  
- Machine learning model predicts price  
- Instant output display  

### 📈 Insights Page
- Data visualizations and analysis  
- Trends in used car prices in India  
- Feature impact on price  

### ℹ️ About Page
- Project explanation  
- Tech stack details  
- Developer information  

---

## ✨ Features

- 🚗 Real-time car price prediction  
- 📊 Interactive analytics dashboard  
- 🧠 Machine Learning regression model  
- 🇮🇳 India-focused resale analysis  
- ⚡ Fast Streamlit web app  
- 🌐 Fully deployed application  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🌐  
- Pandas & NumPy  
- Scikit-learn 🤖  
- Joblib  
- Matplotlib & Seaborn 📊  

---

## 🧠 Machine Learning Pipeline

- Data cleaning and preprocessing  
- Feature encoding  
- Model training using regression algorithms  
- Model evaluation and optimization  
- Model saved using Joblib  
- Deployed using Streamlit  

---

# App Preview

Home Page
<img width="1836" height="850" alt="Screenshot 2026-06-30 140151" src="https://github.com/user-attachments/assets/59f4ff38-901f-4bc8-9a85-683216924b7e" />

Prediction Page
<img width="1853" height="847" alt="Screenshot 2026-06-30 140231" src="https://github.com/user-attachments/assets/20eb94b2-175f-4af4-9498-3d8fbfaf2e11" />


Insights Page
<img width="1847" height="847" alt="Screenshot 2026-06-30 140301" src="https://github.com/user-attachments/assets/7517cb97-dd0d-4a0b-9f43-cd5e30b95050" />


About Page
<img width="1842" height="852" alt="Screenshot 2026-06-30 140331" src="https://github.com/user-attachments/assets/aee7668d-bd6b-47bc-ae5e-5e0b529621d6" />

---

## 👩‍💻 Author

- Ashlin Theres James
- B.Tech Computer Science (AI & Data Science)

---

# Future Improvements
- Improve model accuracy using advanced algorithms like XGBoost and Random Forest tuning
- Add more real-time market data for better prediction reliability
- Include feature importance explanation for better user understanding
- Add user authentication and login system
- Expand insights dashboard with deeper analytics and trend forecasting
- Deploy with a custom domain for a more professional presence
- Optimize model loading for faster prediction response time
- Extend support to electric vehicles (EV price prediction)
- Improve UI/UX for mobile responsiveness

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/CarValue-AI.git
cd CarValue-AI
pip install -r requirements.txt
streamlit run app.py
