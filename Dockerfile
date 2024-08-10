# Stage 1: Build the Next.js frontend
FROM node:18-alpine AS frontend-build

# Set working directory for the frontend
WORKDIR /app/front/gymmy2front

# Copy the frontend files
COPY front/gymmy2front/package*.json ./
COPY front/gymmy2front/ .

# Install dependencies and build the Next.js app
RUN npm install
RUN npm run build

# Stage 2: Build the FastAPI backend
FROM python:3.10-slim AS backend-build

# Set working directory for the backend
WORKDIR /app/backend

# Copy the backend files
COPY venv/app /app/backend

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Stage 3: Production image with both apps
FROM python:3.10-slim

# Install Node.js (for running the frontend)
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory
WORKDIR /app

# Copy backend files from the backend build stage
COPY --from=backend-build /app/backend /app/backend

# Copy frontend build files from the frontend build stage
COPY --from=frontend-build /app/front/gymmy2front/.next /app/front/gymmy2front/.next
COPY --from=frontend-build /app/front/gymmy2front/public /app/front/gymmy2front/public
COPY --from=frontend-build /app/front/gymmy2front/node_modules /app/front/gymmy2front/node_modules
COPY --from=frontend-build /app/front/gymmy2front/package.json /app/front/gymmy2front/package.json

# Install Uvicorn and any other Python packages needed to run the backend
RUN pip install --no-cache-dir uvicorn && pip install --no-cache-dir -r /app/backend/requirements.txt

# Expose the ports for frontend (3000) and backend (80)
EXPOSE 3000
EXPOSE 80

# Start both applications
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 80 & npm --prefix /app/front/gymmy2front run start"]
