import {useState} from "react"

function Counter() {
  const [count, setCount] = useState(0)
  const incrementCount = () => {
    setCount(count + 1)
  }
  return (<div className="min-h-screen flex items-center justify-center">
    <h1 className="text-2xl font-bold gap-4">Counter: {count}</h1>
    <button className="btn btn-primary gap-4" onClick={incrementCount}>CLICK
    </button>
  </div>
  )
}

export default Counter