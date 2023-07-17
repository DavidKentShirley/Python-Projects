# Python Projects
 * Library of projects in Python. Includes (FastApi)
 * Will be updated as new projects are made
 
 # FastAPI
 [Here](https://github.com/DavidKentShirley/Python-Projects/tree/main/Python-FastAPI-Basic1)
 
### About
<details><summary>Overview</summary>

 # FastAPI
 1. [Basic Knowledge](https://github.com/DavidKentShirley/Python-Projects/tree/main/Python-FastAPI-Basic1/Books_example(Basic%20Fastapi%20Info)): Some basic API functionality using a pre-made object to work with based off books. Complete RESTful API
 * CRUD model requests (get, post, put, delete)
 * Basic Data models
 * Response schema
 * Data validation + Path parameters
 2. [To do App](https://github.com/DavidKentShirley/Python-Projects/tree/main/Python-FastAPI-Basic1/TodoApp): Project to use more advanced features of FastAPI [WIP]
 * Implementing databases with SQLite and PostgressSQL (Local database and production database) [WIP]
 * Using sqlalchemy to implement databases within FastAPI  
 * Authentication and Authorization [WIP]
 * Request Authentication [WIP]
 * Data Migration [WIP]
 
 ### Future Plans
 1. Full Stack application [Will be added soon]
 2. Web Deployment [Will be added soon]
 
</details>

# Gender Classification 2.0
[Here](https://github.com/DavidKentShirley/Python-Projects/tree/main/Gender%20Classification%202.0)

### About
<details><summary>Overview</summary>

## Objective

How well can you predict genders based on about 10k photos of men and 10k photos of women without going into deep learning?

* The objective of this project was to learn image recognition using genders (Male/Female).
* Main tools Used
  * SKLEAN 
  * OpenCV python
  * PYWT

## Business Case

Many tech companies and government agencies use facial recognition today to help them in many different ways, some of the use cases for facial recognition are: 

* Suspect Detection
  * When given an image of a suspect who has committed a crime facial recognition is used to help identify them.
* People Recognition in Photos
  * Companies like Facebook use this type of technology to make a more user friendly experience by identifying people in a photo so you can tag them easier.

There are many more use cases for Facial recognition, right now this project only identifies gender, you can check out the other project of artist recognition to see a demo model of facial recognition for people. 

**Note**: These are only ML models and not DL, There is a much better way of producing these models which I will be doing at a later date.



## What Goes Into Gender Classification

![](https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/photo3.png?raw=true)

If you are new to image classification, specifically for facial recognition there is a library called [OpenCV](https://opencv.org/) which I used in order to pick out faces and crop them to use for training. After the images were cropped the next thing to do was make them readable by a computer([Wavelets](https://pywavelets.readthedocs.io/en/latest/)). If you are interested in what Wavelets are and how it works in python please click the [link](https://pywavelets.readthedocs.io/en/latest/).

![](https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/photo5.png?raw=true)

The two photos would be stacked on top of each other and compared when a model is training. After we have gathered and converted all the images the next step would be to train a model.



## Modeling

The first model that was run was a SVM model to get a decent understand of where we are with the predictions. The base model is very good and will most likely be used for our final model but we will need to check other models and see how they perform in order to get the best model we can produce. 



<img src="https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/model%201%20results.png?raw=true" style="zoom: 67%;" />



After doing a basic model the next step was to check other models to see how they perform, we want to produce the best model, doing this we used a pipeline and grid search for three different types of models (SVM, Random Forest, Logistic Regression).



<img src="https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/grid%20search.png?raw=true" style="zoom:67%;" />

The best model in both cases was the SVM model so for deployment I went with the SVM model, with the GridSearchCV Hyper parameters. 



## Results



After running the model with the test data we get a nice confusion matrix to see how well it classified each gender based on facial pictures.



![](https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/cm.png?raw=true)

After we see this model we can than check the output of the model to see what it predicts with a new image. 

![](https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/000019.jpg?raw=true)

![](https://github.com/DavidKentShirley/Gender_Classification_ML/blob/main/Presentation%20Photos/better.png?raw=true)

We can see what the model predicted with the probability for each class. 



## The Future

•The next step to this model would be adding age detection.

​		•Having a model to be able to predict gender and age would benefit even more than just gender.



•Using a deep learning model would help increase the score significantly 

​		•Having a deep learning model would help the model learn on its own what each gender is using more complicated algorithms which would increase the model score by a good amount
</details>

 
 # PySpark
 ### Will be added soon
 
 
