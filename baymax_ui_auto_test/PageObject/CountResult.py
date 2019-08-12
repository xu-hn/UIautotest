# -*- coding: utf-8 -*-

from common.Count import count_info, count_sum

def count_result(**kwargs):
    count_info(**kwargs)
    count_sum(kwargs['result'])