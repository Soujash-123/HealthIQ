from flask import Flask, render_template, request, jsonify
import openai
from imageGEN import imageGeneration 
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

def chat_with_fitness_bot(user_info, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": user_info},
            {"role": "assistant", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

@app.route('/')
def index():
    return render_template('healthiq_interface.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '')
    
    if 'show' in user_message.lower():
        try:
            image_url = imageGeneration(user_input)
            if image_url:
                bot_response = ("DALL-E Image URL:" + image_url)
                print(image_url)
            else:
                bot_response = ("Failed to generate image from DALL-E.")
        except:
            bot_response = ("The Command goes against our policies. Please be more specific. For example: Show me how to do a jumping jack exercise.")
    # Use the chat_with_fitness_bot function to get the response

    bot_response = chat_with_fitness_bot(user_message, "fitness")
    
    return jsonify({'answer': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
