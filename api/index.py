from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "API is live!",
        "usage": "/parcel_summary?pin=123456789 or /parcel_summary?pins=123456789,987654321"
    }

@app.get("/parcel_summary")
def parcel_summary(
    pins: str = Query(None, description="Comma-separated parcel numbers"),
    pin: str = Query(None, description="Single parcel number for backward compatibility")
):
    if pin:
        pins = pin

    if not pins:
        raise HTTPException(status_code=400, detail="No parcel numbers provided")

    pin_list = [p.strip() for p in pins.split(",") if p.strip()]
    results = []

    for p in pin_list:
        url = "https://maps.nashville.gov/arcgis/rest/services/Cadastral/Parcels/MapServer/0/query"
        params = {"where": f"PIN='{p}'", "outFields": "*", "f": "json"}
        try:
            response = requests.get(url, params=params)
            data = response.json()
            features = data.get("features")
            if not features:
                results.append({"pin": p, "error": "Parcel not found"})
                continue

            attributes = features[0]["attributes"]
            summary = f"""
The property with Parcel Number {attributes.get('PIN')} is located at {attributes.get('SITEADDR', 'N/A')}. 
It is owned by {attributes.get('OWNERNAME', 'N/A')} and is zoned {attributes.get('ZONING', 'N/A')}. 
The lot size is approximately {attributes.get('ACRES', 'N/A')} acres. 
Permits / Notes: {attributes.get('PERMITS', 'None')}.
"""
            results.append({"pin": p, "parcel_data": attributes, "summary": summary.strip()})
        except Exception as e:
            results.append({"pin": p, "error": str(e)})

    return {"results": results}
