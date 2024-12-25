from display import *
from matrix import *
from gmath import *

vnormals = {}

def draw_scanline(x0, z0, x1, z1, y, screen, zbuffer, color):
    if x0 > x1:
        tx = x0
        tz = z0
        x0 = x1
        z0 = z1
        x1 = tx
        z1 = tz

    x = x0
    z = z0
    delta_z = (z1 - z0) / (x1 - x0 + 1) if (x1 - x0 + 1) != 0 else 0

    while x <= x1:
        plot(screen, zbuffer, color, x, y, z)
        x+= 1
        z+= delta_z

def scanline_convert(polygons, i, screen, zbuffer, color, view, ambient, light, symbols, reflect):
    global vnormals
    #print(len(vnormals))
    flip = False
    BOT = 0
    TOP = 2
    MID = 1

    points = [ (polygons[i][0], polygons[i][1], polygons[i][2]),
               (polygons[i+1][0], polygons[i+1][1], polygons[i+1][2]),
               (polygons[i+2][0], polygons[i+2][1], polygons[i+2][2]) ]

    # alas random color, we hardly knew ye
    #color = [0,0,0]
    #color[RED] = (23*(i/3)) %256
    #color[GREEN] = (109*(i/3)) %256
    #color[BLUE] = (227*(i/3)) %256

    points.sort(key = lambda x: x[1])

    # --- set initial values ---

    x0 = points[BOT][0]
    z0 = points[BOT][2]
    x1 = points[BOT][0]
    z1 = points[BOT][2]

    #figuring out normals
    pseudov = [points[BOT][0], points[BOT][1], points[BOT][2], 1.0] # adds a 1.0 to the point
    vertex = tuple(pseudov) # finds the key for vnormals
    throwaway = vnormals[vertex] # list, then deep copy
    n0 = [throwaway[0], throwaway[1], throwaway[2]]
    n1 = [throwaway[0], throwaway[1], throwaway[2]]
    # print("initial n0: " + str(n0))
    # print("initial n1: " + str(n1))

    y = int(points[BOT][1])

    # --- set value change increments ---

    distance0 = int(points[TOP][1]) - y * 1.0 + 1
    # print("distance0: " + str(distance0))
    distance1 = int(points[MID][1]) - y * 1.0 + 1
    distance2 = int(points[TOP][1]) - int(points[MID][1]) * 1.0 + 1

    dx0 = (points[TOP][0] - points[BOT][0]) / distance0 if distance0 != 0 else 0
    dz0 = (points[TOP][2] - points[BOT][2]) / distance0 if distance0 != 0 else 0
    dx1 = (points[MID][0] - points[BOT][0]) / distance1 if distance1 != 0 else 0
    dz1 = (points[MID][2] - points[BOT][2]) / distance1 if distance1 != 0 else 0

    nbot = vnormals[vertex]
    pseudov = [points[MID][0], points[MID][1], points[MID][2], 1.0]
    vertex = tuple(pseudov)
    nmid = vnormals[vertex]
    pseudov = [points[TOP][0], points[TOP][1], points[TOP][2], 1.0]
    vertex = tuple(pseudov)
    ntop = vnormals[vertex]

    # print("nbot: " + str(nbot));
    # print("nmid: " + str(nmid));
    # print("ntop: " + str(ntop));
    dnx0 = (ntop[0] - nbot[0]) / distance0 if distance0 != 0 else 0
    dny0 = (ntop[1] - nbot[1]) / distance0 if distance0 != 0 else 0
    dnz0 = (ntop[2] - nbot[2]) / distance0 if distance0 != 0 else 0

    #throwaway = [dnx0, dny0, dnz0]
    # print("bot-top slope: " + str(throwaway))

    dnx1 = (nmid[0] - nbot[0]) / distance1 if distance1 != 0 else 0
    dny1 = (nmid[1] - nbot[1]) / distance1 if distance1 != 0 else 0
    dnz1 = (nmid[2] - nbot[2]) / distance1 if distance1 != 0 else 0

    #throwaway = [dnx1, dny1, dnz1]
    # print("bot-mid slope: " +  str(throwaway))
    
    # --- iterate the two ends of the line ---
    while y <= int(points[TOP][1]):
        if ( not flip and y >= int(points[MID][1])): # switch to middle-top slope
            flip = True

            dx1 = (points[TOP][0] - points[MID][0]) / distance2 if distance2 != 0 else 0
            dz1 = (points[TOP][2] - points[MID][2]) / distance2 if distance2 != 0 else 0
            x1 = points[MID][0]
            z1 = points[MID][2]

            dnx1 = (ntop[0] - nmid[0]) / distance2 if distance2 != 0 else 0
            dny1 = (ntop[1] - nmid[1]) / distance2 if distance2 != 0 else 0
            dnz1 = (ntop[2] - nmid[2]) / distance2 if distance2 != 0 else 0

            #throwaway = [dnx1, dny1, dnz1]
            # print("mid-top slope: " +  str(throwaway))

            pseudov = [points[MID][0], points[MID][1], points[MID][2], 1.0]
            vertex = tuple(pseudov)
            throwaway = vnormals[vertex]
            n1 = [throwaway[0], throwaway[1], throwaway[2]]
            # print("new n1: " + str(n1));

        #draw_line(int(x0), y, z0, int(x1), y, z1, screen, zbuffer, color)

        # ====== iterate over the line
        #draw_scanline(int(x0), z0, int(x1), z1, y, screen, zbuffer, color)
        x0s = int(x0);
        z0s = z0;
        nx0s = n0[0]
        ny0s = n0[1]
        nz0s = n0[2]
        throwaway = [nx0s, ny0s, nz0s]
        # print("scanline 0: " + str(throwaway))
        x1s = int(x1);
        z1s = z1;
        ys = y;
        nx1s = n1[0]
        ny1s = n1[1]
        nz1s = n1[2]
        throwaway = [nx1s, ny1s, nz1s]
        # print("scanline 1: " + str(throwaway))
        
        if x0s > x1s:
            tx = x0s
            tz = z0s
            tnx = nx0s
            tny = ny0s
            tnz = nz0s

            x0s = x1s
            z0s = z1s
            nx0s = nx1s
            ny0s = ny1s
            nz0s = nz1s

            x1s = tx
            z1s = tz
            nx1s = tnx
            ny1s = tny
            nz1s = tnz

        xs = x0s
        zs = z0s
        nxs = nx0s
        nys = ny0s
        nzs = nz0s
        delta_z = (z1s - z0s) / (x1s - x0s + 1) if (x1s - x0s + 1) != 0 else 0
        # normal slopes
        delta_nx = (nx1s - nx0s) / (x1s - x0s + 1) if (x1s - x0s + 1) != 0 else 0
        delta_ny = (ny1s - ny0s) / (x1s - x0s + 1) if (x1s - x0s + 1) != 0 else 0
        delta_nz = (nz1s - nz0s) / (x1s - x0s + 1) if (x1s - x0s + 1) != 0 else 0

        while xs <= x1s:
            color = get_lighting([nxs, nys, nzs], view, ambient, light, symbols, reflect )

            plot(screen, zbuffer, color, xs, ys, zs)
            xs+= 1
            zs+= delta_z
            nxs += delta_nx
            nys += delta_ny
            nzs += delta_nz
            throwaway = [nxs, nys, nzs]
            # print("new iteration: " + str(throwaway));
        
        # ======
        x0+= dx0
        z0+= dz0

        n0[0] += dnx0
        n0[1] += dny0
        n0[2] += dnz0

        x1+= dx1
        z1+= dz1

        n1[0] += dnx1
        n1[1] += dny1
        n1[2] += dnz1
        # print("new n0: " + str(n0))
        # print("new n1: " + str(n1))
        y+= 1

def draw_polygons( polygons, screen, zbuffer, view, ambient, light, symbols, reflect):
    global vnormals

    if (len(polygons) < 3 and len(polygons > 0)):
        raise ValueError('Need at least 3 points to draw a polygon')
        return
    
    # creating or updating the value corresponding to each vertex in the vertex normal dictionary
    for point in range(0, len(polygons) - 2, 3):

        normal = calculate_normal(polygons, point)[:]
        
        vertex = tuple(polygons[point])
        if (vertex in vnormals):
            prev = [];
            prev.append(vnormals[vertex][0])
            prev.append(vnormals[vertex][1])
            prev.append(vnormals[vertex][2])
            prev[0] += normal[0]
            prev[1] += normal[1]
            prev[2] += normal[2]
            vnormals[vertex] = prev;
        else:
            vnormals[vertex] = normal

        vertex = tuple(polygons[point+1])
        if (vertex in vnormals):
            prev = [];
            prev.append(vnormals[vertex][0])
            prev.append(vnormals[vertex][1])
            prev.append(vnormals[vertex][2])
            prev[0] += normal[0]
            prev[1] += normal[1]
            prev[2] += normal[2]
            vnormals[vertex] = prev;
        else:
            vnormals[vertex] = normal

        vertex = tuple(polygons[point+2])
        if (vertex in vnormals):
            prev = [];
            prev.append(vnormals[vertex][0])
            prev.append(vnormals[vertex][1])
            prev.append(vnormals[vertex][2])
            prev[0] += normal[0]
            prev[1] += normal[1]
            prev[2] += normal[2]
            vnormals[vertex] = prev;
        else:
            vnormals[vertex] = normal
    
    # normalize
    for v in vnormals:
        normalize(vnormals[v]);

    for point in range(0, len(polygons) - 2, 3):
    #for point in range (27,30,3):
        normal = calculate_normal(polygons, point)[:]
        #print normal
        if normal[2] > 0:

            color = get_lighting(normal, view, ambient, light, symbols, reflect )
            scanline_convert(polygons, point, screen, zbuffer, color, view, ambient, light, symbols, reflect)

            # draw_line( int(polygons[point][0]),
            #            int(polygons[point][1]),
            #            polygons[point][2],
            #            int(polygons[point+1][0]),
            #            int(polygons[point+1][1]),
            #            polygons[point+1][2],
            #            screen, zbuffer, color)
            # draw_line( int(polygons[point+2][0]),
            #            int(polygons[point+2][1]),
            #            polygons[point+2][2],
            #            int(polygons[point+1][0]),
            #            int(polygons[point+1][1]),
            #            polygons[point+1][2],
            #            screen, zbuffer, color)
            # draw_line( int(polygons[point][0]),
            #            int(polygons[point][1]),
            #            polygons[point][2],
            #            int(polygons[point+2][0]),
            #            int(polygons[point+2][1]),
            #            polygons[point+2][2],
            #            screen, zbuffer, color)

def add_polygon( polygons, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(polygons, x0, y0, z0)
    add_point(polygons, x1, y1, z1)
    add_point(polygons, x2, y2, z2)


def add_box( polygons, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon(polygons, x, y, z, x1, y1, z, x1, y, z)
    add_polygon(polygons, x, y, z, x, y1, z, x1, y1, z)

    #back
    add_polygon(polygons, x1, y, z1, x, y1, z1, x, y, z1)
    add_polygon(polygons, x1, y, z1, x1, y1, z1, x, y1, z1)

    #right side
    add_polygon(polygons, x1, y, z, x1, y1, z1, x1, y, z1)
    add_polygon(polygons, x1, y, z, x1, y1, z, x1, y1, z1)
    #left side
    add_polygon(polygons, x, y, z1, x, y1, z, x, y, z)
    add_polygon(polygons, x, y, z1, x, y1, z1, x, y1, z)

    #top
    add_polygon(polygons, x, y, z1, x1, y, z, x1, y, z1)
    add_polygon(polygons, x, y, z1, x, y, z, x1, y, z)
    #bottom
    add_polygon(polygons, x, y1, z, x1, y1, z1, x1, y1, z)
    add_polygon(polygons, x, y1, z, x, y1, z1, x1, y1, z1)

def add_cylinder(polygons, cx, cy, cz, r, h, step):
    circles = generate_cylinder(cx, cy, cz, r, h, step)
    c_bottom = circles[0]
    c_top = circles[1]

    # top
    p0 = c_top[0]
    for i in range (1, step-1):
        p1 = c_top[i]
        p2 = c_top[i+1]
        add_polygon(polygons,
                    p0[0], p0[1], p0[2],
                    p1[0], p1[1], p1[2],
                    p2[0], p2[1], p2[2])
        
    # bottom
    p0 = c_bottom[0]
    for i in range (1, step-1):
        p1 = c_bottom[i+1]
        p2 = c_bottom[i]
        add_polygon(polygons,
                    p0[0], p0[1], p0[2],
                    p1[0], p1[1], p1[2],
                    p2[0], p2[1], p2[2])
        
    # curved sides
    for i in range (step):
        pb0 = c_bottom[i]
        pb1 = c_bottom[i+1]
        pt0 = c_top[i]
        pt1 = c_top[i+1]
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pt0[0], pt0[1], pt0[2],
                    pb0[0], pb0[1], pb0[2])
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pb0[0], pb0[1], pb0[2],
                    pb1[0], pb1[1], pb1[2])

def add_hollow_cylinder(polygons, cx, cy, cz, r0, r1, h, step):
    inner = generate_cylinder(cx, cy, cz, r0, h, step)
    outer = generate_cylinder(cx, cy, cz, r1, h, step)
    c_inner_bottom = inner[0]
    c_inner_top = inner[1]
    c_outer_bottom = outer[0]
    c_outer_top = outer[1]

    # top
    for i in range (step):
        po0 = c_outer_top[i]
        po1 = c_outer_top[i+1]
        pi0 = c_inner_top[i]
        pi1 = c_inner_top[i+1]
        add_polygon(polygons,
                    po0[0], po0[1], po0[2],
                    po1[0], po1[1], po1[2],
                    pi1[0], pi1[1], pi1[2])
        add_polygon(polygons,
                    po0[0], po0[1], po0[2],
                    pi1[0], pi1[1], pi1[2],
                    pi0[0], pi0[1], pi0[2])
    
    # bottom
    for i in range (step):
        po0 = c_outer_bottom[i+1]
        po1 = c_outer_bottom[i]
        pi0 = c_inner_bottom[i+1]
        pi1 = c_inner_bottom[i]
        add_polygon(polygons,
                    po0[0], po0[1], po0[2],
                    po1[0], po1[1], po1[2],
                    pi1[0], pi1[1], pi1[2])
        add_polygon(polygons,
                    po0[0], po0[1], po0[2],
                    pi1[0], pi1[1], pi1[2],
                    pi0[0], pi0[1], pi0[2])
    
    # curved OUTER sides
    for i in range (step):
        pb0 = c_outer_bottom[i]
        pb1 = c_outer_bottom[i+1]
        pt0 = c_outer_top[i]
        pt1 = c_outer_top[i+1]
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pt0[0], pt0[1], pt0[2],
                    pb0[0], pb0[1], pb0[2])
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pb0[0], pb0[1], pb0[2],
                    pb1[0], pb1[1], pb1[2])
    
    # curved INNER sides
    for i in range (step):
        pb0 = c_inner_bottom[i+1]
        pb1 = c_inner_bottom[i]
        pt0 = c_inner_top[i+1]
        pt1 = c_inner_top[i]
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pt0[0], pt0[1], pt0[2],
                    pb0[0], pb0[1], pb0[2])
        add_polygon(polygons,
                    pt1[0], pt1[1], pt1[2],
                    pb0[0], pb0[1], pb0[2],
                    pb1[0], pb1[1], pb1[2])
    

def generate_cylinder(cx, cy, cz, r, h, step):
    c_bottom = generate_circle(cx, cy, cz, r, step)
    c_top = generate_circle(cx, cy+h, cz, r, step)
    return [c_bottom, c_top]

def generate_circle(cx, cy, cz, r, step):
    points = []
    for i in range (step+1):
        t = (-1) * i / step
        x = r * math.cos(2 * math.pi * t) + cx
        y = cy
        z = r * math.sin(2 * math.pi * t) + cz
        points.append([x, y, z])
    return points


def add_sphere(polygons, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    step+= 1
    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt
            p1 = p0+1
            p2 = (p1+step) % (step * (step-1))
            p3 = (p0+step) % (step * (step-1))

            if longt != step - 2:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p1][0],
                             points[p1][1],
                             points[p1][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2])
            if longt != 0:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2],
                             points[p3][0],
                             points[p3][1],
                             points[p3][2])


def generate_sphere( cx, cy, cz, r, step ):
    points = []

    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop+1):
            circ = circle/float(step)

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
    return points

def add_torus(polygons, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt;
            if (longt == (step - 1)):
                p1 = p0 - longt;
            else:
                p1 = p0 + 1;
            p2 = (p1 + step) % (step * step);
            p3 = (p0 + step) % (step * step);

            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p3][0],
                        points[p3][1],
                        points[p3][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2] )
            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2],
                        points[p1][0],
                        points[p1][1],
                        points[p1][2] )


def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop):
            circ = circle/float(step)

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            points.append([x, y, z])
    return points


def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    i = 1

    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        i+= 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        i+= 1


def draw_lines( matrix, screen, zbuffer, color ):
    if (len(matrix) < 2 and len(matrix) > 0):
        raise ValueError('Need at least 2 points to draw an edge')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   matrix[point][2],
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   matrix[point+1][2],
                   screen, zbuffer, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )



def draw_line( x0, y0, z0, x1, y1, z1, screen, zbuffer, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        zt = z0
        x0 = x1
        y0 = y1
        z0 = z1
        x1 = xt
        y1 = yt
        z1 = zt

    x = x0
    y = y0
    z = z0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    wide = False
    tall = False

    if ( abs(x1-x0) >= abs(y1 - y0) ): #octants 1/8
        wide = True
        loop_start = x
        loop_end = x1
        dx_east = dx_northeast = 1
        dy_east = 0
        d_east = A
        distance = x1 - x + 1
        if ( A > 0 ): #octant 1
            d = A + B/2
            dy_northeast = 1
            d_northeast = A + B
        else: #octant 8
            d = A - B/2
            dy_northeast = -1
            d_northeast = A - B

    else: #octants 2/7
        tall = True
        dx_east = 0
        dx_northeast = 1
        distance = abs(y1 - y) + 1
        if ( A > 0 ): #octant 2
            d = A/2 + B
            dy_east = dy_northeast = 1
            d_northeast = A + B
            d_east = B
            loop_start = y
            loop_end = y1
        else: #octant 7
            d = A/2 - B
            dy_east = dy_northeast = -1
            d_northeast = A - B
            d_east = -1 * B
            loop_start = y1
            loop_end = y

    dz = (z1 - z0) / distance if distance != 0 else 0

    while ( loop_start < loop_end ):
        plot( screen, zbuffer, color, x, y, z )
        if ( (wide and ((A > 0 and d > 0) or (A < 0 and d < 0))) or
             (tall and ((A > 0 and d < 0) or (A < 0 and d > 0 )))):

            x+= dx_northeast
            y+= dy_northeast
            d+= d_northeast
        else:
            x+= dx_east
            y+= dy_east
            d+= d_east
        z+= dz
        loop_start+= 1
    plot( screen, zbuffer, color, x, y, z )