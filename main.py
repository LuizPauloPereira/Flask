from flask import Flask
from hello.views import hello
from tarefas.views import tarefas

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(tarefas)

if __name__ == '__main__':
    app.run(debug=True, port=8080)