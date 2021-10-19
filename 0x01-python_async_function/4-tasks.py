#!/usr/bin/env python3
""" The basics of async """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay.
    """
    array0, array1 = [], []

    for _ in range(n):
        array0.append(task_wait_random(max_delay))

    for runner in asyncio.as_completed(array0):
        result = await runner
        array1.append(result)

    return array1
