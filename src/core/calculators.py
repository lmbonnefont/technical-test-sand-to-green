from src.core.entities import IrrigationAdvice
from src.core.entities import SensorReading

HUMIDITY_THRESHOLD_CRITICAL = 15.0  # %
HUMIDITY_THRESHOLD_REQUIRED = 40.0  # %


def calculate_irrigation_need(
    reading: SensorReading, kc: float = 1.0
) -> IrrigationAdvice:
    """
    Calculates the water requirement in Liters/m2 based on:
    - Evapotranspiration (ET0)
    - Plant-specific Crop Coefficient (Kc)
    - Soil humidity (baseline)

    Logic:
    1. Compute target humidity based on ET0 and Kc.
    2. Compare current humidity to target.
    3. Determine status: SURPLUS, OPTIMAL, DEFICIT, or CRITICAL.
    """

    # Target humidity based on ET0 and Kc (Fake computation for the test)
    # Higher ET0 and Kc mean the plant needs higher soil moisture.
    target_humidity = 30.0 + (reading.et0 * kc * 10.0)

    diff = reading.soil_humidity - target_humidity

    # Calculate water needed
    # Simple factor: 0.5 L/m2 per percentage point below target.
    water_liters = max(0.0, (target_humidity - reading.soil_humidity) * 0.5)

    # Determine status
    if diff > 10:
        status = "SURPLUS"
    elif 0 <= diff <= 10:
        status = "OPTIMAL"
    elif -10 <= diff < 0:
        status = "DEFICIT"
    else:
        status = "CRITICAL"

    details = (
        f"ET0: {reading.et0}mm/h | Kc: {kc} | "
        f"Hum: {reading.soil_humidity}% | Target: {target_humidity:.1f}%"
    )

    return IrrigationAdvice(
        node_id=reading.node_id,
        timestamp=reading.timestamp,
        water_liters_m2=round(water_liters, 2),
        status=status,
        details=details,
    )
