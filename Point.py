class Point:

    def __init__(self, model_time, model_rpm, time_scale_factor, rpm_scale_factor, window_size):
        self.model_time = model_time
        self.model_rpm = model_rpm
        self.time_scale_factor = time_scale_factor
        self.rpm_scale_factor = rpm_scale_factor
        self.window_size = window_size

    def get_draw_x(self):
        return self.model_time * self.time_scale_factor

    def get_draw_y(self):
        return self.window_size - (self.model_rpm * self.rpm_scale_factor)
