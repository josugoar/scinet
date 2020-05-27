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
from scinet.core import network
```

Initialize network
```py
G = network()
```

Manipulate data

* Add vertex
```py
G[vertex := "JoshGoA"]
```

* Add edge
```py
G[source_vertex := "JoshGoA"][target_vertex := "gvanrossum"]
```

* Set vertex and edge data
```py
G[vertex := "JoshGoA"] = dict(id=vertex)

for source_vertex, target_vertex in enumerate(range(5)):
    G[source_vertex][target_vertex] = dict(weight=source_vertex)
```

* Range through vertex neighbors
```py
for neighbor in G[vertex]
```

See [docs](docs/scinet.html) for further details.

## Contributors

* **JoshGoA** - *Main contributor* - [GitHub](https://github.com/JoshGoA)
