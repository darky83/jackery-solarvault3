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
DOMAIN = "jackery-solarvault3"

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
        value=lambda data: (data.get("cellTemp") / 10.0) if data.get("cellTemp") is not None else None,
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
    # PV sensors
    JackerySensorEntityDescription(
        key="pv1_name",
        name="PV1 Name",
        value=lambda data: data.get("pv1", {}).get('name'),
        icon="mdi:solar-panel",
    ),
    JackerySensorEntityDescription(
        key="pv1_pvPw",
        name="PV1 Power",
        value=lambda data: data.get("pv1", {}).get('pvPw'),
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="pv1_commState",
        name="PV1 Communication State",
        value=lambda data: data.get("pv1", {}).get('commState'),
        icon="mdi:wifi",
    ),
    JackerySensorEntityDescription(
        key="pv2_name",
        name="PV2 Name",
        value=lambda data: data.get("pv2", {}).get('name'),
        icon="mdi:solar-panel",
    ),
    JackerySensorEntityDescription(
        key="pv2_pvPw",
        name="PV2 Power",
        value=lambda data: data.get("pv2", {}).get('pvPw'),
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="pv2_commState",
        name="PV2 Communication State",
        value=lambda data: data.get("pv2", {}).get('commState'),
        icon="mdi:wifi",
    ),
    JackerySensorEntityDescription(
        key="pv3_name",
        name="PV3 Name",
        value=lambda data: data.get("pv3", {}).get('name'),
        icon="mdi:solar-panel",
    ),
    JackerySensorEntityDescription(
        key="pv3_pvPw",
        name="PV3 Power",
        value=lambda data: data.get("pv3", {}).get('pvPw'),
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="pv3_commState",
        name="PV3 Communication State",
        value=lambda data: data.get("pv3", {}).get('commState'),
        icon="mdi:wifi",
    ),
    JackerySensorEntityDescription(
        key="pv4_name",
        name="PV4 Name",
        value=lambda data: data.get("pv4", {}).get('name'),
        icon="mdi:solar-panel",
    ),
    JackerySensorEntityDescription(
        key="pv4_pvPw",
        name="PV4 Power",
        value=lambda data: data.get("pv4", {}).get('pvPw'),
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    JackerySensorEntityDescription(
        key="pv4_commState",
        name="PV4 Communication State",
        value=lambda data: data.get("pv4", {}).get('commState'),
        icon="mdi:wifi",
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
