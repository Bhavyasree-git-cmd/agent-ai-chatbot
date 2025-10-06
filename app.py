from flask import Flask, render_template, request

app = Flask(__name__)

class SimpleAgent:
    def __init__(self):
        self.knowledge = {
            "hello": "Hi there! How can I help you?",
            "bye": "Goodbye! Have a nice day.",
            "name": "I am your AI agent."
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        return self.knowledge.get(user_input, "I don't understand, can you rephrase?")

agent = SimpleAgent()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["query"]
        if user_input.lower() == "exit":
            response = "Goodbye!"
        else:
            response = agent.respond(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
