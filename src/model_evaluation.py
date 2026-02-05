"""
Model Evaluation Module
Handles model evaluation, metrics calculation, and visualization
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from data_preprocessing import DataPreprocessor
from model_training import CancerPredictionModel


class ModelEvaluator:
    """
    Class for evaluating cancer prediction model
    """
    
    def __init__(self, model):
        """
        Initialize the evaluator
        
        Args:
            model: Trained model instance
        """
        self.model = model
        self.predictions = None
        self.accuracy = None
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on test data
        
        Args:
            X_test: Test features
            y_test: True test labels
        """
        print("Evaluating model...")
        
        # Make predictions
        self.predictions = self.model.predict(X_test)
        
        # Calculate accuracy
        self.accuracy = accuracy_score(y_test, self.predictions)
        
        print(f"\nModel Accuracy: {self.accuracy:.4f} ({self.accuracy*100:.2f}%)")
    
    def print_classification_report(self, y_test):
        """
        Print detailed classification report
        
        Args:
            y_test: True test labels
        """
        print("\n" + "=" * 50)
        print("CLASSIFICATION REPORT")
        print("=" * 50)
        print(classification_report(y_test, self.predictions, 
                                   target_names=['Benign', 'Malignant']))
    
    def plot_confusion_matrix(self, y_test, save_path=None):
        """
        Plot and optionally save confusion matrix
        
        Args:
            y_test: True test labels
            save_path (str): Path to save the plot (optional)
        """
        # Calculate confusion matrix
        cm = confusion_matrix(y_test, self.predictions)
        
        # Create plot
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                   xticklabels=['Benign', 'Malignant'],
                   yticklabels=['Benign', 'Malignant'])
        plt.xlabel("Predicted Class", fontsize=12)
        plt.ylabel("Actual Class", fontsize=12)
        plt.title("Confusion Matrix - Cancer Prediction", fontsize=14, fontweight='bold')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"\nConfusion matrix saved to {save_path}")
        
        plt.show()
    
    def print_detailed_metrics(self, y_test):
        """
        Print detailed performance metrics
        
        Args:
            y_test: True test labels
        """
        cm = confusion_matrix(y_test, self.predictions)
        
        # Extract values from confusion matrix
        tn, fp, fn, tp = cm.ravel()
        
        # Calculate metrics
        sensitivity = tp / (tp + fn)  # Recall for malignant
        specificity = tn / (tn + fp)  # Recall for benign
        ppv = tp / (tp + fp)  # Precision for malignant
        npv = tn / (tn + fn)  # Precision for benign
        
        print("\n" + "=" * 50)
        print("DETAILED METRICS")
        print("=" * 50)
        print(f"True Negatives (Benign correctly classified):  {tn}")
        print(f"False Positives (Benign misclassified):        {fp}")
        print(f"False Negatives (Malignant misclassified):     {fn}")
        print(f"True Positives (Malignant correctly classified): {tp}")
        print(f"\nSensitivity (Recall for Malignant): {sensitivity:.4f}")
        print(f"Specificity (Recall for Benign):    {specificity:.4f}")
        print(f"Positive Predictive Value:          {ppv:.4f}")
        print(f"Negative Predictive Value:          {npv:.4f}")


def main():
    """
    Main function to evaluate the model
    """
    print("=" * 50)
    print("CANCER PREDICTION MODEL EVALUATION")
    print("=" * 50)
    
    # Preprocess data
    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.preprocess()
    
    # Train model (or load existing model)
    print("\n" + "=" * 50)
    model = CancerPredictionModel(n_estimators=100, random_state=42)
    model.train(X_train, y_train)
    
    # Evaluate model
    print("\n" + "=" * 50)
    evaluator = ModelEvaluator(model)
    evaluator.evaluate(X_test, y_test)
    
    # Print reports
    evaluator.print_classification_report(y_test)
    evaluator.print_detailed_metrics(y_test)
    
    # Plot confusion matrix
    print("\n" + "=" * 50)
    print("GENERATING CONFUSION MATRIX")
    print("=" * 50)
    evaluator.plot_confusion_matrix(y_test, save_path='../results/confusion_matrix.png')
    
    print("\n" + "=" * 50)
    print("EVALUATION COMPLETED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    main()
