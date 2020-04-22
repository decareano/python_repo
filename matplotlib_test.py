import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')


data = pd.read_json("file://localhost/Users/marcelo/Documents/response.json")

data['date'] = pd.to_datetime(data['date'])
data.sort_values('date', inplace=True)

covid_date = data['date']
covid_death = data['death']
plt.plot_date(covid_date, covid_death, linestyle='solid')
plt.gcf().autofmt_xdate()

#date_format = mpl_dates.DateFormatter('%b, %d, %Y')
date_format = mpl_dates.DateFormatter('%Y%m%d')

plt.gca().xaxis.set_major_formatter(date_format)


plt.title('Covid Info')
plt.xlabel('date')
plt.ylabel('death')

plt.tight_layout()
plt.show()

