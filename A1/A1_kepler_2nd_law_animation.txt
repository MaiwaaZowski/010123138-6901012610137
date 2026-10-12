import math
# ---------- Orbit parameters (tweak these) ----------
a = 300.0        # semi-major axis (pixels)
e = 0.6          # eccentricity (0 = circle, closer to 1 = more elongated)
T = 400          # orbital period (frames)
# ---------- Derived quantities ----------
b = a * math.sqrt(1 - e * e)    # semi-minor axis
c = a * e                       # distance from center to focus (where the Sun sits)
n = 2 * math.pi / T             # mean motion (constant rate of mean anomaly)
t = 0.0                         # time (frames elapsed)
# For visualizing equal-area sweeps: store recent positions to draw wedges
trail = []
wedge_interval = T / 25.0       # sweep a new "equal time" wedge this often
last_wedge_time = 0.0
wedge_points = []               # list of (x,y) marking wedge boundaries

def setup():
    size(900, 700)
    smooth()

def solve_kepler(M, e, tol=1e-6, max_iter=50):
    # Newton-Raphson solve for E in: M = E - e*sin(E)
    E = M if e < 0.8 else math.pi  # decent initial guess
    for i in range(max_iter):
        f  = E - e * math.sin(E) - M
        fp = 1 - e * math.cos(E)
        dE = f / fp
        E -= dE
        if abs(dE) < tol:
            break
    return E

def orbit_position(t):
    M = (n * t) % (2 * math.pi)         # mean anomaly, advances uniformly
    E = solve_kepler(M, e)              # eccentric anomaly, NOT uniform
    x = a * math.cos(E) - c             # focus (Sun) is at origin (0,0)
    y = b * math.sin(E)
    return x, y

# ---------- Minimal, flat-style bodies (no images needed) ----------
def draw_sun(x, y, r):
    noStroke()
    # soft outward glow: a few translucent rings, largest+faintest first
    for i in range(4, 0, -1):
        a_alpha = 14 * (5 - i)
        fill(255, 185, 70, a_alpha)
        ellipse(x, y, r * 2 + i * 16, r * 2 + i * 16)
    # solid core
    fill(255, 200, 80)
    ellipse(x, y, r * 2, r * 2)
    # slightly brighter inner highlight, off-center for a touch of depth
    fill(255, 228, 150)
    ellipse(x - r * 0.15, y - r * 0.15, r * 1.1, r * 1.1)

def draw_earth(x, y, r):
    noStroke()
    # thin atmosphere halo
    fill(130, 190, 255, 70)
    ellipse(x, y, r * 2 + 6, r * 2 + 6)
    # ocean base
    fill(40, 110, 200)
    ellipse(x, y, r * 2, r * 2)
    # a couple of simplified, static "continent" blobs
    fill(75, 160, 95)
    pushMatrix()
    translate(x, y)
    ellipse(-r * 0.25, -r * 0.20, r * 0.95, r * 0.55)
    ellipse(r * 0.30, r * 0.15, r * 0.70, r * 0.45)
    ellipse(-r * 0.05, r * 0.45, r * 0.45, r * 0.30)
    popMatrix()
    # small bright highlight for a subtle "lit sphere" feel
    fill(255, 255, 255, 60)
    ellipse(x - r * 0.35, y - r * 0.35, r * 0.5, r * 0.5)

def draw():
    global t, last_wedge_time, wedge_points
    background(10, 10, 20)
    translate(width*.7, height/2)

    # --- draw the orbital ellipse (path), focus at origin ---
    stroke(80)
    noFill()
    beginShape()
    for i in range(361):
        E = radians(i)
        ex = a * cos(E) - c
        ey = b * sin(E)
        vertex(ex, ey)
    endShape(CLOSE)

    # --- draw the Sun at the focus ---
    draw_sun(0, 0, 17)

    # --- current planet position ---
    px, py = orbit_position(t)

    # --- record equal-time wedges to visually prove equal-area law ---
    if t - last_wedge_time >= wedge_interval:
        wedge_points.append((px, py))
        last_wedge_time = t
        if len(wedge_points) > 2:
            wedge_points.pop(0)

    # draw the most recent swept wedge (Sun -> p1 -> p2)
    if len(wedge_points) == 2:
        fill(80, 160, 255, 120)
        noStroke()
        beginShape()
        vertex(0, 0)
        vertex(wedge_points[0][0], wedge_points[0][1])
        vertex(wedge_points[1][0], wedge_points[1][1])
        endShape(CLOSE)

    # --- trail ---
    trail.append((px, py))
    if len(trail) > 30:
        trail.pop(0)
    noFill()
    stroke(100, 200, 255)
    beginShape()
    for (tx, ty) in trail:
        vertex(tx, ty)
    endShape()

    # --- planet (Earth) ---
    draw_earth(px, py, 8)

    # --- advance time ---
    t += 1.0

    # --- HUD ---
    resetMatrix()
    fill(255)
    textSize(14)
    text("Kepler's 2nd Law: equal areas in equal times", 20, 30)
    text("Watch the blue wedge -- it stays equal area even though its shape changes", 20, 50)
    text("Speed near Sun (perihelion) > speed far from Sun (aphelion)", 20, 70)

#6901012610137
#A1