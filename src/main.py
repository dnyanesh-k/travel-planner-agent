from graph import create_graph

app = create_graph()

while True:

    # get the user input
    user_input = input(">>> ")

    if user_input in ['ecxit', 'quit']:
        break

    # create a state
    state = {"user_request": user_input}

    response =  app.invoke(state)
    print(response)