from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
import os

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from langchain_tavily import TavilySearch
from tavily import TavilyClient

class Source(BaseModel):
    """Scheme for a source used by the agent."""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Scheme for agent response with answer and sources"""
    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="The list of sources used to generate the answer")

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet.
    Args:
        query: The query to search for
    Returns:
        The search result   
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key = os.getenv("NVIDIA_API_KEY"),
    base_url = "https://integrate.api.nvidia.com/v1",
)

tools = [search]

# tools = [TavilySearch()]

agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="What are the best cities in the world to live in in terms of top things to consider by a woman?")})
    print(result)

if __name__ == "__main__":
    main()
