import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def save_model_to_file(model, file_path):
    """Save a trained model to a file."""
    with open(file_path, "wb") as file:
        pickle.dump(model, file)


def load_model_from_file(file_path):
    """Load a trained model from a file."""
    with open(file_path, "rb") as file:
        return pickle.load(file)


def train_model(data):
    """Train a logistic regression model for weather prediction."""
    # Select feature columns for the model input
    X = data[["Temperature_C", "Humidity_pct", "Precipitation_mm", "Wind_Speed_kmh"]]
    # Select the target column for the model output
    y = data["Weather_Condition"]

    # Encode the target labels as integers
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Standardize the feature columns (mean=0, variance=1)
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, train_size=0.8, random_state=0
    )

    # Create a logistic regression model
    model = LogisticRegression()
    # Train the model using the training data
    model.fit(X_train, y_train)

    return model


def predict_weather(model, data, new_data):
    """
    Predict weather conditions using a pre-trained model based on new weather data
    (temperature, humidity, precipitation and wind speed) passed as an argument.
    """
    # Select feature columns for the model input
    X = data[["Temperature_C", "Humidity_pct", "Precipitation_mm", "Wind_Speed_kmh"]]
    # Select the target column for the model output
    y = data["Weather_Condition"]

    # Standardize the new data using the same scaler used for training data
    scaler = StandardScaler()
    scaler.fit_transform(X)
    new_data = scaler.transform(new_data)

    # Predict the weather condition using the trained model
    prediction = model.predict(new_data)

    # Convert the predicted label back to the original string label
    label_encoder = LabelEncoder()
    label_encoder.fit_transform(y)
    prediction_label = label_encoder.inverse_transform(prediction)

    return prediction_label
