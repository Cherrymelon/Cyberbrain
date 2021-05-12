"""Certain instructions can only be tested outside of a function."""

from cyberbrain import tracer, InitialValue, Deletion, Mutation, Symbol

x = 1

tracer.start()
del x  # DELETE_NAME
y: int
try:
    from xxx import *
except ImportError:
    pass

try:
    del aaa
except NameError:
    pass
tracer.stop()


def test_module():
    assert tracer.events == [
        InitialValue(target=Symbol("x"), value="1", lineno=-1),
        Deletion(target=Symbol("x"), lineno=8),
        InitialValue(target=Symbol("__annotations__"), value="{}", lineno=-1),
        Mutation(
            target=Symbol("__annotations__"),
            value='{"y":{"py/type":"builtins.int"}}',
            sources={
                Symbol("__annotations__")
            },  # `int` is a built-in so is excluded from sources.
            lineno=9,
        ),
    ]
