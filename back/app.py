from flask import Flask, request
from flask_cors import CORS
import openai

app = Flask(__name__)

CORS(app)

openai.api_key = "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"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("POST")
        data = request.get_json()
        print(data)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": data["msg"]},
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
