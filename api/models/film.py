from sqlalchemy import (ARRAY, Column, DateTime, Enum, ForeignKey, Integer,
                        Numeric, SmallInteger, String, Text, and_, cast,
                        distinct, func, or_, text)
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.orm import contains_eager, relationship

from . import BaseModel
from .actor import Actor
from .category import Category
from .film_actor import FilmActor
from .film_category import FilmCategory
from .language import Language

film_actor = FilmActor.__table__
film_category = FilmCategory.__table__

search_like_escape = BaseModel.search_like_escape


class Film(BaseModel):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True, server_default=text(
        "nextval('film_film_id_seq'::regclass)"))
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(ForeignKey('language.language_id',
                                    ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    rental_duration = Column(
        SmallInteger, nullable=False, server_default=text("3"))
    rental_rate = Column(Numeric(4, 2), nullable=False,
                         server_default=text("4.99"))
    length = Column(SmallInteger)
    replacement_cost = Column(
        Numeric(5, 2), nullable=False, server_default=text("19.99"))
    rating = Column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17',
                         name='mpaa_rating'), server_default=text("'G'::mpaa_rating"))
    last_update = Column(DateTime, nullable=False,
                         server_default=text("now()"))
    special_features = Column(ARRAY(Text()))
    fulltext = Column(TSVECTOR, nullable=False, index=True)

    language = relationship('Language')

    categories = relationship('Category', secondary=film_category,
                              back_populates="films")
    actors = relationship('Actor', secondary=film_actor,
                          back_populates="films")

    def __repr__(self):
        return '<Film {} {}>'.format(self.film_id, self.title)

    @classmethod
    def datatable_search(cls, args):

        offset = args.get('offset') or 0
        limit = args.get('limit') or 10
        orders = args.get('order') or []
        filters = args.get('filters') or {}
        orders = args.get('orders') or []

        records_total = Film.query.count()

        rs_filters = []
        for filter in filters:
            filter_id = filter.get('id')

            search_value = filter.get('value') or ''
            if search_value == '':
                continue

            if filter_id == 'title':
                rs_filters.append(Film.title.ilike(
                    search_like_escape(search_value)))
                continue

            if filter_id == 'categories.category':
                rs_filters.append(Film.categories.any(
                    Category.name.ilike(search_like_escape(search_value))
                ))
                continue

            if filter_id == 'actors.full_name':
                rs_filters.append(
                    Film.actors.any(
                        Actor.full_name.ilike(
                            search_like_escape(search_value)),
                    )
                )
                continue

            if filter_id == 'length':
                rs_filters.append(cast(Film.length, Text).ilike(
                    search_like_escape(search_value)))
                continue

            if filter_id == 'rating':
                rs_filters.append(cast(Film.rating, Text).ilike(
                    search_like_escape(search_value)))
                continue

            if filter_id == 'language.name':
                rs_filters.append(Language.name.ilike(
                    search_like_escape(search_value)))
                continue

            if filter_id == 'rental_rate':
                rs_filters.append(cast(Film.rental_rate, Text).ilike(
                    search_like_escape(search_value)))
                continue

        rs_filtered = Film.query.join(Language).filter(and_(*rs_filters))

        # Count without limit
        records_filtered = rs_filtered.with_entities(
            func.count(distinct(Film.film_id))).scalar()

        order_columns = []
        for order in orders:
            order_id = order.get('id')
            order_desc = order.get('desc')

            if order_id == 'title':
                order_columns.append([Film.title, order_desc])
                continue

            if order_id == 'length':
                order_columns.append([Film.length, order_desc])
                continue

            if order_id == 'rating':
                order_columns.append([cast(Film.rating, Text), order_desc])
                continue

            if order_id == 'language.name':
                order_columns.append([Language.name, order_desc])
                continue

            if order_id == 'rental_rate':
                order_columns.append([Film.rental_rate, order_desc])
                continue

            raise NameError('Unknown sort column {}'.format(order_id))

        rs_orders = list(map(lambda order: order[0].desc() if order[1] else order[0].asc(),
                             order_columns))
        select_columns = list(map(lambda order: order[0], order_columns))

        # Only interested on film_id AFTER order and limit
        filtered_with_limit_subq = rs_filtered \
            .with_entities(Film.film_id).order_by(*rs_orders) \
            .limit(limit).offset(offset).subquery()

        final_query = Film.query \
            .join(filtered_with_limit_subq, Film.film_id == filtered_with_limit_subq.c.film_id) \
            .join(Language).outerjoin(Category, Film.categories).outerjoin(Actor, Film.actors) \
            .options(contains_eager(Film.language), contains_eager(Film.categories), contains_eager(Film.actors)) \
            .order_by(*rs_orders)   # Apply order again for eager loading

        # Force order on actor and category
        final_query = final_query.order_by(
            Actor.full_name.asc(), Category.name.asc())

        films = final_query.all()

        film_list = {
            'records_total': records_total,
            'records_filtered': records_filtered,
            'films': films,
        }

        return film_list
