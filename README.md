# Cancer Prediction Using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Project Overview

This project implements a **Machine Learning model for Cancer Prediction** using the Wisconsin Breast Cancer dataset. The model classifies tumors as **Malignant (M)** or **Benign (B)** based on diagnostic measurements derived from tumor imaging.

### 🎯 Objectives

- Build a reliable cancer prediction model using Random Forest Classifier
- Achieve high accuracy and reproducible results
- Maintain clean, well-documented code
- Demonstrate practical application of ML in healthcare

## 🔬 Dataset Description

The dataset contains medical diagnostic measurements from tumor imaging:
- **569 patient records**
- **30 features** (mean, standard error, and worst values of 10 measurements)
- **Target variable**: Diagnosis (M = Malignant, B = Benign)
- **Source**: [Wisconsin Breast Cancer Dataset](https://github.com/YBIFoundation/Dataset/raw/main/Cancer.csv)

### Features Include:
- Radius, Texture, Perimeter, Area
- Smoothness, Compactness, Concavity
- Concave points, Symmetry, Fractal dimension

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shravan44338/Cancer-Prediction-ML.git
cd Cancer-Prediction-ML
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
cancer-prediction-ml/
│
├── data/                          # Dataset directory
│   └── README.md                  # Data description
│
├── notebooks/                     # Jupyter notebooks
│   └── Project_Cancer_Prediction.ipynb
│
├── src/                           # Source code
│   ├── __init__.py
│   ├── data_preprocessing.py      # Data loading and preprocessing
│   ├── model_training.py          # Model training
│   └── model_evaluation.py        # Model evaluation and metrics
│
├── models/                        # Saved models
│   └── .gitkeep
│
├── results/                       # Results and visualizations
│   └── .gitkeep
│
├── docs/                          # Documentation
│   └── methodology.md
│
├── .gitignore                     # Git ignore file
├── requirements.txt               # Project dependencies
├── LICENSE                        # License file
└── README.md                      # This file
```

## 🔧 Usage

### Running the Jupyter Notebook

```bash
jupyter notebook notebooks/Project_Cancer_Prediction.ipynb
```

### Running Python Scripts

```bash
# Train the model
python src/model_training.py

# Evaluate the model
python src/model_evaluation.py
```

## 📊 Model Performance

The Random Forest Classifier achieved the following results:

| Metric | Score |
|--------|-------|
| **Accuracy** | 96.49% |
| **Precision (Benign)** | 96% |
| **Precision (Malignant)** | 98% |
| **Recall (Benign)** | 99% |
| **Recall (Malignant)** | 93% |
| **F1-Score** | 96% |

### Confusion Matrix

```
                Predicted
              Benign  Malignant
Actual Benign    70       1
     Malignant    3      40
```

## 🛠️ Methodology

### 1. Data Preprocessing
- Removed identifier columns (ID, Unnamed columns)
- Encoded diagnosis labels (M → 1, B → 0)
- Split data into training (80%) and testing (20%) sets
- Applied StandardScaler for feature normalization

### 2. Model Selection
**Random Forest Classifier** was chosen because:
- High accuracy on classification tasks
- Handles complex feature interactions
- Resistant to overfitting through ensemble learning
- Provides feature importance insights

### 3. Model Configuration
```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

### 4. Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-Score)

## 📈 Key Findings

1. **High Accuracy**: The model achieves 96.49% accuracy on unseen data
2. **Balanced Performance**: Both benign and malignant cases are classified with high precision
3. **Clinical Relevance**: Low false negative rate (3 cases) is crucial for cancer detection
4. **Reproducibility**: Fixed random seed ensures consistent results

## 🔮 Future Improvements

- [ ] Implement cross-validation for robust evaluation
- [ ] Experiment with other algorithms (SVM, XGBoost, Neural Networks)
- [ ] Perform hyperparameter tuning using GridSearchCV
- [ ] Add feature importance analysis
- [ ] Create a web interface for predictions
- [ ] Deploy model as REST API

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shravan Niranjan Ajetrao**
- GitHub: [@Shravan44338](https://github.com/Shravan44338)
- Email: sna443388@gmail.com

## 🙏 Acknowledgments

- Dataset provided by [YBI Foundation](https://github.com/YBIFoundation/Dataset)
- Wisconsin Breast Cancer Dataset (Original)
- scikit-learn documentation and community

## 📚 References

1. Wolberg, W.H., Street, W.N., & Mangasarian, O.L. (1995). Breast Cancer Wisconsin (Diagnostic) Data Set.
2. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.
3. scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐
