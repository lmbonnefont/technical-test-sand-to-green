from typing import List

from src.core.calculators import calculate_impact_score
from src.core.entities import ImpactScore
from src.infrastructure.data_access import load_node_metadata
from src.infrastructure.data_access import load_sensor_readings


class ScoringPipelineUseCase:
    """
    Orchestrates the processing of sensor data into impact scores.
    """

    def __init__(self, readings_path: str, metadata_path: str):
        self.readings_path = readings_path
        self.metadata_path = metadata_path

    def execute(self) -> List[ImpactScore]:
        # 1. Load data
        readings = load_sensor_readings(self.readings_path)
        metadata = load_node_metadata(self.metadata_path)

        # 2. Process
        scores = []
        for reading in readings:
            # BUG: We should probably check if node exists in metadata
            # and if it's active before calculating score.
            score = calculate_impact_score(reading)
            scores.append(score)

        return scores
