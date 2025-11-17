from fastapi import APIRouter, UploadFile, File
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import io

ai_router = APIRouter(prefix="/api/ai", tags=["AI"])

root = Path(__file__).resolve().parent.parent
model_path = root / "models" / "ReDine_AI_Model.pt"
model = YOLO(model_path)

@ai_router.post("/ingredients/detect")
async def detect_ingredients(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    ingredients_list = set()
    results = model.predict(image, device="cuda", save=False)
    
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            ingredients_list.add(class_name)

    return {"detected_ingredients": list(ingredients_list)}

@ai_router.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint"}