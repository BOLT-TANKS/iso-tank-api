from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load the Excel sheet into a pandas DataFrame
df = pd.read_excel("cargo_data.xlsx", engine="openpyxl")

class CargoRequest(BaseModel):
    cargo: str

@app.post("/get_iso_tank")
async def get_iso_tank(request: CargoRequest):
    cargo_name = request.cargo.upper()
    # Try to match by cargo name
    matched_row = df[df['Cargo Name'].str.upper() == cargo_name]
    
    if not matched_row.empty:
        tank_type = matched_row.iloc[0]['UNTANKINS']
        return {"iso_tank": tank_type}
    else:
        return {"error": "Cargo not found"}
