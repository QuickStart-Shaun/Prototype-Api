
  const addTodoButton = document.querySelector('[data-todo="add-todo"]')
  const clearTodosButton = document.querySelector('[data-todo="clear-todos"]')
  const empty = document.querySelector('[data-todo="empty"]')
  const todo = document.querySelector('[data-todo="todo"]')
  const todosParent = todo.parentNode

  let currentTodo = 0

  const addTodo = async () => {
    try {
      currentTodo++
      console.log("trying api");
      const data = await fetch(
        `https://demo-api-gs.herokuapp.com`, {
          method: 'GET',
          headers: {
            'X-RapidAPI-Key': 'your-rapidapi-key',
            'X-RapidAPI-Host': 'famous-quotes4.p.rapidapi.com',
          },
        })
      const json = await data.json();
      console.log(json);

      const todos = [...document.querySelectorAll('[data-todo="todo"]')]
      const newTodo = currentTodo === 1 ? todos[0] : todos[0].cloneNode(true)

      const title = newTodo.querySelector('[data-todo="title"]')
      const id = newTodo.querySelector('[data-todo="id"]')

      title.innerText = `Title: ${json.title}`
      id.innerText = `ID: ${json.id}`

      if (currentTodo > 1) {
        todosParent.appendChild(newTodo)
      }
      newTodo.style.display = 'flex'

      const removeButton = newTodo.querySelector('[data-todo="remove"]')
      removeButton.addEventListener('click', () => {
        const todos = [...document.querySelectorAll('[data-todo="todo"]')]
        if (todos.length === 1) {
          currentTodo = 0
          newTodo.style.display = 'none'
        } else {
          newTodo.parentNode.removeChild(newTodo)
        }
      })
    } catch (err) {
      console.error(`Error getting todo: ${err}`)
    }
  }

  addTodoButton.addEventListener('click', addTodo)

  const clearTodos = () => {
    currentTodo = 0
    const todos = [...document.querySelectorAll('[data-todo="todo"]')]
    todos.forEach((todo, index) => {
      if (index === 0) {
        todo.style.display = 'none'
      } else {
        todo.parentNode.removeChild(todo)
      }
    })
  }

  clearTodosButton.addEventListener('click', clearTodos);
