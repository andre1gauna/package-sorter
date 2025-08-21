from fastapi import FastAPI, HTTPException
from app.PackageSorting import sort
from pydantic import BaseModel

app = FastAPI()

class Package(BaseModel):
    length: int
    width: int
    height: int
    mass: int
    
@app.get("/")
def root():
    return {"app": "Running"}

@app.post("/packages/classify" )
def sort_package(pkg: Package) -> dict:
    try:
        result = sort(pkg.length, pkg.width, pkg.height, pkg.mass)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")