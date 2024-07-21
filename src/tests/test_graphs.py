import pytest
import os
from src.graph_generator.graph_generator import GraphGenerator
from langchain_community.graphs.graph_document import GraphDocument


@pytest.fixture
def graph_gen():
    graph_gen = GraphGenerator()
    return graph_gen


@pytest.fixture
def graph_doc(graph_gen):
    texts_dir = os.path.abspath(os.path.join(
        __file__,
        '..', '..', '..',
        'testing_texts'
    ))
    testing_texts = ''
    for text in os.listdir(texts_dir):
        with open(os.path.join(texts_dir, text), 'r', encoding='utf-8') as file:
            testing_texts += file.read().rstrip() + '\n'
    graph_doc = graph_gen.make_graphs(testing_texts)
    return graph_doc


def test_graph_generation(graph_doc):
    assert isinstance(graph_doc, GraphDocument)


def test_database_update(graph_gen, graph_doc):
    graph_gen.upload_graphs(graph_doc)
    assert len(graph_gen.conn.query('MATCH (node) RETURN node')) > 0
