const tasks_performer_manager = JSON.parse(document.getElementById('tasks_performer_manager').textContent);
const vm2 = new Vue({
    delimiters: ["[[", "]]"],
el: '#app4',
data: {
    tasks: tasks_performer_manager.tasks,
    performer: `${tasks_performer_manager.performer.lastname} ${tasks_performer_manager.performer.firstname} ${tasks_performer_manager.performer.patronymic}`,
    manager: `${tasks_performer_manager.manager.lastname} ${tasks_performer_manager.manager.firstname} ${tasks_performer_manager.manager.patronymic}`,
},
});