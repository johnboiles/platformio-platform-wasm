"""
    Builder for web assembly
"""

from SCons.Script import AlwaysBuild, Default, DefaultEnvironment

env = DefaultEnvironment()

env.Append(
    LINKFLAGS=["--bind"],
)

env.Replace(
    CXX='em++',
    CC='emcc',
    AR='emar',
    RANLIB='emranlib',
    PROGSUFFIX=".html"
)

#
# Target: Build wasm
#
target_bin = env.BuildProgram()

#
# Default targets
#
Default([target_bin])
