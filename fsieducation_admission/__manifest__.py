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
    'name': "FSI Education Admission",
    'version': '18.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    'sequence': 3,
    'summary': "Manage Admissions""",
    'complexity': "easy",
    'author': 'FSI Inc',
    'website': 'https://fsibgroup.com/',
    'depends': [
        'fsieducation_core',
        'fsieducation_fees'
    ],
    'data': [
        'security/fsi_admission_security.xml',
        'security/ir.model.access.csv',
        'data/admission_sequence.xml',
        'data/parameter_data.xml',
        'views/fsi_admission_register_views.xml',
        'views/fsi_admission_views.xml',
        'views/fsi_student_course_views.xml',
        'views/res_config_settings_views.xml',
        'views/fsi_menu_views.xml',
        'report/report_admission_analysis.xml',
        'report/report_action.xml',
        'wizard/admission_analysis_wizard_view.xml',
    ],
    'demo': [
        'demo/admission_register_demo.xml',
        'demo/admission_demo.xml',
    ],
    'test': [],
    'images': [
        # 'static/description/fsieducation-admission_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
