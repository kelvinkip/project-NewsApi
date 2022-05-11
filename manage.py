from app import create_app
from flask_script import  Manager,Server

# creating app instance
app = create_app ()

manager = Manager(app)
manager .add_command('server',Server)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=6015)
