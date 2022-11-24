from taipy import Gui
import pandas as pd

# Interactive GUI and state, we maintain states for each individual client
# hence we can have multiple clients with each client having its own state,
# change of the state of one client will not affect the other client's state.

# Each client has its own state and global values are made local to this states,
# example n_weeks, can be stored as state.n_weeks hence changing the state of one
# client does not affect the global n_week or the state of other clients.

# Each time the on_change() is called, three arguments are passed in:
# 1. state
# 2. var_name,
# 3. var_value
# where the state is unique to that client that made the call.

# Whenever a state of a client get changed, on_change() is called with three
# params, this function is a special function in Taipy.

n_weeks = 10


def read_data(dataset_path: str):
    df = pd.read_csv(dataset_path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


dataset = read_data("./dataset/dataset.csv")
dataset_week = dataset[dataset["Date"].dt.isocalendar().week == n_weeks]


def on_change(state, var_name: str, var_value):
    if var_name == "n_weeks":
        state.dataset_week = dataset[dataset["Date"].dt.isocalendar(
        ).week == var_value]


page = """
# Taipy Basics

*Week number*: *<|{n_weeks}|>*

<|{n_weeks}|slider|min=3|max=52|>

<|{dataset_week}|chart|type=bar|x=Date|y=Value|height=100%|width=100%|>
"""

Gui(page=page).run(dark_mode=False)
