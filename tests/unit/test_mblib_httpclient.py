import pytest
import requests
import requests_mock

from mblib import errors, httpclient


def test_request_no_auth():
  c = httpclient.Client('https://mbs.fedoraproject.org/module-build-service/1')
  with requests_mock.Mocker() as m:
    m.get('https://mbs.fedoraproject.org/module-build-service/1/', text='foo')
    code, res = c.request('/')

  assert code == 200
  assert res == 'foo'


def test_request_krb_auth(mocker):
  #TODO: find a better way to mock kerberos
  class HTTPKerberosAuth(httpclient.HTTPKerberosAuth):
    def handle_response(self, response, **kwargs):
      return response

  mocker.patch('mblib.httpclient.HTTPKerberosAuth', new=HTTPKerberosAuth)

  krb_auth = httpclient.KRBAuth(principal='local@DOMAIN.COM')
  c = httpclient.Client('https://mbs.fedoraproject.org/module-build-service/1', auth=krb_auth)
  with requests_mock.Mocker() as m:
    m.get('https://mbs.fedoraproject.org/module-build-service/1/', text='foo')
    code, res = c.request('/')

  assert code == 200
  assert res == 'foo'


def test_request_exception():
  c = httpclient.Client('https://mbs.fedoraproject.org/module-build-service/1')
  with requests_mock.Mocker() as m, pytest.raises(errors.MBError):
    m.get('https://mbs.fedoraproject.org/module-build-service/1/', exc=requests.exceptions.ConnectTimeout)
    code, res = c.request('/')


def test_custom_base_url():
  c = httpclient.Client('https://foo.bar')
  with requests_mock.Mocker() as m:
    m.get('https://foo.bar', text='foobar')
    code, res = c.request('/')

  assert code == 200
  assert res == 'foobar'
