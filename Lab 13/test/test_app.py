#!/usr/bin/python
# -*- coding: utf-8 -*-

from bubblesort import bubblesort
import pytest


testdata_bubble = [([2, 5, 4, 2, 1, 89, 45, 3, 2], [1, 2, 2, 2, 3, 4, 5, 45, 89]),
                   ([6, 4, 1, 2, 6, 7, 10, 12, 11], [1, 2, 4, 6, 6, 7, 10, 11, 12]),
                   ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]


@pytest.mark.parametrize('sample, expected_output', testdata_bubble)
def test_bubblesort(sample, expected_output):

    assert bubblesort(sample) == expected_output
