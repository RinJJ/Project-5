import { createContext, useState, useEffect } from "react";
import { Switch, Route, NavLink, useHistory } from "react-router-dom";


// below are route imports
import PageLookingForGroup from "./PageLookingForGroup";
import NavBar from './NavBar'
import PageLogin from "./PageLogin";
import PageMyCharacters from "./PageMyCharacters";
import PageMyGroups from "./PageMyGroups";
import PageHome from "./PageHome";






export const LoginContext = createContext();

function App() {
    
    const [loggedIn, setLoggedIn] = useState();







    return (
        <>
        <LoginContext.Provider>
            <header>
                <NavBar className='navbar'/>
            </header>
            <div>
                <Switch>
                    <Route path='/LoginCreate'>
                        <PageLogin className=''/>
                    </Route>
                    <Route path='/MyCharacters'>
                        <PageMyCharacters className=''/>
                    </Route>
                    <Route path='/MyGroups'>
                        <PageMyGroups className=''/>
                    </Route>
                    <Route path='/LookingForGroup'>
                        <PageLookingForGroup className=''/>
                    </Route>
                    <Route path='/'>
                        <PageHome className=''/>
                    </Route>
                </Switch>
            </div>
        </LoginContext.Provider>
        </>
    );
}

export default App;
