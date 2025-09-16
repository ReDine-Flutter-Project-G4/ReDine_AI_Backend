from fastapi import APIRouter, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io

ai_router = APIRouter(prefix="/api/ai", tags=["AI"])

model = YOLO("/Users/snudhana/Documents/CS@SIT/year_2/ReDine/redine_ai_backend/app/models/ReDine_AI_Model.pt")

@ai_router.post("/ingredients/detect")
async def detect_ingredients(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    results = model(image)
    
    ingredients_list = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            class_name = model.names[cls]
            ingredients_list.append(class_name)

    return {"detected_ingredients": ingredients_list}

@ai_router.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint"}