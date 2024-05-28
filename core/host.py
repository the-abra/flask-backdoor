from flask import Flask, render_template, request, redirect, url_for
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from causal_graph import create_causal_graph, check_backdoor_criterion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    nodes = request.form.get('nodes').split(',')
    edges = [tuple(edge.split('->')) for edge in request.form.get('edges').split(',')]
    treatment = request.form.get('treatment')
    outcome = request.form.get('outcome')

    G = create_causal_graph(nodes, edges)
    is_backdoor = check_backdoor_criterion(G, treatment, outcome)

    img = io.BytesIO()
    nx.draw(G, with_labels=True)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('graph.html', plot_url=plot_url, is_backdoor=is_backdoor)

if __name__ == '__main__':
    app.run(debug=True, port=467)
