"""Create scatter plots and correlation matrix."""

import numpy as np
import pandas as pd
import math

import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from Variable_Class import Variable


# Dictionary
# key: variable name (str)
# value:
# for categorical/continuous variables


def scatter_plots(variable_dict: Dict):
    """Create scatter plots of outcome on continuous predictors."""
    fig, axs = plt.subplots(math.ceil(len(variable_dict) / 3), 3)

    num = 0
    for i in variable_dict:
        if (
            variable_dict[i].get_x_or_y == "y"
            and variable_dict[i].get_type == "Continuous"
        ):
            y = variable_dict[i].values
            y_name = variable_dict[i].name

        if (
            variable_dict[i].get_x_or_y == "x"
            and variable_dict[i].get_type == "Continuous"
        ):
            x = variable_dict[i].values
            x_name = variable_dict[i].name
            x_ = []
            y_ = []
            x_ = [float(d) for d in x]
            y_ = [float(d) for d in y]
            # print(x_)
            # print(y_)

            axs[num // 3, num % 3].scatter(x_, y_, color="black")
            # plt.scatter(x_, y_, color="black")
            axs[num // 3, num % 3].set_xlabel(f"{x_name}")
            axs[num // 3, num % 3].set_ylabel(f"{y_name}")
            num += 1
    plt.show()


def cor_mtx(variable_dict: Dict):
    """Plot correlation matrix or continuous predictors."""
    df = pd.read_csv("test_data.csv", sep=",")
    # var_list = df.columns.values.tolist()

    var_for_plot = []
    df_for_plot = df
    # print(variable_dict)
    for i in variable_dict:
        if not (
            variable_dict[i].get_x_or_y == "x"
            and variable_dict[i].get_type == "Continuous"
        ):
            var_for_plot.append(variable_dict[i])
            for j in range(len(var_for_plot)):
                df_for_plot = df.drop(j)

    matrix = df_for_plot.corr(
        method="pearson",  # might need to test normality for this method
        min_periods=1,  # minimum number of observations required
    ).round(2)
    # print(matrix)

    sns.heatmap(matrix, annot=True)
    plt.title("Correlation Matrix")
    plt.show()
