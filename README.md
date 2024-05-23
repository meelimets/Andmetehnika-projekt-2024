# GBIF Estonia | Global Biodiversity Information Facility ETL

## Superset Image setup
Followed the intsructions from the webpage:
https://hub.docker.com/r/apache/superset

To facilitate a collaborative environment for our group project, we followed these instructions to set up and configure two Docker containers that shared the same folder as a mount point:

1. A Superset container with our project mounted.
2. A Python development container with our project mounted.

## Superset Container Setup
### 1. Created and Started the Superset Container

Executed the following command to create and start the Superset container. Replaced <replace with image name> the name of the image created previously (my/superset:duckdb). 

```docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset <replace with image name>```

### 2. Created an Admin User

Created an admin user for Superset by running the following command. Updated the username, firstname, lastname, email, and password as needed:

```docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin```

### 3. Upgraded the Database

Upgraded the database by running:

```docker exec -it superset superset db upgrade```

### 4. Initialize Superset

Initialized Superset by executing:

```docker exec -it superset superset init```

### Python Development Container Setup in Visual Studio Code

* Opened the project folder in Visual Studio Code.

* Opened the command palette using the keyboard shortcut Ctrl+Shift+P (Windows/Linux).

* Typed and selected ```Dev Containers: Add Dev Container Configuration Files....```

* Selected ```Add Configuration to Workspace```.

* Chosed ```Python 3``` and then selected ```3.12-bullseye``` as the version.

* Selected none when asked for additional packages and clicked ```OK```.

* Reopened the Project in the Container

## Extract

For our project, we focused on extracting data related to Estonia. The data extraction process involved querying the database with specific conditions to subset the data:

```Basis of Record: Human observation```
```Country or Area: Estonia```
```Has Coordinate: True```
```Has Geospatial Issue: False```
```Occurrence Status: Present```
```Year Range: From the start of 2000 to the end of 2024```
The output was downloaded as a tabular data file in .csv format.

### 1. Data cleaning 

Ensured that all data points were on land by removing records related to marine areas.

### 2. Adding Additional Information

For each data record (row), additional information was added to indicate the county where the data point was recorded.

### 3. Column Selection

The original dataset contained 50 different columns. To reduce the file size and retain only useful information for visualization, only selected columns were kept.


## Transforming the data

The transformation process was carried out using Python script ```transform_GBIF.py```. The script took the downloaded CSV file, adjusted the number format and column names, saved the transformed data as a Parquet file, which is convenient while processing large data. Later the dataset was augmented with an ISO code, a county identifier for each row, together with county name. This was done to ensure the compatibility with Superset’s column display requirements. The transformed data is stored in a directory named parquet.

The script can run with the command below:

```for fn in $(ls csv); do
    echo "Transforming $fn..."
    python transform_GBIF.py csv/$fn parquet/$(basename $fn .csv).parquet
done```

## Load

The loading stage involved visualizing the transformed data using Apache Superset. The project is utilizing Docker containers for both Superset and Python environments. These containers are created with the project, mounted on the same project folder. The superset container is set up with a secret key. Later, the Docker environment was used for loading the data into Apache Superset (commands are described in the project file). The data was later visualized with appropriate charts, scripts are available in the project file. The Python Script ```Species_Richness_And_Density_plots_Script.py``` was used to create species richness map and species hexbin density plot.

## Visualizing Data in Superset

Visualization process was carried out using Apache Superset and Python libraries. The final summary can be seen on a dashboard, provided below. The dashboard contains multiple visualizations, including a bar chart showing species richness in Estonia from 2000-2023, a horizontal bar chart showing species observations by county, a map plotting individual species observations across Estonia and three line graphs showing separate trends over the time for animals, fungi and plants. The Species Richness Map displayed the count for distinct species in each county. It was created by grouping the data by county identifier code and calculating the distinct species count.



