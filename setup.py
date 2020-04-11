import cx_Freeze

executables = [cx_Freeze.Executable("/media/hadi/laban/vstudioProjects/SNAKE/SNAKE.py")]

cx_Freeze.setup(
    name="SNAKE",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )
