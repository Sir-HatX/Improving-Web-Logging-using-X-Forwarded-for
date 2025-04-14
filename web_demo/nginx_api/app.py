from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Flask API Test</title>
</head>
<body>
    <h2>Test Flask API</h2>
    <h3>GET Request</h3>
    <button onclick="fetchData()">Send GET Request</button>
    <pre id="getResponse"></pre>

    <h3>POST Request</h3>
    <form onsubmit="sendPost(event)">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Send POST Request</button>
    </form>
    <pre id="postResponse"></pre>

    <script>
        function fetchData() {
            fetch('/')
                .then(response => response.json())
                .then(data => document.getElementById('getResponse').textContent = JSON.stringify(data, null, 2))
                .catch(error => console.error('Error:', error));
        }

        function sendPost(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            fetch('/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name: name })
            })
            .then(response => response.json())
            .then(data => document.getElementById('postResponse').textContent = JSON.stringify(data, null, 2))
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    source_ip = request.headers.get("X-Real-IP", request.remote_addr)
    return jsonify({
        "message": "Flask API is running!",
        "headers": dict(request.headers),
        "source_ip": source_ip
    })

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    source_ip = request.headers.get("X-Real-IP", request.remote_addr)
    return jsonify({
        "message": "POST request received",
        "received_data": data,
        "source_ip": source_ip
    })

@app.route("/test", methods=["GET"])
def test_page():
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
