# Transaction Processing Service

A Python-based service that processes transactions using Google Cloud Vertex AI. This service handles data processing with configurable logging and supports multiple input datasets.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)

## ✨ Features
- Transaction processing with Vertex AI integration
- Configurable logging system
- YAML-based configuration management
- Support for multiple input datasets
- Automated result generation

## 🔧 Prerequisites
- Python 3.8 or higher
- Google Cloud Platform account
- Vertex AI API enabled
- Valid GCP credentials

## 📥 Installation

1. Clone the repository:
```bash
git clone
```

2. Install the required using poetry or pip:
```bash
poetry install
```
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Configure your credentials:
   - Place your GCP service account key in `credentials/credential.json`
   - Update `config.yaml` with your project settings

2. Example `config.yaml` structure:
```yaml
project_id: "your-project-id"
location: "us-central1"
model_id: "your-model-id"
input_datasets:
  - name: "dataset1"
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "logs.log"
```

## 🚀 Usage
Run the service using the following command:
```bash
python main.py
```
The service will:
1. Process input files from the `dataset` directory
2. Generate logs in the `logs` directory
3. Output results to the `results` directory

## 📂 Project Structure
```
.
├── config.py # Configuration management
├── config.yaml # Configuration settings
├── credentials/credential.json # GCP credentials
├── dataset/ # Input data files
├── logs/ # Application logs
├── main.py # Application entry point
├── services/ # Core service modules
└── utils/ # Utility functions
```

## 📝 Logging
- Logs are automatically generated in the `logs` directory
- Format: `process_YYYYMMDD_HHMMSS.log`
- Contains detailed processing information and error tracking

## ❗ Troubleshooting

### Common Issues

1. **Credential Error**
   ```
   Solution: Ensure credentials/credential.json is properly configured and has the required permissions
   ```

2. **Configuration Error**
   ```
   Solution: Verify config.yaml format and required fields
   ```

3. **Processing Error**
   ```
   Solution: Check input data format in dataset directory and logs for specific error messages
   ```
