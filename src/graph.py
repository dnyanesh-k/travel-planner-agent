import os
import logging

from config import setup_logging
from langgraph.graph import StateGraph, START, END
from state import State
from nodes import planner, executor, final_result, route

# Run the logging configuration first thing
setup_logging()

# create a logger
logger = logging.getLogger(__name__)

model = os.environ['MODEL']
model_provider = os.environ['MODEL_PROVIDER']

logger.info(f"LangChain model {model} successfully initialized!")

def create_graph():
    # create a graph
    graph = StateGraph(State)


    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.add_node("final", final_result)

    # add the edges 
    # from START -> planner -> executor -> final with conditional adge to reexecute the executor based on condition
    graph.add_edge(START, "planner")
    graph.add_edge("planner", "executor")
    graph.add_conditional_edges("executor", route, {"executor": "executor", "final": "final"})
    graph.add_edge("final", END)

    # compile the graph
    app = graph.compile()

    # create a graph image
    image = app.get_graph().draw_mermaid_png()
    with open('src/graphs/image.png', 'wb') as file:
        file.write(image)

    return app