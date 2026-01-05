import sys
import os
from datetime import datetime

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.entities import SensorReading
from src.core.calculators import calculate_irrigation_need


def test_irrigation():
    test_cases = [
        # node_id, hum, et0, kc, expected_status
        ("OLIVE_DRY", 30.0, 0.8, 0.7, "CRITICAL"),
        ("OLIVE_V_DRY", 20.0, 0.8, 0.7, "CRITICAL"),
        ("DATE_DRY", 30.0, 0.8, 0.9, "CRITICAL"),
        ("DATE_V_DRY", 20.0, 0.8, 0.9, "CRITICAL"),
        ("OPTIMAL_CASE", 40.0, 0.5, 0.7, "OPTIMAL"),
    ]

    # Recalculate expectations based on new logic
    # target = 30.0 + (et0 * kc * 10.0)
    # > 10: SURPLUS, [0, 10]: OPTIMAL, [-10, 0[: DEFICIT, < -10: CRITICAL

    header = (
        f"{'Node ID':<15} | {'Hum':<5} | {'ET0':<5} | {'Kc':<5} | "
        f"{'Target':<6} | {'Need':<5} | {'Status':<10}"
    )
    print(header)
    print("-" * 75)

    for node_id, hum, et0, kc, expected_status in test_cases:
        reading = SensorReading(
            node_id=node_id,
            timestamp=datetime.now(),
            soil_humidity=hum,
            air_temperature=25.0,
            wind_speed=2.0,
            et0=et0
        )
        advice = calculate_irrigation_need(reading, kc=kc)

        # Extract target from details
        target_str = advice.details.split("Target: ")[1].replace("%", "")

        row = (
            f"{node_id:<15} | {hum:<5.1f} | {et0:<5.1f} | {kc:<5.1f} | "
            f"{target_str:<6} | {advice.water_liters_m2:<5.1f} | "
            f"{advice.status:<10}"
        )
        print(row)


if __name__ == "__main__":
    test_irrigation()
