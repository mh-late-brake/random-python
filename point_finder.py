from typing import Union
from math import floor, sqrt


def find_intermediate_points(
    a_position: tuple[float, float],
    b_position: tuple[float, float],
    distance: float,
    include_a: bool = False,
    include_b: bool = False,
) -> list[dict[str, Union[float, int]]]:
    """
    Given the position of A, B and the distance D.
    Find all the possible positions of point X that satisfy:
    - X lies on the line segment AB (A and B are function parameters)
    - Distant from point X to A (d(A,X)) is a multiple of D: d(A,X) = kD (k is integer)

    Args:
        a_position (tuple[float, float]): position of point A in Oxy plane. tuple[0]: x. tuple[1]: y.
        b_position (tuple[float, float]): position of point B in Oxy plane. tuple[0]: x. tuple[1]: y.
        distance (float): distance D in (d(A,X) = kD (k is integer)). D must be greater than 0
        include_a (bool): whether to include point A in the (beginning of) return list or not (default to False)
        include_b (bool): whether to include point B in the (end of) return list or not (default to False) (if d(A,B) % D == 0, point B is always included)

    Returns:
        list[dict[str, Union[float, int]]]: a list of dict. Each dict is a position of X. Each dict has this form: { "id": int (equal to the index of this point in the return list), "x": float, "y": float }

    Raises:
        ValueError if A and B coincide
        ValueError if D is not greater than 0
    """

    # Check inputs valid or not
    if a_position == b_position:
        raise ValueError("Point A and B concide.")

    if not distance > 0:
        raise ValueError("Distance is invalid (must be greater than 0)")

    # Calculate scaled vector
    vector_ab: tuple[float, float] = (
        b_position[0] - a_position[0],
        b_position[1] - a_position[1],
    )
    scaled_vector: tuple[float, float] = scale_vector_to_size(vector_ab, distance)

    num_of_satisfying_points = calculate_num_of_points(a_position, b_position, distance)

    # This is the final return list
    satisfying_points: list[dict[str, Union[int, float]]] = []

    # Calculate positions and add to the return list
    start_count = 0
    end_count = (
        num_of_satisfying_points if not include_a else num_of_satisfying_points + 1
    )
    offset = 1 if not include_a else 0

    for i in range(start_count, end_count):
        new_satisfying_point = {
            "id": i,
            "x": a_position[0] + (i + offset) * scaled_vector[0],
            "y": a_position[1] + (i + offset) * scaled_vector[1],
        }
        satisfying_points.append(new_satisfying_point)

    # Only add B to the list if include_b == True and B is not already in the list (in case d(B,A) % D == 0)
    if include_b and b_position != (
        satisfying_points[-1]["x"],
        satisfying_points[-1]["y"],
    ):
        satisfying_points.append(
            {
                "id": end_count,
                "x": b_position[0],
                "y": b_position[1],
            }
        )

    return satisfying_points


def calculate_num_of_points(
    a_position: tuple[float, float], b_position: tuple[float, float], distance: float
) -> int:
    """
    Calculate number of points on the line segment AB that satisfy: d(A,X) = k * distance (k is integer)

    Args:
        a_position (tuple[float, float]): position of A. tuple[0] is x. tuple[1] is y
        b_position (tuple[float, float]): position of B. tuple[0] is x. tuple[1] is y
        distance (float): distance

    Returns:
        int: number of satisfying points

    Raises:
        ValueError if A and B coincide
        ValueError if D is not greater than 0
    """
    if a_position == b_position:
        raise ValueError("Point A and B concide.")

    if not distance > 0:
        raise ValueError("Distance is invalid (must be greater than 0)")

    (x1, y1) = a_position
    (x2, y2) = b_position

    distance_ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    num_of_satisfying_points = floor(distance_ab / distance)

    return num_of_satisfying_points


def scale_vector_to_size(
    origin_vector: tuple[float, float], desired_size: float
) -> tuple[float, float]:
    """
    Return the scaled to desired_size version of the input origin_vector

    Args:
        origin_vector (tuple[float, float]): the input vector. tuple[0] is x. tuple[1] is y.
        desired_size (float): desired_size

    Returns:
        tuple[float, float]: the vector with desired size. tuple[0] is x. tuple[1] is y.

    Raises:
        ValueError if origin_vector == (0,0)
        ValueError if desired_size not > 0
    """
    if origin_vector == (0, 0):
        raise ValueError("Invalid origin_vector")
    if not desired_size > 0:
        raise ValueError("dinvalid esired_size")

    current_size = sqrt(origin_vector[0] ** 2 + origin_vector[1] ** 2)
    scaling_factor = desired_size / current_size
    final_vector = (
        origin_vector[0] * scaling_factor,
        origin_vector[1] * scaling_factor,
    )
    return final_vector
