import pickle
from flask import Flask,render_template,request

#create object of class Flask
app=Flask(__name__)
#craeting varible to load our model into
model=pickle.load(open('model.pkl','rb'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET","POST"])
def predict():
    # features=[[request.form.get("area")],[request.form.get("bedroom")],[request.form.get("bathroom")],[request.form.get("stories")],[request.form.get("mainroad")],[request.form.get("basement")],[request.form.get("hotwaterheating")],[request.form.get("airconditioning")],[request.form.get("parking")],[request.form.get("prefarea")],[request.form.get("furnishingstatus")]]#worng assumption since ndim=2
    
    try:
        features=[[request.form.get("area"),request.form.get("bedroom"),request.form.get("bathroom"),request.form.get("stories"),request.form.get("mainroad"),request.form.get("guestroom"),request.form.get("basement"),request.form.get("hotwaterheating"),request.form.get("airconditioning"),request.form.get("parking"),request.form.get("prefarea"),request.form.get("furnishingstatus")]]
        
        prediction=model.predict(features)
        output=round(prediction[0],2)#till 2 decimals
        #print(output)
        return render_template("index.html",prediction_text=f"Predicted price of housing is Rs. {output}/-")
    except:
        return render_template("index.html",prediction_text=f"Invalid input!!!Try again.")


if __name__=="__main__":
    app.run(debug=True)
