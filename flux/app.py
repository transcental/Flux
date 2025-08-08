from typing import Union

from fastapi import FastAPI

app = FastAPI()

global data

data = {
    "battery": {},
    "location": {}
}

@app.get("/")
async def index():
    return "Hello World"
    
@app.get("/api/battery")
async def get_battery():
    global data
    """
    Endpoint to retrieve battery data.
    Returns the global battery data dictionary.
    """
    return data["battery"]
    
@app.get("/api/location")
async def get_location():
    global data
    """
    Endpoint to retrieve location data.
    Returns the global location data dictionary.
    """
    return data["location"]


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    Returns a simple message indicating the service is healthy.
    """
    return {"status": "healthy"}
    
@app.get("/api/all")
async def get_all_data():
    """
    Endpoint to retrieve all data.
    Returns both battery and location data.
    """
    global data
    return {
        "battery": data["battery"],
        "location": data["location"]
    }


@app.post("/api/locate")
async def locate(
    req_data: Union[dict, str]
):
    """
    Endpoint to handle location data.
    Accepts either a JSON object or a string.
    """
    global data
    data = req_data
    
    if isinstance(data, str):
        return {"message": "Received string data", "data": data}
    elif isinstance(data, dict):
        return {"message": "Received JSON data", "data": data}
    else:
        return {"error": "Unsupported data type"}

def create_app() -> FastAPI:
    """
    Factory function to create and return a FastAPI application instance.
    """
    return app
