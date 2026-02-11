# Weather Dashboard App - Frontend

This is the Frontend service for displaying weather data from the backend service

## Prerequisites:

- Python 3.11 + (if runnign locally)
- pip
- Docker (if running containerized)
- Backend service running

## Local installation (Without Docker):
``` bash
cd frontend
git clone <frontend repo url>
python3 -m venv venv
source venv/bin/activate
pip install -r requirments.txt #install dependencies
export BACKEND_URL=http://localhost:5001   # Linux/Mac
python frontend.py #run the server - Server will start on: http://127.0.0.1:5000
```
- Open in browser: http://127.0.0.1:5000

## Installation with Docker:

```bash 
dockr build -t weather-ui #build the image
docker run -e BACKEND_URL=http://host.docker.internal:5001 -p 5000:5000 weather-frontend
```
- Open in browser: http://127.0.0.1:5000

Notes
-----

- Make sure the backend service is running before using the frontend.
- The default port for frontend is 5000.
