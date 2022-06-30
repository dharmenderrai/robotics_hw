#!/usr/bin/env python
import math


class PID:

    def __init__(self, Kp, Ki=0.0, Kd=0.0):
        self.p_error = 0.0
        self.i_error = 0.0
        self.d_error = 0.0
        self.previous_cte = 0.0

        self.frame_threshold = 0
        self.current_frame = 0
        self.total_error = 0.0

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def UpdateError(self, cte):
        self.p_error = cte
        self.d_error = cte - self.previous_cte
        self.i_error += cte
        self.previous_cte = cte

    def TotalError(self):
        return self.Kp * self.p_error + self.Kd * self.d_error + self.Ki * self.i_error

    def CalculateSteering(self):
        steering_val = 0
        self.UpdatetotalError()
        steering_val = - (self.Kp * self.p_error) - (self.Kd * self.d_error) - (self.Ki * self.i_error)
        self.current_frame += 1
        return steering_val

    def UpdateTotalError(self):
        if self.current_frame > self.frame_threshold:
            self.total_error += self.p_error ** 2

    def GetTotalError(self):
        return self.total_error / self.current_frame

    def GetCurrentFrame(self):
        return self.current_frame