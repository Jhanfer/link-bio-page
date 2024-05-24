import reflex as rx
from typing import Any,Dict,List,Optional,Set,Union,Literal,Callable

literal_var_type=Literal["default","primary"]
literal_var_shape=Literal["circle","square"]

class FloatButton(rx.Component):
    library="antd"
    tag="FloatButton"

    icon=rx.image(src="/icons/mug-hot-solid.svg")
    href:rx.Var[str]
    target:rx.Var[str]
    badge:rx.Var[Dict[str,Union[float,str,bool,dict]]]
    shape:rx.Var[literal_var_shape]
    tooltip:rx.Var[str]
    type:rx.Var[literal_var_type]

float_button = FloatButton.create

