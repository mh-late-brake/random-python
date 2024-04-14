import unittest
from point_finder import find_intermediate_points


class TestFindIntermediatePoints(unittest.TestCase):
    def test_normal_case(self):
        a = (0, 0)
        b = (0, 5)
        distance = 1
        result = find_intermediate_points(a, b, distance)
        expected_result = [
            {
                "id": 0,
                "x": 0.0,
                "y": 1.0,
            },
            {
                "id": 1,
                "x": 0.0,
                "y": 2.0,
            },
            {
                "id": 2,
                "x": 0.0,
                "y": 3.0,
            },
            {
                "id": 3,
                "x": 0.0,
                "y": 4.0,
            },
            {
                "id": 4,
                "x": 0.0,
                "y": 5.0,
            },
        ]
        self.assertEqual(result, expected_result)

    def test_include_AB(self):
        a = (0, 0)
        b = (0, 5)
        distance = 1
        include_a = True
        include_b = True
        result = find_intermediate_points(a, b, distance, include_a, include_b)
        expected_result = [
            {
                "id": 0,
                "x": 0.0,
                "y": 0.0,
            },
            {
                "id": 1,
                "x": 0.0,
                "y": 1.0,
            },
            {
                "id": 2,
                "x": 0.0,
                "y": 2.0,
            },
            {
                "id": 3,
                "x": 0.0,
                "y": 3.0,
            },
            {
                "id": 4,
                "x": 0.0,
                "y": 4.0,
            },
            {
                "id": 5,
                "x": 0.0,
                "y": 5.0,
            },
        ]
        self.assertEqual(result, expected_result)

    def test_include_A(self):
        a = (0, 0)
        b = (0, 5)
        distance = 2
        include_a = True
        result = find_intermediate_points(a, b, distance, include_a=include_a)
        expected_result = [
            {
                "id": 0,
                "x": 0.0,
                "y": 0.0,
            },
            {
                "id": 1,
                "x": 0.0,
                "y": 2.0,
            },
            {
                "id": 2,
                "x": 0.0,
                "y": 4.0,
            },
        ]
        self.assertEqual(result, expected_result)

    def test_include_B(self):
        a = (0, 0)
        b = (0, 5)
        distance = 2
        include_b = True
        result = find_intermediate_points(a, b, distance, include_b=include_b)
        expected_result = [
            {
                "id": 0,
                "x": 0.0,
                "y": 2.0,
            },
            {
                "id": 1,
                "x": 0.0,
                "y": 4.0,
            },
            {
                "id": 2,
                "x": 0.0,
                "y": 5.0,
            },
        ]
        self.assertEqual(result, expected_result)

    def test_invalid_args_points_coincide(self):
        a = (0, 0)
        b = (0, 0)
        distance = 2
        with self.assertRaises(ValueError):
            find_intermediate_points(a, b, distance)

    def test_invalid_args_distance(self):
        a = (1, 2)
        b = (2, 3)
        distance = 0
        with self.assertRaises(ValueError):
            find_intermediate_points(a, b, distance)

    # NOTE: Write more test with float vector and float distance
    def test_float(self):
        a = (0, 0)
        b = (5.5, 5.5)
        distance = 1.4142135623730951
        result = find_intermediate_points(a, b, distance)
        expected_result = [
            {
                "id": 0,
                "x": 1.0,
                "y": 1.0,
            },
            {
                "id": 1,
                "x": 2.0,
                "y": 2.0,
            },
            {
                "id": 2,
                "x": 3.0,
                "y": 3.0,
            },
            {
                "id": 3,
                "x": 4.0,
                "y": 4.0,
            },
            {
                "id": 4,
                "x": 5.0,
                "y": 5.0,
            },
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
