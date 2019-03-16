import connexion
from processSubmissions import ProcessSubmissions
from threading import Thread
import os

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the routes
app.add_api('swagger.yml')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) # This will be read from config file in prod

    #TODO this will be in a config file where the results are stored
    if not os.path.exists("./Results"):
        os.mkdir("./Results")

    #Start thread for processing data