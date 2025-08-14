from mcp_use import MCPClient

# Configure your MCP servers
config = {
    "mcpServers": {
        "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"],
            "env": {"DISPLAY": ":1"}
        }
    }
}

client = MCPClient.from_dict(config)