
# Bayesian Association Rules Mining Algorithm

This repository contains the code for our FDS assignment on the Bayesian Association Rules Mining Algorithm.

**Title:** [A Bayesian Association Rule Mining Algorithm (2013 IEEE International Conference on Systems, Man, and Cybernetics)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6722308)

We will be using the Breast Cancer dataset for demonstration purposes. You can find the dataset [here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer).

### Instructions to Run the Code

The requirements are listed in the `requirements.txt` file. To install the requirements, run the following command:

```bash
pip install -r requirements.txt
```

The dataset is in the `data` folder. To preprocess the data, run the following commands:

```bash
python preprocess.py
bash convert.sh
```

To run the BAR algorithm, use the command:

```bash
python bar.py
```

To display the association rules and class association rules, run:

```bash
python main.py
```

The file `bar.py` generates association rules along with their support, confidence, Bayesian confidence, and lift values. The file `apriori.py` takes two arguments as input: the minimum support value and the minimum confidence value for the Apriori algorithm.

### Dataset Information

- **Number of Instances:** 286
- **Number of Attributes:** 9 + the class attribute

**Attribute Information:**
1. **Class:** no-recurrence-events, recurrence-events
2. **Age:** 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99
3. **Menopause:** lt40, ge40, premeno
4. **Tumor Size:** 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59
5. **Inv-Nodes:** 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26, 27-29, 30-32, 33-35, 36-39
6. **Node Caps:** yes, no
7. **Deg-Malig:** 1, 2, 3
8. **Breast:** left, right
9. **Breast-Quad:** left-up, left-low, right-up, right-low, central
10. **Irradiat:** yes, no

**Missing Attribute Values:**
- **Attribute 6:** 8 instances with missing values
- **Attribute 9:** 1 instance with missing value

**Class Distribution:**
- **No-Recurrence-Events:** 201 instances
- **Recurrence-Events:** 85 instances
