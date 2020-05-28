# SCINET

![Build](https://img.shields.io/badge/build-passing-blue) ![Author](https://img.shields.io/badge/author-JoshGoA-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![PyPi](https://img.shields.io/badge/pypi-v0.5.0-red) ![Python](https://img.shields.io/badge/python->=3.8-red)

Network science abstract data types.

## Installation

1. Install [Python >= 3.8](https://www.python.org/downloads/)
2. Install [scinet]()
```sh
$ pip install scinet
```

## Usage

Import **scinet**
```py
import scinet as sn
```

Initialize network
```py
G = sn.network()
```

Manipulate data

* Add vertex
```py
G[vertex := "Python"] = dict(popularity=0.44)
```

* Add edge
```py
G[source_vertex := "Python"][target_vertex := "C"] = dict(interpreter="CPython")
```

* Range through vertex neighbors
```py
for neighbor in G[vertex := "Python"]: pass
```

* Check vertex adjacency
```py
if target_vertex := "C" in G[source_vertex := "Python"]: pass
```

* Clear network
```py
G.clear()
```

See [docs](docs/scinet.html) for further details.

## Contributors

* **JoshGoA** - *Main contributor* - [GitHub](https://github.com/JoshGoA)

### TODO

1. Multigraph
> https://stackoverflow.com/questions/10664856/make-a-dictionary-with-duplicate-keys-in-python
2. Undirected graph
> Add "directed" mappable property to edge data
3. Network visualization
> Create "matplotlib.pyplot" supported API
