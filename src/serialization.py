import csv
import json
from datetime import datetime
from typing import Dict
from typing import List

from src.entities import NodeMetadata
from src.entities import SensorReading


def load_sensor_readings(file_path: str) -> List[SensorReading]:
    """
    Loads sensor readings from a CSV file.
    """
    readings = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                readings.append(
                    SensorReading(
                        node_id=row["node_id"],
                        timestamp=datetime.fromisoformat(row["timestamp"]),
                        soil_humidity=float(row["soil_humidity"]),
                        air_temperature=float(row["air_temperature"]),
                        wind_speed=float(row["wind_speed"]),
                        et0=float(row.get("et0", 0.0)),
                    )
                )
            except (ValueError, KeyError, TypeError):
                continue
    return readings


def load_node_metadata(file_path: str) -> Dict[str, NodeMetadata]:
    """
    Loads node metadata from a JSON file.
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
        return {
            item["node_id"]: NodeMetadata(
                node_id=item["node_id"],
                location=item["location"],
                installation_date=datetime.fromisoformat(
                    item["installation_date"]
                ),
                is_active=item.get("is_active", True),
                plant_type=item.get("plant_type", "UNKNOWN"),
            )
            for item in data
        }
