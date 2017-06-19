# -*- coding: utf8 -*-
#
#  Copyright (c) 2017 unfoldingWord
#  http://creativecommons.org/licenses/MIT/
#  See LICENSE file for details.
#
#  Contributors:
#  Richard Mahn <richard_mahn@wycliffeassociates.org>
#  Joel Lonbeck <joel@neutrinographics.com>

import boto3

from boto3.session import Session


class SESHandler(object):
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, aws_region_name='us-west-2'):
        if aws_access_key_id and aws_secret_access_key:
            session = Session(aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              region_name=aws_region_name)
            self.client = session.client('ses')
        else:
            self.client = boto3.client('ses')

    def send_email(self, **kwargs):
        return self.client.send_email(**kwargs)
