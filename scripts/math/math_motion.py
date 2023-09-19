# CLASS FOR EQUATIONS OF MOTION

# === list of functions/ methods ===
# final velocity (vf)
# displacement(no final velocity) (s) 
# displacement(no acc value) (s2) 
# acceleration (acc) 

# momentum (p) 
# impulse (*p) 
# potential energy (Ep) 
# kinetic energy (Ek) 
# power
# force (F) 
# weight (w) 
# force(big g) (f2) 
# ====================================


class Motion:
  def vf(vi, t, ac):
    velocity_final = (float(vi) * float(t)) + (float(ac) * float(t))
    return velocity_final

  def displacement1(vi, t, ac):
    displacement = (float(vi) * float(t)) + ((1/2) * (float(ac) * (float(t) ** 2)))
    return displacement

  def displacement2(vf, vi, t):
    s1 = (1/2) * (float(vf) - float(vi)) * float(t)
    return s1 

  def acceleration(vi, vf, t):
    delta_v = float(vf) - float(vi)
    acc = (delta_v) / (float(t))
    return acc 
  
  
  # ==============================
  # energy
  def p_energy(m, h):
      energy_potential = (float(m) * 9.81 * float(h))

  def k_energy(m, v):
    energy_kinetic = (1/2) * (float(m) * (float(v) ** 2))
    return energy_kinetic
  
  def momentum(mass, velocity):
    momentum = (mass * velocity)
    return momentum
  
  def impulse(f, t):
    impulse = (float(f) * float(t))
    return impulse 
  
  def power(work, time):
    power = (work//time)
    return power
  
  # ==============================

  def weight(m, g=9.81):
    w = (float(m) * g)
    return w 
  
  def force(m, a):
    f = float(m) * float(a)
    return f 
 
  # used for objects in space
  def force_big(m1, m2, r):
    big_g = (6.67 * (10 ** (-11)))
    force = (float(big_g)) * float(m1) * float(m2) / (float(r) ** 2)
    return force 
      
# *********************************