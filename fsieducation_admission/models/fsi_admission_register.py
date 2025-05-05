# -*- coding: utf-8 -*-
###############################################################################
#
#    FSI Inc
#    Copyright (C) 2025-TODAY FSI Inc(<https://fsibgroup.com/>).
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
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class FSIAdmissionRegister(models.Model):
    _name = "fsi.admission.register"
    _inherit = "mail.thread"
    _description = "FSI Admission Register"
    _order = 'id DESC'

    name = fields.Char('Name', required=True, readonly=True, help="To Register the admission")
    start_date = fields.Date(
        'Start Date', required=True, readonly=True,
        default=fields.Date.today(),help="Start Date of Admission")
    end_date = fields.Date(
        'End Date', required=False, readonly=True,
        default=(fields.Date.today() + relativedelta(days=30)),help="End Date of Admission")
    course_id = fields.Many2one(
        'fsi.course', 'Course', readonly=True, tracking=True, help="Course Related to the Admission")
    min_count = fields.Integer(
        'Minimum No. of Admission', readonly=True, help="Minimum no. of applications for this admission")
    max_count = fields.Integer(
        'Maximum No. of Admission', readonly=True, default=30,  help="Maximum no. of applications for this admission")
    product_id = fields.Many2one(
        'product.product', 'Course Fees',
        domain=[('type', '=', 'service')], tracking=True, help="Course Fee")
    admission_ids = fields.One2many(
        'fsi.admission', 'register_id', 'Admissions')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'),
         ('cancel', 'Cancelled'), ('application', 'Application Gathering'),
         ('admission', 'Admission Process'), ('done', 'Done')],
        'Status', default='draft', tracking=True, help='States of the admission')
    active = fields.Boolean(default=True, help='To identify whether active or not')
    academic_years_id = fields.Many2one('fsi.academic.year',
                        'Academic Year', readonly=True,
                        tracking=True, help='Academic Year')
    academic_term_id = fields.Many2one('fsi.academic.term',
                                       'Terms', readonly=True,
                                       tracking=True)
    minimum_age_criteria = fields.Integer('Minimum Required Age(Years)', default=3)
    application_count = fields.Integer(string="Total_record", compute="compute_record_application")
    is_favorite = fields.Boolean(string="Is Favorite", default=False)
    company_id = fields.Many2one('res.company', string='Company',default=lambda self: self.env.user.company_id)
    draft_count = fields.Integer(compute="_compute_counts")
    confirm_count = fields.Integer(compute="_compute_counts")
    done_count = fields.Integer(compute="_compute_counts")
    online_count = fields.Integer(compute='_compute_application_counts')
    admission_base = fields.Selection([('program', 'Program'), ('course', 'Course')], default='course')
    program_id = fields.Many2one('fsi.program', string="Program", tracking=True)
    admission_fees_line_ids = fields.One2many('fsi.admission.fees.line', 'register_id', string='Admission Fees Configuration')

    @api.onchange('admission_base')
    def onchange_admission_base(self):
        """To change the values of some field based on admission_base field """
        if self.admission_base:
            if self.admission_base == 'program':
                self.course_id = None
                self.product_id = None
            else:
                self.program_id = None
                self.admission_fees_line_ids = None

    def _compute_counts(self):
        """Used to count values to some fields"""
        for record in self:
            draft_admissions = record.admission_ids.filtered(lambda a: a.state == 'draft')
            confirmed_admissions = record.admission_ids.filtered(lambda a: a.state == 'confirm')
            done_admissions = record.admission_ids.filtered(lambda a: a.state == 'done')
            record.draft_count = len(draft_admissions)
            record.confirm_count = len(confirmed_admissions)
            record.done_count = len(done_admissions)

    def _compute_application_counts(self):
        """To count draft_count and online_count values"""
        for record in self:
            record.draft_count = record.admission_ids.filtered(
                lambda a: a.state == 'draft').mapped('id').__len__()
            record.online_count = record.admission_ids.filtered(
                lambda a: a.state == 'online').mapped('id').__len__()

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        """To check the start date and end date conditions"""
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if end_date and start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

    @api.constrains('min_count', 'max_count')
    def check_no_of_admission(self):
        """ *** To check whether min count and max count is correct"""
        for record in self:
            if (record.min_count <= 0) or (record.max_count <= 0):
                raise ValidationError(
                    _("No of Admission should be positive!"))
            if record.min_count > record.max_count:
                raise ValidationError(_(
                    "Min Admission can't be greater than Max Admission"))

    def action_open_student_application(self):
        """To open student application record"""
        return {
            "type": "ir.actions.act_window",
            "res_model": "fsi.admission",
            "domain": [("register_id", "=", self.id)],
            "name": "Applications",
            "view_mode": "list,form",}

    def compute_record_application(self):
        """To count application_count"""
        self.application_count = self.env["fsi.admission"].search_count([("register_id", "=", self.id)])

    def action_confirm(self):
        """Change the state to confirm"""
        self.state = 'confirm'

    def action_draft(self):
        """Change the state to draft"""
        self.state = 'draft'

    def action_cancel(self):
        """Change the state to cancel"""
        self.state = 'cancel'

    def action_start_application(self):
        """Change the state to application"""
        self.state = 'application'

    def action_start_admission(self):
        """Change the state to admission"""
        self.state = 'admission'

    def action_close_register(self):
        """Change the state to done"""
        self.state = 'done'

    def action_open_draft_courses(self):
        """ *** """
        return {
            'name': 'Draft Admissions',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'fsi.admission',
            'domain': [
                ('id', 'in', self.admission_ids.ids),
                ('state', '=', 'draft'),
            ],
            'target': 'current',
        }

    def action_open_confirmed_courses(self):
        """ *** """
        return {
            'name': 'Confirmed Courses',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'fsi.admission',
            'domain': [('id', 'in', self.admission_ids.ids),('state', '=', 'confirm')],
            'target': 'current',
        }

    def action_open_enrolled_courses(self):
        """ *** """
        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'fsi.admission',
            'domain': [('id', 'in', self.admission_ids.ids),('state', '=', 'done')],
            'target': 'current',
        }

    def action_open_online_courses(self):
        """ *** """
        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'fsi.admission',
            'domain': [('id', 'in', self.admission_ids.ids),('state', '=', 'online')],
            'target': 'current',
        }
