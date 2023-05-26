function loadContent(page) {
    fetch(`content/${page}.html`)
        .then(resp => {
            return resp.text()
        })
        .then(data => {
            $('#content')[0].innerHTML = data
        })
}
