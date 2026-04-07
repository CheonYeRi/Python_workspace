from fastapi import APIRouter, HTTPException
from app.db import get_connection
from app.schemas.posts import PostCreate, PostUpdate

router = APIRouter()

@router.get("/posts")
def get_posts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    result = cursor.fetchall()
    conn.close()
    return result

@router.get("/posts/{author}")
def get_posts_by_author(author: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE author = %s", (author,))
    result = cursor.fetchall()
    conn.close()
    return result

@router.post("/posts")
def create_post(post: PostCreate):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO posts (author, content) VALUES (%s, %s)"
        cursor.execute(sql, (post.author, post.content))
        conn.commit()
        #방금 생성된 데이터 조회해서 반환
        cursor.execute("SELECT * FROM posts WHERE id = %s", (id, ))
        return {"message": "Post created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@router.put("/posts/{post_id}")
def update_post(post_id: int, post: PostUpdate):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "UPDATE posts SET content = %s WHERE id = %s"
        cursor.execute(sql, (post.content, post_id))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Post not found")
        return {"message": "Post updated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@router.delete("/posts/{id}")
def delete_post(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM posts WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Post not found")
        return {"message": "Post deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()    