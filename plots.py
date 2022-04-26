"""Create desired plots."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scatter_plots(
    variable_dict: dict,
    y_name: str,
    folder_name: str,
    variables_df: pd.DataFrame,
):
    """Create scatter plots of outcome on continuous/discrete predictors."""
    for x_name in variable_dict:
        if variable_dict[x_name].get_x_or_y == "x" and (
            variable_dict[x_name].get_type == "Continuous"
            or variable_dict[x_name].get_type == "Discrete"
        ):
            new_df = variables_df[[y_name, x_name]]
            new_df.dropna()

            plt.scatter(new_df[x_name], new_df[y_name], color="black")
            plt.title(f"{y_name} vs {x_name}")
            plt.xlabel(f"{x_name}")
            plt.ylabel(f"{y_name}")
            plt.savefig(folder_name + f"/{x_name}_scatter.png", dpi=300)


def cor_mtx(folder_name: str, variables_df: pd.DataFrame):
    """Plot correlation matrix."""
    corr = variables_df.corr(
        method="pearson",
        min_periods=1,
    ).round(2)

    sns.heatmap(corr, annot=True)
    plt.title("Correlation Matrix")
    plt.savefig(folder_name + "/correlation_matrix.png", dpi=300)


def boxplots(
    variable_dict: dict,
    y_name: str,
    folder_name: str,
    variables_df: pd.DataFrame,
):
    """Create boxplots of outcome on categorical/binary predictors."""
    for x_name in variable_dict:
        if variable_dict[x_name].get_x_or_y == "x" and (
            variable_dict[x_name].get_type == "Categorical"
            or variable_dict[x_name].get_type == "Binary"
        ):
            new_df = variables_df[[y_name, x_name]]
            new_df.dropna()
            plt.clf()
            sns.boxplot(x=x_name, y=y_name, data=variables_df)
            plt.title(f"{y_name} by {x_name}")
            plt.savefig(folder_name + f"/{x_name}_boxplot.png", dpi=300)


def hist_plot(
    variable_dict: dict, folder_name: str, variables_df: pd.DataFrame
):
    """Create histogram plots of variables."""
    for var_name in variable_dict:
        if (
            variable_dict[var_name].get_type == "Continuous"
            or variable_dict[var_name].get_type == "Discrete"
        ):
            new_df = variables_df[var_name]
            plt.clf()
            sns.displot(new_df, kde=True)
            plt.title(f"{var_name} Histogram")
            plt.xlabel(f"{var_name}")
            plt.ylabel("Frequency")
            plt.savefig(folder_name + f"/{var_name}_histogram.png", dpi=300)


def pair_plot(
    variable_dict: dict, folder_name: str, variables_df: pd.DataFrame
):
    """Plot pairplot."""
    cont_vars = []
    for var_name in variable_dict:
        if variable_dict[var_name].get_type == "Continuous":
            cont_vars.append(var_name)
    new_df = variables_df[cont_vars]
    sns.pairplot(new_df)
    plt.savefig(folder_name + "/pairplot.png", dpi=300)
