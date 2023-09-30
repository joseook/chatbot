import requests
from datetime import datetime
from databaseAPI.config import WEATHER_API_KEY
from databaseAPI.config import EXCHANGE_RATE_API_KEY
from databaseAPI.config import NEWS_API_KEY
from databaseAPI.config import GEOLOCATION_API_KEY
from databaseAPI.config import OMDB_API_KEY
from databaseAPI.config import GOOGLE_MAPS_API_KEY

#API CLIMA
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "pt"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        sys = data["sys"]

        # Convertendo o timestamp do nascer e pôr do sol para o formato HH:MM
        sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime('%H:%M')
        sunset = datetime.fromtimestamp(sys["sunset"]).strftime('%H:%M')

        # Construindo a resposta
        response_text = (
            f"Clima em {city}:\n"
            f"- Condição: {weather['description'].capitalize()}\n"
            f"- Temperatura: {main['temp']}°C\n"
            f"- Sensação térmica: {main['feels_like']}°C\n"
            f"- Máxima: {main['temp_max']}°C\n"
            f"- Mínima: {main['temp_min']}°C\n"
            f"- Umidade: {main['humidity']}%\n"
            f"- Velocidade do vento: {wind['speed']} m/s\n"
            f"- Direção do vento: {wind['deg']}°\n"
            f"- Nascer do sol: {sunrise}\n"
            f"- Pôr do sol: {sunset}\n"
        )
        return response_text
    else:
        return f"Erro ao obter informações do clima para {city}."

# API COTAÇÃO
def get_exchange_rate(base_currency, target_currency, amount=1, list_supported=False):
    base_url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(base_url, api_key)
    data = response.json()
    api_key = "EXCHANGE_RATE_API_KEY"
    # Listar moedas suportadas
    if list_supported:
        supported_currencies = ", ".join(data["rates"].keys())
        return f"Moedas suportadas: {supported_currencies}"

    # Verificar se a moeda alvo é suportada
    if target_currency not in data["rates"]:
        return f"A moeda {target_currency} não é suportada. Use a opção 'list_supported=True' para ver todas as moedas suportadas."

    rate = data["rates"][target_currency]
    converted_amount = round(amount * rate, 2)
    last_updated = data["time_last_updated"]

    return (
        f"Taxa de câmbio atual (atualizada em {last_updated}): 1 {base_currency} é igual a {rate} {target_currency}.\n"
        f"{amount} {base_currency} é aproximadamente {converted_amount} {target_currency}."
    )

# Testes
print(get_exchange_rate("USD", "BRL", 10))
print(get_exchange_rate("USD", "XYZ", 10))  # Moeda não suportada
print(get_exchange_rate("USD", "BRL", 10, list_supported=True))

# API NEWS
def get_latest_news(country="br", category="general"):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "category": category,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["status"] == "ok":
        articles = data["articles"][:5]  # Pegando as 5 principais notícias
        news_list = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            description = article['description']
            url = article['url']
            news_item = f"- {title} ({source})\n  {description}\n  [Leia mais]({url})"
            news_list.append(news_item)
        return "\n\n".join(news_list)
    else:
        return "Erro ao obter as últimas notícias."

# API GEOLOCALIZAÇÂO

def get_geolocation(ip_address):
    base_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={GEOLOCATION_API_KEY}&ip={ip_address}"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200 and 'ip' in data:
        city = data.get('city', 'Desconhecido')
        country = data.get('country_name', 'Desconhecido')
        latitude = data.get('latitude', 'Desconhecido')
        longitude = data.get('longitude', 'Desconhecido')
        return (
            f"Informações de Geolocalização para o IP {ip_address}:\n"
            f"- Cidade: {city}\n"
            f"- País: {country}\n"
            f"- Latitude: {latitude}\n"
            f"- Longitude: {longitude}"
        )
    else:
        error_message = data.get('message', 'Erro desconhecido.')
        return f"Erro ao obter informações de geolocalização: {error_message}"

# API FILMES E SERIES

def get_movie_info(movie_name):
    base_url = f"http://www.omdbapi.com/?t={movie_name}&apiKey={OMDB_API_KEY}"
    response = requests.get(base_url)
    data = response.json()

    if data['Response'] == 'True':
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        plot = data['Plot']
        director = data['Director']
        actors = data['Actors']
        imdb_rating = data['imdbRating']
        return (
            f"Informações sobre '{title}':\n"
            f"- Ano: {year}\n"
            f"- Gênero: {genre}\n"
            f"- Diretor: {director}\n"
            f"- Atores principais: {actors}\n"
            f"- Descrição: {plot}\n"
            f"- Avaliação no IMDb: {imdb_rating}/10"
        )
    else:
        error_message = data.get('Error', 'Erro desconhecido.')
        return f"Erro ao obter informações sobre o filme/série '{movie_name}': {error_message}"

# API DE ROTAS E TRANSITO

def get_route_directions(origin, destination, mode="driving"):
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        route = data['routes'][0]
        legs = route['legs'][0]
        distance = legs['distance']['text']
        duration = legs['duration']['text']
        start_address = legs['start_address']
        end_address = legs['end_address']
        steps = legs['steps']
        directions = "\n".join([step['html_instructions'] for step in steps])
        return (
            f"Rota de '{start_address}' para '{end_address}':\n"
            f"- Distância: {distance}\n"
            f"- Duração estimada: {duration}\n"
            f"- Instruções detalhadas:\n{directions}\n"
            f"(Modo de transporte: {mode})"
        )
    else:
        error_message = data.get('error_message', 'Erro desconhecido ao calcular a rota.')
        return error_message

