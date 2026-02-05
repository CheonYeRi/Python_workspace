import { useState } from "react";

function MapUser() {
    const [name, setName] = useState(""); 
    const [inputEmail, setInputEmail] = useState("");
    const [users, setUsers] = useState([]);
    
    const addUsers = () => {
        const newUsers = {
            id: users.length + 1,
            name: name,
            Email: inputEmail,
        };
        setUsers([...users, newUsers]);
        setInputEmail("");
        setName("");
    };
    const deleteUsers = (targetId) => {
        const newUsers = users.filter((users) => users.id !== targetId);
        setUsers(newUsers);
    }

    return(
        <>
            <input type="text" placeholder="이름" value={name} 
            onChange={(e)=> setName(e.target.value)} />

            <input type="text" placeholder="이메일" value={inputEmail} 
            onChange={(e)=> setInputEmail(e.target.value)} />

            <button onClick={addUsers}>등록 </button>
            <hr />

            <ol>
                {users.map((user) => {
                    return <li key={user.id} onDoubleClick={() => deleteUsers(user.id)}> {user.name} : {user.Email}</li>;
                })}
            </ol>
        </>

    );
}


export default MapUser;