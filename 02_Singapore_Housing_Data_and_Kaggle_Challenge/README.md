# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Project 2 - Singapore Housing Data and Kaggle Challenge
---
### Introduction & Problem Statement

Predicting HDB resale prices is vital for homeowners, buyers, and agents. An app with customizable parameters can offer valuable insights. For instance, the Tan family, with a child and considering upgrading from a 3-room to a 5-room flat, seeks fair market rates. By inputting criteria like flat type, preferred location, floor area, and lease commencement date, they can obtain accurate resale price predictions. This empowers them to make informed decisions, understand market dynamics, and navigate the buying and selling process confidently. Such tools cater to diverse stakeholders and enhance transparency in the housing market, ensuring fair deals for all parties involved.

The problem statement is:
**<center>How might we develop a platform for predicting HDB resale flat prices based on preferences, streamlining price comparison process for sellers and buyers, and attracting users to our platform?</center>**

The primary audience will be the executive members of Propertee Guru, with the app targeting the home buyers and sellers.

---

### Data Dictionary

This dataset contains the data of HDB resale flat transactions from the year 2012 to 2021. Out of the 76 features, we have selected only 27 features.

| No. | Column(s)                                | Description                                                                            |
|-----|------------------------------------------|----------------------------------------------------------------------------------------|
| 1   | flat_type                                | type of the resale flat unit, e.g. 3 ROOM                                              |                   
| 2   | lease_commence_date                      | commencement year of the flat unit's 99-year lease                                     |
| 3   | tranc_year                               | year of resale transaction                                                             | 
| 4   | tranc_month                              | month of resale transaction                                                            |                                   
| 5   | mid_storey                               | median value of storey_range                                                           |       
| 6   | floor_area_sqft                          | floor area of the resale flat unit in square features                                  |
| 7   | commercial                               | boolean value if resale flat has commercial units in the same block                    |                   
| 8   | market_hawker                            | boolean value if resale flat has a market or hawker centre in the same block           |
| 9   | multistorey_carpark                      | boolean value if resale flat has a multistorey carpark in the same block               |
| 10  | total_dwelling_units                     | total number of residential dwelling units in the resale flats                         |
| 11  | planning_area                            | Government planning area that the flat is located                                      |
| 12  | mall_within_1km                          | number of malls within 1 kilometre                                                     |
| 13  | mall_nearest_distance                    | distance (in metres) to the nearest mall                                               |
| 14  | hawker_within_1km                        | number of hawker centres within 1 kilometre                                            |
| 15  | hawker_nearest_distance                  | distance (in metres) to the nearest hawker centre                                      | 
| 16  | mrt_nearest_distance                     | distance (in metres) to the nearest MRT station                                        |
| 17  | bus_stop_nearest_distance                | distance (in metres) to the nearest bus stop                                           |
| 18  | pri_sch_nearest_distance                 | distance (in metres) to the nearest primary school                                     |
| 19  | vacancy                                  | number of vacancies in the nearest primary school                                      |
| 20  | pri_sch_affiliation                      | boolean value if the nearest primary school has a secondary school affiliation         |
| 21  | sec_sch_nearest_dist                     | distance (in metres) to the nearest secondary school                                   |
| 22  | cutoff_point                             | PSLE cutoff point of the nearest secondary school                                      |
| 23  | max_floor_lvl                            | highest floor of the resale flat                                                       |
| 24  | city_distance                            | distance (in metres) to the city (Raffles Place)                                       |
| 25  | age_sold                                 | difference between tranc_year and lease_commence_date                                  |
| 26  | citydist*mallneardist                   | interaction term between city_distance and mall_nearest_distance                        |
| 27  | midstorey*floorarea                     | interaction term between mid_storey and floor_area_sqft                                 |

---

### Methodology

Our methodology is as follows:
1. Cleaning of Data (Train and Test)
    1. Handling of null values
    2. Handling duplicated values
    3. Handling data type errors
    4. Handling other data issues
2. Exploratory Data Analysis
    1. Summary Statistics of 'resale_price'
    2. Investigating outliers
    3. Generate plots
3. Feature Engineering and Modelling
    1. Feature Review and Creation
    2. Hot End Encoding and Scaling
    3. Modelling using Linear Regression, Lasso Regression and Ridge Regression
    4. Regression using StatsModel
    5. Hyperparameter Tuning (Ridge Model)
    6. Check for Linear Regression Assumptions
    7. Model Evaluation
4. Modelling and Kaggle Submission
    1. Preprocessing Test Data
    2. Kaggle Submission
7. Further Feature Selection
    1. Dropping more features based on multicollinearity and relevance

---

### Model Evaluation

Success of the model will be determined by the Root Mean Square Error of the model and the R2 scores. The lower the RMSE, the better it is at predicting the resale price of a flat given the factors. A higher R2 scores indicates a better fit of the model.

We can say that all the models performed quite well, with R2 values around 0.87. Additionally, the difference between the train and test R2 values are small from 0.0007 (0.08%) to 0.0012 (0.14%). The difference between the train and test Root Mean Square Error values are small too. The results are as follows:

| Regression Type              | Train R2 | Test R2 | Train Root Mean Square Error | Test Root Mean Square Error |
|------------------------------|----------|---------|------------------------------|-----------------------------|
| Linear Regression            | 0.8737   | 0.8727  | 50,990.87                    | 50,938.45                   |
| Lasso Regression             | 0.8718   | 0.8711  | 51,378.28                    | 51,248.59                   |
| Ridge Regression             | 0.8740   | 0.8728  | 50,941.09                    | 50,908.12                   |
| Ridge Regression (hypertuned)| 0.8740   | 0.8728  | 50,941.13                    | 50,908.00                   |


Overall, the ridge regression model has the best performance in terms of R2 score and Root Mean Squared Error. Regularisation enhanced the model predictive performance. When it comes to the submission to Kaggle, I will be using the ridge regression after hyperparameter.

We managed to create a strong model with an R2 value of 0.8740, which means that 87.4% of the variation of the resale price of an HDB flat can be explained by our model. Also, our Root Mean Square Error is approximately 50,900. This means that on average, our predicted price can vary from the actual price by $50,900.

---

### Conclusion and Recommendations
We recommend the Tan family to buy 4 room flat in Queenstown at around S$ 500,000. With the application, we can get more accurate market price instead of viewing the average price. This application can help sellers determine suitable selling price. Setting it too high might take a longer time to sell the unit. Setting it too low does not help the seller to earn profits. Additionally, it can help buyers minimise cost. This is so that buyers can avoid Cash on Valuation.

Data features that we would have liked to have collected to determine even more accurate HDB resale flat prices:
- Areas demarcated by MRT station names
- Distance to fitness areas
- Distance to parks
- Spike in prices from 2022