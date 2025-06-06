# -*- coding: utf-8 -*-
"""Simple ML Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rgI1hvqBqvH9A5bHlxDeq308nmJpLNcM
"""

print("running")

"""#**Bisnis Understanding**

Deskripsi untuk penjelasan masalah yg akan di solve

The sinking of the Titanic

#**Load Data**
"""

import pandas as pd
import numpy as np

# prompt:  give me data from online source

import pandas as pd
# Load data from an online source (example: a CSV file on GitHub)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"  # Replace with your desired URL
df = pd.read_csv(url)
df.head()

# prompt: give me iris dataset

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns= iris.feature_names)
iris_df['target']=iris.target
iris_df.head()

import numpy as np
import pandas as pd
from sklearn import datasets

db = datasets.load_diabetes()
db_array = np.array(db.data)

db

col = ["age","sex","bmi","bp_avg","s1","s2","s3","s4","s5","s6"]
df_diabetes = pd.DataFrame(data=db, columns=col)
df_diabetes['target'] = db.target

# prompt: give me code to load data from google drive

from google.colab import drive
drive.mount('/content/drive')

"""# **Splitting Dataset**"""

# prompt: create code for splitting dataset

from sklearn.model_selection import train_test_split

# For the Titanic dataset (df)
if 'df' in locals():
    X_titanic = df.drop('Survived', axis=1)  # Assuming 'Survived' is the target variable
    y_titanic = df['Survived']
    X_train_titanic, X_test_titanic, y_train_titanic, y_test_titanic = train_test_split(
        X_titanic, y_titanic, test_size=0.2, random_state=42
    )
    print("\nTitanic dataset split into training and testing sets.")
    print("Training set size:", len(X_train_titanic))
    print("Testing set size:", len(X_test_titanic))

# For the Iris dataset (iris_df)
if 'iris_df' in locals():
    X_iris = iris_df.drop('target', axis=1)  # Assuming 'target' is the target variable
    y_iris = iris_df['target']
    X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
        X_iris, y_iris, test_size=0.2, random_state=42, stratify=y_iris # Stratify for classification
    )
    print("\nIris dataset split into training and testing sets.")
    print("Training set size:", len(X_train_iris))
    print("Testing set size:", len(X_test_iris))

# For the Diabetes dataset (df_diabetes)
if 'df_diabetes' in locals():
    # For regression, we typically split features (X) and target (y)
    # The target variable for the diabetes dataset is usually the 'target' from load_diabetes
    # Need to add the target column to the DataFrame if not already there
    if 'target' not in df_diabetes.columns and 'db' in locals() and hasattr(db, 'target'):
        df_diabetes['target'] = db.target

    if 'target' in df_diabetes.columns:
        X_diabetes = df_diabetes.drop('target', axis=1)
        y_diabetes = df_diabetes['target']
        X_train_diabetes, X_test_diabetes, y_train_diabetes, y_test_diabetes = train_test_split(
            X_diabetes, y_diabetes, test_size=0.2, random_state=42
        )
        print("\nDiabetes dataset split into training and testing sets.")
        print("Training set size:", len(X_train_diabetes))
        print("Testing set size:", len(X_test_diabetes))
    else:
        print("\nCould not split Diabetes dataset: 'target' column not found.")

"""# **Modelling**"""

# prompt: create code for training using random forest

import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# --- Training using Random Forest ---

# For the Iris dataset (Classification)
if 'X_train_iris' in locals() and 'y_train_iris' in locals():
    print("\nTraining Random Forest Classifier on Iris dataset...")
    # Initialize the Random Forest Classifier
    rf_classifier_iris = RandomForestClassifier(n_estimators=100, random_state=42) # n_estimators is the number of trees
    # Train the model
    rf_classifier_iris.fit(X_train_iris, y_train_iris)
    print("Random Forest Classifier trained on Iris dataset.")

    # Make predictions on the test set (optional, but good to see performance)
    if 'X_test_iris' in locals() and 'y_test_iris' in locals():
        y_pred_iris = rf_classifier_iris.predict(X_test_iris)
        # Evaluate the model
        accuracy_iris = accuracy_score(y_test_iris, y_pred_iris)
        print(f"Accuracy on Iris test set: {accuracy_iris:.4f}")

# For the Titanic dataset (Classification - assuming 'Survived' is the target)
# Note: The Titanic dataset usually requires significant preprocessing (handling missing values,
# encoding categorical features) before training. This example assumes the data is ready.
if 'X_train_titanic' in locals() and 'y_train_titanic' in locals():
    print("\nTraining Random Forest Classifier on Titanic dataset...")
    # Note: You likely need to handle missing values and encode categorical features
    # in X_train_titanic and X_test_titanic before running this.
    # For demonstration, we'll drop columns with non-numeric types and NaNs for simplicity.
    # In a real scenario, use more robust preprocessing.
    X_train_titanic_processed = X_train_titanic.select_dtypes(include=np.number).fillna(X_train_titanic.select_dtypes(include=np.number).median())
    X_test_titanic_processed = X_test_titanic.select_dtypes(include=np.number).fillna(X_test_titanic.select_dtypes(include=np.number).median())


    # Ensure columns match after preprocessing
    common_cols = list(set(X_train_titanic_processed.columns) & set(X_test_titanic_processed.columns))
    X_train_titanic_processed = X_train_titanic_processed[common_cols]
    X_test_titanic_processed = X_test_titanic_processed[common_cols]

    if not X_train_titanic_processed.empty:
        # Initialize the Random Forest Classifier
        rf_classifier_titanic = RandomForestClassifier(n_estimators=100, random_state=42)
        # Train the model
        rf_classifier_titanic.fit(X_train_titanic_processed, y_train_titanic)
        print("Random Forest Classifier trained on Titanic dataset.")

        # Make predictions on the test set
        if 'X_test_titanic' in locals() and 'y_test_titanic' in locals() and not X_test_titanic_processed.empty:
            y_pred_titanic = rf_classifier_titanic.predict(X_test_titanic_processed)
            # Evaluate the model
            accuracy_titanic = accuracy_score(y_test_titanic, y_pred_titanic)
            print(f"Accuracy on Titanic test set: {accuracy_titanic:.4f}")
    else:
        print("Could not train on Titanic dataset due to missing or non-numeric data after simple preprocessing.")


# For the Diabetes dataset (Regression)
if 'X_train_diabetes' in locals() and 'y_train_diabetes' in locals():
    print("\nTraining Random Forest Regressor on Diabetes dataset...")
    # Initialize the Random Forest Regressor
    rf_regressor_diabetes = RandomForestRegressor(n_estimators=100, random_state=42)
    # Train the model
    rf_regressor_diabetes.fit(X_train_diabetes, y_train_diabetes)
    print("Random Forest Regressor trained on Diabetes dataset.")

    # Make predictions on the test set
    if 'X_test_diabetes' in locals() and 'y_test_diabetes' in locals():
        y_pred_diabetes = rf_regressor_diabetes.predict(X_test_diabetes)
        # Evaluate the model using Mean Squared Error (MSE) or other regression metrics
        mse_diabetes = mean_squared_error(y_test_diabetes, y_pred_diabetes)
        print(f"Mean Squared Error on Diabetes test set: {mse_diabetes:.4f}")

# prompt: create code for training using naive bayes

from sklearn.naive_bayes import GaussianNB

# --- Training using Naive Bayes ---

# For the Iris dataset (Classification)
if 'X_train_iris' in locals() and 'y_train_iris' in locals():
    print("\nTraining Naive Bayes Classifier on Iris dataset...")
    # Initialize the Naive Bayes Classifier (Gaussian Naive Bayes is common for continuous data)
    nb_classifier_iris = GaussianNB()
    # Train the model
    nb_classifier_iris.fit(X_train_iris, y_train_iris)
    print("Naive Bayes Classifier trained on Iris dataset.")

    # Make predictions on the test set
    if 'X_test_iris' in locals() and 'y_test_iris' in locals():
        y_pred_nb_iris = nb_classifier_iris.predict(X_test_iris)
        # Evaluate the model
        accuracy_nb_iris = accuracy_score(y_test_iris, y_pred_nb_iris)
        print(f"Accuracy (Naive Bayes) on Iris test set: {accuracy_nb_iris:.4f}")

# For the Titanic dataset (Classification)
# Note: Similar preprocessing considerations as with Random Forest apply.
if 'X_train_titanic' in locals() and 'y_train_titanic' in locals():
    print("\nTraining Naive Bayes Classifier on Titanic dataset...")
    # Use the processed data from the Random Forest section
    if 'X_train_titanic_processed' in locals() and not X_train_titanic_processed.empty:
        # Initialize the Naive Bayes Classifier
        nb_classifier_titanic = GaussianNB()
        # Train the model
        nb_classifier_titanic.fit(X_train_titanic_processed, y_train_titanic)
        print("Naive Bayes Classifier trained on Titanic dataset.")

        # Make predictions on the test set
        if 'X_test_titanic_processed' in locals() and 'y_test_titanic' in locals() and not X_test_titanic_processed.empty:
            y_pred_nb_titanic = nb_classifier_titanic.predict(X_test_titanic_processed)
            # Evaluate the model
            accuracy_nb_titanic = accuracy_score(y_test_titanic, y_pred_nb_titanic)
            print(f"Accuracy (Naive Bayes) on Titanic test set: {accuracy_nb_titanic:.4f}")
    else:
         print("Could not train Naive Bayes on Titanic dataset due to missing or non-numeric data after simple preprocessing.")


# Note: Naive Bayes is typically used for classification tasks, not regression.
# We won't train a Naive Bayes model on the Diabetes dataset as it is a regression problem.
print("\nNaive Bayes is primarily for classification. Skipping training on Diabetes dataset.")
