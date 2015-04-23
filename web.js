/**
 * @see http://www.senchalabs.org/connect/
 */
var connect = require('connect');
var app = connect()
	.use(connect.basicAuth('username', 'password'))
	.use(connect.static('www'))
	.listen(process.env.PORT || 8080)
