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
        axios
            .get('http://10.0.0.3:8000/api/taskperformermanager/')
            .then(response => (this.tasks = response.data));  

        axios
            .get('http://10.0.0.3:8000/api/getperformers/')
            .then(response => (this.performers = response.data)); 
    }
});