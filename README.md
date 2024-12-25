# python-graphics-engine

To view a presentation on all the steps of this project, see the `presentation.pdf` file in this repository.
This project was developed under the excellent instruction, curriculum, and feedback of JonAlf Dyrland-Weaver.
Step 6 (extensions) of this project was developed via pair programming with Daphne Qin, current student at Rice University. This repository is forked from our originally submitted project repository.

To run this program, clone this repository and run `make` in your terminal. The output will be a graduation cap! Woohoo! This program uses custom `.mdl` files, which supply the instructions for the program to draw. All sample files are in `mdl_files`. To change which file is used, edit the second line of the makefile with the desired `.mdl` file. To write your own instructions for the program to draw something, see our list of implementations and the corresponding commands in `MDL.spec` :)

## Implementations
* Lines (implemented via Bresenham's Line Algorithm)
* Transformations (allow user to translate, dilate, and rotate the edges already present)
* Curves (circles, splines, hermite curves, bezier curves)
* 3D shapes (rectangular prisms, spheres, toruses, cylinders, hollow cylinders), colored and lighted via surface triangulation and scanline conversion
* Relative coordinate system (enables shape dependence and independence)
* Lighting (ambient and point)
* Reflection (diffuse and specular)
* Phong shading (always activated)
* Saved coordinate systems
 
Our added commands
* `cylinder`: takes parameters `x, y, z, r, h`, where `(x,y,z)` is the origin of the base of the bottom circle, `r` is the radius and `h` is the height. Height increases along `y`.
    * Usage: `cylinder [constants] x y z r h [coord_system]`
* `hollow_cylinder`: takes parameters `x, y, z, r0, r1, h`, where `(x,y,z)` is the origin of the base of the bottom circles, `r0` is the radius of the inner circle, `r1` is the radius of the outer circle, and `h` is the height. Height increases along `y`.
    * Usage: `hollow_cylinder [constants] x y z r0 r1 h [coord_system]`
* `save_coord_system`: takes one argument for the name of this saved stack, and saves the current stack of coordinate system. If a line, box, sphere, cylinder, hollow cylinder, or torus specifies the name of this saved coordinate system later on, then the top of that saved stack will be used, rather than the current coordinate system stack.
