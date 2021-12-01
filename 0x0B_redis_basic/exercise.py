#!/usr/bin/env python3
""" Writing strings to Redis"""
from redis import Redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    """ Class to cache data to redis"""
    def __init__(self):
        """constructor method"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in redis
        Args:
            data: data to be stored
        Returns:
            str: key
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Reading from Redis and recovering original type """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Parameterizes a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
