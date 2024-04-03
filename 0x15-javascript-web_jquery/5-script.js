// When the document is ready
$(document).ready(function() {
    // Add a click event listener to the DIV#add_item
    $('div#add_item').click(function() {
        // Create a new <li> element with text "Item"
        const newItem = $('<li>Item</li>');
        
        // Append the new <li> element to UL.my_list
        $('ul.my_list').append(newItem);
    });
});
