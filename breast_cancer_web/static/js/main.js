$(document).ready(function () {
    console.log("script loaded");

    $(".details__summary").click(function () {
        var content = $(this).next();
        if (content.css('max-height') != '0px') {
            content.css('max-height', '0px');
        } else {
            setTimeout(function () {
                content.css('max-height', content.prop('scrollHeight') + 'px');
            }, 0);
            $('html, body').animate({
                scrollTop: $(this).offset().top
            }, 500);
        }
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() >= 50) {
            $('#go-top').fadeIn(200);
        } else {
            $('#go-top').fadeOut(200);
        }
    });
    $('#go-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
    });
});
