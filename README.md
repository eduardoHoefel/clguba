# Clguba - The Python rot13 programming language

## About

Clguba is just about python lambdas with an extra rot13 cryptography.

## How it works

The first argument is the python lambda function to execute, rot13 encoded.
The next arguments are then passed to the lambda function and can be accessed by the variables a, b, c, and so on.

Some functions have alias. For example:

```
R = shapgbbyf.erqhpr (functools.reduce)
```

## Code examples

* Hello world:

```
Uryyb Jbeyq!
```

* 1 + 1:

```
1+1
```

* Find the Nth fibonacci number:

```
R(ynzoqn k,a:[k[1],k[0]+k[1]],enatr(a),[0,1])[0]
```

## System Requirements

* Python 3.6

## Usage

```sh
$ python clguba.py <PROGRAM> <ARG1> <ARG2> ... <ARGN>
```

## Contributions

Any contributions are accepted. However, some of them are more necessary right now. They are:

* To test and look for bugs
* Suggestions about new alias
* More code examples
* Real usage in Code Golf challenges (that would be awesome)

## TODO

* Add new alias
* Enable decode of multiple rot13 layers

## License

See the [LICENSE](LICENSE) file for license rights and limitations (GPLv2).
