import math


class Model:

    def __init__(self, ks, kv, ka):
        self._ks = ks
        self._kv = kv
        self._ka = ka
        self._A = -kv/ka
        self._B = 1/ka

    def get_velocity(self, velocity, voltage, dt):
        disc_A = math.e ** (self._A * dt)
        disc_B = (1/self._A) * (disc_A - 1) * self._B
        return disc_A * velocity + disc_B * voltage


    def get_rpm_scale_factor(self, window_size, max_voltage):
        return (window_size - 100)/(max_voltage/self._kv)
