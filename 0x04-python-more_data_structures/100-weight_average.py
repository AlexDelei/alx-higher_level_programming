#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ttl_score = sum(score * weight for score, weight in my_list)
    ttl_weight = sum(weight for _, weight in my_list)

    if ttl_weight == 0:
        return 0
    else:
        return ttl_score / ttl_weight
