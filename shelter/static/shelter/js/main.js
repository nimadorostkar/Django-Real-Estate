/*

    Template:  Sheltek Real Estate HTML5 Template
    Author: http://devitems.com/
    Version: 1
    Design and Developed by: http://devitems.com/
    NOTE: If you have any note put here. 

*/
/*================================================
[  Table of contents  ]
================================================
	1. jQuery MeanMenu
	2. wow js active
	3. scrollUp jquery active
    4. Nivo Slider 
    5. Price Slider
	6. slick carousel 
    6. tooltip
    7. Service Carousel
    8. Agents Carousel
    9. Testimonial Carousel
    10. Blog Carousel
    11. Brand Carousel
    12. Blog Carousel
    13. counter
    14. Background Toutube Video 
    15. STICKY sticky-header
 
======================================
[ End table content ]
======================================*/


(function($) {
    "use strict";

    /*-------------------------------------------
        1. jQuery MeanMenu
    --------------------------------------------- */
    jQuery('nav#dropdown').meanmenu();

    /*-------------------------------------------
        2. wow js active
    --------------------------------------------- */
    new WOW().init();

    /*-------------------------------------------
        3. scrollUp jquery active
    --------------------------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });

    /*-------------------------------------------
        4. Nivo Slider
    --------------------------------------------- */
    $('#ensign-nivoslider-3').nivoSlider({
        // effect: 'fade',
        effect: 'random',
        slices: 15,
        boxCols: 8,
        boxRows: 4,
        animSpeed: 500,
        pauseTime: 5000,
        prevText: 'p<br/>r<br/>e<br/>v', 
        nextText: 'n<br/>e<br/>x<br/>t',
        startSlide: 0,
        directionNav: true,
        controlNav: true,
        controlNavThumbs: false,
        pauseOnHover: true,
        manualAdvance: false
    });

    /* ********************************************
        5. Price Slider
    ******************************************** */
    $( "#slider-range" ).slider({
        range: true,
        min: 1000,
        max: 10000,
        values: [ 2000, 6000 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
    " - $" + $( "#slider-range" ).slider( "values", 1 ) ); 

    /*************************
        6. tooltip
    *************************/
    $('[data-toggle="tooltip"]').tooltip();

    /*************************
        7. Service Carousel
    *************************/ 
    $('.service-carousel').slick({
        arrows: false,
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 3,
        responsive: [
            { breakpoint: 991, settings: { slidesToShow: 3, slidesToScroll: 2 } }, // Tablet
            { breakpoint: 767, settings: { slidesToShow: 2, slidesToScroll: 1 } }, // Large Mobile
            { breakpoint: 479, settings: { slidesToShow: 1, slidesToScroll: 1 } }  // Small Mobile
        ]
    });
    
    /*************************
        8. Agents Carousel
    *************************/ 
    $('.agents-carousel').slick({
        arrows: false,
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 3,
        responsive: [
            { breakpoint: 991, settings: { slidesToShow: 3, slidesToScroll: 2 } }, // Tablet
            { breakpoint: 767, settings: { slidesToShow: 1, slidesToScroll: 1 } }, // Large Mobile
            { breakpoint: 479, settings: { slidesToShow: 1, slidesToScroll: 1 } }  // Small Mobile
        ]
    });

    /*************************
        9. Testimonial Carousel
    *************************/ 
    $('.testimonial-carousel').slick({
        arrows: false,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /*************************
        10. Blog Carousel
    *************************/ 
    $('.blog-carousel').slick({
        arrows: false,
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 2,
        responsive: [
            { breakpoint: 991, settings: { slidesToShow: 2, slidesToScroll: 1 } }, // Tablet
            { breakpoint: 767, settings: { slidesToShow: 1, slidesToScroll: 1 } }, // Large Mobile
            { breakpoint: 479, settings: { slidesToShow: 1, slidesToScroll: 1 } }  // Small Mobile
        ]
    });

    /*************************
        11. Brand Carousel
    *************************/ 
    $('.brand-carousel').slick({
        arrows: false,
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 4,
        responsive: [
            { breakpoint: 1169, settings: { slidesToShow: 4, slidesToScroll: 3 } }, // Medium Device
            { breakpoint: 991, settings: { slidesToShow: 3, slidesToScroll: 2 } }, // Tablet
            { breakpoint: 767, settings: { slidesToShow: 2, slidesToScroll: 1 } }, // Large Mobile
            { breakpoint: 479, settings: { slidesToShow: 1, slidesToScroll: 1 } }  // Small Mobile
        ]
    });

    /*************************
        12. Blog Carousel
    *************************/ 
    $('.pro-details-carousel').slick({
        arrows: false,
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 3,
        responsive: [
            { breakpoint: 991, settings: { slidesToShow: 4, slidesToScroll: 3 } }, // Tablet
            { breakpoint: 767, settings: { slidesToShow: 3, slidesToScroll: 2 } }, // Large Mobile
            { breakpoint: 479, settings: { slidesToShow: 2, slidesToScroll: 2 } }  // Small Mobile
        ]
    });

    /*************************
        13. counter
    *************************/ 
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    
    /* ********************************************
        14. Background Toutube Video 
    ******************************************** */
    $(".youtube-bg").YTPlayer({
        videoURL:"Sz_1tkcU0Co",
        containment:'.youtube-bg',
        mute:true,
        loop:true,
    });









})(jQuery);

/* ********************************************
    15. STICKY sticky-header
******************************************** */
    var hth = $('.header-top-bar').height();
    $(window).on('scroll', function() {
        if ($(this).scrollTop() > hth){  
            $('#sticky-header').addClass("sticky");
        }
        else{
            $('#sticky-header').removeClass("sticky");
        }
    });
/* ********************************************************* */