import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'

import './App.css'
import Lotm from './lotm.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Lotm title="LOTM" description="Welcome to LOTM!" />
  )
}

export default App
