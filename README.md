# Web Assembly: development platform for [PlatformIO](http://platformio.org)

Web assembly development platform builds html/js/wasm using Emscripten. Emscripten must be installed and available in `PATH` at build time.

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Usage

```ini
[env:wasm]
platform = https://github.com/johnboiles/platformio-platform-wasm.git
lib_compat_mode = off # Allow libs not set up for this platform
...
```
