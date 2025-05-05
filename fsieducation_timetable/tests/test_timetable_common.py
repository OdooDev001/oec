# -*- coding: utf-8 -*-
###############################################################################
#
#    FSI Inc
#    Copyright (C) 2009-TODAY FSI Inc(<https://fsibgroup.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo.tests import common


class TestTimetableCommon(common.TransactionCase):
    def setUp(self):
        super(TestTimetableCommon, self).setUp()
        self.fsi_faculty = self.env['fsi.faculty']
        self.fsi_session = self.env['fsi.session']
        self.fsi_timing = self.env['fsi.timing']
        self.generate_timetable = self.env['generate.time.table']
        self.wizard_session = self.env['gen.time.table.line']
        self.timetable_report = self.env['time.table.report']
