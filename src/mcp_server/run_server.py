"""Wrapper script to run the Borsdata MCP server with API key."""
import os
import sys

# Set the API key directly here
os.environ["BORSDATA_API_KEY"] = "0fe6f56b667f4323b93c120deca6dc48"

# Add src to path
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Run the server
from mcp_server.server import main
main()
