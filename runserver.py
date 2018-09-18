# -*- encoding=UTF-8 -*-

from nowstagram import app

if __name__ == '__main__':

    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True,Threaded=True)