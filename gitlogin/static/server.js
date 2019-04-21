var root = require('root');
var github = require('github-auth');
var express = require('express');
var path = require('path');
var http = require('http');

// var app = root();
var app = express();


var gh = github('2a900d9e9871c1b4c27f', '450c8bd04e582370a1de97206268c6aa3e07840b', {
  // users: ['wathika']
	organization: 'moringaschool',
  team: 'cohort-5',
	// autologin: true // This automatically redirects you to github to login
});


app.get('/login', gh.login);

// app.use(express.static(__dirname + '/View'));
//  all HTML files in view folder.
app.use(express.static(__dirname + '/'));
//Store all JS and CSS in Scripts folder.

app.all('*', gh.authenticate);
app.all('*', function(req, res, next) {
  // if (!req.github) res.sendFile('login.html');
	if (!req.github) return res.sendFile(__dirname + '/login.html');


  if (!req.github.authenticated) res.sendFile(path.join(__dirname+'/kickout.html'));
  next();
});

app.get('/main',function(req,res){
  res.sendFile(path.join(__dirname+'/main.html'));
});

app.get('/about',function(req,res){
  res.sendFile('/kickout.html');
});

// app.listen(3000);
//
// console.log("Running at Port 3000");

http.createServer(app).listen(process.env.port || 3000, function() {
    console.log('Express app started');
});
