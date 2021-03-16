from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def main():
    if(request.method == 'GET'):
        place = request.args.get('place', None)
        if(place):
            # return(redirect('http://localhost:3000'))
            # return(redirect('http://localhost:3000'))
            return('Goodbye')
    if(request.method == 'POST'):
        print(request.form['username'])
        print(request.form['password'])
        return('Hi')
    return('lul')


app.run(debug=True)
