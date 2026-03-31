from pydantic import BaseModel

class Observation(BaseModel):
    alert_type: str
    failed_logins: int
    malware_detected: bool
    network_traffic: int
    severity: int