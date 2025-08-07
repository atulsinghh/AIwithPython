from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType



llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key="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"  # Replace with your key
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