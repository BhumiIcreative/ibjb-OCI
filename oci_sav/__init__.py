# -*- coding: utf-8 -*-

from . import models


def pre_init_hook(env):
    record_question = env.ref("helpdesk.type_question", raise_if_not_found=False)
    record_incident = env.ref("helpdesk.type_incident", raise_if_not_found=False)
    if record_question:
        record_question.unlink()
    if record_incident:
        record_incident.unlink()
