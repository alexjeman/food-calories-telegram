from sqlalchemy import create_engine

from app.database.models import Base
from app.config import DATABASE


# engine_string = '{ENGINE}://{USER}:{PASS}@{HOST}:{PORT}/{BASE}'.format(
#     **DATABASE
# )


engine_string = 'sqlite:///food-calories-telegram.sqlite'

engine = create_engine(engine_string)

Base.metadata.create_all(engine)
