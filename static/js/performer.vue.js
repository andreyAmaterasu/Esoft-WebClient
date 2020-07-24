const performer = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app3',
    data: {
        performermanager: [],
        performers: [],
        managers: [],
    },
    mounted() {
        const host = `${window.location.protocol}//${window.location.host}`;
        axios
            .get(host + '/api/performermanager/')
            .then(response => (this.performermanager = response.data));
    }
});