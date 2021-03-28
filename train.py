import random

class TrainingExample: 

    def __init__(self, sky = "NULL", airTemp = "NULL", humidity = "NULL", wind = "NULL", water = "NULL", forecast = "NULL", EnjoySport = "NULL"): 
        

        self.train = [sky, airTemp, humidity, wind, water, forecast, EnjoySport]

    def example(self):

        sky_list = ['sunny', 'cloudy', 'rainy']
        sky_choice = random.choice(sky_list)
        air_temp = ['warm', 'cold']
        air_choice = random.choice(air_temp)
        humidity = ['normal', 'high']
        humidity_choice = random.choice(humidity)
        wind = ['strong', 'weak']
        wind_choice = random.choice(wind)
        water = ['warm', 'cool']
        water_choice = random.choice(water)
        forecast = ['same', 'change']
        forecast_choice = random.choice(forecast)

        EnjoySport = "no"

        if (sky_choice == 'sunny') and (air_choice == 'warm'):
            EnjoySport = "yes"

        self.train = [sky_choice,air_choice,humidity_choice,wind_choice,water_choice,forecast_choice,EnjoySport]


        
        


