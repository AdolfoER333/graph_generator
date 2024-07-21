from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.graphs.graph_document import GraphDocument
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_texts(texts: list[str], chunk_size: int) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=min([chunk_size/2, 100])
    )
    chunks = splitter.create_documents(texts)
    return chunks


def merge_graph_documents(graph_docs: list[GraphDocument]) -> GraphDocument:
    nodes, relationships, sources_str = [], [], ''
    for doc in graph_docs:
        nodes.extend([
            node for node in doc.nodes
            if len(node.id) > 1
        ])
        relationships.extend(
            rel for rel in doc.relationships
            if len(rel.source.id) > 1
            and len(rel.target.id) > 1
        )
        sources_str += doc.source.page_content
    sources_doc = Document(page_content=sources_str)
    merged_graph_doc = GraphDocument(
        nodes=nodes, relationships=relationships, source=sources_doc
    )
    return merged_graph_doc


def text_to_graphs(texts: list[str], llm_transformer: LLMGraphTransformer, chunk_size: int) -> GraphDocument:
    documents = chunk_texts(texts, chunk_size)
    graph_documents = llm_transformer.convert_to_graph_documents(documents)
    graph_document = merge_graph_documents(graph_documents)
    return graph_document
