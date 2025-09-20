#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:05:25 2024

@author: widhi
"""

import requests
import argparse
import sys

BASE = 'http://rest-server:5151'

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"{endpoint}({a},{b}) = {data['result']}")
        else:
            print(f"{endpoint} error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"{endpoint} exception: {e}")

def call_calc(expr):
    try:
        r = requests.get(f"{BASE}/calc", params={'expr': expr}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"calc({expr}) = {data['result']}")
        else:
            print(f"calc error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"calc exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple REST client for add/mul/calc endpoints")
    parser.add_argument('--op', choices=['add','mul', 'calc','both'], default='both', help='Operation to invoke')
    parser.add_argument('--expr', type=str, help='Expression for calc endpoint')
    parser.add_argument('-a', type=int, default=10)
    parser.add_argument('-b', type=int, default=5)
    args = parser.parse_args()
    if args.op in ('add','both'):
        call('add', args.a, args.b)
    if args.op in ('mul','both'):
        call('mul', args.a, args.b)
    if args.op == 'calc':
        if not args.expr:
            print("You must provide --expr when using --op calc")
        else:
            call_calc(args.expr)

if __name__ == '__main__':
    sys.exit(main())
