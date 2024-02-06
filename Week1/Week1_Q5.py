# Write an app that combines all the above apps (already done before in flasktest.py) witha  navigation bar that can switch between al the pages

from flask import Flask, render_template, request, current_app
import datetime, random

import flasktest
from flasktest import isprime, divisors, compile_divisors

app = Flask(__name__)

@app.route("/")
def combined():
   dt = datetime.datetime.now()
   ft = dt.strftime("%H:%M:%S")
   fd = dt.date()
   quotes = ["She'll suck on my pipe but only when ripe", "I like to smell fanny unless it belongs to Granny","light up your smoker, moterboat her", "Imagine my pleasure, when she measures my tether", "Sloppy seconds, when she beckons"]
   chosen = random.choice(quotes)
   return render_template("q5.html", time=ft, date=fd,quote =chosen)

@app.route("/d/<int:n>")
flasktest.compile_divisors()

@app.route("/more_info")
def more_info():
   name = current_app.name
   return render_template("App_Object_and_Request_Values.html", name=name)


def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
         return False
   return True
def prime_divisors(n):
   divisors = []
   for i in range(1, n + 1):
      if n % i == 0 and is_prime(i):
         divisors.append(i)
   return divisors

@app.route('/d/<int:n>')
def show_divisors(n):
   if n < 1:
      return "Please enter a positive integer."
   divisors = prime_divisors(n)
   divisors_str = ', '.join(str(d) for d in divisors)
   return f"Prime divisors of {n}: {divisors_str}"

if __name__ == "__main__":
   app.run(debug=True)
