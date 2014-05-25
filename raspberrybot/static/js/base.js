initKeyboardControls = function () {

    // map key code to command verb
    var command_map = {
        37: 'left',
        38: 'forward',
        39: 'right'
    };

    // execute command depending on the key pressed
    $(document).keydown(function(event){
        $.get("/control/" + command_map[event.keyCode] + "/");
    });

    // send stop command on keyup
    $(document).keyup(function(event){
        $.get("/control/stop/");
    });
}

$(document).ready( function () {
    initKeyboardControls();
});
