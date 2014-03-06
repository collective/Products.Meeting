jq('a[href*=#]').click(function() {
	if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
		var $target = jq(this.hash);
		$target = $target.length && $target || jq('[id=' + this.hash.slice(1) + ']');
		if ($target.length) {
			var targetOffset = $target.offset().top;
			jq('html,body').animate({scrollTop: targetOffset}, 1000);
			return false;
		}
	}
});
