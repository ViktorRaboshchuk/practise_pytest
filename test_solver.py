from unittest import TestCase
import pytest
from solver import square_equation_solver, TYPE_ERROR_TEXT


class TestSquareEquationSolverUnitTest(TestCase):
    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            square_equation_solver("", 1, 1.5)

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 1)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_solver_ok(self):
        res = square_equation_solver(1, -3, -4)
        self.assertEqual(res, (4, -1))


class TestSquareEquationSolver:
    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exc_info:
            square_equation_solver("", 1, 1.5)
        assert str(exc_info.value) == TYPE_ERROR_TEXT

    def test_result_is_tuple(self):
        res = square_equation_solver(0, 0, 1)
        assert isinstance(res, tuple)

    # @pytest.mark.parametrize("args, expected_result", [
    #     ((0, 0, 1), (None, None)),
    #     ((1, -3, -4), (4, -1)),
    # ])
    @pytest.mark.parametrize("args, expected_result", [
        pytest.param(
            (0, 0, 1), (None, None),
            id="general",
        ),
        pytest.param(
            (1, -3, -4), (4, -1),
            id="no results"
        )
    ])
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result
