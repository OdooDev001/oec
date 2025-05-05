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


class TestExamCommon(common.TransactionCase):
    def setUp(self):
        super(TestExamCommon, self).setUp()
        self.fsi_exam = self.env['fsi.exam']
        self.fsi_exam_attendees = self.env['fsi.exam.attendees']
        self.fsi_exam_room = self.env['fsi.exam.room']
        self.fsi_exam_session = self.env['fsi.exam.session']
        self.fsi_exam_type = self.env['fsi.exam.type']
        self.fsi_grade_configuration = self.env['fsi.grade.configuration']
        self.fsi_marksheet_line = self.env['fsi.marksheet.line']
        self.fsi_marksheet_register = self.env['fsi.marksheet.register']
        self.fsi_res_partner = self.env['res.partner']
        self.fsi_result_line = self.env['fsi.result.line']
        self.fsi_result_template = self.env['fsi.result.template']
        self.fsi_held_exam = self.env['fsi.held.exam']
        self.fsi_room_distribution = self.env['fsi.room.distribution']
        self.student_hall_ticket = self.env['student.hall.ticket']
