""" Create a list and generate a table form it with at least four proper 
header using dataframe. Remove auto indexing."""
import pandas as pd

data = [
    ["Ram",30,"Computer Engineering"],
    ["Sita",29,"Mechanical Engineering"],
    ["Raghav",30,"Civil Engineering"],
]


df = pd.DataFrame(data,columns=["Student Name","Age","Faculty"])

print(df.to_string(index=False))
