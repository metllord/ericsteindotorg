"""
This is for runing in a production-like environment.

For serving in actual production, import this into your WSGI file.
"""

from website import app

app.config.from_object('settings.Production')

if __name__ == '__main__':
    print 'This is local production'
    app.run()
