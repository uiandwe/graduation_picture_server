

window.onload = function () {

	$(function () {
		$(".img").hover(function () {
			// alert("!");
		});
		var img_carousel = function(){
			$img_width = $(this).width();
			$(this).mousemove(function (e) {
				if (e.pageX >= $img_width / 2) {
					$(".carousel_right_button").addClass("active");
					$(".carousel_left_button").removeClass("active");
				} else {
					$(".carousel_left_button").addClass("active");
					$(".carousel_right_button").removeClass("active");
				}
			});
		}
		$(document).mouseover($("img.active"), function () {
			img_carousel();
		});

		$(document).hover($("img.active"), function () {
			img_carousel();
		});

		$(document).click($("img.active"), function () {
			var index = $("img").index($("img.active"));
			var total_img_len = $("img").length;
			if($(".carousel_right_button").hasClass("active")){

				$(document).find("img.active").removeClass("active");
				if((total_img_len-1) >= (index+1)){
					$("img:eq("+(index+1)+")").addClass("active");	
				}
				else{
					$("img:eq(0)").addClass("active");		
				}
				
			}
			else{
				$(document).find("img.active").removeClass("active");
				if(0 <= (index-1)){
					$("img:eq("+(index-1)+")").addClass("active");	
				}
				else{
					$("img:eq("+(total_img_len-1)+")").addClass("active");		
				}
			}
		});
	});
};