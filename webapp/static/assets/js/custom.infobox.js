function drawInfobox(json, i){
    var title='';
    var release='';
    var location='';
    var company='';
    var distributor='';
    var director='';
    var writer='';
    var actors='';

    if( json.data[i].title )                { title=json.data[i].title }
    if( json.data[i].release )              { release=json.data[i].release }
    if( json.data[i].location )             { location=json.data[i].location }
    if( json.data[i].company )              { company=json.data[i].company }
    if( json.data[i].distributor )          { distributor=json.data[i].distributor }
    if( json.data[i].director )             { director=json.data[i].director }
    if( json.data[i].writer )               { writer=json.data[i].writer }
    if( json.data[i].actors )               { actors=json.data[i].actors }

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