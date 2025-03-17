# House Price Prediction App

This project predicts house prices based on two features: square meters (`m2`) and location rating (`lage`). The model is built using linear regression, and the application is built using Streamlit for the front-end.

## Features

- Predict house price based on square meters and location, as of now
- Ability to adjust the weight of the location feature.
- Standardization of input data for better model performance.

## Requirements

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas
- NumPy

## Installation

1. Clone this repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run UI/app.py
    ```

## How It Works

- **Data Standardization:** The input features (square meters and location rating) are standardized using `StandardScaler` to ensure that both features contribute equally to the model.
  
- **Prediction Logic:** The model uses linear regression to predict house prices based on the standardized features. The location feature is boosted in the model to make it more influential using feature engineering.

## File Descriptions

- `UI/app.py`: The Streamlit application where users can input the square meters and location rating to predict the house price.
- `machine_learning/predict.py`: The file containing the logic for training the linear regression model and making predictions based on new inputs.
- PS. The dataset is not in this remote repository

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
