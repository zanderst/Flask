### Flask application to find the prime numbers of numbers in an url (format = http://127.0.0.1:5000/d/99)

from flask import Flask


app = Flask(__name__)


def isprime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    d = []
    for i in range(1, n+1):
        if isprime(i) and n % i == 0:
            d.append(i)
    return d

@app.route("/d/<int:n>")
def compile_divisors(n):
    if n <= 1:
        return "Please enter a positive number bruv"
    d = divisors(n)

    rstring = ", ".join(str(i) for i in d)
    return f"the prime divisors of {n} are: {rstring}"

if __name__ == "__main__":
    app.run(debug = True)


### write an app that shows values form the app object on one page and the request object on another

# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# # Route for displaying values from the app object
# @app.route('/')
# def app_values():
#     app_name = "random app name honey"
#
#     app_secret_key = "random secret key string"
#     return render_template('app_values.html', theappname=app_name, app_secret_key=app_secret_key)
#
# # Route for displaying values from the request object
# @app.route('/request_values')
# def request_values():
#     request_method = request.method
#     request_url = request.url
#     request_headers = dict(request.headers)
#     return render_template('request_values.html', request_method=request_method, request_url=request_url, request_headers=request_headers)
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def app_values():
#     name = "Whitby"
#     secret_key = "A long tim ago"
#
#     return render_template("testing_template.html", name=name, secret=secret_key)
#
#
# @app.route("/request_info")
# def request_info():
#     method_request = request.method
#     path_request = request.path
#     url_request = request.url
#     headers_request = dict(request.headers)
#     environ_request = request.environ
#
#
#     return render_template("request.html", method=method_request, path=path_request, url=url_request,
#                            headers=headers_request, environ=environ_request)
#
# if __name__ == "__main__":
#     app.run(debug=True)

