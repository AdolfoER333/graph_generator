from langchain_ollama.llms import OllamaLLM
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.language_models.base import BaseModel
from langchain_community.graphs import Neo4jGraph
from langchain_community.graphs.graph_document import GraphDocument
from src.utils.graph_utils import text_to_graphs
from src.db.connection import get_conn


class GraphGenerator:
    def __init__(self, model: BaseModel = None, conn: Neo4jGraph = None):
        self.llm_graph_transformer = LLMGraphTransformer(
            model if isinstance(model, BaseModel) else OllamaLLM(model='llama3')
        )
        self.conn = conn if isinstance(conn, Neo4jGraph) else get_conn()

    def make_graphs(self, text: str) -> GraphDocument:
        graphs = text_to_graphs([text], self.llm_graph_transformer, 1000)
        return graphs

    def upload_graphs(self, graphs: GraphDocument) -> None:
        self.conn.add_graph_documents([graphs])
