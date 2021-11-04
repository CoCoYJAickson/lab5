# Student Number 400422179, Xiaoyu Wu
# the second requirement need two cases to test
# one for main street color and main side signal color
# another for side street color and side signal color
# use two separate cases to make sure it is working as expected

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


class MainSignal():
    signalLight = ""

    def set_signal_light(self, color):
        return NotImplemented

    def check_signal_light(self):
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


class SideSignal():
    signalLight = ""

    def set_signal_light(self, color):
        return NotImplemented

    def check_signal_light(self):
        return NotImplemented


def test_case_two():
    main = MainTrafficLight()
    walking = MainSignal()
    color = "green"
    main.set_traffic_light(color)
    # Main Street Light should be green"
    assert main.check_traffic_light() == "green"
    # Main walking signal should be green"
    assert walking.check_signal_light() == "green"

def test_case_twoB():
    side = SideTrafficLight()
    walking_side = SideSignal()
    color = "red"
    side.set_traffic_light(color)
    # Side Street Light should be red
    assert side.check_traffic_light() == "red"
    # Side walking signal should be red
    assert walking_side.check_signal_light() == "red"
