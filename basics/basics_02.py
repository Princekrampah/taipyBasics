from taipy import Gui
import pandas as pd

# visual elements: Taipy adds visual elements on top of markdown
# to give you the ability to add charts, tables... The format for
# it is as follows:

# <|{variable}|visual_element_name|param_1=param_1|param_2=param_2| ... |>.
# variable: python variable eg dataframe
# visual_element_name: Name of the visual element eg table
# para_1: parameters passed in

n_weeks = 10

def read_data(dataset_path: str):
    df = pd.read_csv(dataset_path)
    return df

dataset = read_data("./dataset/dataset.csv")

page = """
# Taipy Basics

*Week number*: *<|{n_weeks}|>*

<|{n_weeks}|slider|min=2|max=30|>

<|{dataset[9000:]}|chart|type=bar|x=Date|y=Value|height=100%|>

# Table Format
<|{dataset}|table|height=400px|width=95%|>
"""


Gui(page=page).run(dark_mode=False)
    