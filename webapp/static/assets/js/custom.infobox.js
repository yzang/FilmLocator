function drawInfobox(json, i){
    var title='';
    var release='';
    var location='';
    var company='';
    var distributor='';
    var director='';
    var writer='';
    var actors='';

    if( json[i].title )                { title=json[i].title }
    if( json[i].release )              { release=json[i].release }
    if( json[i].location )             { location=json[i].location }
    if( json[i].company )              { company=json[i].company }
    if( json[i].distributor )          { distributor=json[i].distributor }
    if( json[i].director )             { director=json[i].director }
    if( json[i].writer )               { writer=json[i].writer }
    if( json[i].actors )               { actors=json[i].actors }

    var ibContent =
    '<div class="infobox">' +
        '<div class="left">' +
            '<article class="animate move_from_top_short">' +
                '<dl>' +
                    '<dt>Title</dt>' +
                    '<dd>'+title+'</dd>' +
                    '<dt>Release Year</dt>' +
                    '<dd>'+release+'</dd>' +
                    '<dt>Location</dt>' +
                    '<dd>'+location+'</dd>' +
                    '<dt>Production Company</dt>' +
                    '<dd>'+company+'</dd>' +
                '</dl>' +
            '</article>' +

        '</div>' +
        '<div class="right">' +
            '<article class="animate move_from_top_short">' +
                '<dl>' +
                    '<dt>Distributor</dt>' +
                    '<dd>'+distributor+'</dd>' +
                    '<dt>Director</dt>' +
                    '<dd>'+director+'</dd>' +
                    '<dt>Writer</dt>' +
                    '<dd>'+writer+'</dd>' +
                    '<dt>Actors</dt>' +
                    '<dd>'+actors+'</dd>' +
                '</dl>' +
            '</article>' +
        '</div>' +
    '</div>';

    return ibContent;
}