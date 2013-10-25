function get_blogs_by_category(category_id) {
	$.get('blog/ajax_get_blogs_by_category', {
		'category_id' : category_id
	}, function(ret) {
		alert(ret);
	});
}