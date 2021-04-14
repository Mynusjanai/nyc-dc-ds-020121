
# Phase 4 Code Challenge Review: PCA and NLP


```python
from src.student_caller import one_random_student
from src.student_list import quanggang 
```

TOC:

  - [PCA](#pca)
  - [NLP](#nlp)


<a id='pca'></a>

# PCA

When creating principle components, PCA aims to find a vector in the direction of our feature space that is fit to what?

> Your answer here


```python
one_random_student(quanggang)
```

    Christos


How is the 1st principle component related to the 2nd?

> Your answer here


```python
one_random_student(quanggang)
```

    Christos


What are some reasons for using PCA?


> Your answer here


```python
one_random_student(quanggang)
```

    Christos


> Your answer here


```python
one_random_student(quanggang)
```

    Christos


> Your answer here


```python
one_random_student(quanggang)
```

    Christos


> Your answer here


```python
one_random_student(quanggang)
```

    Christos


How can one determine how many principle components to use in a model?

> Your answer here


```python
one_random_student(quanggang)
```

    Christos



```python
# Now let's implement PCA in code.
```


```python
driver = one_random_student(quanggang)
```

    Christos



```python
import pandas as pd
from sklearn.datasets import  load_breast_cancer
data = load_breast_cancer()
X = pd.DataFrame(data['data'], columns = data['feature_names'])
X.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean radius</th>
      <th>mean texture</th>
      <th>mean perimeter</th>
      <th>mean area</th>
      <th>mean smoothness</th>
      <th>mean compactness</th>
      <th>mean concavity</th>
      <th>mean concave points</th>
      <th>mean symmetry</th>
      <th>mean fractal dimension</th>
      <th>...</th>
      <th>worst radius</th>
      <th>worst texture</th>
      <th>worst perimeter</th>
      <th>worst area</th>
      <th>worst smoothness</th>
      <th>worst compactness</th>
      <th>worst concavity</th>
      <th>worst concave points</th>
      <th>worst symmetry</th>
      <th>worst fractal dimension</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17.99</td>
      <td>10.38</td>
      <td>122.80</td>
      <td>1001.0</td>
      <td>0.11840</td>
      <td>0.27760</td>
      <td>0.3001</td>
      <td>0.14710</td>
      <td>0.2419</td>
      <td>0.07871</td>
      <td>...</td>
      <td>25.38</td>
      <td>17.33</td>
      <td>184.60</td>
      <td>2019.0</td>
      <td>0.1622</td>
      <td>0.6656</td>
      <td>0.7119</td>
      <td>0.2654</td>
      <td>0.4601</td>
      <td>0.11890</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20.57</td>
      <td>17.77</td>
      <td>132.90</td>
      <td>1326.0</td>
      <td>0.08474</td>
      <td>0.07864</td>
      <td>0.0869</td>
      <td>0.07017</td>
      <td>0.1812</td>
      <td>0.05667</td>
      <td>...</td>
      <td>24.99</td>
      <td>23.41</td>
      <td>158.80</td>
      <td>1956.0</td>
      <td>0.1238</td>
      <td>0.1866</td>
      <td>0.2416</td>
      <td>0.1860</td>
      <td>0.2750</td>
      <td>0.08902</td>
    </tr>
    <tr>
      <th>2</th>
      <td>19.69</td>
      <td>21.25</td>
      <td>130.00</td>
      <td>1203.0</td>
      <td>0.10960</td>
      <td>0.15990</td>
      <td>0.1974</td>
      <td>0.12790</td>
      <td>0.2069</td>
      <td>0.05999</td>
      <td>...</td>
      <td>23.57</td>
      <td>25.53</td>
      <td>152.50</td>
      <td>1709.0</td>
      <td>0.1444</td>
      <td>0.4245</td>
      <td>0.4504</td>
      <td>0.2430</td>
      <td>0.3613</td>
      <td>0.08758</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11.42</td>
      <td>20.38</td>
      <td>77.58</td>
      <td>386.1</td>
      <td>0.14250</td>
      <td>0.28390</td>
      <td>0.2414</td>
      <td>0.10520</td>
      <td>0.2597</td>
      <td>0.09744</td>
      <td>...</td>
      <td>14.91</td>
      <td>26.50</td>
      <td>98.87</td>
      <td>567.7</td>
      <td>0.2098</td>
      <td>0.8663</td>
      <td>0.6869</td>
      <td>0.2575</td>
      <td>0.6638</td>
      <td>0.17300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20.29</td>
      <td>14.34</td>
      <td>135.10</td>
      <td>1297.0</td>
      <td>0.10030</td>
      <td>0.13280</td>
      <td>0.1980</td>
      <td>0.10430</td>
      <td>0.1809</td>
      <td>0.05883</td>
      <td>...</td>
      <td>22.54</td>
      <td>16.67</td>
      <td>152.20</td>
      <td>1575.0</td>
      <td>0.1374</td>
      <td>0.2050</td>
      <td>0.4000</td>
      <td>0.1625</td>
      <td>0.2364</td>
      <td>0.07678</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
# This code instruction is intentionally sparse. As a group, walk through the steps of fitting a PCA object. 
# Start with just one principle component, and discuss as a group whether reducing our data
# to 1 principle component would be advisable to feed into an algorithm. 
# Perform model all model building steps as you usually would.
# Experiment with different parameters, and inspect important attributes of the object after fitting.


```

<a id='nlp'></a>


# NLP

For NLP data, what is the entire data of records called?

> your answer here


```python
one_random_student(quanggang)
```

    Christos


What is an individual record called?

> your answer here


```python
one_random_student(quanggang)
```

    Christos


What is a group of two words that appear next to one-another in a document?

> Your answer here

What is a high frequency, semantically low value word called? 

> Your answer here


```python
one_random_student(quanggang)
```

    Christos


List the preprocessing steps we can employ to create a cleaner feature set to our models.

> Your answer here


```python
one_random_student(quanggang)
```

    Christos


What sklearn tools do we have at our disposal to turn our raw text into numerical representations?

> Your Answer here

Explain the difference between the two main vectorizors we employ to transform the data into the document-term matrix.

> Your answer here


```python
one_random_student(quanggang)
```

    Christos


What form do the two main vectorizors expect our data to be fed to them?

> Your answer here

Now let's write some code.


```python
# As a group, preprocess the data using an appropriate cross-validation strategy. 
# Test out different parameters in the vectorizer of choice
# Select a model and score it on the test set.
# If we have time.  Look at the frequency distributions of the words for a specific candidate.
```


```python
driver = one_random_student(quanggang)
```

    Rachel



```python
policies = pd.read_csv('data/2020_policies_feb_24.csv')
policies.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>name</th>
      <th>policy</th>
      <th>candidate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>100% Clean Energy for America</td>
      <td>As published on Medium on September 3rd, 2019:...</td>
      <td>warren</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>A Comprehensive Agenda to Boost America’s Smal...</td>
      <td>Small businesses are the heart of our economy....</td>
      <td>warren</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>A Fair and Welcoming Immigration System</td>
      <td>As published on Medium on July 11th, 2019:\nIm...</td>
      <td>warren</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A Fair Workweek for America’s Part-Time Workers</td>
      <td>Working families all across the country are ge...</td>
      <td>warren</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>A Great Public School Education for Every Student</td>
      <td>I attended public school growing up in Oklahom...</td>
      <td>warren</td>
    </tr>
  </tbody>
</table>
</div>


