#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# 加自定义的DoubleSlider


from PySide2 import QtWidgets, QtCore


class DoubleSlider(QtWidgets.QSlider):
    # create our our signal that we can connect to if necessary
    doubleValueChanged = QtCore.Signal(float)

    def __init__(self, parent=None, min=-99, max=99, decimals=2, *args, **kargs):
        super(DoubleSlider, self).__init__(*args, **kargs)
        if parent is not None:
            self.setParent(parent)
        self._multi = 10 ** decimals
        self.valueChanged.connect(self.emitDoubleValueChanged)

        self.setSingleStep(1)
        self.setMinimum(min)
        self.setMaximum(max)
        self.setOrientation(QtCore.Qt.Horizontal)

    def emitDoubleValueChanged(self):
        value = float(super(DoubleSlider, self).value()) / self._multi
        self.doubleValueChanged.emit(value)

    def value(self):
        return float(super(DoubleSlider, self).value()) / self._multi

    def setMinimum(self, value):
        return super(DoubleSlider, self).setMinimum(value * self._multi)

    def setMaximum(self, value):
        return super(DoubleSlider, self).setMaximum(value * self._multi)

    def setSingleStep(self, value):
        return super(DoubleSlider, self).setSingleStep(value * self._multi)

    def singleStep(self):
        return float(super(DoubleSlider, self).singleStep()) / self._multi

    def setValue(self, value):
        super(DoubleSlider, self).setValue(int(value * self._multi))
