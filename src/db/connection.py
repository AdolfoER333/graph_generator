import os
from langchain_community.graphs import Neo4jGraph


os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "password"


def get_conn(db_name: str = 'graph-db'):
    conn = Neo4jGraph(database=db_name)
    return conn
