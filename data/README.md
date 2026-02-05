# Dataset Information

## Wisconsin Breast Cancer Dataset

### Overview
This dataset contains diagnostic measurements from breast mass imaging used to predict whether a tumor is malignant or benign.

### Source
- **Original Source**: UCI Machine Learning Repository
- **Current Source**: [YBI Foundation GitHub](https://github.com/YBIFoundation/Dataset/raw/main/Cancer.csv)
- **License**: Public Domain

### Dataset Statistics
- **Total Samples**: 569
- **Features**: 30 numerical features + 1 ID column
- **Target Variable**: Diagnosis (M = Malignant, B = Benign)
- **Class Distribution**:
  - Malignant: 212 (37.3%)
  - Benign: 357 (62.7%)

### Features Description

The features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

#### Feature Groups

Each group contains 10 measurements:

1. **Mean Values** (columns 3-12)
2. **Standard Error** (columns 13-22)
3. **Worst/Largest Values** (columns 23-32)

#### 10 Measurements

For each cell nucleus, the following characteristics are measured:

| Feature | Description |
|---------|-------------|
| **radius** | Mean of distances from center to points on the perimeter |
| **texture** | Standard deviation of gray-scale values |
| **perimeter** | Perimeter of the nucleus |
| **area** | Area of the nucleus |
| **smoothness** | Local variation in radius lengths |
| **compactness** | perimeter² / area - 1.0 |
| **concavity** | Severity of concave portions of the contour |
| **concave points** | Number of concave portions of the contour |
| **symmetry** | Symmetry of the nucleus |
| **fractal dimension** | "Coastline approximation" - 1 |

### Column Names

```
1. id
2. diagnosis (M = malignant, B = benign)

Mean values (3-12):
3. radius_mean
4. texture_mean
5. perimeter_mean
6. area_mean
7. smoothness_mean
8. compactness_mean
9. concavity_mean
10. concave points_mean
11. symmetry_mean
12. fractal_dimension_mean

Standard Error (13-22):
13. radius_se
14. texture_se
15. perimeter_se
16. area_se
17. smoothness_se
18. compactness_se
19. concavity_se
20. concave points_se
21. symmetry_se
22. fractal_dimension_se

Worst values (23-32):
23. radius_worst
24. texture_worst
25. perimeter_worst
26. area_worst
27. smoothness_worst
28. compactness_worst
29. concavity_worst
30. concave points_worst
31. symmetry_worst
32. fractal_dimension_worst
```

### Data Quality

- **Missing Values**: None (except Unnamed: 32 column which is empty)
- **Duplicates**: None
- **Outliers**: Present but valid (medical measurements)

### Usage

The dataset is automatically downloaded when running the preprocessing script:

```python
from src.data_preprocessing import DataPreprocessor

preprocessor = DataPreprocessor()
preprocessor.load_data()
```

### Citation

If you use this dataset, please cite:

```
Wolberg, W.H., Street, W.N., & Mangasarian, O.L. (1995). 
Breast Cancer Wisconsin (Diagnostic) Data Set. 
UCI Machine Learning Repository.
```

### References

1. W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction for breast tumor diagnosis. IS&T/SPIE 1993 International Symposium on Electronic Imaging: Science and Technology, volume 1905, pages 861-870, San Jose, CA, 1993.

2. O.L. Mangasarian, W.N. Street and W.H. Wolberg. Breast cancer diagnosis and prognosis via linear programming. Operations Research, 43(4), pages 570-577, July-August 1995.

---

**Note**: This dataset is for educational and research purposes only. It should not be used for actual medical diagnosis without proper validation and regulatory approval.
