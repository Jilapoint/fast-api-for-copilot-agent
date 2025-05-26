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

## License
This project is licensed under the MIT License.