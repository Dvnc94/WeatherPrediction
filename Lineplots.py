import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime
import requests
style.use('seaborn-darkgrid')

df = pd.read_csv('clean.csv')
df['Date'] = pd.to_datetime(df['Date'], utc=True)
df['Date'] = df['Date'].dt.tz_convert(None)
df = df.set_index('Date')

Final_url = "https://api.openweathermap.org/data/2.5/forecast?id=715429&appid=da65465c77788de1fe66daa030389b8a"
weather_data = requests.get(Final_url).json()

forecasts = {'date': [], 'temp': []}
forecasts_temp = [weather_data['list'][list_index]['main']['temp'] - 273 for list_index in range(0, 40)]
forecasts_dates = [weather_data['list'][list_index]['dt_txt'] for list_index in range(0,40)]

forecast_list = [forecasts_temp[i] for i in range(0, len(forecasts_temp), 2)]
prediction_temps = [6.5, 6.21, 7.83, 5.74, 3.02, 1.11, 4.95, 1.33, 2.06, 3.26, 5.45, 2.87, 0.12, 0.07, 1.04, 2.79, 3.13,
                    1.18, 6.69, 3.72]

forecasts_dates = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in forecasts_dates]

df_forecast = pd.DataFrame(np.column_stack([forecasts_dates, forecasts_temp]), columns=['Date', 'Temp'])
df_forecast = df_forecast.set_index('Date')

index = [i for i in range(0, 20)]
plt.plot(index, forecast_list, color='black', label='forecast')
plt.plot(index, prediction_temps, color='green', label='predict')
plt.legend()
plt.show()