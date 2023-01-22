#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy


def bubblesort(unsorted_list):

    sorted_list = copy.deepcopy(unsorted_list)
    n = len(sorted_list)
    for i in range(n):
        for j in range(n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list
