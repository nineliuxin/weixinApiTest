from weixin.api.wework import WeWork


class TestToken(WeWork):
    def test_get_contact_token(self):
        r = self.get_contact_token()
        print(r)
        assert r != ""

    def test_get_client_token(self):
        r = self.get_client_token()
        print(r)
        assert r != ""

    def test_get_selfbulit_app_token(self):
        r = self.get_selfbulit_app_token()
        print(r)
        assert r != ""

    def test_get_basic_schedule_token(self):
        r = self.get_basic_schedule_token()
        print(r)
        assert r != ""

    def test_get_basic_meetingroom_token(self):
        r = self.get_basic_meetingroom_token()
        print(r)
        assert r != ""

    def test_get_basic_publiccall_token(self):
        r = self.get_basic_publiccall_token()
        print(r)
        assert r != ""

    def test_get_basic_live_token(self):
        r = self.get_basic_live_token()
        print(r)
        assert r != ""

    def test_get_basic_clockin_token(self):
        r = self.get_basic_clockin_token()
        print(r)
        assert r != ""

    def test_get_basic_approval_token(self):
        r = self.get_basic_approval_token()
        print(r)
        assert r != ""

    def test_get_basic_healthreport_token(self):
        r = self.get_basic_healthreport_token()
        print(r)
        assert r != ""

    def test_get_basic_businesspay_token(self):
        r = self.get_basic_businesspay_token()
        print(r)
        assert r != ""

