# Azure Data Factory Pipeline Orchestration

This repository contains the orchestration logic, pipeline definitions, and CI/CD workflows for [Project Name]. It uses Azure Data Factory (ADF) to automate data movement and transformation across [List Source Systems] and [List Target Systems].

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

## 🚀 Setup & Integration
