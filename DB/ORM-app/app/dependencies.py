from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db #라우트로 세션을 전달
    finally:
        db.close() #요청 끝나면 세션 자동 종료


