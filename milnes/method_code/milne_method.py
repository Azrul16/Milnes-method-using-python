import numpy as np

def solve_ode_milne(f, t0, y0, t_end, h):
    def predictor(y0, y1, y2, y3, h):
        return y0 + 4*h*(2*f(t2, y2) - f(t1, y1) + 2*f(t0, y0))/3
    
    def corrector(y1, y2, y3, yp, h):
        return y1 + h*(f(t3, y3) + 4*f(t2, y2) + f(t1, y1) + f(t4, yp))/3

    t = np.arange(t0, t_end + h, h)
    y = np.zeros(t.shape)
    y[:4] = y0

    for i in range(3, len(t) - 1):
        yp = predictor(y[i-3], y[i-2], y[i-1], y[i], h)
        y[i+1] = corrector(y[i-2], y[i-1], y[i], yp, h)
    
    return t, y

def solve_fluid_velocity(v0, t_end, h):
    t0 = 0
    f = lambda t, v: 0.1 * v
    return solve_ode_milne(f, t0, v0, t_end, h)

def solve_spacecraft_position(y0, t_end, h):
    t0 = 0
    f = lambda t, y: -0.2 * y
    return solve_ode_milne(f, t0, y0, t_end, h)

def solve_pollutant_concentration(C0, t_end, h):
    t0 = 0
    f = lambda t, C: -0.05 * C
    return solve_ode_milne(f, t0, C0, t_end, h)

def solve_bacteria_population(N0, t_end, h):
    t0 = 0
    f = lambda t, N: 0.3 * N
    return solve_ode_milne(f, t0, N0, t_end, h)

def solve_financial_asset(V0, t_end, h):
    t0 = 0
    f = lambda t, V: 0.05 * V
    return solve_ode_milne(f, t0, V0, t_end, h)
