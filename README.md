# xlsx-to-json

A simple command line utility to convert excel sheets into JSON files.

## Conversion rules
Say that the desired JSON has the following structure:
```
    "foo": {
        "bar": {
            "field3": {
                ...
            },
        "bar2": val
        }
    }
```
Then `foo.bar2` should be represented in the excel sheet as a column called `foo__bar2`
Similarly, `foo.bar.field3...{last_field}` should be represented as the column `foo__bar__field3__...__{last_field}`.

Every terminal property value value in the JSON schema (that is, every value that is not composed of further nested JSON subschemas) should be stored in the cell of a column, where columns are named as explained above.

Each row generates a single JSON object. Thus multiple rows are coupled into an array of such JSON objects. 
Therefore if a single row is present in the sheet, a single JSON object is created. If multiple rows are present, an array of JSON objects is created.  

Therefore this excel sheet
| foo__bar2 | foo__bar__field3__last_field | foo__bar__field4       |
|-----------|------------------------------|------------------------|
| 1 .00     | terminal value               | another terminal value |
| val2      |                              |                        |


Generates the following file:
```json
[
 {
    "foo": {
        "bar2": 1.00,
        "bar": {
            "field3": {
                "last_field": "terminal value"
            },
            "field4": "another terminal value"
        }
    }
 },
 {
     "foo": {
         "bar2": "val2"
     }
 }
]
```
## Usage
Python and its modules must be on your PATH. The CLI can be used as follows:
```bash
xlsx_to_json path/to/excel_sheet path/to/output.json
```
### Installation

The package is available on PyPi. Simply do -
```sh
pip install xlsx_to_json
```
License
----

MIT


