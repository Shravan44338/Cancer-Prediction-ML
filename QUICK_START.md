# Cancer Prediction ML - Quick Start Guide

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Complete Pipeline
```bash
cd src
python model_evaluation.py
```

This will:
- ✅ Load and preprocess the data
- ✅ Train the Random Forest model
- ✅ Evaluate performance
- ✅ Generate confusion matrix
- ✅ Save results

## 📊 Expected Output

```
==================================================
CANCER PREDICTION MODEL EVALUATION
==================================================

Loading dataset...
Dataset loaded successfully. Shape: (569, 33)

Cleaning dataset...
Removed columns: ['id', 'Unnamed: 32']

Encoding labels...
Labels encoded successfully

Splitting dataset...
Training set size: 455
Testing set size: 114

Scaling features...
Features scaled successfully

Preprocessing completed successfully!

==================================================
Training Random Forest Classifier...
Model trained successfully!

==================================================
Evaluating model...

Model Accuracy: 0.9649 (96.49%)

==================================================
CLASSIFICATION REPORT
==================================================
              precision    recall  f1-score   support

      Benign       0.96      0.99      0.97        71
   Malignant       0.98      0.93      0.95        43

    accuracy                           0.96       114
   macro avg       0.97      0.96      0.96       114
weighted avg       0.97      0.96      0.96       114
```

## 📁 Project Structure After Setup

```
cancer-prediction-ml/
├── data/
│   └── README.md
├── docs/
│   └── methodology.md
├── models/
│   └── cancer_prediction_model.pkl  (created after training)
├── notebooks/
│   ├── Project_Cancer_Prediction.ipynb
│   └── README.md
├── results/
│   └── confusion_matrix.png  (created after evaluation)
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── model_evaluation.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── QUICK_START.md  (this file)
```

## 🎯 Common Tasks

### Run Jupyter Notebook
```bash
jupyter notebook notebooks/Project_Cancer_Prediction.ipynb
```

### Train Model Only
```bash
cd src
python model_training.py
```

### Evaluate Existing Model
```bash
cd src
python model_evaluation.py
```

### Run Individual Components
```python
# In Python interpreter or script
from src.data_preprocessing import DataPreprocessor
from src.model_training import CancerPredictionModel

# Preprocess data
preprocessor = DataPreprocessor()
X_train, X_test, y_train, y_test = preprocessor.preprocess()

# Train model
model = CancerPredictionModel()
model.train(X_train, y_train)
model.save_model()
```

## 🔧 Troubleshooting

### Issue: Module not found
**Solution**: Make sure you're in the correct directory
```bash
cd "d:\Internship Project"
pip install -r requirements.txt
```

### Issue: Import errors in src/
**Solution**: Run from project root or add to PYTHONPATH
```bash
# Windows
set PYTHONPATH=%PYTHONPATH%;d:\Internship Project

# Or run from src directory
cd src
python model_evaluation.py
```

### Issue: Jupyter kernel not found
**Solution**: Install ipykernel
```bash
pip install ipykernel
python -m ipykernel install --user
```

## 📝 Next Steps

1. ✅ Review the comprehensive [README.md](README.md)
2. ✅ Read the [methodology documentation](docs/methodology.md)
3. ✅ Explore the [Jupyter notebook](notebooks/Project_Cancer_Prediction.ipynb)
4. ✅ Check the [dataset information](data/README.md)

## 🎓 For Your Internship Presentation

### Key Highlights to Mention:
1. **96.49% Accuracy** - High performance model
2. **Low False Negatives** - Only 3 malignant cases misclassified
3. **Reproducible** - Fixed random seed, documented process
4. **Production-Ready** - Modular code, proper structure
5. **Well-Documented** - README, methodology, code comments

### Demonstration Flow:
1. Show the project structure
2. Run the evaluation script
3. Display the confusion matrix
4. Explain the metrics
5. Discuss real-world applications

## 📧 Support

If you encounter any issues:
1. Check the main [README.md](README.md)
2. Review [methodology.md](docs/methodology.md)
3. Check Python version (3.8+)
4. Verify all dependencies are installed

---

**Good luck with your internship presentation! 🎉**
