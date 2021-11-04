from stubs_main_signal_light import MainSignal
from stubs_side_signal_light import SideSignal
from stubs_main_traffic_light import MainTrafficLight
from stubs_side_traffic_light import SideTrafficLight

# Student Number 400422179, Xiaoyu Wu
# These tests are designed for the three requirement, checking the color of light to find out if the code is
# working as the requirement or not. The set is enough for normal red test, without any exception tests.

def test_case_one():
    main = MainTrafficLight()
    side = SideTrafficLight()
    color = "green"
    main.set_traffic_light(color)
    # Main Street Light should be green"
    assert main.check_traffic_light() == "green"
    # Side walking signal should be green"
    assert side.check_traffic_light() == "red"


def test_case_two():
    main = MainTrafficLight()
    walking = MainSignal()
    color = "green"
    main.set_traffic_light(color)
    # Main Street Light should be green"
    assert main.check_traffic_light() == "green"
    # Main walking signal should be green"
    assert walking.check_signal_light() == "green"


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
