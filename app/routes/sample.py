from fastapi import APIRouter, HTTPException
from app.models.item import Item

router = APIRouter()

# POST route that accepts JSON data and processes it
@router.post("/process")
def process_data(item: Item):
    try:
        result = item.value1 + item.value2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET route to concatenate two strings as query parameters
@router.get("/concat")
def concatenate(param1: str, param2: str):
    return {"result": param1 + param2}

# GET route to return the length of a string as a query parameter
@router.get("/length")
def length_of_string(string: str):
    return {"length": len(string)}
