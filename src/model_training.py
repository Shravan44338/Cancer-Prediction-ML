"""
Model Training Module
Handles model creation, training, and saving
"""

import joblib
from sklearn.ensemble import RandomForestClassifier
from data_preprocessing import DataPreprocessor


class CancerPredictionModel:
    """
    Class for training cancer prediction model
    """
    
    def __init__(self, n_estimators=100, random_state=42):
        """
        Initialize the model
        
        Args:
            n_estimators (int): Number of trees in the forest
            random_state (int): Random seed for reproducibility
        """
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )
        self.is_trained = False
    
    def train(self, X_train, y_train):
        """
        Train the Random Forest model
        
        Args:
            X_train: Training features
            y_train: Training labels
        """
        print("Training Random Forest Classifier...")
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print("Model trained successfully!")
    
    def predict(self, X):
        """
        Make predictions on new data
        
        Args:
            X: Features to predict
            
        Returns:
            array: Predictions
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """
        Get prediction probabilities
        
        Args:
            X: Features to predict
            
        Returns:
            array: Prediction probabilities
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        return self.model.predict_proba(X)
    
    def save_model(self, filepath='../models/cancer_prediction_model.pkl'):
        """
        Save the trained model to disk
        
        Args:
            filepath (str): Path to save the model
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before saving")
        
        joblib.dump(self.model, filepath)
        print(f"Model saved to {filepath}")
    
    @staticmethod
    def load_model(filepath='../models/cancer_prediction_model.pkl'):
        """
        Load a trained model from disk
        
        Args:
            filepath (str): Path to the saved model
            
        Returns:
            CancerPredictionModel: Loaded model instance
        """
        model_instance = CancerPredictionModel()
        model_instance.model = joblib.load(filepath)
        model_instance.is_trained = True
        print(f"Model loaded from {filepath}")
        return model_instance


def main():
    """
    Main function to train and save the model
    """
    # Preprocess data
    print("=" * 50)
    print("CANCER PREDICTION MODEL TRAINING")
    print("=" * 50)
    
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.preprocess()
    
    # Train model
    print("\n" + "=" * 50)
    model = CancerPredictionModel(n_estimators=100, random_state=42)
    model.train(X_train, y_train)
    
    # Save model
    print("\n" + "=" * 50)
    model.save_model()
    
    print("\n" + "=" * 50)
    print("TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    main()
