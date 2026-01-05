import os

from src.use_cases import IrrigationPipelineUseCase


def test_pipeline_execution():
    # Use the sample data
    base_dir = os.path.dirname(os.path.dirname(__file__))
    readings_path = os.path.join(base_dir, "data", "readings.csv")
    metadata_path = os.path.join(base_dir, "data", "nodes.json")

    pipeline = IrrigationPipelineUseCase(readings_path, metadata_path)
    results = pipeline.execute()

    # We expect 5 rows (NODE_003 is inactive and skipped)
    assert len(results) == 5

    # Check if NODE_003 (inactive) is skipped
    node_003_results = [r for r in results if r.node_id == "NODE_003"]
    assert len(node_003_results) == 0

