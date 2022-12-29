const mb = require('mountebank');
const settings = require('./settings');
const currencyService = require('./currency-service.js');

const mbServerInstance = mb.create({
        port: settings.port,
        pidfile: '../mb.pid',
        logfile: '../mb.log',
        protofile: '../protofile.json',
        ipWhitelist: ['*'],
        allowInjection: true
    });

mbServerInstance.then(() => {
    currencyService.addService();
})