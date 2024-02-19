from flask import *
from users import *
app=Flask(__name__)

app.config['SECRET_KEY']='87c725f6be51b16e19446e14b59149e7'

Tests=[
    {
        'ID':0,
        'name':'Aadi',
        'age':19,
        'UID':2022300113
    },
    {
        'ID':1,
        'name':'Siddhesh',
        'age':19,
        'UID':2022300114
    },
    {
        'ID':2,
        'name':'Areeb',
        'age':19,
        'UID':2022300109
    }
]

@app.route("/")
def mai():
    return render_template("test.html")

@app.route("/SignUp",methods=['POST','GET'])
def RegiRock():
    form=SignUpForm()
    if form.validate_on_submit():
        flash("Account created successfully!!!",'success')
        n_name=form.name.data
        n_age=int(form.age.data)
        n_UID=int(form.UID.data)
        n_ID=Tests[-1]['ID']+1
        
        new_obj={
            'ID':n_ID,
            'name':n_name,
            'age':n_age,
            'UID':n_UID
        }
        Tests.append(new_obj)
        print(form.UID)
        return redirect(url_for('test'))
    return render_template("Regirock.html",form=form)



@app.route("/test",methods=['GET','POST'])
def test():
    if(request.method=='GET'):
        return jsonify(Tests)
    else:
        'Nothing found',404
    if(request.method=='POST'):
        n_name=request.form['name']
        n_age=request.form['age']
        n_UID=request.form['UID']
        n_ID=Tests[-1]['ID']+1
        
        new_obj={
            'ID':n_ID,
            'name':n_name,
            'age':n_age,
            'UID':n_UID
        }
        Tests.append(new_obj)
        return jsonify(Tests),201
    
if(__name__=='__main__'):
    app.run(debug=True)
        
