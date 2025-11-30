#!/usr/bin/env python3
"""
Test script for STPyV8 ARM stub
"""

from . import STPyV8, JSContext, JSError, JSEngine, evaljs, STPyV8NotAvailableError

def main():
    print("STPyV8 ARM Stub")
    print("Engine:", JSEngine.version)
    print()

    # Test that stub raises exception
    print("Testing stub behavior:")
    try:
        evaljs("1 + 2")
    except STPyV8NotAvailableError as e:
        print("✓ evaljs() correctly raises exception:", str(e)[:60] + "...")
    except Exception as e:
        print("✗ Unexpected exception type:", type(e).__name__)

    try:
        with JSContext() as ctx:
            pass
    except STPyV8NotAvailableError as e:
        print("✓ JSContext() correctly raises exception:", str(e)[:60] + "...")
    except Exception as e:
        print("✗ Unexpected exception type:", type(e).__name__)

    print()
    print("STPyV8 is not available on ARM architecture.")
    print("This stub provides the same interface but raises exceptions when used.")

if __name__ == "__main__":
    main()
