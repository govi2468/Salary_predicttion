
from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('LinearReg (1).pkl','rb'))

@app.route('/',methods = ['GET'])
def Home():
    return render_template('index.html', message='Welcome to the Home Page!')

@app.route('/salary_predict', methods=['POST'])
def salary_predict():
    if request.method == 'POST':
        Years = int(request.form['YearsExperience'])
        prediction = model.predict([[Years]])
        if Years >= 0 and Years <= 100:
            return render_template('index.html', prediction_text="The Predicted salary in Rs. {} lakhs".format(prediction[0]))
        else:
            return render_template('index.html', prediction_text="You have entered wrong years of exprieance")


if __name__ == '__main__':
    app.run(debug=True)