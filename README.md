## Usage:
```shell
$ python app.py [input_file.json] [output_file.json]
```
### [input_file.json]
[input_file.json]: the .json file to be inputed.  
Input file should have a LIST of DICT.  

```json
[dict, dict, dict]
```

Example:

```json
[
  {
    "a_position": [0, 0],
    "b_position": [0, 5],
    "distance": 1,
    "include_a": false,
    "include_b": false
  },
  {
    "a_position": [0, 0],
    "b_position": [0, 5],
    "distance": 2,
    "include_a": false,
    "include_b": true
  }
]
```

In the above example, there are 2 dicts in the list. Each dict contain all the parameter that will be inputed into the "find_intermediate_points" function.

Note: "include_a" and "include_b" can be omitted. When omit, will default to false.

### [output_file.json]
output file will contain a LIST of DICT.

Example:

```json
[
  {
    "index": 0,
    "args": {
      "a_position": [0, 0],
      "b_position": [0, 5],
      "distance": 1,
      "include_a": false,
      "include_b": false
    },
    "result": [
      { "id": 0, "x": 0.0, "y": 1.0 },
      { "id": 1, "x": 0.0, "y": 2.0 },
      { "id": 2, "x": 0.0, "y": 3.0 },
      { "id": 3, "x": 0.0, "y": 4.0 },
      { "id": 4, "x": 0.0, "y": 5.0 }
    ]
  },
  {
    "index": 1,
    "args": {
      "a_position": [0, 0],
      "b_position": [0, 5],
      "distance": 2,
      "include_a": false,
      "include_b": true
    },
    "result": [
      { "id": 0, "x": 0.0, "y": 2.0 },
      { "id": 1, "x": 0.0, "y": 4.0 },
      { "id": 2, "x": 0, "y": 5 }
    ]
  }
]
```
Each dict contain:
- index: index.
- args: the argument from input file (used as parameters to call the "find_intermediate_points" function).
- result: the return result from "find_intermediate_points" function.

## Run test:
```shell
$ python test_find_intermediate_points.py
```

## Write test:
Modify test_find_intermediate_points.py file.
