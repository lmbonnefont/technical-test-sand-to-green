from typing import List

from src.lib import calculate_irrigation_need
from src.entities import IrrigationAdvice
from src.serialization import load_node_metadata
from src.serialization import load_sensor_readings


class IrrigationPipelineUseCase:
    """
    Orchestrates the processing of sensor data into irrigation advice.
    """

    def __init__(self, readings_path: str, metadata_path: str):
        self.readings_path = readings_path
        self.metadata_path = metadata_path

    def execute(self) -> List[IrrigationAdvice]:
        # 1. Load data
        readings = load_sensor_readings(self.readings_path)
        metadata_map = load_node_metadata(self.metadata_path)

        # Kc Mapping
        KC_MAP = {
            "OLIVE_TREE": 0.7,
            "DATE_PALM": 0.9,
        }

        # 2. Process
        advices = []
        for reading in readings:
            # 2.1 Filter by metadata and activity status
            node_meta = metadata_map.get(reading.node_id)
            if not node_meta or not node_meta.is_active:
                continue

            # 2.2 Get Kc for the plant
            kc = KC_MAP.get(node_meta.plant_type, 1.0)

            # 2.3 Calculate advice
            advice = calculate_irrigation_need(reading, kc=kc)
            advices.append(advice)

        return advices
