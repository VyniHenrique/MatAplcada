import plotly.express as pw
from data.dowload import download_data

data = download_data('AAPL')

pw.line(
        data.reset_.index(),
        x = "Date" , y = "Clone" , title = "BRAS3"
)