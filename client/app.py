from flask import Flask,render_template,request
import requests

app=Flask(__name__)


locations=requests.get('http://127.0.0.1:5000/get_location_names')
locations=locations.json()['locations']
pred_price=None
@app.route('/',methods=['POST','GET'])
def hello():
    global locations


    return render_template('app.html',pred_price=None,locations=locations)

@app.route('/send_data',methods=['GET','POST'])
def send_data():
    global locations

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

        print(area,bhk,bath,balcony,location)


        pred_price= requests.post('http://127.0.0.1:5000/predict_home_price',data=data)

        final =str(pred_price.json()['estimated_price']) + " Lakh"


        print(pred_price.json()['estimated_price'])
        return render_template('app.html',pred_price=final,locations=locations)

    else:
        return render_template('app.html',pred_price=None,locations=locations)

if __name__=='__main__':

    app.run(port=51,debug=True)