import tkinter as tk
from chatbot.gui import ChatbotGUI  # Importa a classe ChatbotGUI do arquivo gui.py
from chatbot.bot import Bot  # Importa a classe Bot do arquivo bot.py
from chatbot import databaseconfig as dbconfig  # Importa o módulo databaseconfig como dbconfig
from chatbot import api_functions as api

# Inicializando o banco de dados
dbconfig.initialize_db()

class ChatbotMain:
    def __init__(self):
        self.root = tk.Tk()
        self.gui = ChatbotGUI(self.root, self.process_user_input)
        self.bot = Bot()  # Inicializa o chatbot
        self.root.mainloop()

    def process_user_input(self, user_input):
        # Lógica para processar a entrada do usuário
        bot_response = self.bot.get_response(user_input)
        return bot_response

# Executando o chatbot
if __name__ == "__main__":
    ChatbotMain()
