# Corona Landkreis Waldshut

This component has been created to be used with Home Assistant.

Corona Landkreis Waldshut allows you to track corona data issued by Gesundheitsamt Waldshut in Home Assistant.

### Data source

The data is fetched from https://www.landkreis-waldshut.de/aktuelles/informationen-zum-neuartigen-coronavirus

**Warning:**
As this is no official API this component can break at any time if they decide to change their website structure.

### Installation:

#### HACS

- Ensure that HACS is installed.
- Add as custom repo and install.
- Restart Home Assistant.

#### Manual installation

- Download the latest release.
- Unpack the release and copy the custom_components/corona_landkreis_waldshut directory into the custom_components directory of your Home Assistant installation.
- Restart Home Assistant.

### Example entry for configuration.yaml

```
corona_landkreis_waldshut
```

### Notes

The component will download the map image and store it into the www directory for later use.
