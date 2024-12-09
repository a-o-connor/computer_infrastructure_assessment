# Computer Infrastructure Assessment Respository
**By A. O'Connor**
*********
<p align ="center"><img src="https://tethys-engineering.pnnl.gov/sites/default/files/taxonomy-images/met-logo.png" /></p>

*********

## Introduction 
This repository contains all assessment elements for the module **Computer Infrastructure** as part of the HDip in Computer Science and Data Analytics program at Atlantic Technological University (ATU). The repository is structured to demonstrate command-line proficiency, scripting, and automation skills, as well as Python-based data processing and analysis.  

## Contents
### 1. `weather.sh` Bash Script
- **Purpose**: Downloads the latest weather data for the Athenry weather station from [Met Éireann](https://prodapi.metweb.ie/observations/athenry/today.in).
  - The script saves the data to the `data/weather/` directory.
  - Filenames are timestamped in the format `YYYYmmdd_HHMMSS.json`.
- **Usage**: This script is executable and can be run using:
  ```bash
  ./weather.sh
  ````
- **Pre-requisites**: Ensure that `wget`  is installed to run `weather.sh`.
    ````bash
    sudo apt install wget
    ````
### 2. Github Actions Workflow
- A **GitHub Actions Workflow** automates the execution of the weather.sh script, running daily at 10 AM on a Linux virtual machine. The workflow pushes new weather data files to the repository.
    - This workflow can also be triggered manually using the ``workflow-dispatch`` event by going to the 'Actions' tab in the repository and running the workflow.
### 3. `weather.ipnyb` Jupyter Notebook
- **Purpose**: This notebook provides a short report describing each task completed as part of the Computer Infrastucture assessment. A data analysis section summarizing and plotting data from one of the downloaded weather data files is also included. 
- **Dependencies**: `requirements.txt` lists the Python dependencies for running the Jupyter Notebook.
- Install dependencies using:
    ````bash
    pip install -r requirements.txt
    ````
- The Jupyter notebook can be opened in Google Colab by clicking on the link below:

<br>

<a target="_blank" href="https://colab.research.google.com/github/a-o-connor/computer_infrastructure_assessment/blob/main/weather.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<br>

