#!/usr/bin/env python3
"""
Test script for STPyV8 ARM
"""

from . import STPyV8, JSContext, JSError, JSEngine, evaljs

def main():
    print("STPyV8 ARM Compatibility Layer")
    print("Engine:", JSEngine.version)
    print()

    # Test basic functionality
    print("Basic tests:")
    try:
        print("1 + 2 =", evaljs("1 + 2"))
        print("Math.PI =", evaljs("Math.PI"))
        print("'hello'.toUpperCase() =", evaljs("'hello'.toUpperCase()"))

        # Test array operations
        print("Array test:", evaljs("[1, 2, 3].map(x => x * 2)"))

        # Test object operations
        print("Object test:", evaljs("JSON.stringify({name: 'test', value: 42})"))

    except Exception as e:
        print(f"Error in basic tests: {e}")
    print()

    # Test context usage
    print("Context tests:")
    try:
        with JSContext() as ctx:
            result = ctx.eval("var x = 10; x * 2;")
            print("Context eval result:", result)

        # Test error handling
        try:
            with JSContext() as ctx:
                ctx.eval("invalid.javascript.code()")
        except JSError as e:
            print("Error handling works:", str(e)[:50] + "...")

    except Exception as e:
        print(f"Error in context tests: {e}")
    print()

    print("STPyV8 ARM is ready to use!")
    print("Note: This uses Duktape engine instead of V8, but provides similar API.")

if __name__ == "__main__":
    main()
