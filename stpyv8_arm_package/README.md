# STPyV8 ARM Stub

This is a stub package for STPyV8 on ARM processors. STPyV8 (which uses Google V8 JavaScript engine) is not available for ARM architecture, so this package provides the same interface but raises an exception when used.

## Purpose

This stub allows code that imports STPyV8 to work without modification, but clearly indicates that STPyV8 functionality is not available on ARM systems. When any STPyV8 functionality is accessed, a `STPyV8NotAvailableError` exception is raised.

## Installation

```bash
pip install .
```

No additional dependencies are required.

## Usage

```python
# Main import method (compatible with original STPyV8)
import STPyV8 as v8

# Any attempt to use STPyV8 will raise an exception
try:
    result = v8.evaljs("1 + 2")
except STPyV8.STPyV8NotAvailableError as e:
    print(f"STPyV8 is not available: {e}")

# Same for JSContext
try:
    with v8.JSContext() as ctx:
        result = ctx.eval("Math.PI * 2")
except STPyV8.STPyV8NotAvailableError as e:
    print(f"STPyV8 is not available: {e}")

# Direct class imports also work
from STPyV8 import JSContext, JSError, STPyV8NotAvailableError

try:
    with JSContext() as ctx:
        result = ctx.eval("some_code()")
except STPyV8NotAvailableError as e:
    print(f"STPyV8 is not available: {e}")
```

## Why a stub?

Building STPyV8 from source requires:
1. Building Google V8 JavaScript engine from source
2. Managing complex build dependencies
3. Working with large V8 codebase and build system

On ARM processors, this process is especially complex due to:
- Cross-compilation difficulties
- Memory requirements for building V8
- Platform-specific optimizations

This stub provides the same interface as STPyV8, allowing code to import it without errors, but clearly indicates that the functionality is not available on ARM systems.

## API compatibility

The package provides the following classes and functions compatible with STPyV8:

- `STPyV8.JSContext` - JavaScript execution context (raises exception when instantiated)
- `STPyV8.JSError` - JavaScript exception class
- `STPyV8.JSEngine` - Engine information stub
- `STPyV8.JSClass` - Decorator/metaclass stub (raises exception when used)
- `STPyV8.evaljs(code)` - Function stub (raises exception when called)
- `STPyV8.STPyV8NotAvailableError` - Exception raised when STPyV8 functionality is requested

## Testing

```bash
# Run this file for testing
python -m STPyV8
```