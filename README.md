# scinet

<p align="center">
  <img src="assets/scinet.png" alt="scinet" width="640" height="320" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-blue" alt="build" />
  <img src="https://img.shields.io/badge/author-josugoar-green" alt="author" />
  <img src="https://img.shields.io/badge/license-MIT-red" alt="license" />
  <img src="https://img.shields.io/badge/pypi-v0.4.9-yellow" alt="pypi" />
  <img src="https://img.shields.io/badge/python->=3.8-orange" alt="python" />
</p>

<h1></h1>

> Network science abstract data types

**scinet.Graph** is designed upon the [graph (abstract data type)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) definition and functions as a bare bones skeletal graph data mapping, containing abstract vertices and edges.

Includes DiGraph and MultiGraph support, with HyperGraph capabilities.

## Installation

1. Install [Python >= 3.8](https://www.python.org/downloads/)
2. Install [scinet]()
```sh
$ pip install scinet-josugoar
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

* neighbours
```py
set(G[(vertex := "foo")])
>>> { "neighbour_1", "neighbour_2", ... }
```

See [docs](docs/scinet.html) for further details.
