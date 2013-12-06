# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from bottle import route, run, request

@route("/")
def f():
    cookie = request.query.get("cookie")
    if cookie:
        with open("cookie.txt", "w+") as f:
            f.write(cookie)
    return ""

run(host='0.0.0.0', port=8081, debug=True)

