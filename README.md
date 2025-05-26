# Product API for Copilot Studio

## Overview
This is a FastAPI-based application that provides a simple API for managing products. It includes endpoints for retrieving product details and checking the health of the application.

## Features
- **Health Check Endpoint**: Verify the application's health status.
- **Product Retrieval**: Fetch details of a product by its ID.

## Endpoints

### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Returns the health status of the application.
- **Response**:
  ```json
  {
    "status": "ok"
  }
  ```

### Product Retrieval
- **URL**: `/products/{product_id}`
- **Method**: `GET`
- **Description**: Retrieves details of a product by its ID.
- **Response**:
  - **Success**:
    ```json
    {
      "id": 1,
      "name": "Widget",
      "price": 19.99,
      "description": "A useful widget for everyday tasks."
    }
    ```
  - **Error**:
    ```json
    {
      "detail": "Product not found"
    }
    ```

## Setup and Run

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd FastAPIAudit
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Application
Start the application using Uvicorn:
```bash
uvicorn main:app --reload
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Documentation
Interactive API documentation is available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure
```
FastAPIAudit/
├── main.py          # Application code
├── requirements.txt # Dependencies
├── Dockerfile       # Docker configuration
└── swagger2.json    # Swagger documentation
```
## Deployment Steps

### Deploy Locally with Docker
1. Build the Docker image:
   ```bash
   docker build -t fastapi-audit .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 fastapi-audit
   ```
3. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Deploy to Azure
1. **Create an Azure Container Registry (ACR):**
   ```bash
   az acr create --resource-group <ResourceGroupName> --name <RegistryName> --sku Basic
   ```
2. **Log in to ACR:**
   ```bash
   az acr login --name <RegistryName>
   ```
3. **Tag the Docker image for ACR:**
   ```bash
   docker tag fastapi-audit <RegistryName>.azurecr.io/fastapi-audit:latest
   ```
4. **Push the image to ACR:**
   ```bash
   docker push <RegistryName>.azurecr.io/fastapi-audit:latest
   ```
5. **Deploy the container to Azure App Service:**
   ```bash
   az appservice plan create --name <AppServicePlanName> --resource-group <ResourceGroupName> --is-linux --sku B1
   az webapp create --resource-group <ResourceGroupName> --plan <AppServicePlanName> --name <WebAppName> --deployment-container-image-name <RegistryName>.azurecr.io/fastapi-audit:latest
   ```
6. **Configure ACR authentication for the web app:**
   ```bash
   az webapp config container set --name <WebAppName> --resource-group <ResourceGroupName> --docker-custom-image-name <RegistryName>.azurecr.io/fastapi-audit:latest --docker-registry-server-url https://<RegistryName>.azurecr.io
   ```
7. Access the deployed application at:
   ```
   https://<WebAppName>.azurewebsites.net
   ```

## Known Issues and Troubleshooting



### 1. Docker Engine Connection Error
**Error:**
```
error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.49/containers/json": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```
**Solution:**
- Restart Docker Desktop.
- Verify that the "Enable the WSL 2 based engine" option is enabled in Docker Desktop settings.

### 2. Python Package Installation Issues
**Error:**
```
ERROR: Could not install packages due to an OSError: [WinError 2] The system cannot find the file specified.
```
**Solution:**
- Manually delete the problematic `.exe` or `.deleteme` files in the `Scripts` directory of your Python installation.
- Run the installation command with administrative privileges.

### 3. Azure Deployment Issues
**Error:**
```
Failed to deploy container to Azure App Service.
```
**Solution:**
- Ensure the Azure Container Registry (ACR) is properly configured and the image is pushed successfully.
- Verify that the web app is configured to authenticate with ACR.

If you encounter any other issues, feel free to document them here for future reference.

## License
This project is licensed under the MIT License.
