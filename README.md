# **The HGNC App**

## What the application does:

The hgnc app is a lightweight Django web application that provides rapid access to gene information upon user input of either the active gene_symbol or the hgnc_id. The information provided includes:

- **HGNC-approved gene symbol**
- **HGNC ID**
- **Approved gene name**
- **Previous gene symbols**
- **Previous gene names**
- **Gene aliases/synonyms**
- **MANE Select transcript**
- **MANE Plus Clinical transcript(s)***

## Data source

The application will use data provided by the HUGO Gene Nomenclature Committee (HGNC):

[https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt](https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt)

The original TSV files are actively converted to dictionary nosql format, providing a single entry per gene request.

Installation
The project uses a reproducible Conda environment to ensure consistent behaviour across systems.:

- 1. **Clone the repository**
        git clone https://github.com/Salomics/p2_learning
- 2. **Create the Conda environment**
        conda env create -f p2_learning/env.yml
- 3. **Activate the environment**
        conda activate hgnc_conda_dep
- 4. **Make the virtual environment the local conda**
        poetry config virtualenvs.create false --local
- 5. **Install the project**
        pip install -e . **or** pip install for final build
- 6. **Optional globalisation of versioning**
        poetry self add "poetry-dynamic-versioning[plugin]"

The editable installation allows changes made to the source code to be immediately reflected without reinstalling the package.

## Start the development server:

Use the command **python manage.py runserver** to activate the server

By default the application will be available at:

[http://127.0.0.1:8000/]

Navigating using the link in your local browser will open the app
