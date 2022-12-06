import datetime
import os
from os.path import dirname, abspath
from time import sleep
import cv2
from testrunner.device_mgmt.device import Device
from testrunner.test.appium_test import AppiumTest
from testrunner.test.appium_test_step import AppiumTestStep

from Android.Screens.CommonActions.CommonActions import CommonActions, randomString
from Android.Screens.ListView_screen import ListView


def randomFileName():
    initial_time = datetime.datetime.now()
    return str(initial_time.strftime("%m_%d_%Y_%H_%M_%S"))


class MakeOutLineToElement(AppiumTestStep):
    ref_point = []
    crop = False
    actual_devices = ""

    def _runStep(self, **kwargs) -> None:
        expected_channel_name = "Channel1"

        def red_line(element):
            # filename = dirname(abspath(__file__)) + "\\" + str(datetime.datetime.now())
            # driver.save_screenshot(filename + ".png")
            filename = path + randomFileName() + ".png"
            driver.save_screenshot(filename)
            coordinates = common_code.coordinatesOfElement(element)
            image_path = filename
            x = coordinates[0]
            y = coordinates[1]
            h = coordinates[2]
            w = coordinates[3]
            image = cv2.imread(image_path)
            window_name = 'Image'
            # start_point = (5, 5)
            start_point = (x, y)

            # Ending coordinate, here (220, 220)
            # represents the bottom right corner of rectangle
            end_point = (x + h, y + w)

            # Blue color in BGR
            color = (0, 0, 225)

            # Line thickness of 2 px
            thickness = 8

            # Using cv2.rectangle() method
            # Draw a rectangle with blue line borders of thickness of 2 px
            image = cv2.rectangle(image, start_point, end_point, color, thickness)

            # Displaying the image

            # cv2.imshow('Original Image', image)
            cv2.waitKey(0)
            cv2.imwrite(image_path, image)

            cv2.destroyAllWindows()

        def green_line(element):
            # filename = dirname(abspath(__file__)) + "\\" + str(datetime.datetime.now())
            # driver.save_screenshot(filename + ".png")
            filename = path + randomFileName() + ".png"
            driver.save_screenshot(filename)
            coordinates = common_code.coordinatesOfElement(element)
            image_path = filename
            x = coordinates[0]
            y = coordinates[1]
            h = coordinates[2]
            w = coordinates[3]
            image = cv2.imread(image_path)
            window_name = 'Image'
            # start_point = (5, 5)
            start_point = (x, y)

            # Ending coordinate, here (220, 220)
            # represents the bottom right corner of rectangle
            end_point = (x + h, y + w)

            # Blue color in BGR
            color = (127, 255, 0)

            # Line thickness of 2 px
            thickness = 8

            # Using cv2.rectangle() method
            # Draw a rectangle with blue line borders of thickness of 2 px
            image = cv2.rectangle(image, start_point, end_point, color, thickness)

            # Displaying the image

            # cv2.imshow('Original Image', image)
            cv2.waitKey(0)
            cv2.imwrite(image_path, image)
            sleep(2)
            cv2.destroyAllWindows()

        driver: Device = self._getDiscoveredDevices()[0]
        log = self._log
        soft_assert = self._softAssert
        hard_assert = self._assert
        list_view = ListView(driver, log, soft_assert, hard_assert)
        common_code = CommonActions(driver, log, soft_assert, hard_assert)
        path = f"{dirname(dirname(abspath(__file__)))}\\ScreenShots\\"
        os.chdir(path)
        os.path.join(path, )
        for file in os.listdir():
            if file.endswith('.png') or file.endswith('.jpg'):
                os.remove(file)
        if list_view.channelsHeader("Channels"):
            green_line(list_view.headerValidation())
        else:
            red_line(list_view.headerValidation())

        if list_view.searchBoxButton():
            green_line(list_view.searchBoxButton())
        else:
            red_line(list_view.searchBoxButton())
        list_view.searchBox("ad4d")
        channel_name = list_view.channelName(1)
        if channel_name:
            if list_view.channelName(1).text == expected_channel_name:
                log('Channel Name is as expected')
                green_line(channel_name)
            else:
                soft_assert(False, "Channels name is not as expected")
                red_line(channel_name)
        else:
            soft_assert(False, "Channel name is not available")


class OutlineTheElementWithColor(AppiumTest):
    def __int__(self):
        self.dir_path = None

    # def _setup(self) -> None:
    #     self.dir_path =

    def _execute(self) -> None:
        MakeOutLineToElement()()
