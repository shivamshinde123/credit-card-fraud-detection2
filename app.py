from flask import Flask, render_template, request
import jsonify
from prediction_service.prediction import api_response, form_response
import os

webapp_root = "webpage"

static_dir = os.path.join(webapp_root, "static")
templates_dir = os.path.join(webapp_root, "templates")


app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        try:
            if request.form:
                data_requirement = dict(request.form)
                prediction = form_response(data_requirement)
                return render_template('index.html', prediction=prediction)

            elif request.json:
                data_requirement = dict(request.json)
                prediction = api_response(data_requirement)
                return jsonify(prediction)

        except Exception as e:
            print(e)
            return render_template('404.html', error=e)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
