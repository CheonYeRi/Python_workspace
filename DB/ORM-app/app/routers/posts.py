from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.dependencies import get_db
from app.models.posts import Post
from app.schemas.posts import PostCreate, PostUpdate

router = APIRouter()

@router.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(author=post.author, content=post.content)
    try:
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return {"message": "Post created successfully"}
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/posts/{id}")
def update_post(id: int, post: PostUpdate, db: Session = Depends(get_db)):
    try:
        db_post = db.query(Post).filter(Post.id == id).first()
        if not db_post:
            raise HTTPException(status_code=404, detail="Post not found")

        db_post.author = post.author
        db_post.content = post.content
        db.commit()
        return {"message": "Post updated successfully"}
    
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/posts/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    try:
        db_post = db.query(Post).filter(Post.id == id).first()
        if not db_post:
            raise HTTPException(status_code=404, detail="Post not found")

        db.delete(db_post)
        db.commit()
        return {"message": "Post deleted successfully"}
    
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=400, detail=str(e))