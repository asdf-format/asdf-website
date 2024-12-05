let themeSetting = document.body.dataset.theme;
if ( themeSetting != 'light' ) {
    let graphElem = document.getElementsByClassName('graphviz');
    if ( graphElem.length > 1 ) {
        graphObj = graphElem[1];
        graphObj.setAttribute("style", "background-color: white;");
    }
}