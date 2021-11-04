# Student Number 400422179, Xiaoyu Wu
# the third requirement has nothing to do with walking signal, so we only need two class
# the factor we need to check including waiting time, color of each lights and traffic is clean or not.

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


def test_case_three():
    main = MainTrafficLight()
    side = SideTrafficLight()
    # check if the waiting time of side walk is bigger than 90 seconds
    if side.check_waiting_time() >= 90:
        # if it is, then check main light is red or not
        assert main.check_traffic_light() == "red"
        # if it is red, then wait for the side work traffic to clean
        if side.check_traffic_clean():
            # reset the waiting time
            side.set_waiting_time(0)
            # check if the waiting time after thr road is clean exceeds 30 seconds
            if side.check_waiting_time() >= 30:
                # check if the main road traffic light is green or not
                assert main.check_traffic_light() == "green"
    else:
        # check if the side traffic light is red
        assert side.check_traffic_light() == "red"
