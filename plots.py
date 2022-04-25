"""Create scatter plots and correlation matrix."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scatter_plots(variable_dict: dict, y_name: str, folder_name: str):
    """Create scatter plots of outcome on continuous predictors."""
    y = variable_dict[y_name].values
    for i in variable_dict:
        if variable_dict[i].get_x_or_y == "x" and (
            variable_dict[i].get_type == "Continuous"
            or variable_dict[i].get_type == "Discrete"
        ):
            x = variable_dict[i].values
            x_name = variable_dict[i].name
            x_float = [float(d) for d in x]
            y_float = [float(d) for d in y]

            plt.scatter(x_float, y_float, color="black")
            plt.title(f"{y_name} vs {x_name}")
            plt.xlabel(f"{x_name}")
            plt.ylabel(f"{y_name}")
            plt.savefig(folder_name + f"/{x_name}_scatter.png", dpi=300)


def cor_mtx(variable_dict: dict, csv_name: str, folder_name: str):
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
        method="pearson",
        min_periods=1,
    ).round(2)

    sns.heatmap(matrix, annot=True)
    plt.title("Correlation Matrix")
    plt.savefig(folder_name + "/correlation_matrix.png", dpi=300)


def boxplots(
    variable_dict: dict, y_name: str, csv_name: str, folder_name: str
):
    """Create boxplots of outcome on categorical/binary predictors."""
    df = pd.read_csv(csv_name, sep=",")
    for i in variable_dict:
        if variable_dict[i].get_x_or_y == "x" and (
            variable_dict[i].get_type == "Categorical"
            or variable_dict[i].get_type == "Binary"
        ):
            x_name = variable_dict[i].name
            plt.clf()
            sns.boxplot(x=f"{x_name}", y=f"{y_name}", data=df)
            plt.title(f"{y_name} by {x_name}")
            plt.savefig(folder_name + f"/{x_name}_boxplot.png", dpi=300)


def hist_plot(variable_dict: dict, folder_name: str):
    """Create histogram plots of variables."""
    for i in variable_dict:
        if (
            variable_dict[i].get_type == "Continuous"
            or variable_dict[i].get_type == "Discrete"
        ):
            var_values = variable_dict[i].values
            var_name = variable_dict[i].name
            var_values_float = [float(d) for d in var_values]
            plt.clf()
            plt.hist(var_values_float)
            plt.title(f"{var_name} Histogram")
            plt.xlabel(f"{var_name}")
            plt.ylabel("Frequency")
            plt.savefig(folder_name + f"/{var_name}_histogram.png", dpi=300)
