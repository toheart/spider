var page = require('webpage').create();
page.open('http://www.sample.com', function(){
	page.includeJs('https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js', function(){
		page.evaluate(function(){
			$('button').click();
			console.log('click');
		});
		phantom.exit();
	});
});
