# test_dueswitch.py (tests)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# Pylint skip this file because it wasn't created by EPA:
# pylint: skip-file
# Also disabling docstrings since this is not an EPA file
# py-lint: disable=C0301,W0611,R0903,C0103,C0114,C0115,C0116

"""Not an EPA File, Skipping Doc."""

# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# See COPYING file distributed along with the duecredit package for the
# copyright and license terms.

import atexit
# Note: Could not find a version that satisfies the requirement atexit.
import pytest

from ..injections.injector import DueCreditInjector
from ..dueswitch import DueSwitch, due


def test_dueswitch_activate(monkeypatch):
    """Not an EPA File, Skipping Doc."""
    if due.active:
        pytest.skip("due is already active, can't test more at this point")

    state = dict(activate=0, register=0, register_func=None)

    # Patch DueCreditInjector.activate.
    def activate_calls(*args, **kwargs):
        state["activate"] += 1

    monkeypatch.setattr(DueCreditInjector, "activate", activate_calls)

    # Patch atexit.register.
    def register(func):
        state["register"] += 1
        state["register_func"] = func

    monkeypatch.setattr(atexit, "register", register)

    due.activate()

    # Was not active, so should have called activate of the injector class.
    assert state["activate"] == 1
    assert state["register"] == 1
    assert state["register_func"] == due.dump


def test_a_bad_one():
    """Not an EPA File, Skipping Doc."""
    # We might get neither of those and should fail.
    # see https://github.com/duecredit/duecredit/issues/142
    # So let us through ValueError right away.
    pytest.raises(ValueError, DueSwitch, None, None, True)
