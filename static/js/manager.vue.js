        const managers = JSON.parse(document.getElementById('managers').textContent);
      const vm2 = new Vue({
          delimiters: ["[[", "]]"],
      el: '#app2',
      data: {
        managers,

      },
      });