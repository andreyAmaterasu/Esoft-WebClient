// const managers_persormers = JSON.parse(document.getElementById('managers_persormers').textContent);
// const vm2 = new Vue({
//     delimiters: ["[[", "]]"],
// el: '#app3',
// data: {
//     managers_persormers,
// },
// });

const vm2 = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app3',
    data: {
        performermanager: [],
        performers: [],
        managers: [],
    },
    mounted() {
        axios
            .get('http://10.0.0.3:8000/api/performermanager/')
            .then(response => (this.performermanager = response.data));
    }
});