import { useState, useEffect } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  // this is how we get the front end to get the frontend to remember transactions and update them if they change. 

  const [transactions, setTransactions] = useState([]); // we use '[]' instead of 0 because my api returns a list.

  const [category, setCategory] = useState("")

  const [description, setDescription] = useState("")

  const [date, setDate] = useState("")

  const [price, setPrice] = useState("")

  // useEffect runs code outside of React  after first render "connecting" to it our API/Python
  useEffect(() => {
    fetch("http://127.0.0.1:8000/Transactions") // this calls our API
      .then(res => res.json())
      .then(data => setTransactions(data))
      // this gets call when the data is ready
  }, [])

  console.log(transactions)

  return (
    <>
      <ul>
        {transactions.map(transaction => (
          <li key={transaction.id}>{transaction.description} - ${transaction.price} - {transaction.date} - {transaction.category} </li>
        ))}
      </ul>

      <input
        className="box-wide"
        placeholder="Category"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      />
      <input
        className="box-wide"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        className="box-short"
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <input
        className="box-short"
        type="number"
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
    </>
  )
}

export default App