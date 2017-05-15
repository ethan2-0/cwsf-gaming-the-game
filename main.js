// Thanks http://stackoverflow.com/a/5920206
// details-block-content
var PARTIY = 0;
var MODULUS = 4;
function doRequest() {
    fetch(`http://localhost:5001/word/${PARITY}`).then(function(response) {
        return response.text();
    }).then(function(text) {
        var textElm = document.querySelector(".menu-input");
        textElm.value = word'
        textElm.focus();
        PARITY += MODULUS;
    });
}
function doInsanity() {
    setInterval(function() {
        doRequest();
    }, 2000);
}
// setInterval(doRequest, 2500);
