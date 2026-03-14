import plotly.express as px
import pandas as pd
from plotly.offline import plot  


df = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]*3,
    "Country": ["USA"]*11 + ["China"]*11 + ["India"]*11,
    "GDP": [18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 11, 12, 13, 14, 15, 15.5, 16, 16.5, 17, 17.5, 18, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]})


fig = px.bar(
    df,
    x="Country",
    y="GDP",
    color="Country", 
    animation_frame="Year",
    range_y=[0, 22],
    title="Animated GDP Comparison (2015–2025)"
)


plot(fig)
