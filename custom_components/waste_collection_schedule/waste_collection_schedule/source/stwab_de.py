import json
import logging

import requests
from waste_collection_schedule import Collection  # type: ignore[attr-defined]
from waste_collection_schedule.service.ICS import ICS

_LOGGER = logging.getLogger(__name__)

TITLE = "Stadtwerke Aschaffenburg"
DESCRIPTION = "Source for Stadtwerke Aschaffenburg."
URL = "https://www.stwab.de/"
TEST_CASES = {"Bezirk Innenstadt": {"district": "1649", "year": 2022}}


class Source:
    def __init__(self, district, year):
        self._district = district
        self._year = year
        self._ics = ICS()

    def fetch(self):
        params = {
            "Bezirk_ID": self._district,
            "Jahr": self._year,
            "SessionMandant": "Aschaffenburg",
            "Anwendung": "Abfuhrkalender",
            "Methode": "TermineAnzeigenICS",
            "Mandant": "Aschaffenburg",
            "Abfuhrkalender": "Aschaffenburg",
        }

        # download ICS File (Fill User-Agent to prevent 403)
        r = requests.get(
            "https://www.stwab.de/aschaffenburgGips/Gips",
            params=params,
            headers={"User-Agent": "Mozilla/5.0"},
        )

        dates = self._ics.convert(r.text)

        entries = []
        for d in dates:
            entries.append(Collection(d[0], d[1]))
        return entries
