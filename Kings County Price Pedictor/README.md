# Kings County Price Predictor

# Objective 
The objecive of this project is to create a price predictor model for houses that were sold in the years of 2014 and 2015 in Kings County, WA. The First part of this note book contains data exploration and data cleaning. The second part of this notebook contains feature exploration and feature creation.

There is a second note book where the modeling process is contained and evaluated. After the model is created it will be imported into this note book at the end to test its results and see if we have an accurate housin price predictor for Kings County.

# Data Exploration 
The first step is to look at how different features affect the prices of houses, and graph them to see if there could be any relations between them and prices. I seperated them into groups and graphed the groups. 

Group 1: 
![](https://raw.githubusercontent.com/DavidKentShirley/Kings_County_Price_Pedictor/main/images/corr_1.png)

Group 2: 
![](https://raw.githubusercontent.com/DavidKentShirley/Kings_County_Price_Pedictor/main/images/group2.png)

Group 3: 
![](https://raw.githubusercontent.com/DavidKentShirley/Kings_County_Price_Pedictor/main/images/group_3.png)

# Feature Engineering
After looking through the current features, we want to see if we can make some of our own so some of the features we create in this model are: <br>
* renovation_age
* sale_year
* sale_quarter
* bath_to_bed
* family_house

### Creating Polynomials 
We created a new data frame with the poly nomials added to it. 

### Creating dummy variables
With the new features we have we also want to make some dummy variables. The zipcodes were transformed into dummy variables

### Creating and testing models
When creating the models and doing feature testing we used the F-Test and Wrapper method in order to see insights on what features to use. We got some decent scores with these tests and decided to go with the F-test results. 
The RMSE for these were ~131K 

# Final Steps
The last thing to do was bring the model over and test it out on the testing set and see what prices it comes up with. We did not have issues with this step and we were able to get price predictions with 4,322 houses (All the houses within the testing csv!).

