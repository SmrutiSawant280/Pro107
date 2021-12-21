import csv 
import pandas as p
import plotly.express as pg
df = p.read_csv("C:/Users/DELL/Desktop/PRO97/level.csv")
mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
fig = pg.scatter(mean,x = "student_id",y = "level",size = "attempt",color = "attempt")
fig.show()