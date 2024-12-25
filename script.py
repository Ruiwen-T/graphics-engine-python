import mdl
import copy
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,0,1]
    ambient = [50,50,50]
    light = [[0.5,0.75,1],[255,255,255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    for command in commands:
        #print(command)
        c = command['op']
        args = command['args']

        if c == 'box':
            if command['constants']:
                reflect = command['constants']
            add_box(tmp,
                    args[0], args[1], args[2],
                    args[3], args[4], args[5])
            #print(symbols[command['cs']][1][-1])
            #print(stack[-1])
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            #print(symbols)
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
            tmp = []
            reflect = '.white'
        elif c == 'cylinder':
            if command['constants']:
                reflect = command['constants']
            add_cylinder(tmp,
                         args[0], args[1], args[2], args[3], args[4], step_3d)
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
            tmp = []
            reflect = '.white'
        elif c == 'hollow_cylinder':
            if command['constants']:
                reflect = command['constants']
            add_hollow_cylinder(tmp,
                                args[0], args[1], args[2], args[3], args[4], args[5], step_3d)
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
            tmp = []
            reflect = '.white'
        elif c == 'sphere':
            if command['constants']:
                reflect = command['constants']
            add_sphere(tmp,
                       args[0], args[1], args[2], args[3], step_3d)
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
            tmp = []
            reflect = '.white'
        elif c == 'torus':
            if command['constants']:
                reflect = command['constants']
            add_torus(tmp,
                      args[0], args[1], args[2], args[3], args[4], step_3d)
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
            tmp = []
            reflect = '.white'
        elif c == 'line':
            add_edge(tmp,
                     args[0], args[1], args[2], args[3], args[4], args[5])
            if 'cs' in command and command['cs'] is not None:
                matrix_mult(symbols[command['cs']][1][-1], tmp)
            else:
                matrix_mult( stack[-1], tmp )
            draw_lines(tmp, screen, zbuffer, color)
            tmp = []
        elif c == 'move':
            tmp = make_translate(args[0], args[1], args[2])
            matrix_mult(stack[-1], tmp)
            stack[-1] = [x[:] for x in tmp]
            tmp = []
        elif c == 'scale':
            tmp = make_scale(args[0], args[1], args[2])
            matrix_mult(stack[-1], tmp)
            stack[-1] = [x[:] for x in tmp]
            tmp = []
        elif c == 'rotate':
            theta = args[1] * (math.pi/180)
            if args[0] == 'x':
                tmp = make_rotX(theta)
            elif args[0] == 'y':
                tmp = make_rotY(theta)
            else:
                tmp = make_rotZ(theta)
            matrix_mult( stack[-1], tmp )
            stack[-1] = [ x[:] for x in tmp]
            tmp = []
        elif c == 'push':
            stack.append([x[:] for x in stack[-1]] )
        elif c == 'pop':
            stack.pop()
        elif c == 'save_coord_system':
            throwaway = copy.deepcopy(stack)
            coord_sys_name = command['cs']
            if (not coord_sys_name in symbols):
                symbols[coord_sys_name] = ['coord_sys', []]
            symbols[coord_sys_name][1] = throwaway
        elif c == 'display':
            display(screen)
        elif c == 'save':
            save_extension(screen, args[0])
