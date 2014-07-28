var express = require('express');

var app = express();

app.get("/", function(req, res)
{
	res.send("<html><body>This is some text.</body></html>");
});

app.get("/showList", function(req, res)
{
	res.send({name: "Patrick Taylor", occupation: "Developer"});
});

app.listen("1337");
console.log("Listening on 1337");
