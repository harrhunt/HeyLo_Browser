$(document).ready(function () {
    $(".grid-interests").on("click", function (eve) {
        let target = $(eve.target);
        if (target.is("a[href*=\"#\"]")) {
            let interestID = target.attr("href");
            $(interestID).stop().css("background-color", "#ffff50").animate({backgroundColor: "#ffffff"}, 2500);
        }
    })
})