import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')

# Retrieving latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus country wise.
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(result)


"C:\Users\Manan K. Garg\PycharmProjects\practice\venv\Scripts\python.exe" "C:/Users/Manan K. Garg/PycharmProjects/practice/Covid19 Data Retrieval.py"
C:/Users/Manan K. Garg/PycharmProjects/practice/Covid19 Data Retrieval.py:6: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
  result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
                     Country/Region  Confirmed  Deaths  Recovered  Active
0                       Afghanistan         20       0          1      19
1                           Albania         55       1          0      54
2                           Algeria         60       4         12      44
3                           Andorra         39       0          1      38
4               Antigua and Barbuda          1       0          0       1
..                              ...        ...     ...        ...     ...
154                         Uruguay         29       0          0      29
155                      Uzbekistan         10       0          0      10
156                       Venezuela         33       0          0      33
157                         Vietnam         66       0         16      50
158  occupied Palestinian territory          0       0          0       0

[159 rows x 5 columns]

Process finished with exit code 0
