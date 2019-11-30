import json, requests
from danglaoshi.Common import Settings


class BaseApi(object):
    # url = ""
    base_url = Settings.API_TEST_BASE_URL

    def __init__(self):
        self.response = None

    # 拼接url地址
    def _get_url(self, custom_url):
        url = "{0}{1}".format(self.base_url, custom_url)
        return url

    def post(self, custom_url, data=None, header=None):
        if not custom_url:
            RuntimeError('url未指定')
        if not data:
            data = {}
        self.response = requests.post(url=self._get_url(custom_url), json=data, headers=header)
        return self.response

    # 获取http状态码
    def get_status_code(self):
        if self.response:
            return self.response.status_code

    # 获取返回参数中的状态码code
    def get_response_code(self):
        if self.response:
            return json.loads(self.response.text)['code']

    # 获取返回参数中的消息msg
    def get_response_msg(self):
        if self.response:
            return json.loads(self.response.text)['msg']

    # 获取返回参数中的数据data
    def get_response_data(self):
        if self.response:
            try:
                return json.loads(self.response.text)['data']
            except Exception as e:
                print(e)
                return None

    # 获取返回参数中的时间戳timestamp
    def get_response_timestamp(self):
        if self.response:
            return json.loads(self.response.text)['timestamp']

    '''
    def __init__(self, url_params=None):
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = self.base_url

    def _get_url(self):
        format_url = self.url.format(self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    def api_url(self):
        if not self.url:
            raise RuntimeError('未指定url')
        return self._get_url()

    # 所有接口共有的入参（sessionId、userId）
    def build_base_param(self):
        return {}

    # 除共有参数以外的参数
    def build_custom_param(self, data):
        return {}

    # 封装post请求
    def post(self, data=None):
        if not data:
            data = {}
        base_param = self.build_base_param()
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        self.response = requests.post(url=self.url, data=data)
        return self.response

    # 获取http状态码
    def get_status_code(self):
        if self.response:
            return self.response.status_code

    # 获取返回参数中的状态码code
    def get_response_code(self):
        if self.response:
            return json.load(self.response.text)['code']

    # 获取返回参数中的消息msg
    def get_response_msg(self):
        if self.response:
            return json.load(self.response.text)['msg']

    # 获取返回参数中的数据data
    def get_response_data(self):
        if self.response:
            return json.load(self.response.text)['data']

    # 获取返回参数中的时间戳timestamp
    def get_response_timestamp(self):
        if self.response:
            return json.load(self.response.text)['timestamp']
'''
