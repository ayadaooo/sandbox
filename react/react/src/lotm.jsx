function Lotm({ title, description }) {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-neutral-950">
      <h1 className="text-4xl font-bold text-yellow-500">{title}</h1>
      <p className="text-lg text-yellow-600">{description}</p>
    </div>

  )
}
export default Lotm