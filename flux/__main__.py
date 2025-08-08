from flux.app import create_app
import uvicorn

app = create_app()

def start():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")    

if __name__ == "__main__":
    start()
