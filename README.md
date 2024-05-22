# Memphis Traffic Analyzer

This package provides a graphic analyzer for [Memphis-V](https://github.com/gaph-pucrs/Memphis-5).

## Installation

```console
python -m build
python -m installer dist/*.whl
```

* Requires Python >=3.8

## Usage

Plot an application traffic:
```console
memphis-ta <SCENARIO> <ID>
```

You can plot multiple IDs:
```console
memphis-ta <SCENARIO> <ID> <ID> <ID>
```

Instead of plotting, it is possible to save the graph:
You can plot multiple IDs:
```console
memphis-ta <SCENARIO> <ID> --save <FILE>
```

You can also plot another traffic on top for comparison:
```console
memphis-ta <SCENARIO> <ID> --compare <COMPARE_SCENARIO> <COMPARE_ID>
```

It is also possible to discard application warmup traffic by defining the initial plot time:
```console
memphis-ta <SCENARIO> <ID> --start <MS>
```
