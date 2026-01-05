from datetime import datetime

from src.core.calculators import calculate_irrigation_need
from src.core.entities import SensorReading


def test_calculate_irrigation_need_critical():
    reading = SensorReading(
        node_id="TEST", timestamp=datetime.now(), soil_humidity=5.0, air_temperature=40.0, wind_speed=10.0  # Very low
    )
    advice = calculate_irrigation_need(reading)
    assert advice.status == "CRITICAL"
    assert advice.water_liters_m2 > 0


def test_calculate_irrigation_need_optional():
    reading = SensorReading(
        node_id="TEST", timestamp=datetime.now(), soil_humidity=80.0, air_temperature=15.0, wind_speed=1.0  # High
    )
    advice = calculate_irrigation_need(reading)
    assert advice.status == "OPTIONAL"
