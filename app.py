from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = create_app()

if __name__ == '__main__':
    flask_env = os.getenv('FLASK_ENV', 'production')  # Default to 'production' if not set
    print("Current Working Directory:", os.getcwd())  # Print the current working directory
    print("FLASK_ENV:", flask_env)  # Print the FLASK_ENV value
    app.run(debug=flask_env != 'production')
