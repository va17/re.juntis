var express = require('express');
var app = express();
var port = process.env.PORT || 8080;
var morgan = require('morgan');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var path = require('path');

var router = express.Router();
var appRoutes = require('./app/routes/api')(router);

app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(__dirname+'/public'));
app.use('/api',appRoutes);

mongoose.connect('mongodb://localhost:27017/rejuntis',function(err){
	if(err){
		console.log('Not connected to the database: '+err);
	}
	else{
		console.log('Successfully connected to MongoDB');
	}
});

app.get('*',function(req,res){
	res.sendFile(path.join(__dirname+'/public/app/views/index.html'));
});

/* app.get('/home',function(req,res){
	res.send('Hello from home');
}); */



app.listen(port,function(){
	console.log('Runnig the server on port '+port);
});