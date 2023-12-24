#!/usr/bin/env python
# -*- coding: utf-8 -*-
from geo.quadrant import Quadrant
from geo.tycat import tycat
from random import Random
from collections import defaultdict
from math import log

# a exporter :
# export PYTHONHASHSEED=0

XSCALE = 8
YSCALE = 12


class Dummy:
    def __init__(self):
        pass


DUMMY = Dummy()


def clip(var):
    string = str(var)
    if len(string) >= 10:
        return "..."+string[-7:]
    else:
        return string


def hashes(key):
    """
    iterates on all hashes for given key
    """
    real_hash = hash(key)
    yield real_hash
    generator = Random(0)
    while True:
        yield generator.randint(0, 2**64-1) ^ real_hash


class HashTable:
    def __init__(self, elements=(), size=8):
        self.buckets = [[None, None, None] for _ in range(size)]
        self.occupancy = 0
        for e in elements:
            self.insert(*e)

    def resize(self, size):
        """
        resize the table to given size
        """
        new_table = HashTable(self.items(), size)
        self.buckets = new_table.buckets
        self.occupancy = new_table.occupancy

    def insert(self, key, value):
        """
        insert key/value pair into table
        """
        b = self.bucket_for(key)
        old_value = b[2]
        b[1] = key
        b[2] = value
        self.occupancy += 1
        if self.occupancy > 2/3*len(self.buckets):
            self.resize(2*len(self.buckets))
        return old_value

    def items(self):
        """
        iterates on all key/value pairs
        """
        for _, key, value in self.buckets:
            if key is not None and key is not DUMMY:
                yield key, value

    def bucket_for(self, key):
        """
        return bucket for given key.
        if not yet in the table also register the hash used
        """
        for h in hashes(key):
            index = h % len(self.buckets)
            if self.buckets[index][1] is None or\
               self.buckets[index][1] is DUMMY:
                self.buckets[index][0] = h
                return self.buckets[index]
            if self.buckets[index][0] == h:
                if self.buckets[index][1] == key:
                    return self.buckets[index]

    def __contains__(self, key):
        """
        do we contain given key ?
        """
        b = self.bucket_for(key)
        return b[1] is not None

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        """
        remove target key if any.
        """
        b = self.bucket_for(key)
        if b[1] is not None and b[1] is not DUMMY:
            b[1] = DUMMY
            b[2] = None
            self.occupancy -= 1

    def stats(self):
        distances = defaultdict(int)
        for i, bucket in enumerate(self.buckets):
            if bucket[1] is not None and bucket[1] is not DUMMY:
                distance = next(d for d, h in enumerate(hashes(bucket[1])) if h % len(self.buckets) == i) + 1
                distances[distance] += 1
        for distance, count in distances.items():
            print(distance, count)
        total_distances = sum(d*c for d, c in distances.items())
        m = len(self.buckets)
        n = self.occupancy
        print("buckets number:", m)
        print("keys number:", n)
        print("prediction:", m/n*(log(m) - log(m-n)))

        print("real average:", total_distances / self.occupancy)

    def bounding_quadrant(self):
        column_sizes = [
                max(len(clip(c[i])) for c in self.buckets)
                for i in range(3)
        ]
        width = sum(column_sizes)
        width += 3  # add 3 characters to display distances
        return Quadrant([0, 0], [width*XSCALE, len(self.buckets)*YSCALE])

    def svg_content(self):
        string = ""
        column_sizes = [
                max(len(clip(c[i])) for c in self.buckets)
                for i in range(3)
        ]
        for i, columns in enumerate(self.buckets):
            x = 0
            if columns[1] is not None and columns[1] is not DUMMY:
                fill = "lightgray"
                text_color = "black"
            else:
                fill = "black"
                text_color = "lightgray"
            for data, size in zip(columns, column_sizes):
                string += "<rect x='{}' y='{}' width='{}' height='{}' fill='{}' stroke='black'/>\n".format(x, i*YSCALE, size*XSCALE, YSCALE, fill)
                text = "DUMMY" if data is DUMMY else clip(data)
                string += "<text x='{}' y='{}' fill='{}' stroke='none'>{}</text>".format(x, i*YSCALE + 10, text_color, text)
                x += size * XSCALE
            if columns[1] is not None and columns[1] is not DUMMY:
                distance = next(d for d, h in enumerate(hashes(columns[1])) if h % len(self.buckets) == i) + 1
                if distance == 1:
                    color = "green"
                elif distance == 2:
                    color = "orange"
                else:
                    color = "red"
                string += "<text x='{}' y='{}' fill='{}' stroke='none'>{}</text>".format(x+XSCALE, i*YSCALE + 10, color, distance)
        return string


def main():
    # keys = ["hello", "world", "j'aime", "le", "python"]
    # t = HashTable(((s, len(s)) for s in keys))
    # tycat(t)
    # t.insert("boom", 4)
    # tycat(t)
    # # del t["boom"]
    # # tycat(t)
    # # t[5] = 5
    # # tycat(t)
    # # print(list(t.items()))
    # # print(0 in t, 1 in t)

    with open("words.txt") as words:
        d = HashTable(((w, len(w)) for w in words))
        d.stats()


main()
