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
import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class FSIExam(models.Model):
    """FSI Exam Details"""
    _name = "fsi.exam"
    _inherit = "mail.thread"
    _description = "FSI Exam"

    session_id = fields.Many2one('fsi.exam.session', 'Exam Session',
                                 domain=[('state', 'not in',
                                          ['cancel', 'done'])])
    course_id = fields.Many2one(
        'fsi.course', related='session_id.course_id', store=True,
        readonly=True)
    batch_id = fields.Many2one(
        'fsi.batch', 'Batch', related='session_id.batch_id', store=True,
        readonly=True)
    subject_id = fields.Many2one('fsi.subject', 'Subject', required=True)
    exam_code = fields.Char('Exam Code', size=16, required=True)
    attendees_line = fields.One2many(
        'fsi.exam.attendees', 'exam_id', 'Attendees', readonly=True)
    start_time = fields.Datetime('Start Time', required=True)
    end_time = fields.Datetime('End Time', required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('schedule', 'Scheduled'), ('held', 'Held'),
         ('result_updated', 'Result Updated'),
         ('cancel', 'Cancelled'), ('done', 'Done')], 'State',
        readonly=True, default='draft', tracking=True)
    note = fields.Text('Note')
    responsible_id = fields.Many2many('fsi.faculty', string='Responsible')
    name = fields.Char('Exam', size=256, required=True)
    total_marks = fields.Integer('Total Marks', required=True)
    min_marks = fields.Integer('Passing Marks', required=True)
    active = fields.Boolean(default=True)
    attendees_count = fields.Integer(string='Attendees Count',
                                        compute='_compute_attendees_count')

    _sql_constraints = [
        ('unique_exam_code',
         'unique(exam_code)', 'Code should be unique per exam!')]

    @api.constrains('total_marks', 'min_marks')
    def _check_marks(self):
        """checking mark validation"""
        if self.total_marks <= 0.0 or self.min_marks <= 0.0:
            raise ValidationError(_('Enter proper marks!'))
        if self.min_marks > self.total_marks:
            raise ValidationError(_(
                "Passing Marks can't be greater than Total Marks"))

    @api.constrains('start_time', 'end_time')
    def _check_date_time(self):
        """Checking date validation"""
        session_start = datetime.datetime.combine(
            fields.Date.from_string(self.session_id.start_date),
            datetime.time.min)
        session_end = datetime.datetime.combine(
            fields.Date.from_string(self.session_id.end_date),
            datetime.time.max)
        start_time = fields.Datetime.from_string(self.start_time)
        end_time = fields.Datetime.from_string(self.end_time)
        if start_time > end_time:
            raise ValidationError(_('End Time cannot be set before Start Time.'))
        elif start_time < session_start or start_time > session_end or \
                end_time < session_start or end_time > session_end:
            raise ValidationError(
                _('Exam Time should in between Exam Session Dates.'))

    def open_exam_attendees(self):
        """action to view exam attendees"""
        return {
            "type": "ir.actions.act_window",
            "res_model": "fsi.exam.attendees",
            "domain": [("exam_id", "=", self.id)],
            "name": "Students",
            "view_mode": "list,form",
        }

    def _compute_attendees_count(self):
        """compute attendees count"""
        for record in self:
            record.attendees_count = self.env["fsi.exam.attendees"].search_count([("exam_id", "=", record.id)])

    @api.constrains('subject_id','start_time','end_time')
    def _check_overlapping_times(self):
        """checking validation"""
        for record in self:
            existing_exams = self.env['fsi.exam'].search([
                ('subject_id', '=', record.subject_id.id),
                ('id', '!=', record.id),
                ('start_time', '<', record.end_time),
                ('end_time', '>', record.start_time),
            ])
            if existing_exams:
                raise ValidationError(_('The exam time overlaps with an existing exam for the same subject.'))

    def action_result_updated(self):
        """Change the state to result_updated"""
        self.state = 'result_updated'

    def action_done(self):
        """Change the state to done"""
        self.state = 'done'

    def action_draft(self):
        """Change the state to draft"""
        self.state = 'draft'

    def action_cancel(self):
        """Change the state to cancel"""
        self.state = 'cancel'
