# Transfer-Service-API
Transfer Service API

## Installation
- **Clone the repository:**
  ```git clone https://github.com/GihaniWijekoon/Transfer-Service-API.git```
- **Install dependencies:**
    ```pip install -r requirements.txt```

## Running the API
```uvicorn app:app --reload```

## API Usage
- **Endpoint:** `POST /transfer`
- **Request Body:**
  
```json
{
    "source": "123",
    "destination": "456",
    "amount": 50.0
}
```
- **Response:**
 ```json
{
    "status": "success",
    "message": "Transfer completed successfully"
}
```

## Running Tests
- **Run:**
```python tests.py```


