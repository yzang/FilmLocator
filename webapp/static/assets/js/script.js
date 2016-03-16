/**
 * Created by Yiming on 3/15/2016.
 */
$(document).ready(function ($) {


    $(".select2-select").select2({
        ajax: {
            url: "https://api.github.com/search/repositories",
            dataType: 'json',
            delay: 250,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                // parse the results into the format expected by Select2
                // since we are using custom formatting functions we do not need to
                // alter the remote JSON data, except to indicate that infinite
                // scrolling can be used
                params.page = params.page || 1;

                return {
                    results: data.items,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        escapeMarkup: function (markup) {
            return markup;
        }, // let our custom formatter work
        minimumInputLength: 1
    });

//  No UI Slider ------------------------------------------

    if ($('.ui-slider').length > 0) {
        $('.ui-slider').each(function () {
            var step;
            if ($(this).attr('data-step')) {
                step = parseInt($(this).attr('data-step'));
            }
            else {
                step = 10;
            }
            var valueMin = parseInt($(this).attr('data-value-min'));
            var valueMax = parseInt($(this).attr('data-value-max'));
            $(this).noUiSlider({
                start: [valueMin, valueMax],
                connect: true,
                range: {
                    'min': valueMin,
                    'max': valueMax
                },
                step: step
            });
            $(this).Link('lower').to($(this).children('.values').children('.value-min'), null, wNumb({decimals: 0}));
            $(this).Link('upper').to($(this).children('.values').children('.value-max'), null, wNumb({decimals: 0}));
        });
    }

    // Bootstrap Animated Tabs --------------------------------
    var activeTab;
    var transitionParent;

    $('body').find('a[data-toggle="collapse"]').click(function () {
        var where = $(this).attr('href');
        activeTab = $(this).attr('data-tab');
        $(activeTab).addClass('active');
        $(where + ' a[href="' + activeTab + '"]').tab('show');
        transitionParent = $(this).attr('data-transition-parent');
    });



});

