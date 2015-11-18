var list = [];

function type( str ) {
    str = str.split( '' );
    var letter = str.shift();
    document.getElementById( 'text' ).innerHTML += letter;
    var time = Math.random() * 200 + 100;
    setTimeout( function() {
        if ( str.length ) {
            type( str.join( '' ) );
        } else {
            setTimeout( function() {
                if ( list.length ) {
                    document.getElementById( 'text' ).innerHTML = "";
                    type( list.shift() );
                } else {
                    document.getElementById( 'text' ).innerHTML = "";
                    getList();
                }
            }, 1500 );
        }

    }, time );
}

function getList() {
    $.get( 'http://stats-rawdata-test.55labs.com/trends' ).done( function( resp ) {
        list = JSON.parse( resp );
        type( list.shift() );
    } );
};

getList();