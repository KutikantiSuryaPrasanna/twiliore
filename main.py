from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from urllib.parse import quote as url_quote

from chatgpt import GPT

app = Flask(__name__)



@app.route("/bot_gpt", methods=["POST"])
def bot_gpt():

    chat_model = GPT(str(request.values.get("WaId", "")))
    incoming_msg = request.values.get("Body", "")
    answer = chat_model.bot(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(answer)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
