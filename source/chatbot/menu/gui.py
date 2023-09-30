# gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox, Scrollbar

class ChatbotGUI:
    def __init__(self, root, chatbot_response_callback):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("500x600")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="#1a1a2e")

        # Cabeçalho
        header = tk.Label(root, text="ChatBot", bg="#1a1a2e", fg="#e94560", font=("Arial", 24, "bold"))
        header.pack(pady=20)

        self.chat_window = tk.Text(root, bd=1, bg="#0f3460", fg="#e94560", font=("Arial", 16), wrap=tk.WORD)
        self.chat_window.place(x=25, y=80, height=420, width=450)
        self.chat_window.configure(state=tk.DISABLED)

        scrollbar = Scrollbar(self.root, command=self.chat_window.yview, bg="#0f3460")
        scrollbar.place(x=475, y=80, height=420)
        self.chat_window['yscrollcommand'] = scrollbar.set

        self.message_entry = tk.Entry(root, bg="#0f3460", fg="#e94560", font=("Arial", 16), relief=tk.GROOVE, borderwidth=2)
        self.message_entry.place(x=25, y=520, height=50, width=350)
        self.message_entry.bind("<Return>", self.send_message_event)

        self.send_button = tk.Button(root, text="Enviar", bg="#e94560", activebackground="#9a031e", fg='#ffffff', font=("Arial", 12), relief=tk.GROOVE, borderwidth=2, command=self.send_message)
        self.send_button.place(x=385, y=520, height=50, width=90)

        self.chatbot_response_callback = chatbot_response_callback

    def send_message_event(self, event=None):
        self.send_message()

    def send_message(self):
        user_message = self.message_entry.get()
        if user_message:
            self.chat_window.configure(state=tk.NORMAL)
            self.chat_window.insert(tk.END, "\nVocê: " + user_message)
            self.chat_window.configure(state=tk.DISABLED)
            self.message_entry.delete(0, tk.END)
            try:
                bot_response = self.chatbot_response_callback(user_message)
                self.chat_window.configure(state=tk.NORMAL)
                self.chat_window.insert(tk.END, "\nChatBot: " + bot_response)
                self.chat_window.configure(state=tk.DISABLED)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root, lambda message: "Resposta padrão do chatbot")
    root.mainloop()
