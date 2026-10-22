    import LotmItem from './LotmItem.jsx'

    function LotmList() {
    const names = ["Zhou Mingrui", "Klein Moretti", "The Fool", "Sherlock Moriarty", "Gehrman Sparrow", "The World", "Dwayne Dantes", "Merlin Hermes", "Mysteries"]


    return (
        <ul className="text-xl text-white min-h-screen bg-neutral-950 flex flex-row items-center justify-center gap-4">
        {names.map((person) => (
            <LotmItem name={person} isMain={person === "Klein Moretti"} />
        ))}
        </ul>
    )
    }
    export default LotmList