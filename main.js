var list = [],
    colors = [ '#F44336', '#03A9F4', '#E91E63', '#9C27B0', '#3F51B5', '#2196F3', '#009688', '#FF5722', '#607D8B', '#4CAF50', '#FFC107' ];

function type( str ) {
    str = str.split( '' );
    var letter = str.shift();
    document.getElementById( 'text' ).innerHTML += letter;
    var time = Math.random() * 300 + 50;
    setTimeout( function() {
        if ( str.length ) {
            type( str.join( '' ) );
        } else {
            setTimeout( function() {
                document.getElementById( 'text' ).innerHTML = "";
                document.body.style.background = colors[ Math.floor( Math.random() * colors.length ) ];
                if ( list.length ) type( list.shift() );
                else getList();
            }, 1000 );
        }

    }, time );
}

function getList() {
    $.get( '/trends' ).done( function( resp ) {
        list = JSON.parse( resp );
        type( list.shift() );
    } );
};

getList();
