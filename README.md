#CarNameGen

Dirt simple and tiny fun Python 3 script to generate fictional car names.

```
$ carnamegen --help

Car model and brand name generator.

Usage: car_name_gen.py [-h] [-m|-b] [-s STATE_SIZE] [-n COUNT]

-h --help                               Show this message
-m --model-only                         Generate only model names
-b --brand-only                         Generate only brand names
-s, --state-size STATE_SIZE  Set state size [default: 2]
-n COUNT       

$ carnamegen -n10
Voley Man GT-R
Acury Sunfini
Isubach Leming
Merati Moderies
Audillman Colibur
Landa Fir Septort
Chryslet Maxiessigon GX
Ramborpe Explort
Corgan Trado
Hiley 9290
```

# Installation

Requires [poetry].

```
$ git clone git@github.com:slavfox/CarNameGen.git
$ cd CarNameGen
$ poetry install
```

Or not! You can also manually install the requirements and run `carnamegen.py`:

```
$ pip install markovify docopt schema
$ python3 carnamegen.py -n5
Toycedesla Menge
McLan Excudelub
Hills-Ben Brontus
Audillman Yare
Morpe Silly
```

I'm not your mom to tell you what to do.


# License
Carnamegen is licensed [WTFPL].
```
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004
 
Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.
 
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
```


The [dataset] was compiled by [Nate Barr] and is used here under its 
[CC-BY-2.5] license.

[poetry]: https://github.com/sdispater/poetry
[wtfpl]: http://www.wtfpl.net
[dataset]: https://github.com/n8barr/automotive-model-year-data
[Nate Barr]: https://github.com/n8barr/
[CC-BY-2.5]: https://creativecommons.org/licenses/by/2.5/
