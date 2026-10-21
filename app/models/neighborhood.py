from sqlachemy import Column, Integer, String
from geoalchemy2 improt Geometry
from app.db.session import Base

class Neighborhood(Base):
    __tablename__ = "neighborhoods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    earthquake_risk_score = Column(Float, nullable=False)
    avg_rent = Column(Float, nullable=True)
    geom = Column(Geometry(geometry_type='GEOMETRY', srid=4326), nullable=True)