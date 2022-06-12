#https://pypi.org/project/covid/

# c_data = covid.get_data()
# # print(c_data)

# c_df= pd.DataFrame(c_data)
# # print(c_df.head())
# print(c_df[c_df['country'] == "US"]['deaths'])

from flask import Flask,render_template,url_for,request
from covid import Covid
import pandas as pd 

covid = Covid()

app = Flask(__name__)

@app.route('/')
def home():
    country='United Kingdom'
    return render_template('index.html',data = country)


@app.route('/info',methods=['POST'])
def info():
    if request.method=="POST":
        # return 'Covid Details'
        country= request.form['country']

        #country = "United Kingdom"
        C_cases = covid.get_status_by_country_name(country)
        #print(C_cases['confirmed'])
    return render_template('index.html',data = C_cases)

if __name__ == "__main__":
    app.run(debug=True)