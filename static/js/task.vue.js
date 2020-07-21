const tasks = JSON.parse(document.getElementById('tasks_json').textContent);
const vm2 = new Vue({
    delimiters: ["[[", "]]"],
el: '#app4',
data: {
    tasks: tasks.tasks,
    performers: tasks.performers,
    manager: `${tasks.manager.lastname} ${tasks.manager.firstname} ${tasks.manager.patronymic}`,
    selectedPerformer: 'Все',
    selectedStatus: 'Все'
},
});