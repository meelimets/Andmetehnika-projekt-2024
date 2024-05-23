# GBIF Estonia | Global Biodiversity Information Facility ETL

## Setup

To facilitate a collaborative environment for our group project, we followed these instructions to set up and configure two Docker containers that shared the same folder as a mount point:

1. A Superset container with our project mounted.
2. A Python development container with our project mounted.

### Superset Container Setup
1. Create and Start the Superset Container

Executed the following command to create and start the Superset container. Replaced your_new_secret_key with a new secret value and replaced <replace with image name> with the name of the image created previously (e.g., my/superset:duckdb). 

docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset <replace with image name>

2. Create an Admin User

Created an admin user for Superset by running the following command. Updated the username, firstname, lastname, email, and password as needed:

docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin

3. Upgrade the Database

Upgraded the database by running:

docker exec -it superset superset db upgrade

4. Initialize Superset

Initialized Superset by executing:

docker exec -it superset superset init

### Python Development Container Setup in Visual Studio Code

Opened the project folder in Visual Studio Code.

Added Dev Container Configuration Files

Opened the command palette using the keyboard shortcut Ctrl+Shift+P (Windows/Linux).

Typed and selected Dev Containers: Add Dev Container Configuration Files....

Select Configuration

Selected Add Configuration to Workspace.

Chosed Python 3 and then selected 3.12-bullseye as the version.

Selected none when asked for additional packages and clicked OK.

Reopened the Project in the Container

Used the keyboard shortcut Ctrl+Shift+P or Cmd+Shift+P and typed and selected Dev Containers: Reopen in Container.

## Extract

Since the biodiversity database is not updated weekly, we directly downloaded the database as a csv file from the website.

## Data cleaning and preparation

The dataset was augmented with an ISO code (the county's identifier) for each row, alongside the county name and a code assigned by the national authority (essentially the same ISO code but without the 'EE' prefix). This was done to ensure compatibility with Superset's column display requirements. Both codes are now included.

Species located outside of the mainland were filtered out to retain only mainland results. This was done to ensure clarity when displaying them on the map later.


## Transforming the data

The script located in the transform_GBIF file takes the downloaded .csv file, adjusts the number format and column names, and saves the transformed data as a Parquet file.

This step assumes a parquet directory where the transformed files will be stored. 

The script can run with the command below:

for fn in $(ls csv); do
    echo "Transforming $fn..."
    python transform_GBIF.py csv/$fn parquet/$(basename $fn .csv).parquet
done


## Visualizing Data in Superset

Here's how to get started with visualizing your air quality data in Apache Superset:

Open your web browser and navigate to localhost:8080. This will take you to the Apache Superset login page.
Enter the credentials you set up during the initialization process to log in.



