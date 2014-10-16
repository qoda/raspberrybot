initKeyboardControls = function () {

    // map key code to command verb
    var current_command = 'stop';
    var command_map = {
        37: 'left',
        38: 'forward',
        39: 'right',
        68: 'detect'
    };

    // execute command depending on the key pressed
    $(document).keydown(function(event){
        var event_command = command_map[event.keyCode];
        if ((event_command != undefined) && (current_command != event_command)) {
            current_command = event_command;
            $.get("/control/" + event_command + "/");
        }
    });

    // send stop command on keyup
    $(document).keyup(function(event){
        if (current_command != 'stop') {
            current_command = 'stop';
            $.get("/control/stop/");
        }
    });

    // log the command to console
    console.log(current_command);
}

initButtonControls = function () {
    var current_command = 'stop';

    // execute command depending on the button pressed
    $(".btn-command").on({'touchstart mousedown': function(event){
        var event_command = $(this).data('command');
        if (current_command != event_command) {
            current_command = event_command;
            $.get("/control/" + event_command + "/");

        }
    }});

    // send stop command on keyup
    $(".btn-command").on({'touchend mouseup': function(event){
        if (current_command != 'stop') {
            current_command = 'stop';
            $.get("/control/stop/");
        }
    }});

    // log the command to console
    console.log(current_command);
}

$(document).ready( function () {
    initKeyboardControls();
    initButtonControls();
});
