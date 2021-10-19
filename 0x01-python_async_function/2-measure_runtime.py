#!/usr/bin/env python3
""" The basics of async """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    starting = time()

    run(wait_n(n, max_delay))

    ending = time()

    return (ending - starting) / n
