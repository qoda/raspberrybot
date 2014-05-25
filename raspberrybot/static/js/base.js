initKeyboardControls = function () {

    // map key code to command verb
    var current_command = null;
    var command_map = {
        37: 'left',
        38: 'forward',
        39: 'right'
    };

    // execute command depending on the key pressed
    $(document).keydown(function(event){
        var event_command = command_map[event.keyCode];
        if ((event_command != undefined) && (current_command != event_command)) {
            $.get("/control/" + event_command + "/");
            current_command = event_command;
        }

    });

    // send stop command on keyup
    $(document).keyup(function(event){
        if (current_command != 'stop') {
            $.get("/control/stop/");
            current_command = 'stop';
        }
    });

    // log the command to console
    console.log(current_command);
}

$(document).ready( function () {
    initKeyboardControls();
});
