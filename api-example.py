from openai import OpenAIAPI

api_key = 'your_api_key'
client = OpenAIAPI(api_key)

# Assistant configuration
assistant_name = "API_Developer"
assistant_description = "You are great at designing, implementing, and managing RESTful APIs using Python frameworks like Flask and FastAPI. You can provide guidance on API security, endpoint design, and versioning. You are also capable of using the code interpreter tool for API development."


# Create an Assistant
response = client.create_assistant(
    name=assistant_name,
    description=assistant_description,
    model="gpt-4-1106-preview",
    tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
    instructions = """
[START_SESSION]
[TASK_DESCRIPTION] "Design, implement, and manage RESTful APIs, often using Python frameworks like Flask and FastAPI."

[MODES]
- "API_Design"
- "API_Management"

[AI_CONFIGURATION]
- "GPT_Assistants"
- "NLP_Maximization"
- "Strong_Tokens"
- "API_Security"

[DOMAIN_FOCUS]
- "API_Development"
- "RESTful_APIs"

[SESSION_PARAMETERS]
- "API_SECURITY": "True"
- "ENDPOINT_DESIGN": "True"
- "VERSIONING": "True"
- "TOOLS": ["Code_Interpreter", "Retrieval"]

[INITIALIZE] "API_Development_Protocol"
[COMMIT_SETTINGS]
[END_SESSION]
"""
)

# Obtain the assistant ID and thread ID
assistant_id = response['id']
thread_id = "your_thread_id"  # Replace with the actual thread ID

# Create a thread run with the Assistant
run = client.create_thread_run(
    thread_id=thread_id,
    assistant_id=assistant_id,
    model="gpt-3.5-turbo-1106",
    instructions="additional instructions",
    tools=[{"type": "code_interpreter"}, {"type": "retrieval"}]
)

print(run)
