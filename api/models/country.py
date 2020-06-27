from sqlalchemy import Column, DateTime, Integer, Numeric, String, text

from . import BaseModel


class Country(BaseModel):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('country_country_id_seq'::regclass)"))
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))

    def __repr__(self):
        return '<Country {} {}>'.format(self.country_id, self.country)
