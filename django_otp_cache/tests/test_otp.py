from django.test import TestCase

from django_otp_cache import one_time_password


class OTPTest(TestCase):

    def test_otp(self) -> None:
        otp = one_time_password.create('key')

        self.assertFalse(one_time_password.verify('key', '123', release_key_on_success=False))
        self.assertTrue(one_time_password.verify('key', otp, release_key_on_success=False))
        self.assertTrue(one_time_password.verify('key', otp))

        # otp has deleted from memory
        self.assertFalse(one_time_password.verify('key', otp))
