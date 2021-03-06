
# Software Requirements
- dotnet core version 2.2
- postgresql 10
    - You'll also need the npgsql driver, available through the dependency installer
- npm
- Python 3.3
    - virtualenv

# Setup
## Database
- Make note of the port you set for the database (default is 5432)
- Also make note of the password you set for the default user
- Create the database and clientserver user. Open a terminal.
    - Login to postgres using the postgres user: 
        - `psql -U postgres`
        - Enter the password you set during the installation
    - Create the clientserver database: 
        - `CREATE DATABASE clientserver;`
        - (NOTE: You can change the username, database name and/or password. Just remain consistent, and modify `appsettings.json` as appropriate)
    - Create the clientserver user: 
        - `CREATE USER clientserver WITH ENCRYPTED PASSWORD 'password';`
    - Give privileges to the new user: 
        - `GRANT ALL PRIVILEGES ON DATABASE clientserver TO clientserver;`
    - Quit psql: 
        - `\q`
- Setup the tables. In a terminal, navigate to the `ClientServer` directory (the directory that contains this README). 
    - Create the Migrations model definitions: 
        - `dotnet ef migrations add InitialCreate`
    - Create the tables in the database: 
        - `dotnet ef database update`

## Angular App
- Navigate to the `ClientServer/ClientApp` directory in a terminal. Install the dependencies:
    - `npm install`

## Scrubbing Script
- Navigate to the `ClientServer/scrubbing` directory in a terminal. 
- Create a virtualenv
    - `virtualenv env`
- Activate the virtualenv
    - On Windows: `env\Scripts\activate`
    - On Linux: `source env/bin/activate`
- Install dependencies
    - `pip install -r requirements.txt`
- Deactivate the virtualenv
    - On Windows: `env\Scripts\deactivate`
    - On Linux: `deactivate`

# Running the Client Server + Client Portal
- In the `ClientServer` directory, open a terminal to run the project.
    - `dotnet run`
    - This serves the api on [http://localhost:5000](http://localhost:5000) and [https://localhost:5001](https://localhost:5001)
    - If you are actively developing the api, you can use the file watcher to automatically reload the app when you save a file
        - Instead of `dotnet run` use `dotnet watch run`
        - This means your app will always be up to date with the filesystem, however the build process does take a while

# Dotnet Core Helpful Links
- Base overview of how to structure the api:
    https://docs.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-2.2
- Querying Related Data:
    https://docs.microsoft.com/en-us/ef/core/querying/related-data
- HTTP Requests:
    https://docs.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-2.2

Base overview of how to structure the api:
    https://docs.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-2.2

Querying Related Data:
    https://docs.microsoft.com/en-us/ef/core/querying/related-data

# Setup
## Database
- Make note of the port you set for the database (default is 5432)
- Also make note of the password you set for the default user
- Create the database and clientserver user. Open a terminal.
    - Login to postgres using the postgres user: 
        - `psql -U postgres`
        - Enter the password you set during the installation
    - Create the clientserver database: 
        - `CREATE DATABASE clientserver;`
        - (NOTE: You can change the username, database name and/or password. Just remain consistent, and modify `appsettings.json` as appropriate)
    - Create the clientserver user: 
        - `CREATE USER clientserver WITH ENCRYPTED PASSWORD 'password';`
    - Give privileges to the new user: 
        - `GRANT ALL PRIVILEGES ON DATABASE clientserver TO clientserver;`
    - Quit psql: 
        - `\q`
- Setup the tables. In a terminal, navigate to the `ClientServer` directory (the directory that contains this README). 
    - Create the Migrations model definitions: 
        - `dotnet ef migrations add InitialCreate`
    - Create the tables in the database: 
        - `dotnet ef database update`
    
# Server Setup
- https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-2.2

# Dotnet Core Helpful Links
- Base overview of how to structure the api:
    https://docs.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-2.2
- Querying Related Data:
    https://docs.microsoft.com/en-us/ef/core/querying/related-data
- HTTP Requests:
    https://docs.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-2.2

