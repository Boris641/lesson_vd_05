from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def website_1():
    content = {
        "link": "Кофе по-льежски"
    }

    return render_template("website_1.html", **content)


@app.route("/website_2/")
def website_2():
    content = {
        "link1": "Чай по-льежски"
    }

    return render_template("website_2.html", **content)






if __name__ == "__main__":
    app.run()
