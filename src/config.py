from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model

load_dotenv()

model = os.environ['MODEL'] 
model_provider = os.environ['MODEL_PROVIDER']


llm = init_chat_model(model=model, model_provider=model_provider)
