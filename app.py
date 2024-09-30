from flask import Flask
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def get_public_ip():
    # Make a request to the ipify API to get the public IP address
    ip = requests.get('https://api.ipify.org').text
    # Return the public IP address as a response
    return f'Your public IP address is: {ip}'

# Run the Flask application
if __name__ == '__main__':
    # The application will be accessible on all public IPs on port 5000
    app.run(host='0.0.0.0', port=5000)
