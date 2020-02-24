import connexion
from flask import render_template


app = connexion.App(__name__,
                    specification_dir="./",
                    host="127.0.0.1",
                    port=8080)

app.add_api('swagger.yaml')


@app.route("/")
def index():
    """
    This function just responds to the browser URL
    127.0.0.1:8080/
    :return:        the rendered template "index.html"
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
