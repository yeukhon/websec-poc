# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from bottle import route, run, request, response
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="testing")
cursor = db.cursor()

@route('/login')
def login():
    has_cookie = request.get_cookie("visited")
    if has_cookie and has_cookie == "yes":
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/logout')
def logout():
    response.delete_cookie("visited")
    return "Logged out."

@route('/users')
def hello():
    id = request.query.get("id")
    cursor.execute("SELECT * FROM users WHERE id=" + str(id))
    return str(cursor.fetchall())

@route('/search')
def search():
    html = """
    <html>
     <head>
     <title>XSS Search Engine</title>
     </head>
      <body>
     
       <form method="get" action="xss">
       Search query:
       <input type="text" name="search" size="100" />
       <input type="submit" class="button" value="Submit" />
       </form>
     
     </body>
    </html>
    """
    return html

@route('/xss')
def xss():
    html = """
    <html>
     <head>
     <title>XSS Search Result Page</title>
     </head>
      <body>
       <h2> Search result:</h2>
       <p>{result}</p>
     </body>
    </html>
    """.format(result=request.query.get("search"))
    return html

run(host='0.0.0.0', port=8080, debug=True)
