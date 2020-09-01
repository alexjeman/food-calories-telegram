from sqlalchemy.orm import sessionmaker

from app.database.engine import engine


Session = sessionmaker(bind=engine)
