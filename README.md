# Echo Service - FastAPI Deployment Learning Project

A simple FastAPI application designed for learning backend deployment with Docker and CI/CD.

## 🎯 Features

- **Echo API Endpoint**: Takes user input via query parameter and echoes it back
- **Simple Web Interface**: Basic HTML page with input box for testing
- **Health Check**: Endpoint for monitoring service status
- **Dockerized**: Ready for containerized deployment
- **CI/CD Pipeline**: Automated deployment via GitHub Actions

## 🚀 Local Development

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized testing)

### Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser at `http://localhost:8000`

### Run with Docker

1. Build the Docker image:
```bash
docker build -t echo-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 echo-api
```

3. Access at `http://localhost:8000`

## 📡 API Endpoints

### `GET /`
Returns the main HTML interface

### `GET /api/echo?message={your_message}`
Echo endpoint that returns the provided message

**Parameters:**
- `message` (required): The text to echo back

**Example Response:**
```json
{
  "original_message": "Hello World",
  "echo": "Hello World",
  "length": 11,
  "timestamp": "2024-01-20T12:00:00.000000",
  "status": "success"
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "echo-api"
}
```

## 🔧 Deployment to Render.com

### Initial Setup

1. **Create a Render account** at [render.com](https://render.com)

2. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: `echo-api` (or your preferred name)
     - **Environment**: `Docker`
     - **Region**: Choose closest to you
     - **Branch**: `main`
     - **Instance Type**: Free (for learning)

3. **Get your Render API credentials:**
   - Go to Account Settings → API Keys
   - Create a new API key
   - Copy the API key
   - Go to your service dashboard and copy the Service ID from the URL
     - Format: `https://dashboard.render.com/web/srv-XXXXX` (srv-XXXXX is your Service ID)

4. **Configure GitHub Secrets:**
   - Go to your GitHub repository → Settings → Secrets and variables → Actions
   - Add two secrets:
     - `RENDER_API_KEY`: Your Render API key
     - `RENDER_SERVICE_ID`: Your Render service ID

### How CI/CD Works

The GitHub Actions workflow (`.github/workflows/deploy.yml`) will:

1. Trigger on every push to the `main` branch
2. Checkout your code
3. Call Render's API to trigger a deployment
4. Render will pull the latest code, build the Docker image, and deploy

### Manual Deployment

You can also trigger deployments manually:
- Go to your repository → Actions → Deploy to Render → Run workflow

## 📁 Project Structure

```
render_app/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions CI/CD pipeline
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🧪 Testing the Deployment

Once deployed on Render:

1. Find your service URL (e.g., `https://your-service.onrender.com`)
2. Open it in a browser to see the web interface
3. Test the API directly:
   - `https://your-service.onrender.com/api/echo?message=HelloWorld`
   - `https://your-service.onrender.com/health`

## 📚 Learning Points

This project demonstrates:

1. **FastAPI Basics**: Creating endpoints with query parameters
2. **Docker**: Containerizing a Python application
3. **CI/CD**: Automated deployment with GitHub Actions
4. **Cloud Deployment**: Using Render.com as a hosting platform
5. **API Design**: RESTful endpoints with proper responses
6. **Health Checks**: Service monitoring endpoints

## 🔍 Troubleshooting

**Service not starting on Render:**
- Check the logs in Render dashboard
- Ensure the PORT environment variable is being used (Render sets this automatically)

**GitHub Actions failing:**
- Verify your secrets are correctly set
- Check that RENDER_SERVICE_ID includes the "srv-" prefix

**Docker build failing locally:**
- Ensure Docker is running
- Check that all files are present in the directory

## 📝 Next Steps

- Add more endpoints (POST, PUT, DELETE)
- Add authentication
- Connect to a database
- Add comprehensive logging
- Implement rate limiting
- Add unit tests and integration tests

## For future sessions running the app locally
- run the following:
- source .venv/bin/activate
- python main.py

### Run with Docker

#### Option 1: Using Docker Commands

1. Build the Docker image:
```bash
docker build -t echo-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 echo-api
```

3. Stop the container:
```bash
# Press Ctrl+C in the terminal
```

4. Access at `http://localhost:8000`

#### Option 2: Using Docker Compose (Recommended)

1. Build and start the container:
```bash
docker-compose up --build
```

2. Access at `http://localhost:8000`

3. Stop the container:
```bash
# Press Ctrl+C, then run:
docker-compose down
```

**Quick Reference:**
- `docker-compose up --build` - Rebuild image and start container
- `docker-compose up` - Start container (using existing image)
- `docker-compose up -d` - Start in background (detached mode)
- `docker-compose down` - Stop and remove container
- `docker-compose logs -f` - View container logs