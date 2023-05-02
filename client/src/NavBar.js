import React, {useContext, useHistory} from "react";
import { UserContext } from "../context/user";
import Navbar from 'react-bootstrap/Navbar'



function NavBar() {

    const { user, setUser } = useContext(UserContext);
    const history = useHistory()

    const handleLogout = () => {
        fetch('/logout', {
            method:'DELETE'
        })
        .then(r => {
            if(r.ok){
            r.json().then(()=> {
                setUser(null)
                history.push('/')
            })

            }
        })
    }




    return (
    <nav className="navbar navbar-expand-sm navbar-dark bg-dark">
        <div className="container-fluid">
            <a className="navbar-brand" href="./">Home</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="mynavbar">
                <ul className="navbar-nav me-auto">
                    <li className="nav-item">
                        <a className="nav-link" href="/PageLookingForGroup">Looking For Group</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/PageMyCharacters">My Characters</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/PageMyCharacters">My Characters</a>
                    </li>

                </ul>     
            </div>
            {user? //Does this even work?
            <li className="nav-item">
                <a className="nav-link" href="/Login">Login/Create</a>
            </li>
            :
            <li className="nav-item">
                <a onClick={handleLogout}>Logout</a>
            </li>
            }
        </div>
    </nav>
    );
}

export default NavBar;

