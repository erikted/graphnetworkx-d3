import flask

from app import app

import json
import numpy as np
import networkx as nx
from networkx.readwrite import json_graph

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("index.html")


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    # x = 10 * np.random.rand(ndata) - 5
    # y = 0.5 * x + 0.5 * np.random.randn(ndata)
    # A = 10. ** np.random.rand(ndata)
    # c = np.random.rand(ndata)
    # return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
    #     "color": c[i]}
    #     for i in range(ndata)])

    G = nx.barbell_graph(6, 3)
    # this d3 example uses the name attribute for the mouse-hover value,
    # so add a name to each node
    for n in G:
        G.node[n]['name'] = n
        # write json formatted data
    return json.dumps(json_graph.node_link_data(G))  # node-link format to serialize
