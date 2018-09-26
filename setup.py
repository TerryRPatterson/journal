from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('journal', base=base)
]

setup(name='Quest Log',
      version = '0.5',
      description = 'A program to save current life objectives.',
      options = dict(build_exe = buildOptions),
      executables = executables)
