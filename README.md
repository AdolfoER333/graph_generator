# Making Graphs with LLMs

Simple application that uses the LLMGraphGenerator class from Langchain to make graphs
from a text. Furthermore, uploads the generated graphs to a local Neo4j database, also
using the Langchain interface to do so.

The LLM used for testing was the Llama-3 8B from the Ollama platform, and this project
only implements the workflow of making graphs from text and uploading to a database,
with disregard to special treatments on the input text or ID/relationships specified
for the LLM graph generation.
