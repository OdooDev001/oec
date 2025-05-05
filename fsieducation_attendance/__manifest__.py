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

{
    'name': 'FSI Education Attendance',
    'version': '18.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Attendances',
    'complexity': "easy",
    'author': 'FSI Inc',
    'website': 'https://fsibgroup.com/',
    'depends': ['fsieducation_timetable','fsieducation_core'],
    'data': [
        'security/fsi_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/fsi_attendance_register_views.xml',
        'views/fsi_attendance_sheet_views.xml',
        'views/fsi_attendance_line_views.xml',
        'views/fsi_attendance_type_views.xml',
        'views/fsi_attendance_session_views.xml',
        'views/fsi_student_views.xml',
        'views/fsi_menu.xml',
        'wizards/student_attendance_wizard_view.xml',
        'report/student_attendance_report.xml',
        'report/report_action.xml',
    ],
    'demo': [
        'demo/attendance_register_demo.xml',
        'demo/attendance_sheet_demo.xml',
        'demo/attendance_line_demo.xml',
        'demo/attendance_type_demo.xml',
    ],
    'images': [
        # 'static/description/fsieducation-attendance_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
