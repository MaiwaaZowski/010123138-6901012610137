float a = 300;      // semi-major axis (pixels)
float e = 0.6;      // eccentricity
float T = 400;      // orbital period (frames)

float b, c, n;
float t = 0;

ArrayList<PVector> trail = new ArrayList<PVector>();
ArrayList<PVector> wedgePoints = new ArrayList<PVector>();
float wedgeInterval;
float lastWedgeTime = 0;

void setup() {
  size(900, 700);
  smooth();
  b = a * sqrt(1 - e * e);
  c = a * e;
  n = TWO_PI / T;
  wedgeInterval = T / 25.0;
}

float solveKepler(float M, float e) {
  float tol = 1e-6;
  int maxIter = 50;
  float E = (e < 0.8) ? M : PI;
  for (int i = 0; i < maxIter; i++) {
    float f = E - e * sin(E) - M;
    float fp = 1 - e * cos(E);
    float dE = f / fp;
    E -= dE;
    if (abs(dE) < tol) {
      break;
    }
  }
  return E;
}

PVector orbitPosition(float t) {
  float M = (n * t) % TWO_PI;
  float E = solveKepler(M, e);
  float x = a * cos(E) - c;
  float y = b * sin(E);
  return new PVector(x, y);
}

void drawSun(float x, float y, float r) {
  noStroke();
  for (int i = 4; i > 0; i--) {
    int alpha = 14 * (5 - i);
    fill(255, 185, 70, alpha);
    ellipse(x, y, r * 2 + i * 16, r * 2 + i * 16);
  }
  fill(255, 200, 80);
  ellipse(x, y, r * 2, r * 2);
  fill(255, 228, 150);
  ellipse(x - r * 0.15, y - r * 0.15, r * 1.1, r * 1.1);
}

void drawEarth(float x, float y, float r) {
  noStroke();
  fill(130, 190, 255, 70);
  ellipse(x, y, r * 2 + 6, r * 2 + 6);
  fill(40, 110, 200);
  ellipse(x, y, r * 2, r * 2);
  fill(75, 160, 95);
  pushMatrix();
  translate(x, y);
  ellipse(-r * 0.25, -r * 0.20, r * 0.95, r * 0.55);
  ellipse(r * 0.30, r * 0.15, r * 0.70, r * 0.45);
  ellipse(-r * 0.05, r * 0.45, r * 0.45, r * 0.30);
  popMatrix();
  fill(255, 255, 255, 60);
  ellipse(x - r * 0.35, y - r * 0.35, r * 0.5, r * 0.5);
}

void draw() {
  background(10, 10, 20);
  translate(width * 0.7, height / 2);

  // orbital ellipse
  stroke(80);
  noFill();
  beginShape();
  for (int i = 0; i <= 360; i++) {
    float ang = radians(i);
    vertex(a * cos(ang) - c, b * sin(ang));
  }
  endShape(CLOSE);

  // sun at the focus
  drawSun(0, 0, 17);

  // current planet position
  PVector p = orbitPosition(t);

  // equal-time wedges
  if (t - lastWedgeTime >= wedgeInterval) {
    wedgePoints.add(p.copy());
    lastWedgeTime = t;
    if (wedgePoints.size() > 2) {
      wedgePoints.remove(0);
    }
  }

  if (wedgePoints.size() == 2) {
    fill(80, 160, 255, 120);
    noStroke();
    beginShape();
    vertex(0, 0);
    vertex(wedgePoints.get(0).x, wedgePoints.get(0).y);
    vertex(wedgePoints.get(1).x, wedgePoints.get(1).y);
    endShape(CLOSE);
  }

  // trail
  trail.add(p.copy());
  if (trail.size() > 30) {
    trail.remove(0);
  }
  noFill();
  stroke(100, 200, 255);
  beginShape();
  for (PVector tp : trail) {
    vertex(tp.x, tp.y);
  }
  endShape();

  // planet
  drawEarth(p.x, p.y, 8);

  t += 1.0;

  // HUD
  resetMatrix();
  fill(255);
  textSize(14);
  text("Kepler's 2nd Law: equal areas in equal times", 20, 30);
  text("Watch the blue wedge -- it stays equal area even though its shape changes", 20, 50);
  text("Speed near Sun (perihelion) > speed far from Sun (aphelion)", 20, 70);
}

//6901012610137
//A1 Java