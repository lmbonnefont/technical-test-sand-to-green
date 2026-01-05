from datetime import datetime

from src.lib import calculate_irrigation_need
from src.entities import SensorReading


def test_calculate_irrigation_need_critical():
    reading = SensorReading(
        node_id="TEST",
        timestamp=datetime.now(),
        soil_humidity=5.0,
        air_temperature=40.0,
        wind_speed=10.0,
        et0=1.0,
    )
    # target = 30 + (1.0 * 1.0 * 10) = 40. diff = 5 - 40 = -35 (CRITICAL)
    advice = calculate_irrigation_need(reading, kc=1.0)
    assert advice.status == "CRITICAL"
    assert advice.water_liters_m2 > 0


def test_calculate_irrigation_need_surplus():
    reading = SensorReading(
        node_id="TEST",
        timestamp=datetime.now(),
        soil_humidity=80.0,
        air_temperature=15.0,
        wind_speed=1.0,
        et0=0.1,
    )
    # target = 30 + (0.1 * 1.0 * 10) = 31. diff = 80 - 31 = 49 (SURPLUS)
    advice = calculate_irrigation_need(reading, kc=1.0)
    assert advice.status == "SURPLUS"
    assert advice.water_liters_m2 == 0
