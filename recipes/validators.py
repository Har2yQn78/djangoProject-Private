from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError
valid_unit_measurements = ['kg', 'm', 'g', 'cm', 'lbs', 'pound']


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e}")
    except:
        raise ValidationError(f"{value} is invalid, Unknown error")

