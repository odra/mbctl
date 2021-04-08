import json
from copy import copy

import pytest
import requests
import requests_mock
from terminaltables import AsciiTable

from mbctl import cli
from mblib import errors


@pytest.fixture
def mocked():
    return  [
        {
            "id": 11826,
            "name": "firefox",
            "owner": "kalev",
            "rebuild_strategy": "only-changed",
            "koji_tag": "module-firefox-stable-3420210402202719-dab6ca4c",
            "state_name": "ready",
            "state_reason": "Resubmitted by kalev",
            "stream": "stable"
        },
        {
            "id": 11825,
            "name": "astromenace",
            "owner": "kalev",
            "rebuild_strategy": "only-changed",
            "koji_tag": "module-astromenace-f33-3320210402201028-50ef3cd5",
            "state_name": "ready",
            "state_reason": "Resubmitted by kalev",
            "stream": "f33"
        }
    ]

@pytest.fixture
def mocked_text(mocked):
    output = []
    keys = ['ID', 'Name', 'Owner', 'Strategy', 'Koji Tag', 'Status', 'Reason','Stream']
    values = []
    for data in mocked:
        values.append([
            data['id'],
            data['name'],
            data['owner'],
            data['rebuild_strategy'],
            data['koji_tag'],
            data['state_name'],
            data['state_reason'],
            data['stream']
        ])
    
    return AsciiTable([keys] + values).table


@pytest.fixture
def mocked_json(mocked):
    return  [
        {
            "id": 11826,
            "name": "firefox",
            "owner": "kalev",
            "rebuild_strategy": "only-changed",
            "koji_tag": "module-firefox-stable-3420210402202719-dab6ca4c",
            "status": "ready",
            "reason": "Resubmitted by kalev",
            "stream": "stable"
        },
        {
            "id": 11825,
            "name": "astromenace",
            "owner": "kalev",
            "rebuild_strategy": "only-changed",
            "koji_tag": "module-astromenace-f33-3320210402201028-50ef3cd5",
            "status": "ready",
            "reason": "Resubmitted by kalev",
            "stream": "f33"
        }
    ]


def test_list_text(mocked, mocked_text):
    with requests_mock.Mocker() as m:
        m.get('https://mbs.fedoraproject.org/module-build-service/1/module-builds/',
            text=json.dumps({'items': mocked}))
        actual = cli.run(['list'])
    assert mocked_text == actual


def test_list_json(mocked, mocked_json):
    with requests_mock.Mocker() as m:
        m.get('https://mbs.fedoraproject.org/module-build-service/1/module-builds/',
            text=json.dumps({'items': mocked}))
        actual = json.loads(cli.run(['list', '-o', 'json']))
    
    for i in range(0, len(mocked_json)):
        assert mocked_json[i] == actual[i]


def test_list_error():
    with requests_mock.Mocker() as m, pytest.raises(errors.MBError):
        m.get('https://mbs.fedoraproject.org/module-build-service/1/module-builds/', exc=requests.exceptions.ConnectTimeout)
        cli.run(['list'])