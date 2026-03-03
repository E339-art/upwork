# VSCode MCP Server Verification Guide

This guide provides steps to verify that the VSCode MCP Server is working correctly.

## Running the Extension in Development

1.  Open the `vscode-mcp-server` project in Visual Studio Code.
2.  Press `F5` to open a new Extension Development Host window.

## Verifying the MCP Server

1.  In the Extension Development Host window, open the Chat view (Ctrl+Shift+I).
2.  In the chat input, type `@workspace` to activate the workspace agent.
3.  Click the "tools" icon (a wrench) in the chat input to see the list of available tools.
4.  You should see "VSCode MCP Server" in the list of tool providers.

## Testing the `helloWorld` Tool

1.  In the chat view with the `@workspace` agent, type the following prompt:

    ```
    @workspace /helloWorld name: "World"
    ```

2.  You should see the response: `Hello, World!`

## Testing the `helloPrompt` Slash Command

1.  In the chat view, type `/` to see the list of available slash commands.
2.  You should see `/helloPrompt` in the list.
3.  Select `/helloPrompt` and press Enter.

## Testing the `helloResource`

1. In the chat view, type `#` to see the list of available resources.
2. You should see `helloResource` in the list.
