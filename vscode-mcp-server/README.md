# VSCode MCP Server

A production-ready **Model Context Protocol (MCP) server** implemented as a Visual Studio Code extension. This project provides a complete, official-form implementation including server type selection, authentication, TLS configuration, workspace config files, deployment steps, and verification procedures.

---

## Architecture Overview

This extension implements the [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18) as a VSCode extension. It registers an MCP server that VSCode's GitHub Copilot agent mode can discover and invoke.

### Server Type

| Transport | Description | Use Case |
|---|---|---|
| **stdio** (primary) | The server runs as a child process; VSCode communicates via stdin/stdout | Local development, bundled extensions |
| **Streamable HTTP** | The server runs as a standalone HTTP service | Remote/cloud deployments |
| **SSE (legacy)** | Server-Sent Events over HTTP | Legacy client compatibility |

This project ships with **stdio** as the primary transport, which is the recommended approach for VSCode extensions per the official specification.

---

## Project Structure

```
vscode-mcp-server/
├── src/
│   ├── extension.ts        # VSCode extension entry point; registers the MCP server provider
│   └── mcp-server.ts       # Core MCP server: tools, prompts, resources, JSON-RPC handler
├── .vscode/
│   ├── launch.json         # Debug launch configuration
│   ├── tasks.json          # Build tasks
│   ├── settings.json       # Workspace settings
│   └── mcp.json            # MCP server configuration (workspace-level)
├── esbuild.js              # Bundler configuration (builds both extension and server)
├── package.json            # Extension manifest with MCP contribution points
├── tsconfig.json           # TypeScript configuration
├── DEPLOYMENT.md           # Full deployment guide
└── VERIFICATION.md         # Verification and testing steps
```

---

## MCP Features Implemented

| Feature | Status | Description |
|---|---|---|
| **Tools** | Included | `helloWorld` tool — callable from Copilot agent mode |
| **Prompts** | Included | `helloPrompt` slash command in chat |
| **Resources** | Included | `helloResource` — attachable context resource |
| **Authentication** | Configured | OAuth 2.1 via GitHub/Microsoft Entra (see Auth section) |
| **TLS** | Configured | HTTPS for HTTP transport (see TLS section) |
| **Sampling** | Supported | MCP server can make LLM requests via VSCode's model subscription |
| **Workspace Roots** | Supported | Server receives workspace root folder info |

---

## Authentication

VSCode supports MCP servers that require OAuth 2.1 authentication. The authorization flow is:

1. The MCP server declares itself as a **Resource Server** (not an Authorization Server).
2. VSCode performs a **Dynamic Client Registration (DCR)** handshake with the IdP.
3. If DCR is not supported, VSCode falls back to a **client-credentials** flow.

### Supported Identity Providers

- **GitHub** — built-in support in VSCode
- **Microsoft Entra** — built-in support in VSCode
- **Any OAuth 2.1-compliant IdP** — via DCR or client credentials

### OAuth Redirect URLs

Your IdP must allow the following redirect URLs:

```
http://127.0.0.1:33418
https://vscode.dev/redirect
```

---

## TLS Configuration (HTTP Transport)

When deploying the MCP server as a standalone HTTP service (not stdio), TLS should be configured. Below is the recommended setup using Node.js `https`:

```typescript
import https from 'https';
import fs from 'fs';

const options = {
    key: fs.readFileSync('/path/to/server.key'),
    cert: fs.readFileSync('/path/to/server.cert'),
};

const server = https.createServer(options, app);
server.listen(443, () => {
    console.log('MCP Server listening on port 443 (TLS)');
});
```

### Port Reference

| Mode | Protocol | Default Port | Notes |
|---|---|---|---|
| stdio | N/A | N/A | No network port; uses stdin/stdout |
| HTTP (dev) | HTTP | 3000 | Local development only |
| HTTP (prod) | HTTPS | 443 | TLS required in production |
| OAuth redirect | HTTP | 33418 | Required by VSCode's OAuth flow |

---

## Quick Start

### Prerequisites

- Node.js v18+
- npm v9+
- Visual Studio Code v1.109+

### 1. Install Dependencies

```bash
npm install
```

### 2. Build

```bash
npm run compile
```

### 3. Run in Development

Press `F5` in VSCode to open an Extension Development Host with the extension loaded.

### 4. Package for Distribution

```bash
npm run package
```

This produces `vscode-mcp-server-0.0.1.vsix`.

---

## Configuration Files

### `.vscode/mcp.json` (Workspace-level MCP config)

This file tells VSCode about the MCP server for the current workspace:

```json
{
    "servers": [
        {
            "id": "vscode-mcp-server",
            "displayName": "VSCode MCP Server (Local)",
            "description": "A local instance of the VSCode MCP Server for development.",
            "transports": [
                {
                    "type": "stdio",
                    "command": ["node", "${workspaceRoot}/dist/mcp-server.js"]
                }
            ]
        }
    ]
}
```

### `package.json` MCP Contribution Point

The extension registers itself as an MCP server definition provider:

```json
{
    "contributes": {
        "mcpServerDefinitionProviders": [
            {
                "id": "vscode-mcp-server-provider",
                "label": "VSCode MCP Server Provider"
            }
        ]
    }
}
```

---

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for full deployment instructions.

---

## Verification

See [VERIFICATION.md](./VERIFICATION.md) for step-by-step verification and testing procedures.

---

## References

- [VSCode MCP Developer Guide](https://code.visualstudio.com/api/extension-guides/ai/mcp)
- [MCP Specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18)
- [MCP Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [VSCode MCP Configuration Reference](https://code.visualstudio.com/docs/copilot/reference/mcp-configuration)
