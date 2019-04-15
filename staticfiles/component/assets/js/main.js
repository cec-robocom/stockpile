/**
 * request multiple components simultaneously
 */
let borrow_form = document.getElementById('borrow-form');
let newComponentButton = document.getElementById('get-another-one');
let append = 'none';
let temporaryNode = document.createElement('label');

temporaryNode.innerHTML = `<div class="component">
    <select name="component_name" id="component_name">
        <option value="none" selected>--Select a component--</option>
        <option value="resistor">Resistor</option>
        <option value="capacitor">Capacitor</option>
        <option value="diode">Diode</option>
    </select>
    <label for="component_count">Count: </label>
    <input type="number" name="component_count" min="0" placeholder="Eg. 10" required>
</div>`;

let nodeToInsert = null;
newComponentButton.addEventListener('click', function() {
    nodeToInsert = temporaryNode.cloneNode(true);
    borrow_form.insertBefore(nodeToInsert, newComponentButton);
    console.log('clicked button');
});



