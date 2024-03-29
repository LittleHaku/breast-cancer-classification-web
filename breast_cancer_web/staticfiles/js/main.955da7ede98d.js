$(document).ready(function () {
    console.log("script loaded");

    // Get all the images
    var imgs = document.querySelectorAll(".popup-img img");

    // Loop through the images
    imgs.forEach(function (img) {
        // When the user clicks on an image, add the active class
        img.onclick = function () {
            this.parentElement.classList.add("popup-img-active");
        }
    });

    window.onclick = function (event) {
        if (!event.target.matches('.popup-img img')) {
            imgs.forEach(function (img) {
                img.parentElement.classList.remove("popup-img-active");
            });
        }
    }

    // smooth dropdown
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

    // return to top
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

    // disappear header on scroll
    var scrollableContent = document.querySelector('.scrollable-content');

    scrollableContent.addEventListener('scroll', function () {
        var header = document.querySelector('header');
        var sectionOne = document.querySelector('.one');
        var sectionOneHeight = sectionOne.offsetHeight / 2;

        console.log("Scroll position: " + scrollableContent.scrollTop);
        console.log("Section one height: " + sectionOneHeight);

        if (scrollableContent.scrollTop > sectionOneHeight) {
            console.log("Hiding header");
            header.classList.add('hide-header');
        } else {
            console.log("Showing header");
            header.classList.remove('hide-header');
        }
    });


    // indicate section
    window.onload = function () {
        menuItems[0].classList.add('active');
    };

    var scrollableContent = document.querySelector('.scrollable-content');
    var sections = document.querySelectorAll('section');
    var menuItems = document.querySelectorAll('#lateral-menu div');
    var header = document.querySelector('header');
    var headerHeight = header.offsetHeight;


    menuItems.forEach((menuItem, index) => {
        menuItem.addEventListener('click', function () {
            sections[index].scrollIntoView({ behavior: 'smooth' });
        });
    });

    scrollableContent.addEventListener('scroll', function () {
        sections.forEach((section, index) => {
            var sectionTop = section.offsetTop - headerHeight;
            var sectionBottom = sectionTop + section.offsetHeight;

            if (scrollableContent.scrollTop >= sectionTop && scrollableContent.scrollTop < sectionBottom) {
                menuItems.forEach(item => item.classList.remove('active'));
                menuItems[index].classList.add('active');

                var bgColor = window.getComputedStyle(section).backgroundColor;


                var match = bgColor.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
                var red = parseInt(match[1]);
                var green = parseInt(match[2]);
                var blue = parseInt(match[3]);


                var brightness = Math.round(((red * 299) + (green * 587) + (blue * 114)) / 1000);


                if (brightness < 128) {
                    menuItems.forEach(item => item.style.color = 'white');
                } else {
                    menuItems.forEach(item => item.style.color = 'black');
                }
            }
        });
    });






});
