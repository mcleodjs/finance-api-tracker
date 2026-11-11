import { useState, useEffect } from 'react'

import './App.css'

function App() {
  const [transactions, setTransactions] = useState([])
// this is how we get the front end to get the frontend to remember transactions and update them if they change.
  // this is how we get the front end to get the frontend to remember transactions and update them if they change. 

  

  const [category, setCategory] = useState("")

  const [description, setDescription] = useState("")

  const [date, setDate] = useState("")

  const [price, setPrice] = useState("")



function handleAdd(e){
  e.preventDefault()
  fetch("http://127.0.0.1:8000/Transactions", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({description: description, category: category, date: date, price: Number(price)})
  })
    .then(res => res.json())
    .then(newTransaction => {
      setTransactions([...transactions, newTransaction])
      setCategory("")
      setDescription("")
      setDate("")
      setPrice("")
    })
}

  // useEffect runs code outside of React  after first render "connecting" to it our API/Python
  useEffect(() => {
    fetch("http://127.0.0.1:8000/Transactions") // this calls our API
      .then(res => res.json())
      .then(data => setTransactions(data))
      // this gets call when the data is ready
  }, [])



  return (
  <main className="app">
    <header className="app-header">
      <h1>Finance Tracker</h1>
      <p>Track what you spend, one transaction at a time.</p>
    </header>

    <section className="card">
      <h2>Transactions</h2>
      <ul className="tx-list">
        {transactions.map(transaction => (
          <li key={transaction.id} className="tx-item">
            <div className="tx-main">
              <span className="tx-desc">{transaction.description}</span>
              <span className="tx-cat">{transaction.category}</span>
            </div>
            <span className="tx-date">{transaction.date}</span>
            <span className="tx-price">${transaction.price}</span>
          </li>
        ))}
      </ul>
    </section>

    <section className="card">
      <h2>Add transaction</h2>
      <form className="tx-form" onSubmit={handleAdd}>
        <input className="box-wide" placeholder="Category" value={category} onChange={(e) => setCategory(e.target.value)} />
        <input className="box-wide" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <input className="box-short" type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        <input className="box-short" type="number" placeholder="Price" value={price} onChange={(e) => setPrice(e.target.value)} />
        <button type="submit">Add transaction</button>
      </form>
    </section>
  </main>
)
}
export default App