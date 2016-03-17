/**
 * Created by Yiming on 3/15/2016.
 */
$(document).ready(function ($) {
function formatRepo (item) {
      return item;
    }

    function formatRepoSelection (item) {
      return item
    }
    $(".select2-select").select2({
        ajax: {
            url: "/getSuggestion",
            dataType: 'json',
            delay: 300,
            data: function (params) {
                return {
                    q: params.term, // search term
                    f: $(this).attr("name")
                };
            },
            processResults: function (data) {
                // parse the results into the format expected by Select2
                // since we are using custom formatting functions we do not need to
                // alter the remote JSON data, except to indicate that infinite
                // scrolling can be used
                return {
                    results: data.items,
                };
            },
            cache: true
        },
        escapeMarkup: function (markup) {
            return markup;
        }, // let our custom formatter work
        minimumInputLength: 2,
        templateResult: formatRepo, // omitted for brevity, see the source of this page
        templateSelection: formatRepoSelection // omitted for brevity, see the source of this page
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

