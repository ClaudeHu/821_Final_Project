# Exploratory Data Analysis (EDA) Tool

Team members: Claude Hu, Caitlyn Nguyen, Luenna Wu

## Overview
This tool can be used to produce graphical displays without any necessary end-user coding. It provides a quick preliminary analysis for researchers or scientists to understand their results. 

## Description
A graphical user interface (GUI) was coded in python. This GUI instructs the user to upload a `.csv` file containing a dataset with an outcome (y) and predictor(s) (x). The back-end code then read in the data. The next screen of the GUI then instructs the user of which variable is the outcome and which are the predictors. Next, the user selects the types of data (binary, categorical, discrete, or continuous) for each outcome and predictor. The GUI will then have different options for the tool to generate which the user can select through square checkboxes, including:

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

Once the user submits their selection, a new folder will be created within the local directory. Graphical displays will be outputted as `.png` files in the folder.

## Setup and Installation
### Python Setup
To install Python and all necessary packages listed in `Requirements.txt`, please refer to [Python Packaging Installation Instructions](https://packaging.python.org/en/latest/tutorials/installing-packages/).

To install Git, please refer to [Git Guides](https://github.com/git-guides/install-git).

To install Pytest, please refer to [Pytest Documentation](https://docs.pytest.org/en/6.2.x/getting-started.html).

### Data Setup
Data should be recorded in a `.csv` file with columns being each variable. Each column should have a header/variable name, in the first row.

The accepted variable types are: <br>
* Binary
* Categorical
* Discrete
* Continuous

### Scripts Setup
The following `.py` scripts should be downloaded and saved in the same folder within your local drive:
* `Variable_Class.py`
* `final_project_main.py`
* `plots.py`

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

## Instructions

The `.csv` file should be saved in your local drive in a location which can be easily accessed again.

1. Set the folder with all of your scripts as the working directory within VScode.
2. In the cmd terminal, write:
``` python
python final_project_main.py
```
3. A GUI window will show up instructing with a button to "Select Input Table". Click the "Select Input Table" button.

<img src = "https://user-images.githubusercontent.com/63687625/165211352-64fc2319-4602-4027-92a6-61d1c0b14ecd.PNG">

4. The file directory will pop up. Find and select your `.csv` file, then click "Open".

<img src = "https://user-images.githubusercontent.com/63687625/165211877-45dd3694-9558-449c-89c1-d38b9038ccd0.PNG">

5. The file path should now populate within the GUI. Click on "Next".

<img src = "https://user-images.githubusercontent.com/63687625/165212073-821a8888-aa57-4a6a-8b63-5cd3357e5a0b.PNG">

6. A list of all of the variable names will appear. Select your outcome variable and click on "Next".

<img src = "https://user-images.githubusercontent.com/63687625/165212191-c15857a5-800b-4d7e-858f-e21677ceae44.PNG">

7. Select the type of variable for the outcome from the list of variable types and click on "Next".

<img src = "https://user-images.githubusercontent.com/63687625/165212558-c1682670-1d7d-416d-a7fc-5d648d45e8f7.PNG">

8. Select which predictors you would like to include and the variable type for each predictor. Click on "Next" when done.

<img src = "https://user-images.githubusercontent.com/63687625/165213485-80e00b68-2009-4053-887f-97c82bfcefaa.PNG">

9. Select the visualizations you would like to be produced. Click on "Run" to run the generation of plots.

<img src = "https://user-images.githubusercontent.com/63687625/165213285-773c9cef-3d20-4c8b-b7d7-d6444c3cd45a.PNG">

10. A new folder named `EDA_[year]_[month]_[day]_[hour]_[minute]_[second]` will be created in your local directory. All plot figures are outputted into this folder as `.png` files.

<img src = "https://user-images.githubusercontent.com/63687625/165213746-0d388399-ab92-4e1d-b58a-b22158dfcb35.PNG">

## Example Outputs
An example output of each plot type is given below.

### Boxplot

<img src = "https://user-images.githubusercontent.com/63687625/165214263-9ed1250f-c62a-45db-9e91-cd29d33e5fda.png" width = "700" height = "500">

### Correlation Matrix

<img src = "https://user-images.githubusercontent.com/63687625/165214141-f89eb969-fae7-4cb0-aa48-4644e4c889ba.png" width = "700" height = "500">

### Histogram

<img src = "https://user-images.githubusercontent.com/63687625/165214718-ad6db76f-4da6-4e38-946a-6f40e828cac4.png" width = "550" height = "500">

### Pairplot

<img src = "https://user-images.githubusercontent.com/63687625/165214345-2ce4cdcc-739a-4b27-b879-4a982a772a68.png" width = "550" height = "500">

### Scatterplot

<img src = "https://user-images.githubusercontent.com/63687625/165214374-6c723b3e-4275-48fc-a992-00663c21391f.png" width = "650" height = "500">

## Testing
Test modules are placed in the `test_Variable_Class.py`. Importation of pytest is required for testing. The files `test_data.csv` and `test_data_2.csv` are included to be used for testing.

To test the `Variable_Class.py` module, run the `test_Variable_Class.py` module by typing in the console:

``` python
pytest test_Variable_Class.py
```

A 100% passed test result should appear similar to:

``` python
test_Variable_Class.py ....                                                                    [100%]

======================================== 1 passed in 0.12s ========================================
```