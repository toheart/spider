var page = require('webpage').create();
page.open('http://www.cnblogs.com/qiyeboy',function(status) {
	console.log("status :" + status);
	if(status === "success"){
		page.render('qiye.png');
	}
	phantom.exit();
});
