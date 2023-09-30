# Python ChatBot

This project is a Python ChatBot that integrates various APIs to provide information and perform specific tasks. It offers a graphical user interface (GUI) for interacting with the ChatBot and exploring its functionalities.

## Requirements

- Python 3.x
- Libraries: `chatterbot`, `requests`, `tk`, `sqlite3`, `datetime`

## Project Structure

```
source/ (main folder)
│
├── chatbot/
│ ├── data/
│ │ ├── feedback.db
│ │
│ ├── database/
│ │ ├── databaseconfig.py
│ │
│ ├── databaseAPI/
│ │ ├── config.py
│ │
│ ├── menu/
│ │ ├── gui.py
│ │
│ ├── init.py
│ ├── api_functions.py
│ ├── bot.py
│ ├── utils.py
│
├── main.py
```

## How to Use

1. **Installing Dependencies**:
   Make sure all the required libraries are installed by running the following command in the root directory of the project:

   ```bash
   pip install -r requirements.txt
   ```

2. **Starting the Project**:

   To start the project, run the following command in the root directory of the project:

   ```bash
   python main.py
   ```

   This will open a command-line interface where you can choose between the Graphical User Interface (GUI) or advanced email generation and verification functionalities.

3. **Graphical User Interface (GUI)**:

   - Choose the "Start GUI" option in the menu.
   - The GUI interface will allow you to converse with the ChatBot and explore its functionalities.
   - You can copy the ChatBot's responses by clicking the "Copy" button and save the conversation history to a text file.

## User Feedback

The project allows users to provide feedback on the ChatBot's responses, including ratings and comments. The feedback is stored in a SQLite database for future analysis.

## Final Considerations

This project provides a solid and flexible foundation for developing high-quality ChatBots. You can customize and expand the system by adding additional features and refining natural language processing models as needed.

Enjoy chatting with the ChatBot!

## Notes:

Make sure the necessary data, such as the `feedback.db` file, is present in the appropriate folders before running the system. Also, ensure that Python virtual environments (venv) are properly set up to avoid dependency conflicts.

---