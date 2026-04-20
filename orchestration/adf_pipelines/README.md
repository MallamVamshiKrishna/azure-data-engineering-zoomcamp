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
1. **GitHub Configuration**: In the ADF Studio, go to **Manage** > **Git configuration** and connect this repository.
2. **Branching Strategy**: 
   - Use `main` (or a collaboration branch) for development merges.
   - Use `adf_publish` for generated ARM templates used in deployments.
3. **Secrets**: Configure GitHub Repository Secrets (e.g., `AZURE_CREDENTIALS`) to allow [GitHub Actions](https://blog.devgenius.io/automate-data-engineering-deployment-with-github-actions-36b6bf499533) to deploy to target environments.

## 🛠️ Key Orchestration Components
* **Master Pipeline**: Triggers child pipelines in sequence and handles overall error trapping.
* **Linked Services**: Connected to [Azure Key Vault](https://www.youtube.com/watch?v=Xp-mcWfn7Lw) for secure credential management across Dev and Test environments.
* **Triggers**: [Schedule/Tumbling Window/Storage Event] based triggers defined in the factory.

## 🔄 CI/CD Workflow
Automated deployment is handled via [GitHub Actions](https://www.youtube.com/watch?v=5f0kAgfcOis):
1. **Develop**: Create a feature branch in ADF Studio and save changes.
2. **Merge**: Create a Pull Request to merge into the `main` branch.
3. **Publish**: Click "Publish" in the ADF UI to generate ARM templates into the `adf_publish` branch.
4. **Deploy**: A GitHub Action workflow is triggered on pushes to `adf_publish`, deploying artifacts to the Test/Prod environments.

## 🤝 Contributing
Please follow the [standard Git flow](https://github.com/AdamPaternostro/Azure-Data-Factory-CI-CD-Source-Control/blob/master/README.md). Ensure all new pipelines include proper error handling and are added to the Master Orchestration pipeline.
