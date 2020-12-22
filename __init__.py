import logging
import re
from datetime import timedelta as td

import aiohttp
from homeassistant.util import Throttle

from .const import PATTERNS

LOGGER = logging.getLogger(__name__)

DOMAIN = "corona_landkreis_waldshut"

MIN_TIME_BETWEEN_UPDATES = td(seconds=1800)

# URL = "https://www.landkreis-waldshut.de/nc/aktuelles/informationen-zum-neuartigen-coronavirus/"
URL = "https://www.landkreis-waldshut.de/aktuelles/informationen-zum-neuartigen-coronavirus"


async def async_setup(hass, config):

    hass.data[DOMAIN] = CoronaLandkreisWaldshut()

    LOGGER.debug("Setup done")
    # Return boolean to indicate that initialization was successful.
    return True


class CoronaLandkreisWaldshut:
    def __init__(self):
        self.data = {
            "total": None,
            "delta_active": None,
            "active": None,
            "delta_recovered": None,
            "recovered": None,
            "deaths": None,
            "incidence": None,
        }

    async def get_data(self, sensor):
        await self.update()
        return self.data[sensor]

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def update(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                data = await response.text()
                for s, p in PATTERNS.items():
                    try:
                        v = re.search(p["p"], data.replace("&nbsp;", " ")).group(1)
                        if p["t"] == "int":
                            self.data[s] = int(v)
                        elif p["t"] == "float":
                            self.data[s] = float(v.replace(",", "."))
                    except Exception as e:
                        LOGGER.error("Failed to get value via regex for %s", s)
                        LOGGER.error(e)
                        self.data[s] = None
                    LOGGER.debug("Found value %s for %s", self.data[s], s)
