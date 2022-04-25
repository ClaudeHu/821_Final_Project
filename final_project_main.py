"""
Created on Sat Apr 16 14:04:30 2022

@author: Claude Hu, Caitlyn Nguyen, Luenna Wu
"""

import tkinter as tk
from tkinter import filedialog
import pprint
import csv
import sys
from Variable_Class import Variable
import pandas as pd
import time
from collections import defaultdict
from csv import DictReader
import os

import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plots import *

# set the GUI box of the entry page (select the datafile)
page1 = tk.Tk()
page1.geometry("800x300")
page1.title("Select the data file")


next_page = (
    tk.BooleanVar()
)  # script continues to run only when the 'Next' Button is clicked
next_page.set(False)


inputFilename = tk.StringVar()  # filename
inputFilename.set("")


# set up the function of select input file button
def UploadAction():
    """Input file button."""
    filename = filedialog.askopenfilename(
        filetypes=(("Excel files", ".csv"),)
    )  # only select csv files
    inputFilename.set(filename)
    if filename != "":
        filepath.config(text=filename)
        # button to the next page won't be activated without a file selected
        page2_button["state"] = "normal"


# close current page and move to the next page
def Close_P1():
    """Close current page."""
    next_page.set(True)
    page1.destroy()


# the button that select the input file
input_button = tk.Button(
    page1, text="Select Input Table", width=20, height=4, command=UploadAction
)
input_button.place(relx=0.5, rely=0.5, anchor="center")

# the label that shows the file path
filepath = tk.Label(page1, text="Path of Input File", font=("Aerial 11"))
filepath.place(relx=0.5, rely=0.7, anchor="center")
filepath.config(bg="white", fg="black")

# the button that closes the current page and opens the next page
page2_button = tk.Button(
    page1, text="Next", width=8, height=2, command=Close_P1, state="disabled"
)
page2_button.place(relx=0.99, rely=0.97, anchor="se")

page1.mainloop()

# file name
csv_name = inputFilename.get()

# stop script by clicking the cross on right top
if next_page.get() is False:
    sys.exit()
next_page.set(False)

# read the variable names
values_dict: dict = defaultdict(list)
with open(csv_name, "rU") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        for col, dat in row.items():
            values_dict[col].append(dat)

# list of variables
data_columns = list(values_dict.keys())

# create variable dictionary
variable_dict = dict()
for variable in data_columns:
    variable_dict[variable] = Variable(variable, values_dict[variable])


def Close_P2():
    """Close P2."""
    next_page.set(True)
    page2.destroy()


# set up page 2: select the outcome (y)
page2 = tk.Tk()
page2.geometry("800x300")

page2.title("Select the Outcome")


# the 'Next' button
page3_button = tk.Button(
    page2, text="Next", width=8, height=2, command=Close_P2, state="normal"
)

page3_button.place(relx=0.99, rely=0.97, anchor="se")


# The variable of outcome's name
Y = tk.StringVar()
Y.set("")

# the variable of index (which variable was selected)
y_selection = tk.IntVar()

y_selection.set(0)


# the selection button of y
placement = 10
for i in range(len(data_columns)):
    col_name = data_columns[i]
    select_var = tk.IntVar()

    tk.Radiobutton(page2, text=col_name, variable=y_selection, value=i).grid(
        row=placement, column=10, sticky="w"
    )
    placement += 10


page2.mainloop()

if next_page.get() is False:
    sys.exit()

next_page.set(False)


# set the name of outcome (y)
Y.set(data_columns[y_selection.get()])
variable_dict[data_columns[y_selection.get()]].set_x_or_y("y")


# page 3: select the type of y:
# Categorical, Binary, Discrete, Continuous
page3 = tk.Tk()
page3.geometry("800x300")
page3.title("Select the Type of Outcome Variable")


var_types = ["Binary", "Categorical", "Discrete", "Continuous"]

# the variable of the selected type
Y_type = tk.StringVar()
Y_type.set("")

# the index of selected type in the list var_types
ytype_selection = tk.IntVar()
ytype_selection.set(0)


def Close_P3():
    """Close P3."""
    next_page.set(True)
    page3.destroy()


# the 'Next' button
page4_button = tk.Button(
    page3, text="Next", width=8, height=2, command=Close_P3, state="normal"
)

page4_button.place(relx=0.99, rely=0.97, anchor="se")


# set the buttons that select the variable type
placement = 10
for i in range(len(var_types)):
    variable_type = var_types[i]
    select_var = tk.IntVar()

    tk.Radiobutton(
        page3, text=variable_type, variable=ytype_selection, value=i
    ).grid(row=placement, column=10, sticky="w")
    placement += 10


page3.mainloop()


if next_page.get() is False:
    sys.exit()

next_page.set(False)


Y_type.set(var_types[ytype_selection.get()])
variable_dict[data_columns[y_selection.get()]].set_type(
    var_types[ytype_selection.get()]
)

Y_name = data_columns[y_selection.get()]

# the predictors
X = data_columns
X.pop(y_selection.get())  # remove the y from the list of variables


# page 4: selec the predictors and their types
page4 = tk.Tk()
page4.geometry("800x300")
page4.title("Select the Predictors")


def Close_P4():
    """Close P4."""
    next_page.set(True)
    page4.destroy()


page5_button = tk.Button(
    page4, text="Next", width=8, height=2, command=Close_P4, state="normal"
)

page5_button.place(relx=0.99, rely=0.97, anchor="se")

selected_X: list = []  # store the variables of each predictor
X_types: list = []  # store the variable of each predictor's type
X_type_buttons: list = []  # store the buttons that selects the types


# the button that selected the type of one variable will be disabled
# unless that variable is selected
def check_predictor_selection(*args):
    """Check predictor selection."""
    selection_sum = 0
    for i in range(len(selected_X)):
        selected_var = selected_X[i]
        button_row = X_type_buttons[i]

        for j in range(len(button_row)):
            type_button = button_row[j]
            if selected_var.get() == 1:
                type_button.config(state="normal")
            else:
                type_button.config(state="disabled")
            selection_sum += selected_var.get()
    if selection_sum == 0:
        page5_button.config(state="disabled")
    else:
        page5_button.config(state="normal")


# set the buttons
for i in range(len(X)):
    predictor = X[i]
    selected_var = tk.IntVar()
    selected_var.set(1)
    selected_X.append(selected_var)
    tk.Checkbutton(
        page4, text=predictor, variable=selected_var, onvalue=1, offvalue=0
    ).grid(row=placement, column=10, sticky="w")
    new_row: list = []
    type_of_predictor = tk.IntVar()

    type_of_predictor.set(0)
    X_types.append(type_of_predictor)
    col_cor = 300
    for j in range(len(var_types)):

        variable_type = var_types[j]
        type_button = tk.Radiobutton(
            page4,
            text=variable_type,
            variable=type_of_predictor,
            value=j,
            state="active",
        )
        type_button.grid(row=placement, column=col_cor, sticky="w")

        col_cor += 150
        new_row.append(type_button)

    selected_var.trace("w", check_predictor_selection)
    X_type_buttons.append(row)

    placement += 10


page4.mainloop()


if next_page.get() is False:
    sys.exit()

next_page.set(False)

keep = []

for i in range(len(selected_X)):
    pred_var = selected_X[i]
    # check if the variable is selected
    # if selected add to the list
    if pred_var.get() == 1:
        keep.append(X[i])
        variable_dict[X[i]].set_type(var_types[X_types[i].get()])
        variable_dict[X[i]].set_x_or_y("x")

keep.append(Y_name)
final_var_dict = {k: variable_dict[k] for k in keep}

visualizations = ["Scatter Plot", "Box Plot", "Correlation Matrix"]
page5 = tk.Tk()
page5.geometry("800x300")
page5.title("Select the Visualization")


vis_vars = []  # store the variables
for i in range(len(visualizations)):
    vis_plot = visualizations[i]

    selected_vis = tk.BooleanVar()
    selected_vis.set(True)
    vis_vars.append(selected_vis)
    # selected_vis.set(1)
    tk.Checkbutton(
        page5,
        text=vis_plot,
        variable=selected_vis,
        onvalue=True,
        offvalue=False,
    ).grid(row=placement, column=10, sticky="w")

    placement += 80


def Close_P5():
    """Close P5."""
    next_page.set(True)
    page5.destroy()


page6_button = tk.Button(
    page5, text="Run", width=8, height=2, command=Close_P5, state="normal"
)

page6_button.place(relx=0.99, rely=0.97, anchor="se")

page5.mainloop()

if next_page.get() is False:
    sys.exit()

next_page.set(False)

selected_visualization = []
for i in range(len(vis_vars)):
    if vis_vars[i].get() is True:
        selected_visualization.append(visualizations[i])

folder_name = "EDA_" + time.strftime("%Y_%m_%d_%H_%M_%S")
os.mkdir(folder_name)

for plot in selected_visualization:
    if plot == "Scatter Plot":
        scatter_plots(final_var_dict, Y_name, folder_name)
    elif plot == "Correlation Matrix":
        cor_mtx(final_var_dict, csv_name, folder_name)
    elif plot == "Box Plot":
        boxplots(final_var_dict, Y_name, csv_name, folder_name)
