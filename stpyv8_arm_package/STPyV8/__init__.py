#!/usr/bin/env python3
"""
STPyV8 ARM - Compatibility layer for ARM processors
Uses Duktape engine via dukpy instead of V8 for easier ARM deployment

Original STPyV8 uses Google's V8 JavaScript engine, which is very complex to build on ARM.
This version provides similar functionality using the lighter Duktape engine.
"""

import dukpy

class JSContext:
    """JavaScript execution context, similar to STPyV8.JSContext"""

    def __init__(self, global_obj=None):
        self.global_obj = global_obj or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def eval(self, code):
        """Evaluate JavaScript code"""
        try:
            return dukpy.evaljs(code)
        except Exception as e:
            # Try to provide similar error format as STPyV8
            raise JSError(str(e))

class JSError(Exception):
    """JavaScript execution error"""
    pass

class JSEngine:
    """JavaScript engine information"""
    version = "Duktape via dukpy-0.5.0"

class JSClass(type):
    """
    Metaclass/decorator for creating JavaScript-compatible Python classes.
    
    Usage as decorator:
        @JSClass
        class MyClass:
            pass
    
    Usage as metaclass:
        class MyClass(metaclass=JSClass):
            pass
    """
    
    def __new__(mcs, name_or_cls, bases=None, namespace=None, **kwargs):
        """
        Create a new class with JSClass metaclass.
        Handles both decorator and metaclass usage.
        """
        # Check if this is being called as a decorator (first arg is a class)
        if bases is None and namespace is None and isinstance(name_or_cls, type):
            # Used as decorator: @JSClass
            original_cls = name_or_cls
            # Create a new class with JSClass as metaclass
            cls = super().__new__(mcs, original_cls.__name__, original_cls.__bases__, dict(original_cls.__dict__))
            cls._js_class = True
            return cls
        
        # Normal metaclass usage: JSClass(name, bases, namespace)
        cls = super().__new__(mcs, name_or_cls, bases, namespace)
        cls._js_class = True
        return cls
    
    def __call__(cls, *args, **kwargs):
        """Normal class instantiation"""
        return super().__call__(*args, **kwargs)

# Global functions similar to STPyV8
def evaljs(code):
    """Evaluate JavaScript code"""
    return dukpy.evaljs(code)

# Create the main module interface
STPyV8 = type('STPyV8', (), {
    'JSContext': JSContext,
    'JSError': JSError,
    'JSEngine': JSEngine,
    'JSClass': JSClass,
    'evaljs': staticmethod(evaljs),
})()

# Make classes available at module level for direct import
__all__ = ['STPyV8', 'JSContext', 'JSError', 'JSEngine', 'JSClass', 'evaljs']
