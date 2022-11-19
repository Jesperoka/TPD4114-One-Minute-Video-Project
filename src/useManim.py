# Allows for the use of Manim from any directory

# @param fileName file name of file calling this function
# @param manimDirectory path to directory where manim is installed
# @param
def runManim(fileName: str, manimDirectory: str, className: str):
    from os import chdir, system
    from os.path import abspath
    from sys import path
    absfilePath = abspath(fileName)
    path.append(absfilePath)
    command = "manimgl "+absfilePath+" "+className
    chdir(manimDirectory)
    system(command)