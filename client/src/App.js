import { createContext, useState } from "react";




export const LoginContext = createContext();

function App() {
    const [loggedIn, setLoggedIn] = useState();
    return (
        <LoginContext.Provider value={}>
        <div className="App">
            <header className="App-header">
            </header>
        </div>
        </LoginContext.Provider>
    );
    }

export default App;
