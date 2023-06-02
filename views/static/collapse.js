function toggleCollapse(prefix) {
    let container = $(`#${prefix}_container`)
    let button    = $(`#${prefix}_button`)
    
    if (container.is(':hidden')) {
        // show it
        container.show()
        button[0].innerHTML = '&#9662;'
        
    } else {
        // hide it
        container.hide()
        button[0].innerHTML = '&#9656'
    }
}
