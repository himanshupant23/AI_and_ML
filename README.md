# AI and ML Learning Repository

A comprehensive learning repository containing hands-on tutorials and projects for mastering core Python data science and machine learning libraries. This repository covers essential tools used in data analysis, visualization, and machine learning workflows through practical Jupyter Notebook examples.

## Repository Structure

```
AI_and_ML/
├── Numpy/
│   ├── numpy.ipynb
│   ├── numpy2.ipynb
│   └── numpy3.ipynb
│
├── Pandas/
│   ├── pandas.ipynb
│   ├── pandas2.ipynb
│   ├── pandas4.ipynb
│   ├── pandas5.ipynb
│   └── pandas6.ipynb
│
├── matplotlib/
│   └── matplotlib.ipynb
│
└── Machine Learning/
    ├── Data Cleaning/
    │   ├── Customer_Call_list.ipynb
    │   ├── insurance.ipynb
    │   └── Customer Call List (1).xlsx
    │
    ├── EDA/
    │   └── insurance.ipynb
    │
    └── Feature Engineering and Scaling/
        └── insurance.ipynb
```

## Modules Overview

### 1. NumPy
Learn the fundamentals of numerical computing with NumPy:
- Array creation and manipulation
- Mathematical operations
- Broadcasting and advanced indexing
- Linear algebra operations

**Files:**
- `numpy.ipynb` - Core NumPy concepts
- `numpy2.ipynb` - Advanced operations
- `numpy3.ipynb` - NumPy applications

### 2. Pandas
Master data manipulation and analysis:
- DataFrame and Series operations
- Data loading and cleaning
- Data merging and joining
- Grouping and aggregation
- Time series handling

**Files:**
- `pandas.ipynb` - DataFrame basics
- `pandas2.ipynb` - Data joining
- `pandas4.ipynb` - Advanced manipulation
- `pandas5.ipynb` - Aggregation techniques
- `pandas6.ipynb` - Time series and indexing

### 3. Matplotlib
Create professional data visualizations:
- Basic plotting
- Subplots and layouts
- Customization and styling
- Advanced visualization techniques

**Files:**
- `matplotlib.ipynb` - Complete visualization guide

### 4. Machine Learning Pipeline

#### Data Cleaning
Real-world data cleaning techniques:
- Handling missing values
- Removing duplicates
- Data validation
- Outlier detection

**Datasets:**
- Customer Call List dataset
- Insurance dataset

#### EDA (Exploratory Data Analysis)
Understand your data through statistical analysis:
- Distribution analysis
- Correlation analysis
- Feature relationships
- Statistical summaries

#### Feature Engineering and Scaling
Prepare data for machine learning models:
- Feature scaling and normalization
- Feature transformation
- Feature selection
- Data preprocessing pipelines

## Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/himanshupant23/AI_and_ML.git
cd AI_and_ML
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install required packages:
```bash
pip install numpy pandas matplotlib jupyter
```

4. Launch Jupyter Notebook:
```bash
jupyter notebook
```

5. Open any notebook and start learning!

## Recommended Learning Path

### For Beginners:
1. Start with `Numpy/numpy.ipynb` to learn array fundamentals
2. Move to `Pandas/pandas.ipynb` for data manipulation basics
3. Explore `matplotlib/matplotlib.ipynb` for visualization
4. Practice with Machine Learning projects

### For Intermediate Users:
1. Review advanced NumPy concepts in `numpy2.ipynb` and `numpy3.ipynb`
2. Work through intermediate Pandas notebooks
3. Complete the full Machine Learning pipeline project
4. Experiment with different visualizations

### For Advanced Users:
1. Deep dive into time series analysis with `pandas6.ipynb`
2. Master feature engineering with the ML pipeline
3. Combine all skills for end-to-end projects
4. Extend and customize examples for your own projects

## Quick Examples

### NumPy - Array Operations
```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])

# Mathematical operations
result = arr * 2
print(result)  # [2 4 6 8 10]
```

### Pandas - Data Loading and Exploration
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Quick exploration
print(df.head())
print(df.info())
print(df.describe())
```

### Matplotlib - Simple Plot
```python
import matplotlib.pyplot as plt

# Create a simple plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Plot')
plt.show()
```

## Key Concepts Covered

- NumPy: Arrays, broadcasting, linear algebra
- Pandas: DataFrames, merging, grouping, time series
- Matplotlib: Line plots, scatter plots, histograms, custom styling
- Machine Learning: Data cleaning, EDA, feature engineering, scaling

## Datasets Used

- Insurance Dataset: For practicing data cleaning, EDA, and feature engineering
- Customer Call List: For real-world data cleaning scenarios

## Tips for Learning

- Run each cell in the notebooks one by one
- Modify the code and experiment
- Read the documentation links provided
- Practice with your own datasets
- Review concepts multiple times if needed

## Resources

- NumPy Documentation: https://numpy.org/doc/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Matplotlib Documentation: https://matplotlib.org/stable/contents.html
- Python Documentation: https://docs.python.org/3/

## Notes

- All notebooks are self-contained and can be run independently
- Data files are included in their respective directories
- Ensure you have all required packages installed before running notebooks
- Some notebooks may take time to execute due to large computations

## Project Structure Benefits

- Modular organization makes it easy to focus on specific topics
- Real datasets provide practical learning experience
- Complete ML pipeline shows how libraries work together
- Progressive difficulty allows learning at your own pace

## Contributing

Feel free to fork this repository and add your own examples or improvements!

## License

This repository is open source and available for educational purposes.

## Author

Himanshu Pant - [GitHub](https://github.com/himanshupant23)

---

Last Updated: July 2026

Happy Learning!
