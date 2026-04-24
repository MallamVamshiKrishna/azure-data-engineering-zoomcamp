# Azure Data Factory Pipeline Orchestration

This repository contains the orchestration logic, pipeline definitions, and CI/CD workflows for [Project Name]. It uses Azure Data Factory (ADF) to automate data movement and transformation across [List Source Systems] and [List Target Systems].



## 🚀 Setup & Integration
🎯 Objective

Designed and implemented a batch ingestion pipeline to process raw CSV data and load optimized datasets into Azure Data Lake Storage Gen2.

🏗️ Architecture
Local CSV → Pandas → Transformation → Parquet → Python SDK → ADLS Gen2
⚙️ Technologies Used
Python (pandas)
Azure Storage SDK
Azure Data Lake Storage Gen2

🔄 Workflow
Extract raw NYC taxi dataset
Perform schema validation and datetime transformation
Generate partition-ready column (pickup_date)
Convert data into Parquet format
Upload processed data to ADLS using Python SDK

📊 Key Design Decisions
Used Parquet format for columnar storage and performance
Applied datetime normalization for partitioning
Implemented automated upload instead of manual ingestion
Used modular Python code for maintainability

🧠 Learnings
Built end-to-end batch ingestion pipeline
Understood importance of data formats and schema
Implemented cloud integration using Azure SDK
Debugged real-world issues (file paths,data types,naming)

## 🏗️ Architecture Overview
[Optional: Insert Architecture Diagram here]
The orchestration is built to handle:
- **Data Ingestion**: Extracting data from [Sources].
- **Transformation**: Running [Databricks/Stored Procs/Mapping Data Flows].
- **Monitoring**: Centralized logging and alerting for pipeline failures.

## 📁 Repository Structure
- `ARM-Templates/`: Contains generated templates for production deployment.
- `PowerShell-Scripts/`: Utility scripts for pre- and post-deployment (e.g., stopping/starting triggers).
- `.github/workflows/`: GitHub Action YAML files for automated CI/CD.
- `factory/`: Core ADF resource definitions (pipelines, datasets, linked services).
