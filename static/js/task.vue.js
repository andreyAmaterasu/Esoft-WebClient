const vm2 = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app5',
    data: {
        task: {},
    },
    methods: {
        async createTask() {
            const str = JSON.stringify(this.task);
            await axios.post('http://10.0.0.3:8000/api/task/', str, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            });
        }
    }
});