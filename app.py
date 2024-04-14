from point_finder import find_intermediate_points
import json
import sys


def main():
    if not len(sys.argv) == 3:
        sys.exit("Usage: python app.py [input_file.json] [output_file.json]")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file) as file:
        input_lines = json.load(file)

    outputs = []

    for index, args in enumerate(input_lines):
        a_position: tuple[float, float] = args["a_position"]
        b_position: tuple[float, float] = args["b_position"]
        distance: float = args["distance"]
        include_a: bool = args["include_a"] or False
        include_b: bool = args["include_b"] or False
        result = find_intermediate_points(
            a_position, b_position, distance, include_a, include_b
        )
        output = {
            "index": index,
            "args": args,
            "result": result,
        }
        outputs.append(output)

    with open(output_file, "w") as file:
        json.dump(outputs, file, indent=2)
    return


if __name__ == "__main__":
    main()
