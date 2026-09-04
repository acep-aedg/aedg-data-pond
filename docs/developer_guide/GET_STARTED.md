## Overview

* /aedg-data-pond/README.md
* /aedg-data-pond/docs/README.md

* **ETL Repository:** [`aedg-etl-2024`](https://github.com/acep-aedg/aedg-etl-2024) 


## Requirements
make sure you have the etl repo cloned and the database created and run `dtb build` (see docs)

* **Python:** 3.12
* **yq:** v4


## Environment Setup

### 1. Clone Repositories
Clone all repos into the same local workspace directory:

```bash
git clone https://github.com/acep-aedg/aedg-etl-2024.git
```
```bash
git clone https://github.com/acep-aedg/aedg-data-pond.git
```
```bash
git clone git@github.com:acep-aedg/aedg-metadata.git
```

### 2. Configure Python Environment

Create virtual environment
```bash
python3 -m venv .venv
```
Activate virtual environment
On macOS/Linux:
```bash
source .venv/bin/activate
```
On Windows:
```bash
# .venv\Scripts\activate
```
install requirements 
```bash
pip install -r requirements.txt
```
run main to run all associated scripts (see in main.sh) for public datasets, metadata generation .json and .md.
```bash
./main.sh
```
