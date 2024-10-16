import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBti8G1nmAcKJ39znvO0DQac4yNQ_u7aeQ")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = {
  "blocklist_categories": ["hate", "violence", "sexually_explicit"],  # Block strongly harmful content
  "blocklist_keywords": ["bomb", "weapon", "suicide", "harm", "illegal"],  # Block specific keywords
  "toxicity_threshold": 0.9,  # Stricter threshold for toxicity
  "profanity_threshold": 0.8,  # Stricter threshold for profanity
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings=safety_settings
)


chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("")

print(response.text)
