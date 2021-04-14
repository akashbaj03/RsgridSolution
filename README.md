# Text Classification

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Welcome to the RGrid Machine Learning Solution!

## The Preprocessor

The solution has a text pre-processor which cleans and extracts relevant information from the description column.

It has the following functions -

- Remove HTML tags if any
- Remove extra whitespaces
- Remove accented characters
- Expand shortened words
- Remove special characters
- Convert number words into numeric
- Perform lemmatization

## Feature Engineering

The data has target variable distributed uniformly, hence, it does not warrant any undersampling/oversampling technique

Once the description is pre-processed, divide the data in train, test and validation as

Train Ratio = 75%

Validation ratio = 10%

Test Ratio = 15%

## Model Training

Model was trained and validated using following algorithms -

NB classifier F1 score - 88% 
Linear SVM F1 score - 91%
Logistic Regression - 89%
Random Forest - 91%

Random Forest was chosen because of its superior performance 
RF F1 score on test data - 92%

The model file is randomforest.pkl which has been used by the flask app to generate predictions.

Deep Learning Model like RNN would have been a good experiment, however, because of the low number of the observations, it is not a good choice

## Sample Test using Flask
run python test.py
O/P -
Calling API with test description:
Response:
200
{'prediction': 'Dementia'}
