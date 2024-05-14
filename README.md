# GBIF | Global Biodiversity Information Facility ETL

Setup

For setting up the development container in Visual Studio Code, we followed these steps:

Opened the project folder in VS Code.
Opened the command palette using the keyboard shortcut `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac). Typed and selected Dev Containers: Add Dev Container Configuration Files...
Selected: Add Configuration to Workspace.
Choosed Python 3 and then selected 3.12-bullseye as the version.
Selected' none' when asked for additional packages and clicked OK.
Used the keyboard shortcut `Ctrl+Shift+P` or `Cmd+Shift+P` and typed and selected Dev Containers: Reopen in Container.

Extract

Since the biodiversity database is not updated weekly, we directly downloaded the database as a csv file from the website.

The data cleaning and preparation

The dataset was augmented with an ISO code (the county's identifier) for each row, alongside the county name and a code assigned by the national authority (essentially the same ISO code but without the 'EE' prefix). This was done to ensure compatibility with Superset's column display requirements. Both codes are now included.

Species located outside of the mainland were filtered out to retain only mainland results. This was done to ensure clarity when displaying them on the map later.


Transforming the data


for fn in $(ls csv); do
    echo "Transforming $fn..."
    python transform_GBIF.py csv/$fn parquet/$(basename $fn .csv).parquet
done


Visualizing Data





