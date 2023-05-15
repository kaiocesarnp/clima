import pyowm

# Inicializa o OWM(OpenWeatherMap) com a sua chave API
own = pyowm.OWM('906f1198ac01daf8e0ac43a46d41b4f7')

# Define a cidade que voce quer obeter o clima
city = "Brasília, BR"

# Obtém as informações sobre o clima
weat_manager = own.weather_manager()
observation = weat_manager.weather_at_place(city)
weather = observation.weather

# Imprime a temperatura atual em graus Celsius
temperature = weather.temperature('celsius')['temp']
print(f"A temperatura atual em {city} é de {temperature: .1f}ºC.")

# Explicação linha por linha:

# import pyowm: Essa linha importa o módulo pyowm, que é uma biblioteca Python que fornece uma interface para interagir com a API do OpenWeatherMap.

# own = pyowm.OWM('906f1198ac01daf8e0ac43a46d41b4f7'): Nesta linha, o objeto own é inicializado com a chave da API do OpenWeatherMap. Essa chave é necessária para autenticar e acessar os dados da API.

# city = "Brasília, BR": Aqui, uma variável chamada city é definida com o valor "Brasília, BR". Isso especifica a cidade para a qual desejamos obter informações sobre o clima.

# weat_manager = own.weather_manager() cria um objeto chamado weather_manager que é responsável por gerenciar as solicitações relacionadas ao clima. Podemos pensar nele como uma "gerente do clima". Ele é criado a partir do objeto own, que representa o OpenWeatherMap (OWM), a plataforma que fornece as informações climáticas.

# observation = weather_manager.weather_at_place(city): Nesta linha, é feita uma chamada para weather_at_place() passando a cidade como parâmetro. Essa função retorna um objeto Observation que contém as informações do clima da cidade especificada.

# weather = observation.weather: Aqui, o objeto weather é atribuído com o valor observation.weather. O objeto weather contém informações detalhadas sobre o clima da cidade.

# temperature = weather.temperature('celsius')['temp']: Nesta linha, a temperatura atual é extraída do objeto weather. O método temperature() é chamado, especificando 'celsius' como parâmetro para obter a temperatura em graus Celsius. O valor da temperatura é então armazenado na variável temperature.

# print(f"A temperatura atual em {city} é de {temperature: .1f}ºC."): Por fim, essa linha imprime a temperatura atual em graus Celsius para a cidade especificada. Utiliza {} para indicar onde serão inseridos os valores das variáveis. Utilizando uma f-string, o valor da cidade e da temperatura são inseridos na string de saída, que é exibida no console. O .1f formata o valor de temperatura para exibir apenas uma casa decimal. E ºC, que indica a unidade de medida da temperatura (graus Celsius).




