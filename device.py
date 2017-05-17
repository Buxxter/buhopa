#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

class Device(object):
    @property
    def is_on(self):
        return self._is_on()

    @property
    def state(self):
        return self._is_on()

    def __init__(self, name):
        super(Device, self).__init__()
        self._name = name
        self._state = 0
        self._last_state_dt = datetime.datetime.now()

    def on(self):
        pass

    def off(self):
        pass

    def _get_current_state(self):
        raise NotImplementedError

    def _is_on(self):
        return self._state != 0

    def start_watch


class Light(Device):
    def __init__(self, name):
        super(Light, self).__init__(name=name)


class LightDim(Light):
    def __init__(self, name, min_brightness = 0, max_brightness = 100):
        super(LightDim, self).__init__(name=name)
        self._min_bright = min_brightness
        self._max_bright = max_brightness
        self._cur_bright = self._min_bright

    def _is_on(self):
        return self._min_bright == self._cur_bright
