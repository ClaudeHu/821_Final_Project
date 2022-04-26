# Exploratory Data Analysis (EDA) Tool

## Overview

This tool can be used to produce basic statistics and graphical displays without any necessary end-user coding. It provides a quick preliminary analysis for researchers or scientists to understand their results.

## Project Plan

A graphical user interface (GUI) will be coded in python. This GUI will instruct the user to upload a `.csv` file containing a dataset with an outcome (y) and predictor(s) (x). The back-end code will then read in the data. The next screen of the GUI will then instruct the user of which variable is the outcome and which are the predictors. Later, the user will select the types of data (binary, categorical, discrete, or continuous) for each outcome and predictor. The GUI will also have different options for the tool to generate which the user can select through square checkboxes, including:

* Boxplots:<br>
  Shows the five-number summary of sets of data. It is helpful for comparing distributions across groups.
* Scatterplot matrix:<br>
  Displays scatterplots of the outcome on each continuous predictor. It shows the relationship between the outcome and predictors.
* Correlation matrix:<br>
  Exhibits a heatmap of the correlation coefficients between continuous predictors. It is useful to investigate the dependence between multiple variables at the same time and examine if there is multicollinearity.

Once the user submits their selection, the GUI will output the graphical displays and statistics.

## GUI Tutorial

## Testing
Test modules are placed in the `test_Variable_Class.py`. Importation of pytest is required for testing. The files `test_data.csv` and `test_data_2.csv` are included to be used for testing.