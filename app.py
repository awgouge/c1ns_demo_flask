import os
from webapp import create_app

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
port = int(os.environ.get('LISTEN_PORT', '5000'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
