from point_finder import find_intermediate_points
import json

INPUT_FILE_PATH = "/home/sdv/py_test/depends/NODE.json"
DISTANCE = 1.5


def main():
    # Load input file
    with open(INPUT_FILE_PATH) as file:
        input_points = json.load(file)

    # Prompt user to choose 2 points
    point_a_id = input("Enter point A id: ")
    point_b_id = input("Enter point B id: ")

    # Find 2 user-inputted point
    point_a = None
    point_b = None

    for point in input_points:
        if point["id"] == point_a_id:
            point_a = point
        if point["id"] == point_b_id:
            point_b = point

    # Show error if cannot find 2 user-inputted points
    if not point_a:
        print("Point A does not exist in the input file")
        return
    if not point_b:
        print("Point B does not exist in the input file")
        return

    # Call the "find_intermediate_points" function with 2 user-inputted point
    satisfying_points = find_intermediate_points(
        (point_a["x"], point_a["y"]), (point_b["x"], point_b["y"]), DISTANCE
    )

    # Remove point B if point B exist in the final return list
    # incase (d(A,B) % DISTANCE == 0)
    if (
        satisfying_points[-1]["x"] == point_b["x"]
        and satisfying_points[-1]["y"] == point_b["y"]
    ):
        del satisfying_points[-1]

    # Format the output JSON
    list_of_output_points = []
    for point in satisfying_points:
        output_points = {
            "id": point_a_id + point_b_id + str(point["id"]),
            "x": point["x"],
            "y": point["y"],
            "yaw": "None",
            "collision": "N",
        }
        list_of_output_points.append(output_points)

    output_path = f"result-generate-id-{point_a_id}-and-{point_b_id}.json"

    # Dump JSON to output file
    with open(output_path, "w") as file:
        json.dump(list_of_output_points, file, indent=2)

    print(f"Generated output file: {output_path}")


if __name__ == "__main__":
    main()
