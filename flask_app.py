from flask import Flask, request

app = Flask(__name__)

@app.route("/prompt", methods=["POST"])
def prompt():
    # Get the prompt from the request body.
    gcp_prompt
    prompt = request.json[gcp_prompt]

    # Generate an output based on the prompt.
    output = generate_output(prompt)

    # Return the output to the client.
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)