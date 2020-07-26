var selectedTask = null;
const tasks = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app4',
    data: {
        tasks: [],
        selectedPerformer: 'Все',
        selectedStatus: 'Все',
        performers: [],
        taskId: null,
        deleteSuccess: false,
    },
    methods: {
        async selectTask(taskId) {
            this.taskId = taskId;
        },
        async getTasks() {
            const host = `${window.location.protocol}//${window.location.host}`;
            await axios.get(host + '/api/taskperformermanager/')
            .then(response => (this.tasks = response.data));  
        },
        async getPerformers() {
            const host = `${window.location.protocol}//${window.location.host}`;
            await axios.get(host + '/api/getperformers/')
            .then(response => (this.performers = response.data)); 
        },
        async removeTask(taskId) {
            const host = `${window.location.protocol}//${window.location.host}`;
            await axios.delete(host + '/api/task/' + taskId);
            await this.getTasks();
            this.deleteSuccess = true;
        },
    },
    computed: {
        isManager() {
            if ((this.performers.filter(performer => performer.login == user.login)).length) {
                return false;
            }
            else {
                return true;
            }
        },
    },
    created() {
        this.getTasks();
        this.getPerformers();
    },
});