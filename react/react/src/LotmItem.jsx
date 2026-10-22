function LotmItem({name, isMain}) {
  return (
    <li>{name} {isMain && "⭐"}</li>

  )
}
export default LotmItem