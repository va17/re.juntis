var User = require('../models/user');

module.exports = function(router){
	//http://localhost:8080/api/users
	router.post('/users',function(req,res){
		//res.send('testing users route');
		var user = new User();
		user.username  = req.body.username;
		user.password  = req.body.password;
		user.email  = req.body.email;
		console.log(req);
		if(req.body.username == null || req.body.username == '' || req.body.password == '' || req.body.password == null || req.body.email == '' || req.body.email == null){
			
			console.log(req.body);
			res.json({sucess:false,message:'Ensure username, email and password were provided'});
		}
		else {
			user.save(function(err){
				if(err){
					res.json({sucess:false,message:'username or password already exists!'});
				}
				else {
					res.json({sucess:true, message:'user created!'});
				}
			}); 
		}
	});
	return router;
}