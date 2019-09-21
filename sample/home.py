from flask import Flask, render_template, request
import json

''' get the country name and return the capital of country by reading json file '''
def find_Capital(coun):
    counter=0
    data=json.load(open(r"templates\country_with_capitals.json"))
    coun=coun.lower()
    coun=coun.split()
    coun=' '.join([x.capitalize() for x in coun])
    str1=coun
    for i in data:
        if i['country']==str1:
            return (i['city'])
            break
        else:
            continue
    if counter==len(data):
        return ("not found")

app = Flask(__name__)   #app flask

'''redering entercountry.html file '''
@app.route('/')
def countryfile():
   return render_template('entercountry.html')

''' Request for input and fetch the result from country.py '''
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      '''fetch input from entercountry '''
      result = request.form['Country']
      result2 = str(find_Capital(result))
      if result2 == 'None':
          ''' if result2 is null return message '''
          return "<h1>:please search for valid country :)</h1> "
      else:
          ''' ***Display result*** '''
          return "<br><br><br><br><br><br><br><br><br><br><h1 align='center'>Capital:  "+result2+"</h1>"
      #return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
