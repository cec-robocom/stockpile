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
newComponentButton.addEventListener('click', function () {
    nodeToInsert = temporaryNode.cloneNode(true);
    borrow_form.insertBefore(nodeToInsert, newComponentButton);
    console.log('clicked button');
});

// let borrowPageTransition = anime({
//     targets: '.underline',
//     // width: ['50%', '100%'],
//     left: '+=50%',
//     easing: 'linear',
//     autoplay: false
// });

let menuButtons = document.getElementsByClassName('menu-item');
let header = document.getElementsByTagName('header')[0];

let borrowButton = menuButtons[0];
let returnButton = menuButtons[1];

let borrowPageTransition = anime.timeline({
    autoplay: false,
    easing: 'linear'
});

borrowPageTransition
.add({
    targets: '.underline',
    left: '50%',
    duration: 200,
    complete: function() {
        console.log('first step complete')
    }
})
.add({
    targets: returnButton,
    opacity: 0,
    translateX: '60vw',
    duration: 500
})
.add({
    targets: '.menu',
    // transateX: '500px',
    translateY: '-100vh',
    duration: 200,
    // width: '25%',
    complete: function() {
        console.log('third step complete');
    },
    begin: function() {
        console.log('third step begin');
    }
})
.add({
    targets: '.borrow-form',
    translateY: '-108vh',
    duration: 200
});

borrowButton.addEventListener('click', function () {
    console.log('clicked borrow button');
    borrowPageTransition.play();
    borrowPageTransition.finished.then(function() {
        borrowPageTransition.reverse();
        console.log('animation reversed');
    })
});

document.getElementsByClassName('back-to-home')[0].addEventListener('click', function() {
    // borrowPageTransition.reverse();
    borrowPageTransition.play();
    borrowPageTransition.finished.then(function() {
        borrowPageTransition.reverse();
        console.log('animation reversed');
    })
});