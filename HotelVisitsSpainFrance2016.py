import pygal
from pygal.style import Style
import pandas as pd

df = pd.read_csv('hotel_bookings.csv')

colsOfInterest = ['hotel','is_canceled','arrival_date_year','arrival_date_month',
                  'arrival_date_week_number','adults','children','babies','country'
                ]
cols = df[colsOfInterest]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December'
        ]

#Resort Hotels Spain

resortHotels = df.loc[df['hotel'] == "Resort Hotel"]
resortHotelsSpain = resortHotels.loc[df['country'] == 'ESP']
resortHotelsSpain2016 = resortHotelsSpain.loc[resortHotelsSpain['arrival_date_year'] == 2016]

montlyVisitsCountResort = []
for month in months:
    monthlyData = resortHotelsSpain2016.loc[resortHotelsSpain2016['arrival_date_month'] == month]
    inMonthNotCanceled = monthlyData.loc[monthlyData['is_canceled'] == 0]
    length = len(inMonthNotCanceled['is_canceled'])
    montlyVisitsCountResort.append(length)

#City Hotels Spain

cityHotels = df.loc[df['hotel'] == "City Hotel"]
cityHotelsSpain = cityHotels.loc[df['country'] == 'ESP']
cityHotelsSpain2016 = cityHotelsSpain.loc[cityHotelsSpain['arrival_date_year'] == 2016]

montlyVisitsCountCity = []

for month in months:
    monthlyData = cityHotelsSpain2016.loc[cityHotelsSpain2016['arrival_date_month'] == month]
    inMonthNotCanceled = monthlyData.loc[monthlyData['is_canceled'] == 0]
    length = len(inMonthNotCanceled['is_canceled'])
    montlyVisitsCountCity.append(length)


#Resort Hotels France

resortHotelsFrance = resortHotels.loc[df['country'] == 'FRA']
resortHotelsFrance2016 = resortHotelsFrance.loc[resortHotelsFrance['arrival_date_year'] == 2016]

montlyVisitsCountResortFrance = []
for month in months:
    monthlyData = resortHotelsFrance2016.loc[resortHotelsFrance2016['arrival_date_month'] == month]
    inMonthNotCanceled = monthlyData.loc[monthlyData['is_canceled'] == 0]
    length = len(inMonthNotCanceled['is_canceled'])
    montlyVisitsCountResortFrance.append(length)

#City Hotels France

cityHotelsFrance = cityHotels.loc[df['country'] == 'FRA']
cityHotelsFrance2016 = cityHotelsFrance.loc[cityHotelsFrance['arrival_date_year'] == 2016]

montlyVisitsCountCityFrance = []

for month in months:
    monthlyData = cityHotelsFrance2016.loc[cityHotelsFrance2016['arrival_date_month'] == month]
    inMonthNotCanceled = monthlyData.loc[monthlyData['is_canceled'] == 0]
    length = len(inMonthNotCanceled['is_canceled'])
    montlyVisitsCountCityFrance.append(length)

custom_style = Style(
        colors=('#0343df', '#e50000', '#ffff14', '#929591'),
        font_family = 'Roboto,Helvetica,Arial,sans-serif',
        background = 'transparent',
        label_font_size = 14,
)

bar_chart = pygal.Bar(
    title="Occupancy of hotels in France and Spain throughout the 2016",
    style=custom_style,
    y_title='Number of visits',
    width=1200,
    x_label_rotation=270,
)

bar_chart.x_labels = months
bar_chart.add('Resort Hotel Spain', montlyVisitsCountResort)
bar_chart.add('City Hotel Spain', montlyVisitsCountCity)
bar_chart.add('Resort Hotel France', montlyVisitsCountResortFrance)
bar_chart.add('City Hotel France', montlyVisitsCountCityFrance)
bar_chart.render_to_file('PyChart-HotelVisitsSpainFrance2016.svg')

