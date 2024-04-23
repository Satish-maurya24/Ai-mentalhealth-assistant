import google.generativeai as genai

genai.configure(api_key="AIzaSyBv9n8OkE2tbitATkApVA9_b35JvSd_uY4")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])







def generate_response_action(mental_health_state):
    # Prompt to generate response action based on mental health state
    prompt = f"first chat with the user if they want to know their mental state then help them finding it and then ask for sugeestion" \
             f" and then sugest in this format , the suggested actions are: "
    # Generate response action using GPT-3
    convo.send_message(f'{prompt}')

    # Extract and return the generated response action
    response_action = convo.last.text
    return response_action
