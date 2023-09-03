from flask import Flask, request
from flask_cors import CORS
import openai

app = Flask(__name__)

CORS(app)

openai.api_key = "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"
msgList = [
    {
        "name": "John",
        "msg": [],
    },
    {
        "name": "Jane",
        "msg": [],
    },
    {
        "name": "Kevin",
        "msg": [],
    },
    {
        "name": "Andrew",
        "msg": [],
    },
]


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
