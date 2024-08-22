# Twitter Auto Like & Retweet Admin Panel

## Description
This project is a Flask-based web application that allows you to automatically like and retweet a specific tweet using its URL. The app includes a simple admin panel where you can input the Tweet URL.

## Setup Instructions

### Step 1: Set Up the Project Environment

1. **Install Python**: Ensure that Python is installed on your system.
2. **Create a Virtual Environment (Optional but Recommended)**:
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

### Step 2: Install Dependencies

1. **Install Required Packages**:
   - Run the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

### Step 3: Set Up Twitter API Credentials

1. **Replace API Credentials**:
   - Open the `app.py` file and replace the placeholder values with your actual Twitter API credentials:
     ```python
     API_KEY = 'your_api_key'
     API_SECRET_KEY = 'your_api_secret_key'
     ACCESS_TOKEN = 'your_access_token'
     ACCESS_TOKEN_SECRET = 'your_access_token_secret'
     ```

### Step 4: Run the Application

1. **Start the Flask Application**:
   - Run the following command to start the application:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://127.0.0.1:5000/`.

### Step 5: Deploy to Heroku (Optional)

1. **Deploy to Heroku**:
   - If you want to deploy this app to Heroku, follow these steps:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     heroku create
     git push heroku master
     heroku ps:scale web=1
     ```

   - Your app should now be live on Heroku.

## Notes
- Make sure you have set up a Twitter Developer account and created an app to obtain your API credentials.
- This is a basic implementation and can be further customized or enhanced based on your needs.
