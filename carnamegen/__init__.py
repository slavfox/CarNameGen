#! /usr/bin/env python3
"""Car model and brand name generator.

Usage: car_name_gen.py [-h] [-m|-b] [-s STATE_SIZE] [-n COUNT]

-h --help                               Show this message
-m --model-only                         Generate only model names
-b --brand-only                         Generate only brand names
-s STATE_SIZE, --state-size STATE_SIZE  Set state size [default: 2]
-n COUNT                                Number of names to generate [default: 1]
"""
from typing import List
from schema import Schema, And, Use, SchemaError
from docopt import docopt
from .gen import CarNameGen
from .data import BRANDS, MODELS


def run():
    args = docopt(__doc__)

    schema = Schema({
        '--state-size': And(
            Use(int),
            lambda n: 0 < n < 4,
            error='--state-size STATE_SIZE must be '
                  'an integer 0 < STATE_SIZE < 4!'
        ),
        '-n': Use(int, error='-n COUNT must be an integer!'),
        str: object
    })

    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)

    gens: List[CarNameGen] = []
    if not args['--model-only']:
        gens.append(CarNameGen(BRANDS, state_size=args['--state-size']))
    if not args['--brand-only']:
        gens.append(CarNameGen(MODELS, state_size=args['--state-size']))
    generated = 0
    for _ in range(int(args['-n'])):
        try:
            print(" ".join(g.make_sentence(
                tries=100,
                max_overlap_ratio=0.9
            ) for g in gens))
        except TypeError:
            pass
        else:
            generated += 1
    if generated != args['-n']:
        exit(1)


if __name__ == '__main__':
    run()
