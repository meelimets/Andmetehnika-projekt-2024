# GBIF Estonia | Global Biodiversity Information Facility ETL

## Setup

Created two new Docker containers that utilize the same `ETL_superset` folder as a mount point:

A Superset container with our project mounted.
A Python development container with our project mounted.
Execute the following commands to set up the Superset container. Remember to change the `SUPERSET_SECRET_KEY` to a new secret value and keep it confidential, especially not publishing it on GitHub or any public repositories.

docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset <replace with image name we created last time. i.e. my/superset:duckdb - see docker images for list>

Update user, firstname, lastname, email and password as you see fit

docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init

For setting up the development container in Visual Studio Code, we followed these steps:

Opened the project folder in VS Code.
Opened the command palette using the keyboard shortcut `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac). Typed and selected Dev Containers: Add Dev Container Configuration Files...
Selected: Add Configuration to Workspace.
Choosed Python 3 and then selected 3.12-bullseye as the version.
Selected' none' when asked for additional packages and clicked OK.
Used the keyboard shortcut `Ctrl+Shift+P` or `Cmd+Shift+P` and typed and selected Dev Containers: Reopen in Container.

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



