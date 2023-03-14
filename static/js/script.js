$(document).ready(function() {
    setTimeout(function(){
        if ($('#message-alert').length > 0) {
            $('#message-alert').remove();
        }
    }, 2000);
});
