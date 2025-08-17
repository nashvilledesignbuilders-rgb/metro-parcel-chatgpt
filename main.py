from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/parcel_summary")
def parcel_summary(pins: str = Query(..., description="Comma-separated parcel numbers")):
    pin_list = [pin.strip() for pin in pins.split(",") if pin.strip()]
    if not pin_list:
        raise HTTPException(status_code=400, detail="No parcel numbers provided")

    results = []

    for pin in pin_list:
        url = "https://maps.nashville.gov/arcgis/rest/services/Cadastral/Parcels/MapServer/0/query"
        params = {"where": f"PIN='{pin}'", "outFields": "*", "f": "json"}
        try:
            response = requests.get(url, params=params)
            data = response.json()
            features = data.get("features")
            if not features:
                results.append({"pin": pin, "error": "Parcel not found"})
                continue

            attributes = features[0]["attributes"]
            summary = f"""
The property with Parcel Number {attributes.get('PIN')} is located at {attributes.get('SITEADDR', 'N/A')}. 
It is owned by {attributes.get('OWNERNAME', 'N/A')} and is zoned {attributes.get('ZONING', 'N/A')}. 
The lot size is approximately {attributes.get('ACRES', 'N/A')} acres. 
Permits / Notes: {attributes.get('PERMITS', 'None')}.
"""
            results.append({"pin": pin, "parcel_data": attributes, "summary": summary.strip()})
        except Exception as e:
            results.append({"pin": pin, "error": str(e)})

    return {"results": results}
