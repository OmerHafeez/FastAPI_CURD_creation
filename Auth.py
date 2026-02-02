from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "shittyfastapikey"

api_key_scheme = APIKeyHeader(name="x-api-key", auto_error=False)

def require_api_key(api_key: str = Depends(api_key_scheme)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
