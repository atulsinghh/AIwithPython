from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
model = Ollama(model="llama3.2")
# The above code imports the Ollama model and ChatPromptTemplate from LangChain.
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
print("domminos")
chain.invoke({"reviews":["Domminos"], "question":" What is the best Pizza place in town?"})

result = chain.invoke({"reviews":["domminos"], "question":" What is the best Pizza place in town?"})
print(result)
# This code uses LangChain to create a simple question-answering chain using the Ollama model.
# It defines a prompt template that includes a context of reviews and a question to answer.
