from __future__ import unicode_literals

from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewPublishedEmailHook

class MyReviewPublishedEmailHook(ReviewPublishedEmailHook):
    def get_to_field(self, to_field, review, user, review_request):
        return to_field

    def get_cc_field(self, cc_field, review, user, review_request):
        return cc_field


class EmailHookExt(Extension):
    metadata = {
        'Name': 'EmailHookExt',
    }

    def initialize(self):
        MyReviewPublishedEmailHook(self)
