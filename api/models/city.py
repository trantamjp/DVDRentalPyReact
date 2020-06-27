from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from . import BaseModel


class City(BaseModel):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('city_city_id_seq'::regclass)"))
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id'),
                        nullable=False, index=True)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))

    country = relationship('Country', backref='cities')

    def __repr__(self):
        return '<City {} {} -> country_id {}>'.format(self.city_id, self.city, self.country_id)
