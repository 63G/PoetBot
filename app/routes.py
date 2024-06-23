from openai import OpenAI
import os
from flask import request, render_template, jsonify

# Create an OpenAI client instance
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/ask', methods=['POST'])
    def ask():
        data = request.get_json()
        user_message = data.get('message', '')

        # print(f"Received message from user: {user_message}")

        try:
            system_message = "You are a helpful assistant that explains Arabic poetry using references from the book Kitab al-Aghani. Please format the response with clear sections and line breaks to make it easy to read. always communicate in Arabic. If the user Said 'Muath' or 'معاذ'  tell him a praising poem. if the user sayd 'Made in Abyss' tell him watch it with Muath before he gets bored! if the user enters 'Aisha' or 'عائشة' send out a flirting poem"
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=1000,
                n=1,
                stop=None,
                temperature=0.7
            )
            # print(f"API response: {response}")

            # Format the response content
            bot_response = response.choices[0].message.content.strip().replace('\n', '<br>').replace('**', '<strong>').replace('</strong>', '<strong>')
            # print(f"Extracted and formatted bot response: {bot_response}")

        except Exception as e:
            print(f"Error generating response from OpenAI: {e}")
            # traceback.print_exc()  # This will print the full traceback of the exception
            bot_response = "Sorry, I couldn't process your request at the moment."

        return jsonify({"message": bot_response})

# if __name__ == "__main__":
#     from flask import Flask
#     app = Flask(__name__)
#     init_app(app)
#     app.run(debug=False)
