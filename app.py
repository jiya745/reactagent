import os

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "your-key"

from langgraph.prebuilt import create_react_agent

def search(query: str):
    """Call to surf the web."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."

# Use OpenAI model
agent = create_react_agent("openai:gpt-3.5-turbo", tools=[search])

# Invoke and get response
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# Access AI response and print only the content
ai_response = response.get("content", "")  # Adjusting in case content key is not found
print(ai_response)
