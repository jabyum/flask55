from flask import Flask, render_template, request
# создаем объект
app = Flask(__name__)
# @app.route("/") # urls
# def hello(): # views
#     test = "а это информация с бэка"
#     return render_template("index.html", info=db)
# @app.route("/user/<int:pk>/profile/<string:name>")
# def user_info(pk, name):
#     if pk in db.keys():
#         return {name:pk}
#     else:
#         return "юзер не найден"
@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        front_question = request.form.get("question")
        front_main_text = request.form.get("main_text")
        print(front_question)
        print(front_main_text)
        return render_template("add_question.html")
    else:
        return render_template("index.html")

app.run(debug=True)