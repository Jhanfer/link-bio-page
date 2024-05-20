import reflex as rx
from typing import Any, Dict, List, Optional, Set, Union

class FloatButton(rx.Component):
    library="antd"
    tag="FloatButton"

    icon=rx.image(src="/icons/mug-hot-solid.svg")
    href:rx.Var[str]
    target:rx.Var[str]
    badge:rx.Var[Dict[str,Union[float,str,bool,dict]]]
    shape:rx.Var[str]

float_button = FloatButton.create

