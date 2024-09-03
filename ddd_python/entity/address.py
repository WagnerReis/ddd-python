from pydantic import BaseModel, field_validator, ValidationError


class Address(BaseModel):
    street: str
    number: int
    zip: str
    city: str

    @classmethod
    @field_validator('street', 'zip', 'city', mode="before")
    def validate_string_fields(cls, value: str, field):
        if not value or len(value.strip()) == 0:
            raise ValueError(f'{field.name.capitalize()} cannot be empty')
        return value

    @classmethod
    @field_validator('number', mode="before")
    def validate_number(cls, value: int, field):
        if value <= 0:
            raise ValueError(f'{field.name.capitalize()} must be greater than zero')
        return value

    def to_string(self):
        return f"{self.street}, {self.number}, {self.zip}, {self.city}"
