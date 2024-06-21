import openai
import os
from flask import request, render_template, jsonify

openai.api_key = os.getenv('OPENAI_API_KEY')

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/explain', methods=['POST'])
    def explain():
        data = request.get_json()
        poet = data.get('poet', '')

        prompt = f"اشرح المعنى في الشعر التالي من كتاب الأغاني: {poet}"

        response = openai.Completion.create(
            engine="text-davinci-004",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7
        )
        explanation = response.choices[0].text.strip()
        return jsonify({'explanation': explanation})
