# tools.py
from langchain.tools import Tool
from datetime import datetime

def _get_current_time(input: str = "") -> str:
    """Returns the current time as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _say_hello(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}! How can I help you today?"

# Create Tool objects for compatibility with ConversationalAgent
get_current_time_tool = Tool(
    name="get_current_time",
    description="Returns the current date and time. No input required.",
    func=_get_current_time
)

say_hello_tool = Tool(
    name="say_hello",
    description="Greets the user by name. Input should be the user's name.",
    func=_say_hello
)

TOOLS = [get_current_time_tool, say_hello_tool]
