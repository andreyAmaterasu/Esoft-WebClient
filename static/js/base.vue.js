const user = JSON.parse(document.getElementById('user').textContent);
const vm = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app',
    data: {
        user,
    }
});