import pyowm

# Inicializa o OWM(OpenWeatherMap) com a sua chave API
own = pyowm.OWM('906f1198ac01daf8e0ac43a46d41b4f7')

# Define a cidade que voce quer obeter o clima
city = "São Paulo, BR"

# Obtém as informações sobre o clima
weather_manager = own.weather_manager()
observation = weather_manager.weather_at_place(city)
weather = observation.weather

# Imprime a temperatura atual em graus Celsius
temperature = weather.temperature('celsius')['temp']
print(f"A temperatura atual em {city} é de {temperature: .1f}ºC.")