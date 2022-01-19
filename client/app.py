from flask import Flask,render_template,request
import requests

app=Flask(__name__)



@app.route('/')
def hello():
    return render_template('app.html',pred_price=None)

@app.route('/send_data',methods=['GET','POST'])
def send_data():

    if request.method=='POST':
        area=float(request.form.get('total_sqft'))
        bhk=int(request.form.get('bhk'))
        bath=int(request.form.get('bath'))
        balcony=int(request.form.get('balcony'))
        location=request.form.get('location')

        data={'total_sqft': area,
              'bhk' :bhk,
              'bath':bath,
              'balcony':balcony,
              'location' : location
            }


        pred_price= requests.post('http://127.0.0.1:5000/predict_home_price',data=data)

        final =str(pred_price.json()['estimated_price']) + " Lakh"




        print(pred_price.json()['estimated_price'])
        return render_template('app.html',pred_price=final)

    else:
        return render_template('app.html',pred_price=None)

if __name__=='__main__':

    app.run(port=51,debug=True)