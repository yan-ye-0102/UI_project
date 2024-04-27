$(document).ready(function() {
    // Define descriptions for each player
    var descriptions = {
        '1': 'When the leftmost offensive player has the ball, the left wing defender should step out to apply pressure, while the point guard shifts slightly towards the left to provide support. The other defenders in the zone should adjust their positions to maintain coverage and prevent easy passing lanes to the interior.',
        '2': 'When player 2 has the ball, the left wing defender should continue to pressure the ball, while the center and the opposite wing defender shift towards the middle to protect the paint and contest any potential shots or drives.',
        '3': 'When the ball is with the middle offensive players, the center defender needs to be prepared to step up to challenge shots or drives to the basket, while the two wing defenders should stay alert to close out on any shooters on the perimeter. The main defender should cover the players strongest hand, for example the right hand if they are right handed. ',
        '4': 'If the ball swings to the right side, the right wing defender must step out to pressure the ball handler, while the point guard shifts towards the right to provide support. The rest of the defenders should adjust accordingly to maintain the integrity of the zone defense.',
        '5': "When the rightmost offensive player has the ball, the right wing defender should apply pressure, and the weak-side defenders need to be ready to rotate and provide help defense if the ball is driven towards the basket. It's crucial to communicate and rotate effectively to deny open shots and prevent easy scoring opportunities."
    };

    // Function to handle when a player button is clicked
    $('.player-button').click(function() {
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
    });
});