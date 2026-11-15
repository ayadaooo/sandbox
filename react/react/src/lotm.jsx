function Lotm({ title, description,children }) {
  return (
    <div className="min-h-screen flex items-center justify-center">
    <div data-theme="light" className="card bg-base-100 shadow-md ">
      <div className="card-body">
      <h1 className=" card-title">{title}</h1>
      <p className="">{description}</p>
      <div className="">{children}</div>
      </div>
    </div>
    </div>

  )
}
export default Lotm