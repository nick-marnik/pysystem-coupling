#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.impl.datamodel import *

from .expression import expression
from .expression_function import expression_function
from .instancing import instancing
from .reference_frame import reference_frame


class library(Group):
    """
    'library' child.
    """

    syc_name = "Library"

    child_names = ["expression", "expression_function", "reference_frame", "instancing"]

    expression: expression = expression
    """
    expression child of library.
    """
    expression_function: expression_function = expression_function
    """
    expression_function child of library.
    """
    reference_frame: reference_frame = reference_frame
    """
    reference_frame child of library.
    """
    instancing: instancing = instancing
    """
    instancing child of library.
    """
