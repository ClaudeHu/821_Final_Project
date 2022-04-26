# Exploratory Data Analysis (EDA) Tool

Team members: Claude Hu, Caitlyn Nguyen, Luenna Wu

## Description

This tool can be used to produce basic statistics and graphical displays without any necessary end-user coding. It provides a quick preliminary analysis for researchers or scientists to understand their results.

## Project Plan

A graphical user interface (GUI) will be coded in python. This GUI will instruct the user to upload a `.csv` file containing a dataset with an outcome (y) and predictor(s) (x). The back-end code will then read in the data. The next screen of the GUI will then instruct the user of which variable is the outcome and which are the predictors. Later, the user will select the types of data (binary, categorical, discrete, or continuous) for each outcome and predictor. The GUI will also have different options for the tool to generate which the user can select through square checkboxes, including:

* Boxplots:<br>
  Shows the five-number summary of sets of data. It is helpful for comparing distributions across groups and reveal any potential outliers.
* Scatterplot matrix:<br>
  Displays scatterplots of the outcome on each continuous predictor. It shows the relationship between the outcome and predictors.
* Correlation matrix:<br>
  Exhibits a heatmap of the correlation coefficients between continuous predictors. It is useful to investigate the dependence between multiple variables at the same time and examine if there is multicollinearity.
* Histograms:<br>
  Displays the distribution of each continuous or discrete variable in the dataset. It is useful to show where the peaks of the distribution are, whether the distribution is skewed or symmetric, and any potential outliers.
* Pairplots:<br>
  Plots pairwise relationships of continuous variables in the dataset. A grid of axes is created with each numeric variable as the y-axes of a single row and the x-axes across a single column.

Once the user submits their selection, the GUI will output the graphical displays and statistics.

## Setup and Installation
To install Python and all necessary packages listed in `Requirements.txt`, please refer to [Python Packaging Installation Instructions](https://packaging.python.org/en/latest/tutorials/installing-packages/).

To install Git, please refer to [Git Guides](https://github.com/git-guides/install-git).

To install Pytest, please refer to [Pytest Documentation](https://docs.pytest.org/en/6.2.x/getting-started.html).

## Class Description

### Variable Class

The Variable class is initialized as: `Variable(name: str, values: list)`.

Each instance of the Variable class stores attributes for a single variable listed as a column in the uploaded dataset.

The Variable class has the following instance attributes:
* name
* values

The Variable class has the following properties:
* get_type
* get_x_or_y

The method `set_type(self, var_type: str)` is used to set the variable type for the variable. The variable type can be set as "Binary", "Categorical", "Discrete", or "Continuous". A ValueError is raised if the inputted `var_type` is not one of the four types previously listed. Calling upon `get_type` will return the variable type as a str set from `set_type`.

The method `set_x_or_y(self, x_or_y_type: str)` is used to set whether the variable is a x or y variable. The variable type can be set as "x" or "y". A ValueError is raised if the inputted `x_or_y_type` is not "x" or "y". Calling upon `get_x_or_y` will return if the variable is "x" or "y" as a str set from `set_x_or_y`.

## Testing
Test modules are placed in the `test_Variable_Class.py`. Importation of pytest is required for testing. The files `test_data.csv` and `test_data_2.csv` are included to be used for testing.



