const mbHelper = require('./mountebank-helper');
const settings = require('./settings');

function addService() {
    const response = { 
        '0': { USD: "68.4487" },
        '1': { EUR: "72.6226" },
        '2': { JPY: "51.6594" },
        '3': { GPB: "82.3438" },
        '4': { KZT: "14.8167" }
    }

    const stubs = [
        {
            predicates: [ {
                and: [
                    { equals: { method: "GET" } },
                    { startsWith: { "path": "/exchange-rate/" } }                      
                    
                ]                
            }],
            responses: [
                {
                    is: {
                        statusCode: 200,
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(response)
                        // body: "${id}"
                    },
                    _behaviors: {
                        copy: [{
                            "from": "path",
                            "into": "${id}",
                            "using": { "method": "regex", "selector": "\\d+$" }
                        }],
                        // "decorate": "(request, response) => {     return {headers: {'Content-Type': 'application/json'},body: JSON.stringify({ response })};)"
                        "fromDataSource": {
                            "csv": {
                              "path": "data/currencies.csv",
                              "keyColumn": "id"
                            }
                        }
                    }
                }
            ]
        }
    ];

    
    const imposter = {
        port: settings.currency_api_port,
        protocol: 'http',
        stubs: stubs
    };

    return mbHelper.postImposter(imposter);
}

module.exports = { addService };