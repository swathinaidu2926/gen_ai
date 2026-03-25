from gemini_api import get_response

user_input = input("Enter your question: ")
response = get_response(user_input)

print("AI Response:", response)