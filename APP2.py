from flask import Flask, render_template, request, jsonify
import cohere


app = Flask(__name__)

co = cohere.Client('qVXNWHUtUYvra3zAjvtsBscbI9jIZmV4xsS16ReR')

def generate_response(user_message):
    # Use Cohere's text generation API to generate a response
    response =  co.generate(
      prompt= user_message,
      max_tokens=100
    )
    return response[0]

@app.route('/')
def index():
    return render_template('healthiq_interface.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '')
    bot_response = generate_response("You are a gym fitness trainer, Help the user in staying fit by Answering the following:" + user_message)
    return jsonify({'answer': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
