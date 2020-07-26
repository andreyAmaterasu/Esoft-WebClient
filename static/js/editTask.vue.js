const task = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app6',
    data: {
        tasksPM: [],
        tasks: [],
        performers: [],
        editedTask: {},
        editedSuccess: false,
    },
    methods: {
        async editTask() {
            const host = `${window.location.protocol}//${window.location.host}`;
            await axios.patch(host + '/api/task/' + this.editedTask.taskid + '/', this.editedTask)
            .then((response) => {
                console.log(response);
                this.editedSuccess = true;
            });
        }
    },
    mounted() {
        const host = `${window.location.protocol}//${window.location.host}`;

        axios
            .get(host + '/api/taskperformermanager/')
            .then(response => (this.tasksPM = response.data)); 

        axios
            .get(host + '/api/task/')
            .then(response => (this.tasks = response.data)); 

        axios
            .get(host + '/api/getperformers/')
            .then(response => (this.performers = response.data)); 
    }
});