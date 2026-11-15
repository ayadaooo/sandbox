import {useState} from 'react'


function TextInput() { 
const [text, setText] = useState("")
return (<div className="min-h-screen flex items-center justify-center">
  <input value={text} onChange={(e) => setText(e.target.value)} />
</div>)
}

export default TextInput  