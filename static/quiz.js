$(document).ready(function () {
    $(".draggable").draggable(
        {
            cursor: "move",
            revert: "invalid"
        }
    );
    $("#court_quiz1").droppable({
        hoverClass: "hoverClass", // add this class when an item is hovered over the area
        drop: function (event, ui) {
        }
    });

    $("#submit").click(function () {
        var position_1 = $("#draggable-1").position();
        var position_2 = $("#draggable-2").position();
        var position_3 = $("#draggable-3").position();
        var position_4 = $("#draggable-4").position();
        var position_5 = $("#draggable-5").position();
        var data = {
            position_1: {
                left: position_1.left,
                top: position_1.top
            },
            position_2: {
                left: position_2.left,
                top: position_2.top
            },
            position_3: {
                left: position_3.left,
                top: position_3.top
            },
            position_4: {
                left: position_4.left,
                top: position_4.top
            },
            position_5: {
                left: position_5.left,
                top: position_5.top
            }
        };
        console.log("Sending Position Data:", data);  // Output to console

        // Send data to server
        $.ajax({
            url: url_for_ajax,  // Flask route
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                window.location.href = response.redirect;
            },
            error: function () {
                alert('Error saving position.');
            }
        });
    });

});
