const tasks = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app4',
    data: {
        tasks: [],
        selectedPerformer: 'Все',
        selectedStatus: 'Все',
        performers: [],
    },
    computed: {
        isManager() {
            if ((this.tasks.filter(task => task.taskperformer.manager.login == user.login)).length) {
                return true;
            }
            else {
                return false;
            }
        },
    },
    mounted() {
        const host = `${window.location.protocol}//${window.location.host}`;
        axios
            .get(host + '/api/taskperformermanager/')
            .then(response => (this.tasks = response.data));  

        axios
            .get(host + '/api/getperformers/')
            .then(response => (this.performers = response.data)); 
    }
});