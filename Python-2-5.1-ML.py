new_data_rain = int(input())
new_data_humidity = int(input())

rain_temp,rain_humidity = [45,55,55],[60,65,55]
no_rain_temp,no_rain_humidity=[35,50,40],[45,30,35]

rain=0
no_rain=0
sz=len(rain_temp)

for i in range(sz):
    rain += (rain_temp[i] - new_data_rain) ** 2 + (rain_humidity[i] - new_data_humidity) ** 2
    no_rain += (no_rain_temp[i] - new_data_rain) ** 2 + (no_rain_humidity[i] - new_data_humidity) ** 2

if rain < no_rain: 
  print("RAIN")
else:
  print("NO RAIN")