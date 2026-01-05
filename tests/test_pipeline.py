import os

from src.pipelines.irrigation_pipeline import IrrigationPipelineUseCase


def test_pipeline_execution():
    # Use the sample data
    base_dir = os.path.dirname(os.path.dirname(__file__))
    readings_path = os.path.join(base_dir, "data", "readings.csv")
    metadata_path = os.path.join(base_dir, "data", "nodes.json")

    pipeline = IrrigationPipelineUseCase(readings_path, metadata_path)
    results = pipeline.execute()

    # We expect 6 rows (including one duplicate)
    assert len(results) == 6

    # Check if NODE_003 (inactive) is still processed
    node_003_results = [r for r in results if r.node_id == "NODE_003"]
    assert len(node_003_results) > 0
