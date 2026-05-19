from flaskxyz import Flaskswxq

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "AI DevOps App Running-v13"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)