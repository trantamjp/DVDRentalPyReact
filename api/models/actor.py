from sqlalchemy import Column, DateTime, Integer, String, case, text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, column_property

from . import BaseModel
from .film_actor import FilmActor


class Actor(BaseModel):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('actor_actor_id_seq'::regclass)"))
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))

    full_name = column_property(first_name + " " + last_name)

    # @hybrid_property
    # def full_name(self):
    #     return " ".join(filter(lambda x: x, [self.first_name, self.last_name]))

    # @full_name.expression
    # def full_name(cls):
    #     return case(
    #         [
    #             (cls.first_name != '', case(
    #                 [(cls.last_name != '', cls.first_name + " " + cls.last_name)],
    #                 else_=cls.first_name
    #             ))
    #         ],
    #         else_=cls.last_name)

    films = relationship('Film', secondary='film_actor',
                         back_populates="actors")

    # Add additional columns into dict which are not in cls.__table__.columns
    # e.g. hybrid_property, column_property
    def row2dict(self):
        d = super().row2dict()
        for c in ['full_name']:
            d[c] = getattr(self, c)
        return d

    def __repr__(self):
        return '<Actor {} {} {}>'.format(self.actor_id, self.first_name, self.last_name)
