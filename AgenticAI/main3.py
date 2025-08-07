from langchain_huggingface import HuggingFaceEndpoint
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_huggingface import HuggingFaceEndpoint


llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",  # Replace with the desired model
    huggingfacehub_api_token="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",  # Your HuggingFace API token
    temperature=0.7,
    max_new_tokens=128
)


tools = load_tools(["llm-math"], llm=llm)

agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = "What is 29 * 37?"
response = agent_executor.invoke({"input": query})
print(response)
