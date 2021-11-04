# Student Number 400422179, Xiaoyu Wu
# check two different traffic light to see if the requirement is met
# which needs two lights to be different colors.

class MainTrafficLight():
    trafficLight = "green"
    time = 0

    def set_traffic_light(self, color):
        return NotImplemented

    def check_traffic_light(self):
        return NotImplemented

    def check_signal_light(self):
        return NotImplemented

    def check_waiting_time(self):
        return NotImplemented


class SideTrafficLight():
    trafficLights = "red"
    time = 0

    def set_traffic_light(self, color):
        return NotImplemented

    def check_traffic_light(self):
        return NotImplemented

    def check_signal_light(self):
        return NotImplemented

    def check_waiting_time(self):
        return NotImplemented

    def check_traffic_clean(self):
        return NotImplemented

    def set_waiting_time(self, time):
        return NotImplemented


def test_case_one():
    main = MainTrafficLight()
    side = SideTrafficLight()
    color = "green"
    main.set_traffic_light(color)
    # Main Street Light should be green"
    assert main.check_traffic_light() == "green"
    # Side walking signal should be green"
    assert side.check_traffic_light() == "red"
