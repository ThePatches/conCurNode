var express = require('express');

var app = express();

var theList = [{name: "Patrick Taylor", age: 31, occuptation: "Developer"},
		{name: "Chris McClintock", age: 31, occupation: "Feesh Store"},
		{name: "Tyler Lowry", age: 32, occupation: "Editor"}] 

app.get("/", function(req, res)
{
	res.send("<html><body>This is some text.</body></html>");
});

app.get("/showList", function(req, res)
{
	res.send(theList);
});

app.listen("1337");
console.log("Listening on 1337");
