"""Create scatter plots and correlation matrix."""

import numpy as np
import pandas as pd
import math

import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from Variable_Class import Variable


def scatter_plots(variable_dict: Dict, y_name: str, folder_name: str):
    """Create scatter plots of outcome on continuous predictors."""
    y = variable_dict[y_name].values
    for i in variable_dict:
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

            plt.scatter(x_, y_, color="black")
            plt.title(f"{y_name} vs {x_name}")
            plt.xlabel(f"{x_name}")
            plt.ylabel(f"{y_name}")
            plt.savefig(folder_name + f"/{x_name}_scatter.png", dpi=300)


def cor_mtx(variable_dict: Dict, csv_name: str, folder_name: str):
    """Plot correlation matrix of continuous predictors."""
    df = pd.read_csv(csv_name, sep=",")

    var_for_plot = []
    df_for_plot = df
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

    sns.heatmap(matrix, annot=True)
    plt.title("Correlation Matrix")
    plt.savefig(folder_name + "/correlation_matrix.png", dpi=300)
