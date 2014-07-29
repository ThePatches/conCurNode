var express = require('express');
var bodyParser = require('body-parser');
var url = require('url');

var app = express();
app.use(bodyParser());

var theList = [{id: 1, name: "Patrick Taylor", age: 31, occuptation: "Developer"},
		{id: 2, name: "Chris McClintock", age: 31, occupation: "Feesh Store"},
		{id: 3, name: "Tyler Lowry", age: 32, occupation: "Editor"}]

var nId = 4;

app.get("/", function(req, res)
{
	res.send("<html><body>This is some text.</body></html>");
});

app.get("/showList", function(req, res)
{
	res.send(theList);
});

app.get("/add", function(req, res) {
	var queryData = url.parse(req.url, true).query;

	console.log(queryData);
 
	var inRecord = {};
	inRecord.id = nId++; 
	inRecord.name = queryData["name"];
	inRecord.age = parseInt(queryData["age"]);
	inRecord.occupation = queryData["job"];

	theList.push(inRecord);

	res.send(theList);
});

app.listen("1337");
console.log("Listening on 1337");
