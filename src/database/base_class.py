from sqlalchemy.ext.declarative import declared_attr, as_declarative


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        # Авто-генерация названия таблиц во множественном числе
        return f"{cls.__name__.lower()}s"

    @declared_attr
    def __table_args__(cls) -> dict:
        return {"extend_existing": True}
