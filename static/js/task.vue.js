const task = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app5',
    data: {
        task: {},
        performers: [],
        createSuccess: false,
    },
    methods: {
        async createTask() {
            const str = JSON.stringify(this.task);
            const host = `${window.location.protocol}//${window.location.host}`;
            await axios.post(host + '/api/task/', this.task, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                console.log(response);
                this.createSuccess = true;
            })
            .catch((error) => {
                console.log(error);
            });
        }
    },
    mounted() {
        const host = `${window.location.protocol}//${window.location.host}`;
        axios
            .get(host + '/api/getperformers/')
            .then(response => (this.performers = response.data)); 
    }
});