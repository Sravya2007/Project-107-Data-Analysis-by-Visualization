import csv
import pandas as pd
import plotly.express as px

px.defaults.template = "plotly_dark"

df = pd.read_csv("C:/Users/sravy/White Hat Jr/Project 107- Data Analysis by Visualization/data.csv")

grouped_mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
print(grouped_mean)

chart = px.scatter(grouped_mean,
                x = "student_id",
                y = "level",
                size = "attempt",
                color = "attempt",
                title = "Performance of Students in each Level",
                labels={
                        "student_id": "Student ID",
                        "level": "Level",
                        "attempt": "Attempt"})

chart.update_layout(
                font_family="Papyrus, fantasy",
                title_x = 0.5,
                font_size = 20,
                title_font_size = 30,
                legend_font_size = 30)

chart.update_xaxes(title_font_size = 30)
chart.update_yaxes(title_font_size = 30)

chart.show()