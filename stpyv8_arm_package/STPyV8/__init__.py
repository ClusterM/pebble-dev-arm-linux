#!/usr/bin/env python3
"""
STPyV8 ARM - Stub for ARM processors

STPyV8 is not available for ARM architecture. This stub provides the same
interface but raises an exception when used, indicating that STPyV8 is not
available on ARM systems.
"""


class STPyV8NotAvailableError(Exception):
    """Raised when STPyV8 functionality is requested but not available"""
    pass


def _raise_not_available():
    """Raise exception indicating STPyV8 is not available"""
    raise STPyV8NotAvailableError(
        "STPyV8 is not available for ARM architecture. "
        "STPyV8 requires Google V8 JavaScript engine, which is not provided "
        "for ARM systems in this package."
    )


class JSContext:
    """JavaScript execution context stub"""

    def __init__(self, global_obj=None):
        _raise_not_available()

    def __enter__(self):
        _raise_not_available()

    def __exit__(self, exc_type, exc_val, exc_tb):
        _raise_not_available()

    def eval(self, code):
        """Evaluate JavaScript code"""
        _raise_not_available()


class JSError(Exception):
    """JavaScript execution error"""
    pass


class JSEngine:
    """JavaScript engine information stub"""
    version = "Not available on ARM"


class JSClass(type):
    """
    Metaclass/decorator stub for creating JavaScript-compatible Python classes.
    """

    def __new__(mcs, name_or_cls, bases=None, namespace=None, **kwargs):
        _raise_not_available()

    def __call__(cls, *args, **kwargs):
        _raise_not_available()


def evaljs(code):
    """Evaluate JavaScript code"""
    _raise_not_available()


# Create the main module interface
STPyV8 = type('STPyV8', (), {
    'JSContext': JSContext,
    'JSError': JSError,
    'JSEngine': JSEngine,
    'JSClass': JSClass,
    'evaljs': staticmethod(evaljs),
})()

# Make classes available at module level for direct import
__all__ = ['STPyV8', 'JSContext', 'JSError', 'JSEngine', 'JSClass', 'evaljs', 'STPyV8NotAvailableError']
