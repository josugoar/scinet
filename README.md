# scinet

![Build](https://img.shields.io/badge/build-passing-blue) ![Author](https://img.shields.io/badge/author-JoshGoA-green) ![License](https://img.shields.io/badge/license-MIT-red) ![PyPi](https://img.shields.io/badge/pypi-v0.4.9-yellow) ![Python](https://img.shields.io/badge/python->=3.8-orange)

Graph theory abstract data type.

**scinet.Graph** is designed upon the [graph (abstract data type)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) definition and functions as a bare bones skeletal graph data mapping, containing abstract vertices and edges.

Includes DiGraph and MultiGraph support, with HyperGraph capabilities.

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

Create graph
```py
G = sn.Graph()
```

Manipulate data

* add_vertex
```py
G.add_vertex(vertex := "foo")
```

* add_edge

Edges must be assigned using hashable keys so that no name conflicts exist between source_vertex and target_vertex edges
```py
key = G.add_edge(source_vertex := "foo", target_vertex := "bar"[, edge := "foobar"])
```

* remove_vertex
```py
G.remove_vertex(vertex := "foo")
```

* remove_edge
```py
G.remove_edge(source_vertex := "foo", target_vertex := "bar"[, edge := "foobar"])")
```

* adjacent
```py
(target_vertex := "bar") in G[(source_vertex := "foo")]
>>> True
```

* neighbors
```py
set(G[(vertex := "foo")])
>>> { "neighbor_1", "neighbor_2", ... }
```

See [docs](docs/scinet.html) for further details.

## Contributors

* **JoshGoA** - *Main contributor* - [GitHub](https://github.com/JoshGoA)

### TODO

1. Graph visualization
2. Create "matplotlib.pyplot" supported API
