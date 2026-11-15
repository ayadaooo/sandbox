import LotmItem from "./LotmItem";

function Card(){
    return(
        {names.map((person) => (
            <LotmItem name={person} isMain={person === "Klein Moretti"} />
        ))}
    )}