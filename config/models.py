from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from typing import List

# Clase base para los modelos de las tablas para la db
class Base(DeclarativeBase):
    pass


# Tabla para guardar las queries de los usuarios
class Tuser(Base):
    __tablename__ = "tuser"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    points: Mapped[int] = mapped_column(Integer, nullable=False)
    _redeemhistory: Mapped[List['Tredeemhistory']] = relationship('Tredeemhistory', backref='tuser')
    _challengehistory: Mapped[List['Tchallengehistory']] = relationship('Tchallengehistory', backref='tuser')
    _badge: Mapped[List['Tbadge']] = relationship('Tbadge', backref='tuser')


class Tredeemhistory(Base):
    __tablename__ = "tredeemhistory"

    value: Mapped[int] = mapped_column(Integer, nullable=False)
    times: Mapped[int] = mapped_column(Integer, nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey('tuser.id'), nullable=False, unique=True, primary_key=True)
    id_product: Mapped[int] = mapped_column(ForeignKey('tproduct.id'), nullable=False, unique=True, primary_key=True)


class Tchallengehistory(Base):
    __tablename__ = "tchallengehistory"

    value: Mapped[int] = mapped_column(Integer, nullable=False)
    times: Mapped[int] = mapped_column(Integer, nullable=False)
    parcial_points: Mapped[int] = mapped_column(Integer, nullable=False)
    isactive: Mapped[int] = mapped_column(Integer, nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey('tuser.id'), nullable=False, unique=True, primary_key=True)
    id_challenge: Mapped[int] = mapped_column(ForeignKey('tchallenge.id'), nullable=False, unique=True, primary_key=True)


class Tbadge(Base):
    __tablename__ = "tbadge"

    water: Mapped[int] = mapped_column(Integer, nullable= False)
    emission_reduction: Mapped[int] = mapped_column(Integer, nullable= False)
    reduce_waste: Mapped[int] = mapped_column(Integer, nullable= False)
    health_and_well_being: Mapped[int] = mapped_column(Integer, nullable= False)
    supporting_communities: Mapped[int] = mapped_column(Integer, nullable= False)
    biodiversity: Mapped[int] = mapped_column(Integer, nullable= False)
    develop_people_skills: Mapped[int] = mapped_column(Integer, nullable= False)
    holistic_micro: Mapped[int] = mapped_column(Integer, nullable= False)
    share: Mapped[int] = mapped_column(Integer, nullable= False)
    learn: Mapped[int] = mapped_column(Integer, nullable= False)
    propose: Mapped[int] = mapped_column(Integer, nullable= False)
    promote: Mapped[int] = mapped_column(Integer, nullable= False)
    participate: Mapped[int] = mapped_column(Integer, nullable= False)
    symrise_knowledge: Mapped[int] = mapped_column(Integer, nullable= False)
    inspire: Mapped[int] = mapped_column(Integer, nullable= False)
    holistic_macro: Mapped[int] = mapped_column(Integer, nullable= False)
    holistictotal: Mapped[int] = mapped_column(Integer, nullable= False)
    holistic: Mapped[int] = mapped_column(Integer, nullable= False)
    id_user: Mapped[int] = mapped_column(ForeignKey('tuser.id'), primary_key=True)


class Tchallenge(Base):
    __tablename__ = "tchallenge"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    points: Mapped[int] = mapped_column(Integer, nullable=False)
    completed: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    icon: Mapped[str] = mapped_column(String(100), nullable=True)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    bg_color: Mapped[str] = mapped_column(String(100), nullable=False)
    limit_of_completion: Mapped[int] = mapped_column(Integer, nullable=False)
    form: Mapped[str] = mapped_column(String(255), nullable=True)
    challenge_type: Mapped[str] = mapped_column(String(10), nullable=False)
    _challengehistory: Mapped[List['Tchallengehistory']] = relationship('Tchallengehistory', backref='tchallenge')


class Tproduct(Base):
    __tablename__ = "tproduct"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    _redeemhistory: Mapped[List['Tredeemhistory']] = relationship('Tredeemhistory', backref='tproduct')


class Timpact(Base):
    __tablename__ = "timpact"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[str] = mapped_column(String(255), nullable=False)
    units: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=False)