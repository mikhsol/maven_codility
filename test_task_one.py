from unittest import TestCase

from maven_codility.task_one import solution


class TestTaskOne(TestCase):

    def test_array_size_out_of_range(self):
        self.assertEqual(-1, solution([]))
        self.assertEqual(-1, solution([1] * 100001))
        self.assertEqual(-1, solution([0] * 100000))

    def test_element_out_of_bound(self):
        self.assertEqual(-1, solution([10_001]))
        self.assertEqual(-1, solution([-10_001]))

    def test_single_element_zero(self):
        self.assertEqual(1, solution([0]))

    def test_single_element_non_zero(self):
        self.assertEqual(0, solution([1]))

    def test_two_elements_one_zero_element(self):
        self.assertEqual(1, solution([1, 0]))

    def test_two_elements_sum_is_zero(self):
        self.assertEqual(1, solution([2, -2]))

    def test_two_elements_no_zeros(self):
        self.assertEqual(0, solution([1, 2]))

    def test_three_elements_zero_sum_of_first_two_elements(self):
        self.assertEqual(1, solution([1, -1, 2]))

    def test_three_elements_zero_sum_of_last_two_elements(self):
        self.assertEqual(1, solution([2, -3, 3]))

    def test_three_elements_first_zero_and_zero_sum_of_last_two_elements(self):
        self.assertEqual(3, solution([0, -1, 1]))

    def test_three_elements_zero_in_the_middle_and_zero_sum_of_first_and_last_elements(self):
        self.assertEqual(2, solution([-5, 0, 5]))

    def test_four_elements_all_zeros(self):
        self.assertEqual(10, solution([0] * 4))

    def test_four_elements_all_non_zero_no_zero_sum(self):
        self.assertEqual(0, solution([1, 2, 3, 4]))

    def test_four_elements_all_non_zero_zero_sum_of_first_two_and_third(self):
        self.assertEqual(1, solution([1, 2, -3, 10]))

    def test_four_elements_all_non_zero_zero_sum_of_second_third_and_last(self):
        self.assertEqual(1, solution([1, 5, 5, -10]))

    def test_four_elements_zeros_in_the_middle_sum_of_first_and_last_zero(self):
        self.assertEqual(4, solution([5, 0, 0, -5]))

    def test_four_elements_first_and_sum_of_last_give_zero(self):
        self.assertEqual(1, solution([-10, 4, 4, 2]))

    def test_four_elements_paired_destroy_each_other(self):
        self.assertEqual(3, solution([-1, 1, 2, -2]))

    def test_five_elements_all_zeroes(self):
        self.assertEqual(15, solution([0] * 5))

    def test_five_elements_all_non_zeros_no_zero_sum(self):
        self.assertEqual(0, solution([1] * 5))

    def test_five_elements_all_non_zeros_sum_of_first_and_last_zero(self):
        self.assertEqual(2, solution([3, -3, 4, 12, -12]))

    def test_five_elements_sum_of_first_and_last_zero_and_zero_in_the_middle(self):
        self.assertEqual(6, solution([3, -3, 0, 12, -12]))

    def test_five_elements_sum_of_second_and_last_elements_zero_and_zero_in_the_middle_and_on_start(self):
        self.assertEqual(5, solution([0, -3, 0, -3, 6]))

    def test_five_elements_sum_of_first_and_last_are_zeros_large_in_the_middle(self):
        self.assertEqual(2, solution([1, -1, 1000, 3, -3]))

    def test_six_elements_from_example(self):
        self.assertEqual(4, solution([2, -2, 3, 0, 4, -7]))

