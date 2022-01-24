# Learning- Complete ML model
This is a project that is meant to learn best in industry practices about Linear Regression
 #### Making the model:
 - We Preprocess by dropping irrelevant columns, and fill the na values where possible and drop some na values
 - We clean the columns making the values as same represenation and casting them into required datatypes
 - Add some columns and grouping some rows for better prediction
 - Removing outliers in data using common and domain knowledge
 - Using dummies to do one hot encoding of categorical column 'location'
 - Make the model
 
 #### Making the server
 - The server is made using flask in python (The models are not copied again in the server folder)
 - The server has a main page named server.py that redirects the requests and the prediction and other data processing id done in the util.py page
 - '/predict_home_price' is the route that recives the requests and returns a json with the key 'estimated price' 
 - We also have the /get_loation_names' that returns the location names with key value 'location' which can be used to be displayed in the form as drop down 
 - the util has two methods one loads the artifacts i.e the odel and column names(column names are necessary while predicting as our model has dummies)
 - The other method predicts the estimated price
 
 #### Making the client side
 - The client side is also made using flask
 - The app.py redirects requests, we send the variable pred_price to the html page usign jinja2 of flask
 - The html page contains the form which when submitted calls '/send_data' routine
 - The send_data collects the form data converts it to dictionary and sends it to the flask server usign requests.post method
 - The app first loads the location name and the location names are added using jinja template


#### Changes that can be done
- Making the UI better
 
 
 
 
 The project is a learning project.The model and server is inspired by the [Youtube tutorial](https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg). The client side was implemented using javascript in the tutorial, which I implemented in flask instead to keep the entire project in python.
