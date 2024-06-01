$(document).ready(function () {
    let amenities = {};

    $('input[type="checkbox"]').change(function () {
        const id = $(this).attr('data-id');
        const name = $(this).attr('data-name');

        if ($(this).is(':checked')) {
            amenities[id] = name;
        } else {
            delete amenities[id];
        }

        const amenityList = Object.values(amenities).join(', ');
        $('.Amenities h4').text(amenityList);
    });
});
