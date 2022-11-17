# HVCGroep

Support for schedules provided by [Stadtwerke Aschaffenburg](https://www.stwab.de/).

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: stadtwerke_aschaffenburg_de
      args:
        bezirk: BEZIRK
        year: YEAR
```

### Configuration Variables

**bezirk**<br>
*(string) (required)*
*to find the correct 'bezirk', please visit https://www.stwab.de/Abfall-Stadtreinigung/Muellabfuhr/Abfuhrtermine-und-Bezirk/ and click on your street. You will find the 'bezirk' ID in the URL (e.g. BezirkId=1666)*

**year**<br>
*(string) (required)*

## Example

```yaml
waste_collection_schedule:
  sources:
    - name: stadtwerke_aschaffenburg_de
      args:
        bezirk: 1649
        year: 2022
```
