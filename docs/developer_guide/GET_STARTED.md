## Overview

* /aedg-data-pond/README.md
* /aedg-data-pond/docs/README.md

* **ETL Repository:** [`aedg-etl-2024`](https://github.com/acep-aedg/aedg-etl-2024) 


## Requirements

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

### 2. Configure Python Environment

```bash
# Create virtual environment
python3 -m venv .venv
```
```bash
# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```
```bash
# Install requirements
pip install -r requirements.txt
```
