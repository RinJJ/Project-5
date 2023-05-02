import React, {useState, useEffect} from "react";

const UserContext = React.createContext()

function UserProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() =>
    async function checkAuthStatus() {
        const response = await fetch('/api/check-auth-status')
        const data = await response.json();
        setUser(data.user)
    })
    
    return (
        <UserContext.Provider value={{ user, setUser }}>
            {children}
        </UserContext.Provider>
    );
}

export { UserContext, UserProvider }