<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 4 - Multi-Classification of Stroke, Mild Stroke and No Stroke

> Authors: Suen Si Min, Lee Hongwei, Irfan Muzafar (Group 5)
---

## Overview

Firstly, our model tries to classify people into two groups: Stroke and No Stroke. Afterwhich, clustering is applied to those that were wrongly classified by the model. We aim to get three clusters: Stroke, Mild Stroke and No Stroke. By leveraging machine learning algorithms on data collected from Kaggle, our classifier and clustering seek to better capture mild stroke cases, which are difficult to detect as mild strokes are often over very quickly. Recognizing and treating mild strokes can lower the risk of a major stroke.

## Problem Statement

How might we help patients confidently assess if they experienced a mild stroke, using a precise and sensitive classification model?

## Python Version and Libraries

- Python 3.8 or above
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- Plotly Express
- Numpy
- Scipy
- Itertools

## Data Dictionary

Dataset obtained from [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset).

| No. | Column | Description       |
|-----|------------------------------------------|--------------------------------------------------------|
| 1   | Diabetes_012 | 0 is no diabetes, 1 is prediabetes, 2 is diabetes                       
| 2   | HighBP | 1 if surveyee has high blood pressure, else 0             
| 3   | HighChol | 1 if surveyee has high cholesterol, else 0              
| 4   | CholCheck | 1 if surveyee has done cholesterol check in last 5 years, else 0
| 5   | BMI | surveyee's body mass index                                    
| 6   | Smoker | 1 if surveyee smoked at least 100 cigarettes in entire life, else 0
| 7   | Stroke | 1 if surveyee ever had a stroke, else 0
| 8   | HeartDiseaseorAttack  | 1 if surveyee had coronary heart disease or myocardinal infarction, else 0
| 9   | PhysActivity  | 1 if surveyee did physical activity in past 30days, else 0
| 10  | Fruits | 1 if surveyee consume fruit one or more times per day, else 0
| 11  | Veggies | 1 if surveyee consume vegetables one or more times per day, else 0
| 12  | HvyAlcoholConsump | - for men: 1 if he had more than 14 drinks per week <br>- for women: 1 if she had more than 7 drinks per week, else 0
| 13  | AnyHealthcare | 1 if surveyee has any healthcare coverage, else 0
| 14  | NoDocbcCost  | 1 if for past 12 months, surveyee needed to see doctor but couldnt because of cost, else 0
| 15  | GenHlth | what surveyee thinks his/her general health is, scale 1-5, 5 is poor and 1 is excellent
| 16  | MentHlth | for how many days out of the last 30 days surveyee faces problems with mental health, which includes stress, depression, and problems with emotions  
| 17  | PhysHlth | for how many days out of the last 30 days surveyee faces problems with physical health, which includes physical illness and injury
| 18  | DiffWalk | 1 if surveyee has difficulty walking or climbing stairs, else 0
| 19  | Sex  | 1 is male, 0 is female
| 20  | Age | 13-level age category <br>- 1: 18-24 <br>- 2: 25-29 <br>- 3: 31-34 <br>- 4: 35-39 <br>- 5: 40-44 <br>- 6: 45-49 <br>- 7: 50-54 <br>- 8: 55-59 <br>- 9: 60-64 <br>- 10: 65-69 <br>- 11: 70-74 <br>- 12: 75-79 <br>- 13: 80 or older
| 21  | Education | Highest grade of school completed <br>- 1: never attended school or only kindergarten <br>- 2: grades 1 to 8 (elementary) <br>- 3: grades 9 to 11 (high school) <br>- 4: grade 12 or GED (high school graduate) <br>- 5: college 1 year to 3 years <br>- 6: college 4 years or more
| 22  | Income | Annual household income (USD) <br>- 1: Less than $10,000 <br>- 2: $10,000 to less than $15,000 <br>- 3: $15,000 to less than $20,000 <br>- 4: $20,000 to less than $25,000 <br>- 5: $25,000 to less than $35,000 <br>- 6: $35,000 to less than $50,000 <br>- 7: $50,000 to less than $75,000 <br>- 8: $75,000 or more

## Data Collection, Cleaning and EDA

This project uses the Pandas library to read the CSV file `diabetes_012_health_indicators_BRFSS2015`. The data collected is then processed to remove some columns, ensuring that only meaningful data is used for classification. Various histograms, bar charts and boxplots were plotted.

## Modelling

During the project's exploratory phase, six classification models (Decision Tree, Bagging, Random Forest, AdaBoost, Support Vector and GradientBoost) were tested with the use of Pipeline. Then, three of those models were hypertuned using GridSearchCV for optimization.

## Model Training and Result

The model was trained using a labeled dataset, with the data split into training and testing subsets.

**<span style="color:blue">Before Hypertuning</span> (Baseline Models)**
|   | **Classifier Model**      | **Train CV F1** | **Test CV F1** |
|---|---------------------------|--------------|-------------|
| 1 | Random Forest | 0.753842    | 0.760998    |
| 2 | Support Vector | 0.755588     | 0.765905    |
| 3 | Gradient Boost | 0.761466    | 0.767612    |

<br>

**<span style="color:blue">After Hypertuning</span>**
|   | **Classifier Model**              | **Train CV F1** | **Test CV F1** |
|---|-----------------------------------|--------------|-------------|
| 1 | Random Forest (Tuned)  | 0.763569| 0.769894|
| 2 | Support Vector (Tuned) | 0.764362| 0.764184|
| 3 | Gradient Boost (Tuned) | 0.766811| 0.768999|

**F1-Score** was selected as the primary metric for evaluation as we aim for a balance between precision and sensitivity.

We want to ensure all data in both train and test sets are accounted for in our prediction and in our F1 score, because for all the data which were wrongly classified, we want to reclassify them in the later part of our analysis.
Hence, with our best model, we want to now predict the labels across the full dataset.

|   | **Model**              | **Full Dataset F1** 
|---|-----------------------------------|--------------|
| 1 | Random Forest (Tuned)  | 0.765165|
| 3 | Gradient Boost (Tuned) | 0.767361|

## Model Selection  

The best performance was achieved using GradientBoost since we are selecting model with the highest F1-Score across the full dataset. Based on the above, the full dataset F1-Score for Gradient Boost is 0.767, performing marginally better than Random Forest. 

## Classification
After training and optimising our classification model, we ran a prediction across the full dataset to capture:

- **True Positives: 7421 data points**<br>
    - Correctly classified to have experienced stroke

- **False Negatives: 2808 data points**<br>
    - Wrongly classified

- **False Positives: 2113 data points**<br>
    - Wrongly classified

- **True Negatives: 8116 data points**<br>
    - Correctly classified to not have experienced stroke

We hypothesise that within this context, a wrong classification could have happened for two reasons:
1. Model predicted wrongly due to random error: Actual values are accurate
2. Model predicted wrongly due to a third class: Actual values are inaccurate

With this, we proceed to the next step of unsupervised learning to identify 3 clusters.

## Clustering
We performed unsupervised learning on the wrongly classified datapoints using three clustering algorithms:
* KMeans: silhouette score at 0.142581
* Hierarchical clustering: silhouette score at 0.111030
* DBScan: silhouette score at 0.267901, 

We also evaluated the cluster balance across the three algorithms and eliminated DBScan as it formed a cluster that represented more than 95% of the data.

As the silhouette scores for the other two clustering algorithms were very low, we executed a few methods to attempt an improvement in the clustering:
1. Reducing Dimensionality - Principal Component Analysis
2. Reducing Dimensionality - Used only 5 features for clustering
3. Evaluate other n_cluster values - No improvement on silhouette score

All the above methods did not amount to a significant improvement.

## Limitations & Recommendations
Limitations:
- Too many binary features limit the performance of clustering algorithms.
- The data in our dataset were collected via tele-surveys. No measurements like cholesterol levels.
- Deeper analysis can't be done on stroke/TIA patients without images.

Recommendations:
- Collect continuous data.
- Have continuous data on current categorical features (e.g. income, age, education).
- Collect data in clinics in the presence of medical professionals.
- Image Recognition can be done on stroke/TIA patients such as CT scans and carotid ultrasound scans.

## Cost-Benefit Analysis

While we were not able to create a model that helps to predict the likelihood of TIA, we believe that if we are able to overcome the limitations mentioned earlier, we will be able to create a model that meets our objective.

In our project, we explored the potential costs and benefits at country level and individual level.

## Conclusion


We conducted Data Preprocessing and Analysis, Classification Modelling and Clustering with the aim of creating a Multi-Class Predictor.

Despite the limitations above that eventually posed as a barrier to reach our goal, we believe that there is still value in creating a precise and sensitive multi-class predictor to identify mild stroke as a means to prevent future strokes. The benefits majorly outweighs the cost, both for our citizens and our country as a whole.

---