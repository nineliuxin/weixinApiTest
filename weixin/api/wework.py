import inspect
import logging

import yaml

from weixin.api.base_api import BaseApi


class WeWork(BaseApi):
    _token = dict()

    def get_contact_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_client_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    # test1
    def get_selfbulit_app_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    # 获取日程
    def get_basic_schedule_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_meetingroom_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_publiccall_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_live_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_clockin_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_approval_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_healthreport_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_basic_businesspay_token(self):
        r = self.get_token("../data/access_token.yml")
        return r

    def get_token(self, path):
        conf = yaml.safe_load(open(path))
        logging.debug(conf["token_info_list"])
        key = inspect.stack()[1].function
        token_name = conf['token_info_list']['corpsecret'][key]['token_name']
        url = conf['token_info_list']['token_url']
        if token_name not in self._token.keys():
            r = self.request("get", url,
                             params={
                                 "corpid": conf['token_info_list']['corpid'],
                                 "corpsecret": conf['token_info_list']['corpsecret'][key]['sercret']
                             }).json()
            self._token[token_name] = r['access_token']
        return self._token[token_name]


