from datetime import datetime

from app.db.crud import (
    Session,
    create_area,
    create_scanner,
    recreate_database,
)
from app.schemas.schemas import createArea, Scanner


recreate_database()

s = Session()

newArea = createArea(
    name="Quarto", width=10.5, height=8.2, floorplan="url", created_at=datetime.now()
)
newarea = create_area(db=s, area=newArea)

print(newarea)

newscanner = Scanner(name="Scanner0", x_pos=9.1, y_pos=0.2, area=newarea.id)
newscaner = create_scanner(db=s, scanner=newscanner)
print("end")
