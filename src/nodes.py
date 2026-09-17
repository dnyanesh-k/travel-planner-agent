from langchain.messages import SystemMessage, HumanMessage
from prompts import planner_system_prompt, planner_user_prompt, executor_system_message, executor_user_prompt
from state import State
from config import logger
from llm import llm, search_tool


def planner(state: State):
    """Break user request into search queries."""
    logger.info(f"Planning the research steps : {state['user_request']}")

    # send the user request and get the response
    response = llm.invoke([
        SystemMessage(content=planner_system_prompt),
        HumanMessage(content=planner_user_prompt.format(
            user_request=state['user_request']))
    ])

    logger.info(response.content)

    # process the reponse
    steps = []
    for line in response.content.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        # TODO: remove numbers from the line
        steps.append(line)

    logger.info(f"After cleansing we have {len(steps)} number of steps.")
    logger.info('')

    # return the updated state
    return {
        "plan": steps,
        "current_step": 0,
        "execution_result": []
    }


def executor(state: State):
    """Execute Tavily searches."""
    # get the state members
    step_index = state['current_step']

    step = state['plan'][step_index]

    total_steps = len(state['plan'])

    logger.info(
        f"Executor started execution job for step {step_index/total_steps}")
    logger.info(f"Started executing step = {step}")

    # send the request tpo model
    response = llm.invoke([
        SystemMessage(content="""
        Convert the current step into a valid web search query.
        return the search query only, nothing else.
        """),
        HumanMessage(content=step)
    ])

    search_query = response.content.strip()
    logger.info(f"Search query = {search_query}")

    # search on the internet for real time result
    result = search_tool.invoke(search_query)

    # grab all results
    parts = []
    for r in result['results']:
        title = r['title']
        content = r['content']
        parts.append(f"title: {title}, content: {content}")

    logger.info("Summarizing the results.")

    # get the results summurized
    summarized_results = llm.invoke([
        SystemMessage(content=executor_system_message),
        HumanMessage(content=executor_user_prompt.format(
            step=step, search_results=parts
        ))
    ])

    # create the final result of this step
    step_final_result = summarized_results.content.strip()

    # append the result to the state
    execution_result = list(state['execution_result'])
    execution_result.append(
        f"step: {step}]\nresult: {step_final_result}"
    )

    return {
        "execution_result": execution_result,
        "current_step": step_index + 1
    }

def final_result(state: State):
    """Synthesize final itinerary."""
    pass


def route(state: State):
    """Decide: aggregate or refine."""
    pass
