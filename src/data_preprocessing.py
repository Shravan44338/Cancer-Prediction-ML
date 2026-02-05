"""
Data Preprocessing Module
Handles data loading, cleaning, and preparation for model training
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DataPreprocessor:
    """
    Class for preprocessing cancer prediction dataset
    """
    
    def __init__(self, data_url=None):
        """
        Initialize the preprocessor
        
        Args:
            data_url (str): URL or path to the dataset
        """
        self.data_url = data_url or 'https://github.com/YBIFoundation/Dataset/raw/main/Cancer.csv'
        self.dataset = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()
    
    def load_data(self):
        """
        Load the dataset from URL or file
        
        Returns:
            pd.DataFrame: Loaded dataset
        """
        print("Loading dataset...")
        self.dataset = pd.read_csv(self.data_url)
        print(f"Dataset loaded successfully. Shape: {self.dataset.shape}")
        return self.dataset
    
    def clean_data(self):
        """
        Clean the dataset by removing unnecessary columns
        """
        print("Cleaning dataset...")
        
        # Step 1: Identify identifier-related columns
        columns_to_remove = [col for col in self.dataset.columns if "id" in col.lower()]
        
        # Step 2: Remove the 'Unnamed: 32' column if it exists
        if 'Unnamed: 32' in self.dataset.columns:
            columns_to_remove.append('Unnamed: 32')
        
        # Step 3: Drop only columns that are actually present
        existing_columns_to_remove = [col for col in columns_to_remove if col in self.dataset.columns]
        self.dataset.drop(columns=existing_columns_to_remove, inplace=True)
        
        print(f"Removed columns: {existing_columns_to_remove}")
        print(f"Dataset shape after cleaning: {self.dataset.shape}")
    
    def encode_labels(self):
        """
        Encode diagnosis labels: Malignant (M) -> 1, Benign (B) -> 0
        """
        print("Encoding labels...")
        label_encoding = {"M": 1, "B": 0}
        self.dataset["diagnosis"] = self.dataset["diagnosis"].replace(label_encoding)
        print("Labels encoded successfully")
    
    def split_data(self, test_size=0.2, random_state=42):
        """
        Split dataset into training and testing sets
        
        Args:
            test_size (float): Proportion of dataset for testing
            random_state (int): Random seed for reproducibility
        """
        print("Splitting dataset...")
        
        # Separate features and target
        feature_data = self.dataset.drop("diagnosis", axis=1)
        target_data = self.dataset["diagnosis"]
        
        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            feature_data,
            target_data,
            test_size=test_size,
            random_state=random_state
        )
        
        print(f"Training set size: {len(self.X_train)}")
        print(f"Testing set size: {len(self.X_test)}")
    
    def scale_features(self):
        """
        Apply feature scaling using StandardScaler
        """
        print("Scaling features...")
        
        # Fit scaler on training data and transform both sets
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
        print("Features scaled successfully")
    
    def preprocess(self, test_size=0.2, random_state=42):
        """
        Execute complete preprocessing pipeline
        
        Args:
            test_size (float): Proportion of dataset for testing
            random_state (int): Random seed for reproducibility
            
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        self.load_data()
        self.clean_data()
        self.encode_labels()
        self.split_data(test_size, random_state)
        self.scale_features()
        
        print("\nPreprocessing completed successfully!")
        return self.X_train, self.X_test, self.y_train, self.y_test


if __name__ == "__main__":
    # Example usage
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.preprocess()
    
    print(f"\nFinal shapes:")
    print(f"X_train: {X_train.shape}")
    print(f"X_test: {X_test.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"y_test: {y_test.shape}")
