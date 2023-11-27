from application import create_app
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('logs.txt')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logging.getLogger().addHandler(file_handler)

def main():
    PORT = os.environ.get('PORT')
    DEBUG = os.environ.get('FLASK_DEBUG')
    HOST = os.environ.get('HOST')
    app = create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    main()