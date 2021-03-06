# Kings County Housing Bake-off

For many machine learning projects, the goal is to create a model that best predicts the target variable on unseen data. In order to develop a model, we have a general process, but there is a lot of flexibility within this process. Even when working with the same data, people can produce different models by engineering different features, or by selecting certain features to include in the models. **There is no one correct way to create a model**.

For Phase 2, you will be examining data about home sales in the Seattle, Washington area to understand what factors about a home impact its price, and develop a model that will **predict the prices of homes** sold. This project will be broken up into two parts. Part one will focus on exploring the data and using different statistical tests to understand the relationships present between the price and different features, as well as among the price. For this project there will be **3 deliverables**:

- a inference presentation. 
- a Github repo for this project
- a notebook showing your final modeling process
- a CSV file of your predictions on the holdout set
	- name this file `housing_preds_your_name.csv` (replacing `your_name` with your name) and send via Slack

 

## Inference Presentation

For the first part of the project, you will try to determine what affects housing prices using exploratory data analysis, hypothesis tests, and linear regression. The goal of this analysis is to be able to come away with valuable insights. Imagine a real estate agent ccomes to you and asks for information about the housing market in Kings County. What would youar analysis tell them that would be helpful to them, as they help clients buy and sell houses. 

You will give a short presentation of your insights Wednesday afternoon. Additionally, you will create a final notebook that includes this information. For your presentation, you only need to include graphics and insights that you think are valuable, but for your final notebook, you must innclude the following:

- **Exploratory Data Analysis (EDA):** You must create **at least 4 data visualizations** that help to explain the data. These visualizations should help someone unfamiliar with the data understand the target variable and the features that help explain that target variable.

- **Feature Engineering:** You must create **at least 3 new features** to test in your model. Those features do not have to make it into your final model, as they might be removed during the feature selection process. That is expected, but you still need to explain the features you engineer and your thought process behind why you thought they would explain the selling price of the house.  

- **Statistical Tests:** Your notebook must show **at least 3 statistical tests** that you preformed on your data set. Think of these as being part of your EDA process; for example, if you think houses with a view cost more than those without a view, then perform a two-sample T-test. These can be preliminary evidence that a feature will be important in your model.  

- **Check Model Assumptions:** There are 4 assumptions of a linear regression model, and invesitgating if you are violating one assumption can help you to make a better model. For example, your errors might not be homoscedastic. This could mean that a non-linear transformation of the target variable could improve your model. So after you fit your first model, you want to check the assumptions and make adjustments accordingly. Iis not always possible to perfectly meet those assumptions, so that should not be your goal. For this project, I you need to make atleast one attemmpt to improve your model in order to meet the assumptions. 

- **Model Interpretation:** One of the benefits of a linear regression model is that you can **interpret the coefficients** of the model **to derive insights**. For example, which feature has the biggest impact on the price of the house? Was there a feature that you thought would be significant but was not? Think if you were a real estate agent helping clients price their house: what information would you find most helpful from this model?

## Holdout predictions

You will develop a model using `kc_house_data_train.csv`. Then you will use that model/process to predict on the `kc_house_data_holdout_features.csv`. 

***Important note #1***: If you create a new feature with your training data, you will need to do the same thing with the test data before using the model to predict on the holdout data.  

After using your model to predict the holdout data, you will submit those predictions as a `.csv` file to the instructional staff. We will score the submitted predictions using the RMSE of those predictions.

***Important note #2***: While we will score and rank each submission, your class rank will **not** have any direct impact on passing Phase 2. *The goal is to make sure you can actually produce predictions*.

So as long as you successfully **complete the modeling process** and can **explain the work you did**, you will be able to pass. 


## GitHub Repository

A GitHub repo is a good way to keep track of your work, but also to display the work you did to future employers. Your GitHub should contain the following:

- A `README.md` that briefly describes the project and the files within the repo.
- Your cleaned and annotated notebook showing your work.
- A folder with all of your 'working' notebooks where you played around with your data and the modeling process.

## Data Set Information

This data set contains information about houses that were sold in the Seattle area during the last decade. Below is a description of the column names, to help you understand what the data represents. As with most real world data sets, the column names are not perfectly described, so you'll have to do some research or use your best judgment if you have questions relating to what the data means. 

Like every data set, there are some irregularities and quirks. Trust me, there wasn't a house sold with 33 bedrooms, even though the data says there was. *You have to decide how you want to handle that example*. Also, some houses were sold more than once within the time frame of this dataset. Think about how that can be useful information in predicting the selling price.

As you go through this modeling process, think about what determines how much someone will pay for a house.  For example, the larger the house is, the more people will pay for it. If you understand why certain houses cost more than others and represent that in your model, it will be a more accurate model.  

Have fun!

# Column Names and descriptions for Kings County Data Set
* **id** - unique ID for a house
* **date** - Date day house was sold
* **price** - Price is prediction target
* **bedrooms** - Number of bedrooms
* **bathrooms** - Number of bathrooms
* **sqft_living** - square footage of the home
* **sqft_lot** - square footage of the lot
* **floors** - Total floors (levels) in house
* **waterfront** - Whether house has a view to a waterfront
* **view** - Number of times house has been viewed
* **condition** - How good the condition is (overall)
* **grade** - overall grade given to the housing unit, based on King County grading system
* **sqft_above** - square footage of house (apart from basement)
* **sqft_basement** - square footage of the basement
* **yr_built** - Year when house was built
* **yr_renovated** - Year when house was renovated
* **zipcode** - zip code in which house is located
* **lat** - Latitude coordinate
* **long** - Longitude coordinate
* **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
* **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors
