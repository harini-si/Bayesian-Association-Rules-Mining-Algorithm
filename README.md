# fds-assignment

This repository contains the code for our FDS assignment on Bayesian Association Rules Mining Algorithm.

**Title:** A Bayesian Association Rule Mining Algorithm (2013 IEEE International Conference on Systems, Man, and Cybernetics)[[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6722308).

We would be using the Breast cancer dataset for demonstration purposes,[link](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer)
### Instructions to run the code
The requirements are listed in the requirements.txt file. To install the requirements, run the following command:

```pip install -r requirements.txt```

The dataset is in the data folder,to preprocess the data, run the following command:

```python preprocess.py```

```bash convert.sh```

To run the BAR algorithm, run the following command:

```python bar.py```

To display the association rules and class association rules, run the following command:

```python main.py```

The file bar.py generates association rules along with their support,confidence,bayesian confidence and lift values. The file apriori.py takes 2 arguments as input, the minimuim support value and the minimuim confidence value for the apriori algorithm. 



### Dataset information 
Number of Instances: 286

Number of Attributes: 9 + the class attribute

Attribute Information:
   1. Class:no-recurrence-events, recurrence-events
   2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.
   3. menopause: lt40, ge40, premeno.
   4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44,
                  45-49, 50-54, 55-59.
   5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26,
                 27-29, 30-32, 33-35, 36-39.
   6. node-caps: yes, no.
   7. deg-malig: 1, 2, 3.
   8. breast: left, right.
   9. breast-quad: left-up, left-low, right-up,	right-low, central.
  10. irradiat:yes, no.

Missing Attribute Values: (denoted by "?")
   Attribute #:  Number of instances with missing values:
   
   Atrribute 6: 8
   
   Attribute 9: 1

Class Distribution:
    1. no-recurrence-events: 201 instances
    2. recurrence-events: 85 instances
