from state import State

def planner(state: State):
    """Break user request into search queries."""
    print(f"===inside planner {state}")

def executor(state: State):
    """Execute Tavily searches."""
    pass

def final_result(state: State):
    """Synthesize final itinerary."""
    pass

def route(state: State):
    """Decide: aggregate or refine."""
    pass