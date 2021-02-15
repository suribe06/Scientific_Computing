def euler(f,t0,t,yk,h):
    y_vector = [yk]
    tk = t0 + h
    while tk <= t:

        yk += f(tk,yk)*h
        y_vector.append(yk)
        tk += h

    return y_vector

def taylor(f,ft,fy,t0,t,yk,h):
    y_vector = []
    tk = t0
    while tk <= t:
        y_dx = f(tk,yk)
        y_2dx = ft(tk,yk) + fy(tk,yk)*f(tk,yk)
        y_vector.append(yk)
        yk+= y_dx*h + (y_2dx/2)*h**2
        tk+=h
    return y_vector

def rungekutta2(f,t0,t,yk,h):
    y_vector = []
    tk = t0
    while tk <= t:
        k1 = f(tk,yk)*h
        k2 = f(tk+h,yk+k1)*h
        y_vector.append(yk)
        yk += (1/2)*(k1+k2)
        tk+=h
    return y_vector

def rungekutta4(f,t0,t,yk,h):
    y_vector = []
    tk = t0
    while tk <= t:
        k1 = f(tk,yk)*h
        k2 = f(tk+(h/2),yk+(k1/2))*h
        k3 = f(tk+(h/2),yk+(k2/2))*h
        k4 = f(tk+h, yk+k3)*h
        y_vector.append(yk)
        yk += (1/6)*(k1+2*k2+2*k3+k4)
        tk+=h
    return y_vector


def multipaso2(f,t,yk,h, y_vector,tk):
    while tk <= t:
        tk1 =  tk-h
        y_vector.append(yk)
        yk += (1/2)*((3*f(tk,yk))-(f(tk1,y_vector[-1])))*h
        tk += h
    return y_vector

def multipasoAB(f,t,yk,h, y_vector,tk):
    while tk <= t:
        tk1 =  tk-h
        tk2 = tk1-h
        tk3 = tk2-h
        ec1 = (55*f(tk,yk))
        ec2 = (59*f(tk1,y_vector[-1]))
        ec3 = (37*f(tk2,y_vector[-2]))
        ec4 = (9*f(tk3,y_vector[-3]))
        y_vector.append(yk)
        yk += (1/24)*(ec1-ec2+ec3-ec4)*h
        tk += h
    return y_vector
