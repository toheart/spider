var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0';
page.open('http://movie.mtime.com/108737', function(status){
	if(status !== 'success'){
		console.log('Unable to access network');
	}else{
		var ua = page.evaluate(function(){
			return document.getElementById('ratingRegion').textContent;
		});
		console.log(ua);
	}
	phantom.exit();
});
