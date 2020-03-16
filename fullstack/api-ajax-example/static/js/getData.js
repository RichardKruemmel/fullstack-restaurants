function addTitle() {
    let title = document.createElement('h2');
    title.textContent = 'Restaurants in Berlin:';
    document.body.appendChild(title);
}

function getAllRestaurantNames(){

    let xhr = new XMLHttpRequest()

    xhr.onload = function () {
        console.log(this.responseXML)
    }
    xhr.open("GET", "http://127.0.0.1:5000/api/restaurants/names")
    xhr.send()

}