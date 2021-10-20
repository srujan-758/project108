import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("mobileBrand_reviews.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["average ratings of mobile brands"])
fig.show()