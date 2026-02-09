import Button from "@components/buttons"; 
import DuckImage from "@assets/duck.png"; 

function Header(){
    return(
        <>
        <header>
            <h1> Hello React</h1>
        </header>
        <hr></hr>

        <p>Learning new thing every single day untill i become a system enginner...</p>
        </>
    );
}
//console.log("HEllloo chat....!")
export default Header; 


export function MyPageHeader(){
    return (
        <header className="My-Page-Header" > 
            <div style={{border:"none"}} className="Sub-Box">
                <h2>My page</h2>
                <Button text="Website" command={()=>undefined } />
            </div>
            <div>
                <h1>Personal Proyects PP</h1> 
            </div>
            <div className="Image-Contenter">
                <img title="A little cute duck here :) " id="Duck-Image" className="My-page-Image" src={DuckImage} /> 
            </div>
        </header>
    )
}