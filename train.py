import random

# TrainingExample object: will hold values for each attribute in a given training example. Also has "EnjoySport", which is whether or not the overall example is positive or negative. Will support the "example" function, which will allow for the generation of a random training example.
class TrainingExample: 

    # Class definition for TrainingExample object: will initialize each attribute to NULL unless a specific value is given, in which case each attribute will be initialized to said value.
    def __init__(self, sky = "NULL", airTemp = "NULL", humidity = "NULL", wind = "NULL", water = "NULL", forecast = "NULL", EnjoySport = "NULL"): 
        
        # object parameter train: an array that holds the  values for each attribute
        self.train = [sky, airTemp, humidity, wind, water, forecast, EnjoySport]

    # example function: a method that acts on a TrainingExample object. Will randomly assign a value to each attribute, then determine whether EnjoySport is positive or negative based on the target concept.    
    def example(self):

        # Create a list of possible values for each attribute, then randomly choose a value.
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

        # EnjoySport: a variable that is either "yes" or "no", representing whether the TrainingExample is positive or negative
        # Set EnjoySport to "no" by default
        EnjoySport = "no"

        # Using the target concept, if the training example has the value 'sunny' for attribute "sky" and the value 'warm' for attribute "air" then set EnjoySport to yes, signifying a positive example
        if (sky_choice == 'sunny') and (air_choice == 'warm'):
            EnjoySport = "yes"

        # Set the array to hold the newly generated values
        self.train = [sky_choice,air_choice,humidity_choice,wind_choice,water_choice,forecast_choice,EnjoySport]


        
        


