from typing import TypedDict

class State(TypedDict):
    # what user requests
    user_request: str

    # the actual plan
    plan: list[str]

    # current executing step
    current_step: int

    # result of execution of step
    execution_result: list[str]

    # final result
    final_result: str