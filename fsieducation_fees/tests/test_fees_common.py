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
from odoo.tests import TransactionCase


class TestFeesCommon(TransactionCase):
    def setUp(self):
        super(TestFeesCommon, self).setUp()
        self.fsi_student_fees = self.env['fsi.student.fees.details']
        self.fsi_student = self.env['fsi.student']
        self.fsi_fees_wizard = self.env['fees.detail.report.wizard']
        self.fsi_fees_terms = self.env['fsi.fees.terms']
