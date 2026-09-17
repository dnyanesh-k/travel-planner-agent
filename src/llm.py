
import os
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model

model = os.environ['MODEL']
model_provider = os.environ['MODEL_PROVIDER']

llm = init_chat_model(model=model, model_provider=model_provider)

# create tavily search tool
search_tool = TavilySearch(max_results=5, topic="general")