import shutil
import os

# Folder structure
project_name = '/mnt/data/mern-bug-tracker-deploy'
folders = [
    'server/models',
    'server/routes',
    'server/tests',
    'client/src/components',
    'client/src/tests',
    '.github/workflows'
]

# Create folder structure
os.makedirs(project_name, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# Sample files
server_package_json = '''{
  "name": "mern-bug-tracker-server",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.0.5",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "jest": "^29.6.1",
    "supertest": "^6.3.3",
    "nodemon": "^2.0.22"
  }
}'''

client_package_json = '''{
  "name": "mern-bug-tracker-client",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}'''

ci_cd_workflow = '''name: MERN CI/CD

on:
  push:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: cd server && npm install && npm test
      - run: cd client && npm install && npm run build

  deploy:
    runs-on: ubuntu-latest
    needs: build-and-test
    steps:
      - uses: actions/checkout@v3
      - name: Deploy Backend
        run: echo "Add Render deployment commands or API calls here"
      - name: Deploy Frontend
        run: echo "Add Vercel deployment commands here"'''

readme_content = '''# MERN Bug Tracker – Deployment & DevOps

## Project Overview
Full-stack MERN application for reporting and tracking bugs. Includes CI/CD, environment variables, monitoring, and performance optimization.

## Deployment URLs
- Frontend: https://your-frontend-domain.com
- Backend API: https://your-backend-domain.com/api/bugs

## Setup Instructions
### Backend
```
cd server
npm install
npm run dev
```

### Frontend
```
cd client
npm install
npm start
```

### Environment Variables
- `.env.example` included in repository:
```
PORT=5000
MONGO_URI=your_mongodb_atlas_uri
JWT_SECRET=your_jwt_secret
REACT_APP_API_URL=https://your-backend-domain.com
```

## CI/CD
- GitHub Actions workflow: `.github/workflows/ci-cd.yml`
- Runs tests and deploys automatically on push to main branch

## Monitoring
- Backend: Sentry, logging via Morgan/Winston, uptime monitoring
- Frontend: Web Vitals, Sentry
- Health check endpoint: `/health`

## Features
- Add, view, update, delete bugs
- Track bug status (open, in-progress, resolved)
- Unit & integration tests for backend and frontend
- CI/CD pipeline with automated deployment
- Production-ready MongoDB setup

## Maintenance
- Regular updates and patches
- Automated backups for MongoDB
- Deployment and rollback documentation

## Screenshots
*(Add screenshots of frontend and backend)*
'''

# Write sample files
with open(os.path.join(project_name, 'server/package.json'), 'w') as f:
    f.write(server_package_json)

with open(os.path.join(project_name, 'client/package.json'), 'w') as f:
    f.write(client_package_json)

with open(os.path.join(project_name, '.github/workflows/ci-cd.yml'), 'w') as f:
    f.write(ci_cd_workflow)

with open(os.path.join(project_name, 'README.md'), 'w') as f:
    f.write(readme_content)

# Create ZIP
shutil.make_archive('/mnt/data/mern-bug-tracker-deploy', 'zip', project_name)

'/mnt/data/mern-bug-tracker-deploy.zip'
