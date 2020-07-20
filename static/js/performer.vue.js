const managers_persormers = JSON.parse(document.getElementById('managers_persormers').textContent);
const vm2 = new Vue({
    delimiters: ["[[", "]]"],
el: '#app3',
data: {
    managers_persormers,
},
});