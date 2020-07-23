const performer = new Vue({
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