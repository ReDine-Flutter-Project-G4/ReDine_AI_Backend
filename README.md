# ReDine_AI_Backend

## Project Overview
ReDine_AI_Backend is a Python-based backend service for AI-powered restaurant recommendations and menu analysis. It leverages machine learning models to provide intelligent suggestions and insights for restaurant menus.

## Features
- AI-driven menu suggestion and analysis
- RESTful API endpoints for menu, ingredients, allergens, and categories
- Integration with trained PyTorch models

## Prerequisites
- Python 3.12+
- pip

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd ReDine_AI_Backend
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**
   ```bash
   cd app
   uvicorn app.main:app --reload
   ```

## Project Structure
```
ReDine_AI_Backend/
├── requirements.txt
└── app/
    ├── __init__.py
    ├── main.py
    ├── models/
    │   └── ReDine_AI_Model.pt
    └── routers/
        ├── __init__.py
        └── ai_router.py
```

## API Endpoints
- `/menu` - Get menu suggestions
- `/ingredients` - Get ingredients list
- `/categories` - Get menu categories
- `/allergens` - Get allergen information

## Model
- The AI model is stored in `app/models/ReDine_AI_Model.pt` (PyTorch format).

## Notes
- Ensure the model file exists before running the server.
- For development, use a virtual environment to avoid dependency conflicts.

## License
MIT
