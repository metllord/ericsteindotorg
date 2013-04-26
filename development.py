from website import app
#from settings import Development

app.config.from_object('settings.Development')

if __name__ == '__main__':
    app.run()
else:
    raise RuntimeError('This script should be run directly. DO NOT USE FOR WSGI')
