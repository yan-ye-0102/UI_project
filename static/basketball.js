$(document).ready(function () {
    // Define descriptions for each player
    var descriptions = {
        '1': 'When the leftmost offensive player has the ball, the left wing defender should step out to apply pressure, while the point guard shifts slightly towards the left to provide support. The other defenders in the zone should adjust their positions to maintain coverage and prevent easy passing lanes to the interior.',
        '2': 'When player 2 has the ball, the left wing defender should continue to pressure the ball, while the center and the opposite wing defender shift towards the middle to protect the paint and contest any potential shots or drives.',
        '3': 'When the ball is with the middle offensive players, the center defender needs to be prepared to step up to challenge shots or drives to the basket, while the two wing defenders should stay alert to close out on any shooters on the perimeter. The main defender should cover the players strongest hand, for example the right hand if they are right handed. ',
        '4': 'If the ball swings to the right side, the right wing defender must step out to pressure the ball handler, while the point guard shifts towards the right to provide support. The rest of the defenders should adjust accordingly to maintain the integrity of the zone defense.',
        '5': "When the rightmost offensive player has the ball, the right wing defender should apply pressure, and the weak-side defenders need to be ready to rotate and provide help defense if the ball is driven towards the basket. It's crucial to communicate and rotate effectively to deny open shots and prevent easy scoring opportunities."
    };

    // Function to handle when a player button is clicked
    $('.player-button').click(function () {
        // Get the player number from the clicked button's ID
        var playerNumber = $(this).attr('id').split('-')[1]; // Assuming IDs are in the format "playerX-button"

        // Get the corresponding description for the player
        var description = descriptions[playerNumber];

        // Update the text below the player buttons with the description
        $('#player-description').text(description);

        // Construct the filename for the corresponding image
        var imageUrl = '/static/pass_to_player_' + playerNumber + '.png';
        // Swap out the image with the updated one
        $('#basketball-court').attr('src', imageUrl);
        var popup = document.getElementById("myPopup" + playerNumber);
        popup.innerHTML = description
        popup.classList.toggle("show");
    });


    var playerClicks = { '1': 0, '2': 0, '3': 0, '4': 0, '5': 0 }; // Tracks the number of clicks per player
    var totalPlayers = 5;
    var requiredClicksPerPlayer = 2;
    var totalClicksRequired = totalPlayers * requiredClicksPerPlayer; // Total clicks required for full progression

    $('.player-button').click(function () {
        var playerNumber = $(this).attr('id').split('-')[1];
        popup = $("#myPopup" + playerNumber)
        if ($(popup).hasClass("show")) {


            // Increment the click count for the clicked player if it hasn't reached the maximum required clicks
            if (playerClicks[playerNumber] < requiredClicksPerPlayer) {
                playerClicks[playerNumber]++;
            }

            // Update description and image
            $('#player-description').text(descriptions[playerNumber]);
            $('#basketball-court').attr('src', '/static/pass_to_player_' + playerNumber + '.png');
            var popup = $("#myPopup" + playerNumber);
            // Update the progress bar

            updateProgressBar();
        }
    });

    var $button = $('<button>', {
        text: 'Next',
        id: 'next-button',   // Set button ID
        class: "btn btn-primary",
        click: function () { // Click event handler
            window.location.href = "/connection";
        }
    });

    function updateProgressBar() {
        var totalClicksMade = 0;

        // Sum all clicks made
        Object.values(playerClicks).forEach(function (clicks) {
            totalClicksMade += clicks;
        });

        var progressPercentage = (totalClicksMade / totalClicksRequired) * 100;
        $('.progress-bar-fill').css('width', progressPercentage + '%');

        // Update completed steps visually based on each click
        var completedSteps = Math.floor(totalClicksMade * 12 / totalClicksRequired);
        $('.progress-step').removeClass('completed');
        $('.progress-step').slice(0, completedSteps).addClass('completed');

        console.log(totalClicksMade);
        if (totalClicksMade == 10) {
            $("#showNext").append($button);
        }
    }

    // Event handlers for 'next' and 'previous' buttons...

    updateProgressBar(); // Initial update when page loads


});
