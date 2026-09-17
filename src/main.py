from dotenv import load_dotenv
from graph import create_graph
from config import setup_logging

load_dotenv()

# Run the logging configuration first thing
setup_logging()

app = create_graph()

while True:

    # get the user input
    user_input = input(">>> ")

    if user_input in ['exit', 'quit']:
        break

    # create a state
    state = {"user_request": user_input}

    response =  app.invoke(state)
    print(response)