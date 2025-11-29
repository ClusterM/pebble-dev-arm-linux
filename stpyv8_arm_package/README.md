# STPyV8 ARM

This is a compatible replacement for STPyV8 that works on ARM processors. Since building the original STPyV8 (which uses Google V8 JavaScript engine) is extremely complex on ARM architecture, this package provides similar functionality using the lighter Duktape JavaScript engine via the `dukpy` library.

## Features

- Compatible API with STPyV8
- Works on ARM64 processors
- Uses Duktape engine (lighter than V8)
- Simple installation

## Installation

```bash
pip install .
```

Or install dependencies manually:
```bash
pip install dukpy
```

## Usage

```python
# Main import method (compatible with original STPyV8)
import STPyV8 as v8

# Basic usage
result = v8.evaljs("1 + 2")
print(result)  # 3

# Using JSContext (similar to original STPyV8)
with v8.JSContext() as ctx:
    result = ctx.eval("Math.PI * 2")
    print(result)  # 6.283185307179586

# Direct class imports
from STPyV8 import JSContext, JSError

try:
    with JSContext() as ctx:
        result = ctx.eval("some_invalid_code()")
except JSError as e:
    print(f"JavaScript error: {e}")
```

## Differences from original STPyV8

- Uses Duktape instead of V8 engine
- Some advanced V8-specific features may be unavailable
- Lower memory consumption
- Faster startup time

## Why this replacement?

Building STPyV8 from source requires:
1. Building Google V8 JavaScript engine from source
2. Managing complex build dependencies
3. Working with large V8 codebase and build system

On ARM processors, this process is especially complex due to:
- Cross-compilation difficulties
- Memory requirements for building V8
- Platform-specific optimizations

This replacement provides similar functionality with much simpler deployment.

## API compatibility

The package provides the following classes and functions compatible with STPyV8:

- `STPyV8.JSContext` - JavaScript execution context
- `STPyV8.JSError` - JavaScript exception
- `STPyV8.JSEngine` - Engine information
- `STPyV8.JSClass` - Decorator/metaclass for creating JavaScript-compatible classes
- `STPyV8.evaljs(code)` - Function for quick JavaScript execution

## Testing

```bash
# Run this file for testing
python -m STPyV8
```