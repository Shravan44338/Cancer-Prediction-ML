# Jupyter Notebooks

This directory contains Jupyter notebooks for interactive exploration and analysis.

## Available Notebooks

### Project_Cancer_Prediction.ipynb
The main notebook containing the complete cancer prediction workflow:
- Data loading and exploration
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Model training
- Model evaluation
- Results visualization

## Running the Notebooks

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Navigate to this directory** and open the desired notebook

3. **Run cells sequentially** using Shift+Enter

## Notebook Structure

The main notebook follows this structure:

1. **Introduction & Objectives**
2. **Import Libraries**
3. **Load Dataset**
4. **Exploratory Data Analysis**
   - Dataset info
   - Statistical summary
   - Missing values check
5. **Data Preprocessing**
   - Remove unnecessary columns
   - Encode labels
   - Split data
   - Feature scaling
6. **Model Training**
   - Random Forest Classifier
7. **Model Evaluation**
   - Accuracy score
   - Confusion matrix
   - Classification report
8. **Results & Conclusions**

## Tips

- Run cells in order to avoid dependency issues
- Clear output before committing: `Cell > All Output > Clear`
- Restart kernel if you encounter issues: `Kernel > Restart`

---

**Note**: The notebook is for interactive exploration. For production use, refer to the Python scripts in the `src/` directory.
