
import * as rpc from 'vscode-jsonrpc/node';

const connection = rpc.createMessageConnection(
    new rpc.StreamMessageReader(process.stdin),
    new rpc.StreamMessageWriter(process.stdout)
);

connection.onRequest('initialize', (params) => {
    return {
        capabilities: {
            tools: [
                {
                    name: 'helloWorld',
                    description: 'A simple hello world tool.',
                    parameters: {
                        type: 'object',
                        properties: {
                            name: {
                                type: 'string',
                                description: 'The name to say hello to.'
                            }
                        },
                        required: ['name']
                    }
                }
            ],
            prompts: [
                {
                    name: 'helloPrompt',
                    description: 'A simple hello world prompt.'
                }
            ],
            resources: [
                {
                    name: 'helloResource',
                    description: 'A simple hello world resource.'
                }
            ]
        }
    };
});

connection.onRequest('runTool', (params) => {
    if (params.name === 'helloWorld') {
        return { 
            content: `Hello, ${params.parameters.name}!`
        };
    }
});

connection.listen();
