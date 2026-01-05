import os

from src.pipelines.irrigation_pipeline import IrrigationPipelineUseCase


def main():
    print("--- RegenWise Smart Irrigation Engine ---")

    # Paths
    base_dir = os.path.dirname(os.path.dirname(__file__))
    readings_path = os.path.join(base_dir, "data", "readings.csv")
    metadata_path = os.path.join(base_dir, "data", "nodes.json")

    # Run pipeline
    pipeline = IrrigationPipelineUseCase(readings_path, metadata_path)
    results = pipeline.execute()

    # Summary
    print(f"Processed {len(results)} hourly readings.")

    stats = {
        "SURPLUS": len([r for r in results if r.status == "SURPLUS"]),
        "OPTIMAL": len([r for r in results if r.status == "OPTIMAL"]),
        "DEFICIT": len([r for r in results if r.status == "DEFICIT"]),
        "CRITICAL": len([r for r in results if r.status == "CRITICAL"]),
    }

    print(f"Stats: {stats}")

    # Display top 5 results
    print("\nTop 5 Irrigation Advices:")
    for r in results[:5]:
        print(
            f"[{r.timestamp}] Node: {r.node_id} | "
            f"Need: {r.water_liters_m2} L/m2 | Status: {r.status}"
        )


if __name__ == "__main__":
    main()
