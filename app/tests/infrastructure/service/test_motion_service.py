import pytest
import settings
import responses

from infrastructure.service.motion_service import RealMotionService
from domain.enums.status import MotionDetectionStatus


@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_start__case_1():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/start'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection resumed\nDone \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_start(1) is True

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_start__case_2():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/start'.format(settings.MOTION_SERVER_IP),
        body='wtf',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_start(1) is False

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_stop__case_1():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/pause'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection paused\nDone \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_stop(1) is True

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_stop__case_2():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/pause'.format(settings.MOTION_SERVER_IP),
        body='wtf',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_stop(1) is False

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__get_detection_status__case_1():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/status'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection status ACTIVE \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.get_detection_status(1) == MotionDetectionStatus.enable

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__get_detection_status__case_2():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/status'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection status PAUSE \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.get_detection_status(1) == MotionDetectionStatus.disable

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_status__case_1():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/start'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection resumed\nDone \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_status(1, MotionDetectionStatus.enable) is True

@pytest.mark.in_memory
@responses.activate
def test_real_motion_service__set_detection_status__case_2():
    responses.add(
        responses.GET,
        'http://{}:7999/1/detection/pause'.format(settings.MOTION_SERVER_IP),
        body='Camera 1 Detection paused\nDone \n',
        status=200
    )

    svc = RealMotionService()
    assert svc.set_detection_status(1, MotionDetectionStatus.disable) is True