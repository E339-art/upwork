# VSCode MCP Server Deployment Guide

This guide provides instructions on how to deploy the VSCode MCP Server. It covers building the extension from source, installing it in Visual Studio Code, and configuring it for different environments.

## Building from Source

To build the extension from source, you will need to have Node.js and npm installed. Follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/E339-art/upwork.git
    cd upwork/vscode-mcp-server
    ```

2.  **Install dependencies:**

    ```bash
    npm install
    ```

3.  **Build the extension:**

    ```bash
    npm run package
    ```

    This will create a `vscode-mcp-server-0.0.1.vsix` file in the root of the project. This is the packaged extension file that you can install in VSCode.

## Installing the Extension

To install the extension in Visual Studio Code, follow these steps:

1.  Open Visual Studio Code.
2.  Go to the **Extensions** view (Ctrl+Shift+X).
3.  Click on the **...** menu in the top-right corner of the Extensions view.
4.  Select **Install from VSIX...**.
5.  Navigate to the `vscode-mcp-server-0.0.1.vsix` file and select it.

## Configuration

The MCP server can be configured for different environments. Here are the options:

### Local Development

For local development, you can use the `.vscode/mcp.json` file to configure the server. This file is already set up to run the server from the local build output.

### Production

For a production environment, you would typically package the server with the extension and not rely on a local file path. The `extension.ts` file is already configured to do this.

### Authentication and TLS

This example does not include authentication or TLS, but they can be added to the server. For authentication, you would need to implement an OAuth 2.0 flow. For TLS, you would need to configure the server to use HTTPS.
