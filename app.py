from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def sales_predict():
    tv = float(request.form.get("TV Ad Budget"))
    radio = float(request.form.get("Radio Ad Budget"))
    newspaper = float(request.form.get("Newspaper Ad Budget"))

    # prediction
    result = int(model.predict(np.array([[tv, radio, newspaper]])))  # Changed shape to (1, 3)
    return "sales will be = " + str(result)

if __name__ == '__main__':
    app.run(debug=True)
