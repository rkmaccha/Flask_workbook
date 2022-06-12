
from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    if request.method=="POST":
        sepLen= request.form['sepallength']
        sepWid= request.form['sepalwidth']
        petLen= request.form['petallength']
        petWid= request.form['petalwidth']

        user_data = [[float(sepLen),float(sepWid),float(petLen),float(petWid)]]

        log_reg_model = pickle.load(open('iris_test.pkl','rb'))
        prediction = log_reg_model.predict(user_data)[0]
    return render_template('index.html', pred = prediction)



if __name__ =="__main__":
    app.run(debug=True)