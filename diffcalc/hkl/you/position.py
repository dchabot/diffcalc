from math import pi

from diffcalc.util import AbstractPosition

TORAD = pi / 180
TODEG = 180 / pi


class YouPosition(AbstractPosition):

    def __init__(self, mu=None, delta=None, nu=None, eta=None, chi=None,
                 phi=None):
        self.mu = mu
        self.delta = delta
        self.nu = nu
        self.eta = eta
        self.chi = chi
        self.phi = phi

    def clone(self):
        return YouPosition(self.mu, self.delta, self.nu, self.eta, self.chi,
                           self.phi)

    def changeToRadians(self):
        self.mu *= TORAD
        self.delta *= TORAD
        self.nu *= TORAD
        self.eta *= TORAD
        self.chi *= TORAD
        self.phi *= TORAD

    def changeToDegrees(self):
        self.mu *= TODEG
        self.delta *= TODEG
        self.nu *= TODEG
        self.eta *= TODEG
        self.chi *= TODEG
        self.phi *= TODEG

    def totuple(self):
        return (self.mu, self.delta, self.nu, self.eta, self.chi, self.phi)

    def __str__(self):
        return ("YouPosition(mu %r delta: %r nu: %r eta: %r chi: %r  phi: %r)"
                % self.totuple())
