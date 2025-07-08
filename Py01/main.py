from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatMessagePromptTemplate
model = OllamaLLM("llama3.2") 
template = """
YOu are an expert in answering question about a pizza restaturant

Here are some relevant reviews: {reviews}

Here is the questions to answer: {question}

"""
prompt = ChatMessagePromptTemplate(template)
chain = prompt|model

chain.invoke({"reviews":[], "question":" What is the best Pizza place in town?"})

