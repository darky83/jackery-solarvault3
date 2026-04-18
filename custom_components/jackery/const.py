"""Constants for the Jackery integration."""

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
)

# The domain of your integration. Should be unique.
DOMAIN = "jackery"

# Polling interval
POLLING_INTERVAL_SEC = 60


@dataclass
class JackerySensorEntityDescription(SensorEntityDescription):
    """Describes a Jackery sensor entity."""

    value: Callable[[any], any] | None = None


# Sensor descriptions
# This defines all the sensors we'll create for each device.
# Sensor descriptions
SENSOR_DESCRIPTIONS: tuple[JackerySensorEntityDescription, ...] = (
    JackerySensorEntityDescription(
        key="batSoc",
        name="Battery State of Charge",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="soc",
        name="Inverter State of Charge",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="batInPw",
        name="Battery Charge Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="batOutPw",
        name="Battery Discharge Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="inOngridPw",
        name="Grid Import Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="outOngridPw",
        name="Grid Export Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="pvPw",
        name="Solar Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="stackInPw",
        name="Total System Input Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="stackOutPw",
        name="Total System Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="cellTemp",
        name="Battery Cell Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value=lambda value: value / 10.0,
    ),
    JackerySensorEntityDescription(
        key="maxInvStdPw",
        name="Max Inverter Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    JackerySensorEntityDescription(
        key="maxOutPw",
        name="Max Output Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    JackerySensorEntityDescription(
        key="maxGridStdPw",
        name="Max Grid Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    JackerySensorEntityDescription(
        key="wsig",
        name="WiFi Signal",
        native_unit_of_measurement="dBm",
        icon="mdi:wifi",
    ),
    JackerySensorEntityDescription(
        key="last_updated",
        name="Last Updated",
        device_class=SensorDeviceClass.TIMESTAMP,
        icon="mdi:clock",
    ),
    JackerySensorEntityDescription(
        key="pvEgy",
        name="Solar Energy Total",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="pvOtBatEgy",
        name="Solar to Battery Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="inOngridEgy",
        name="Grid Import Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="outOngridEgy",
        name="Grid Export Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="ongridOtBatEgy",
        name="Grid to Battery Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="batOtGridEgy",
        name="Battery to Grid Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="batChgEgy",
        name="Battery Charged Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="batDisChgEgy",
        name="Battery Discharged Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="acOtBatEgy",
        name="AC to Battery Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="batOtAcEgy",
        name="Battery to AC Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="inEpsEgy",
        name="EPS Input Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    JackerySensorEntityDescription(
        key="outEpsEgy",
        name="EPS Output Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
)

# Binary sensor descriptions
BINARY_SENSOR_DESCRIPTIONS: tuple[BinarySensorEntityDescription, ...] = (
    BinarySensorEntityDescription(
        key="swEps",
        name="EPS Enabled",
        device_class=BinarySensorDeviceClass.POWER,
        icon="mdi:power",
    ),
    BinarySensorEntityDescription(
        key="swEpsState",
        name="EPS Active",
        device_class=BinarySensorDeviceClass.POWER,
        icon="mdi:lightning-bolt",
    ),
)
