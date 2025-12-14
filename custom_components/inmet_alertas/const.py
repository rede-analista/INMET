"""Define constants for the InMet integration."""

from datetime import timedelta

from homeassistant.const import Platform

DOMAIN = "inmet_alertas"

PLATFORMS = [Platform.GEO_LOCATION, Platform.SENSOR]

FEED = "feed"

DEFAULT_ICON = "mdi:check"
ALERT_ICON = "mdi:alert"
DEFAULT_CODE = "3507001"  # Boituva
DEFAULT_NAME = "Boituva"
DEFAULT_SCAN_INTERVAL = timedelta(minutes=30)

# Definindo o número máximo de cidades a exibir
MAX_CITIES = 5
