const vm2 = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app4',
    data: {
        tasks: [],
        selectedPerformer: 'Все',
        selectedStatus: 'Все',
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

        performers: {
            get: function() {
                var performers = [];
                this.tasks.filter(task => {
                    if (task.taskperformer.manager.login == user.login) {
                        performers.push(task.taskperformer);
                    }
                });
                return performers;
            }
        }
    },
    mounted() {
        axios
            .get('http://10.0.0.3:8000/api/taskperformermanager/')
            .then(response => (this.tasks = response.data));  
    }
});