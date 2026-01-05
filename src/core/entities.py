from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SensorReading:
    node_id: str
    timestamp: datetime
    soil_humidity: float  # Percentage (0-100)
    air_temperature: float  # Celsius
    wind_speed: float  # m/s
    et0: float  # Reference Evapotranspiration (mm/hour)


@dataclass(frozen=True)
class NodeMetadata:
    node_id: str
    location: str
    installation_date: datetime
    is_active: bool
    plant_type: str  # e.g., "OLIVE_TREE", "DATE_PALM"


@dataclass(frozen=True)
class IrrigationAdvice:
    node_id: str
    timestamp: datetime
    water_liters_m2: float
    status: str  # OPTIONAL, REQUIRED, CRITICAL
    details: str

    def to_dict(self):
        return asdict(self)
