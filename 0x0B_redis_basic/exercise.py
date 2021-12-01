#!/usr/bin/env python3
""" Writing strings to Redis"""
from redis import Redis
from typing import Union
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
        ramdon_key = str(uuid4()) 
        self._redis.set(ramdon_key, data)   
        return ramdon_key
