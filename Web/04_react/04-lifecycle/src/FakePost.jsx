import { useEffect, useState } from "react";
import fakePosts from "./FakePostChild";

function PostList() {
    const [posts,setPosts] = useState([]);
    useEffect(()=>{
            console.log('컴포넌트 마운트!');
            setTimeout(() =>{
                setPosts(fakePosts);
            }, 2000);} ,[]);
    return (  
    <div>
        <h1>Post List</h1>
        {posts.length === 0 
        ? (<span>loading...</span>) 
        : (
        <ul>
            {posts.map((value) => (
            <li key={value.id}>
                <h3>{value.title}</h3>
                <p>{value.body}</p>
            </li>
            ))}
        </ul>
        )}
    </div>
    );

}

export default PostList;