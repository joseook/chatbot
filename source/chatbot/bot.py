import tkinter as tk
from gui import ChatbotGUI
import database.databaseconfig as dbconfig
import api_functions as api
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Inicializando o banco de dados
dbconfig.initialize_db()

class ChatbotMain:
    def __init__(self):
        self.chatbot = ChatBot('MeuChatBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train('chatterbot.corpus.portuguese')
        self.trainer.train('data.training_data')

        self.root = tk.Tk()
        self.gui = ChatbotGUI(self.root, self.process_user_input)
        self.root.mainloop()

    def process_user_input(self, user_input):
        # Lógica para determinar qual função da API chamar com base na entrada do usuário.
        
        if "clima" in user_input:
            city = user_input.split()[-1]  # supondo que o nome da cidade seja a última palavra
            return api.get_weather(city)
        
        elif "cotação" in user_input:
            words = user_input.split()
            if len(words) >= 3:
                base_currency = words[-2]
                target_currency = words[-1]
                return api.get_exchange_rate(base_currency, target_currency)
            else:
                return "Por favor, especifique as moedas para a cotação. Exemplo: cotação USD BRL"
        
        elif "notícia" in user_input:
            return api.get_latest_news()
        
        elif "geolocalização" in user_input:
            ip = user_input.split()[-1]
            return api.get_geolocation(ip)
        
        elif "filme" in user_input or "série" in user_input:
            name = " ".join(user_input.split()[1:])
            return api.get_movie_info(name)
        
        elif "rota" in user_input:
            words = user_input.split()
            if "para" in words:
                idx = words.index("para")
                origin = " ".join(words[1:idx])
                destination = " ".join(words[idx+1:])
                return api.get_route_directions(origin, destination)
            else:
                return "Por favor, especifique a origem e o destino. Exemplo: rota São Paulo para Rio de Janeiro"
        
        else:
            response = self.chatbot.get_response(user_input)
            return str(response)

    def run_chatbot(self):
        self.root = tk.Tk()
        self.gui = ChatbotGUI(self.root, self.process_user_input)
        self.root.mainloop()

# Executando o chatbot
if __name__ == "__main__":
    chatbot = ChatbotMain()
    chatbot.run_chatbot()
