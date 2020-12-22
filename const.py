
SENSORS = {
    "total": "mdi:emoticon-neutral-outline",
    "delta_active": "mdi:emoticon-sad-outline",
    "active": "mdi:emoticon-sad-outline",
    "delta_recovered": "mdi:emoticon-happy-outline",
    "recovered": "mdi:emoticon-happy-outline",
    "deaths": "mdi:emoticon-cry-outline",
    "incidence": "mdi:numeric-7-box",
}

PATTERNS = {
    "total": {"p": r"Positiv getestete Personen: (\d+)", "t": "int"},
    "delta_active": {"p": r"Positiv getestete Personen: \d+ \(([\+\-\d]+)\)", "t": "int"},
    "active": {"p": r"Derzeit aktive Infektionen: (\d+)", "t": "int"},
    "delta_recovered": {"p": r"Genesene Personen: \d+ \(([\+\-\d]+)\)", "t": "int"},
    "recovered": {"p": r"Genesene Personen: (\d+)", "t": "int"},
    "deaths": {"p": r"Verstorbene Personen: (\d+)", "t": "int"},
    "incidence": {"p": r"7-Tage-Inzidenz: ([\d,]+)", "t": "float"}
}
