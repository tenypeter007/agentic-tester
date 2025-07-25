from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from agent.prompts import get_prompt
from agent.tools import selenium_executor

llm = ChatOpenAI(temperature=0.2)

tools = [
    Tool(
        name="Run Selenium Test",
        func=selenium_executor,
        description="Executes generated Selenium test script."
    )
]

def generate_test_for_url(url):
    prompt = get_prompt(url)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
    return agent.run(prompt)