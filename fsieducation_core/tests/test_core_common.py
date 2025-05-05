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


class TestCoreCommon(TransactionCase):
    def setUp(self):
        super(TestCoreCommon, self).setUp()
        self.fsi_batch = self.env['fsi.batch']
        self.fsi_faculty = self.env['fsi.faculty']
        self.fsi_course = self.env['fsi.course']
        self.res_company = self.env['res.users']
        self.fsi_student = self.env['fsi.student']
        self.hr_emp = self.env['hr.employee']
        self.subject_registration = self.env['fsi.subject.registration']
        self.fsi_update = self.env['publisher_warranty.contract']
        self.employ_wizard = self.env['wizard.fsi.faculty.employee']
        self.faculty_user_wizard = self.env['wizard.fsi.faculty']
        self.studnet_wizard = self.env['wizard.fsi.student']
