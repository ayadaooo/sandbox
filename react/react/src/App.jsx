import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'

import './App.css'
import Lotm from './lotm.jsx'
import LotmList from './lotmList.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <><Lotm title="THE FOOL"
      description="the fool who doesn't belong to this era, the ruler above the gray fog, the king of yellow and black who weilds good luck.">
      praise the fool
    </Lotm>
    <LotmList /></>
  )
}

export default App
