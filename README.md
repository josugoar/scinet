# SCINET

![Build](https://img.shields.io/badge/build-passing-blue) ![Author](https://img.shields.io/badge/author-JoshGoA-green) ![License](https://img.shields.io/badge/license-MIT-red) ![PyPi](https://img.shields.io/badge/pypi-v0.3.0-yellow) ![Python](https://img.shields.io/badge/python->=3.8-orange)

Graph theory abstract data type.

**scinet.Graph** is designed upon the [graph (abstract data type)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) definition and functions as a bare bones skeletal graph data mapping, containing abstract vertices and edges.

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

* remove_vertex
```py
G.remove_vertex(vertex := "foo")
```

* add_edge
```py
G.add_edge(edge := "foobar", source_vertex="foo", target_vertex="bar")
```

* remove_edge
```py
G.remove_edge(edge := "foobar", source_vertex="foo", target_vertex="bar")
```

* adjacent
```py
(target_vertex := "bar") in G[(source_vertex := "foo")]
```

* neighbors
```py
G[(vertex := "foo")].keys()
```

See [docs](docs/scinet.html) for further details.

## Contributors

* **JoshGoA** - *Main contributor* - [GitHub](https://github.com/JoshGoA)

### TODO

1. Undirected graph
> Add "directed" mappable property to edge data
2. Network visualization
> Create "matplotlib.pyplot" supported API
