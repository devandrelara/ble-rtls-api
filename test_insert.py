from ble_rtls_worker.db.crud import Session, recreate_database
from ble_rtls_worker.models.models import Area
from datetime import datetime

recreate_database()

s = Session()

newArea = Area(
    name="Quarto", width=10.5, height=8.2, floorplan="url", created_at=datetime.now()
)
print(newArea)
s.add(newArea)
s.commit()
