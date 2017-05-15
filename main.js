// Thanks http://stackoverflow.com/a/5920206
// details-block-content
function doRequest(word) {
    var textElm = ".menu-input";
    textElm.value = word;
    setTimeout(function() {
        var evt = document.createEvent("KeyboardEvent");
        (evt.initKeyEvent || evt.initKeyboardEvent)("keypress", true, true, window, 0, 0, 0, 0, 0, "\n".charCodeAt(0));
        return body.dispatchEvent(evt);
    }, 3000);
}
doRequest("abcdefg");
// setInterval(doRequest, 2500);
