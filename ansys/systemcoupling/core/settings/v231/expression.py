#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.settings.datamodel import *

from .expression_child import expression_child


class expression(NamedObject[expression_child]):
    """
    Define a named expression that can be referenced in other expressions.
    """

    syc_name = "Expression"

    child_object_type: expression_child = expression_child
    """
    child_object_type of expression.
    """
