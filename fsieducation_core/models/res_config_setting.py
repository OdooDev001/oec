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

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_fsieducation_activity = fields.Boolean(string="Activity")
    module_fsieducation_facility = fields.Boolean(string="Facility")
    module_fsieducation_parent = fields.Boolean(string="Parent")
    module_fsieducation_assignment = fields.Boolean(string="Assignment")
    module_fsieducation_classroom = fields.Boolean(string="Classroom")
    module_fsieducation_fees = fields.Boolean(string="Fees")
    module_fsieducation_admission = fields.Boolean(string="Admission")
    module_fsieducation_timetable = fields.Boolean(string="Timetable")
    module_fsieducation_exam = fields.Boolean(string="Exam")
    module_fsieducation_library = fields.Boolean(string="Library")
    module_fsieducation_attendance = fields.Boolean(string="Attendance")
    module_fsieducation_quiz = fields.Boolean(string="Quiz Enterprise")
    module_fsieducation_discipline = fields.Boolean(
        string="Discipline Enterprise")
    module_fsieducation_health_enterprise = fields.Boolean(
        string="Health Enterprise")
    module_fsieducation_achievement_enterprise = fields.Boolean(
        string="Achievement Enterprise")
    module_fsieducation_activity_enterprise = fields.Boolean(
        string="Activity Enterprise")
    module_fsieducation_admission_enterprise = fields.Boolean(
        string="Admission Enterprise")
    module_fsieducation_alumni_enterprise = fields.Boolean(
        string="Alumni Enterprise")
    module_fsieducation_alumni_blog_enterprise = fields.Boolean(
        string="Alumni Blog Enterprise")
    module_fsieducation_alumni_event_enterprise = fields.Boolean(
        string="Alumni Event Enterprise")
    module_fsieducation_alumni_job_enterprise = fields.Boolean(
        string="Alumni Job Enterprise")
    module_fsieducation_job_enterprise = fields.Boolean(
        string="Job Enterprise")
    module_fsieducation_assignment_enterprise = fields.Boolean(
        string="Assignment Enterprise")
    module_fsieducation_assignment_rubrics = fields.Boolean(
        string="Assignment Rubrics")
    module_fsieducation_attendance_enterprise = fields.Boolean(
        string="Attendance Enterprise")
    module_fsieducation_student_attendance_enterprise = fields.Boolean(
        string="Student Attendance Kiosk")
    module_bigbluebutton = fields.Boolean(
        string="Bigbluebutton Enterprise")
    module_fsieducation_campus_enterprise = fields.Boolean(
        string="Campus Enterprise")
    module_fsieducation_classroom_enterprise = fields.Boolean(
        string="Classroom Enterprise")
    module_fsieducation_exam_enterprise = fields.Boolean(
        string="Exam Enterprise")
    module_fsieducation_facility_enterprise = fields.Boolean(
        string="Facility Enterprise")
    module_fsieducation_fees_plan = fields.Boolean(
        string="Fees Plan")
    module_fsieducation_fees_parent_bridge = fields.Boolean(
        string="Fees Parent Bridge")
    module_fsieducation_library_barcode = fields.Boolean(
        string="Library Barcode Enterprise")
    module_fsieducation_library_enterprise = fields.Boolean(
        string="Library Enterprise")
    module_fsieducation_lms = fields.Boolean(
        string="LMS Enterprise")
    module_fsieducation_lms_blog = fields.Boolean(
        string="LMS Blog Enterprise")
    module_fsieducation_lms_forum = fields.Boolean(
        string="LMS Forum Enterprise")
    module_fsieducation_lms_gamification = fields.Boolean(
        string="LMS Gamification Enterprise")
    module_fsieducation_lms_sale = fields.Boolean(
        string="LMS Sale Enterprise")
    module_fsieducation_lms_survey = fields.Boolean(
        string="LMS Survey Enterprise")
    module_fsieducation_meeting_enterprise = fields.Boolean(
        string="Meeting Enterprise")
    module_fsieducation_online_admission = fields.Boolean(
        string="Online Admission Enterprise")
    module_fsieducation_parent_enterprise = fields.Boolean(
        string="Parent Enterprise")
    module_fsieducation_placement_enterprise = fields.Boolean(
        string="Placement Enterprise")
    module_fsieducation_placement_job_enterprise = fields.Boolean(
        string="Placement Job Enterprise")
    module_fsieducation_scholarship_enterprise = fields.Boolean(
        string="Scholarship Enterprise")
    module_fsieducation_timetable_enterprise = fields.Boolean(
        string="Timetable Enterprise")
    module_fsieducation_transportation_enterprise = fields.Boolean(
        string="Transportation Enterprise")
    module_fsieducation_lesson = fields.Boolean(
        string="Lesson Enterprise")
    module_fsieducation_skill_enterprise = fields.Boolean(
        string="Skill Enterprise")
    module_fsieducation_lms_website = fields.Boolean(
        string="LMS Website")
    module_fsieducation_assignment_grading_enterprise = fields.Boolean(
        string="Assignment Grading Enterprise")
    module_fsieducation_assignment_grading_bridge = fields.Boolean(
        string="Assignment Grading Bridge")
    module_fsieducation_fees_on_session = fields.Boolean(
        string="Fees On Session")
    module_fsieducation_fees_on_duration = fields.Boolean(
        string="Fees On Duration")
    module_fsieducation_lms_admission = fields.Boolean(
        string="LMS Admission")
    module_backend_theme = fields.Boolean(
        string="Backend Theme")
    module_fsieducation_crm_enterprise = fields.Boolean(
        string="CRM Enterprise")
    module_fsieducation_dashboard_kpi = fields.Boolean(
        string="Dashboard KPI")
    module_fsieducation_digital_library = fields.Boolean(
        string="Digital Library")
    module_fsieducation_event_enterprise = fields.Boolean(
        string="Event Enterprise")
    module_fsieducation_exam_gpa_enterprise = fields.Boolean(
        string="Exam GPA Enterprise")
    module_fsieducation_exam_grading_bridge = fields.Boolean(
        string="Exam Grading Bridge")
    module_googlemeet = fields.Boolean(
        string="Google Meet")
    module_fsieducation_grading = fields.Boolean(
        string="Grading")
    module_fsieducation_jitsi_enterprise = fields.Boolean(
        string="Jitsi Enterprise")
    module_fsieducation_quiz_anti_cheating = fields.Boolean(
        string="Quiz Anti Cheating")
    module_fsieducation_skypemeet = fields.Boolean(
        string="Skype Meet")
    module_fsieducation_student_progress_enterprise = fields.Boolean(
        string="Student Progress Enterprise")
    module_fsieducation_subject_material_allocation = fields.Boolean(
        string="Subject Material Allocation")
    module_teams = fields.Boolean(
        string="Teams")
    module_zoom = fields.Boolean(
        string="Zoom")
    module_fsieducation_student_leave_enterprise = fields.Boolean(
        string="Student Leave")
    module_fsieducation_notice_board_enterprise = fields.Boolean(
        string="Notice Board Enterprise")
    module_fsieducation_student_skill_assessment = fields.Boolean(
        string="Skill Assessment Enterprise")
    module_fsieducation_lms_h5p = fields.Boolean(
        string="LMS H5P Enterprise")
    module_online_appointment = fields.Boolean(
        string="Online Appointment Enterprise")
    module_fsieducation_grievance_enterprise = fields.Boolean(
        string="Grievance")
    module_fsieducation_secure = fields.Boolean(
        string="Secure QR")
    module_fsieducation_mass_subject_registration = fields.Boolean(
        string="Mass Subject Registration")
    module_fsieducation_attendance_report_xlsx = fields.Boolean(
        string="Attendance Xlsx Report")
    module_fsieducation_asset_request_enterprise = fields.Boolean(
        string="Asset Request Enterprise")
    module_fsieducation_lms_interactive_video = fields.Boolean(
        string="Lms Interactive Video")
    module_fsieducation_lms_drag_into_text = fields.Boolean(
        string="Lms Drag Into Text")
    module_fsieducation_lms_match_following = fields.Boolean(
        string="Lms Match Following")
    module_fsieducation_lms_match_images = fields.Boolean(
        string="Lms Match Images")
    module_fsieducation_lms_multiple_choice = fields.Boolean(
        string="Lms Multiple Choice")
    module_fsieducation_lms_numeric = fields.Boolean(
        string="Lms Numeric")
    module_fsieducation_lms_sort_paragraphs = fields.Boolean(
        string="Lms Sort Paragraphs")
    module_fsieducation_quiz_drag_into_text = fields.Boolean(
        string="Quiz Drag Into Text")
    module_fsieducation_quiz_match_following = fields.Boolean(
        string="Quiz Match Following")
    module_fsieducation_quiz_match_images = fields.Boolean(
        string="Quiz Match Images")
    module_fsieducation_quiz_multiple_choice = fields.Boolean(
        string="Quiz Multiple Choice")
    module_fsieducation_quiz_numeric = fields.Boolean(
        string="Quiz Numeric")
    module_fsieducation_quiz_sort_paragraphs = fields.Boolean(
        string="Quiz Sort Paragraphs")
    module_fsieducation_live = fields.Boolean(
        string="Live Meeting")
    module_fsieducation_live_assignment = fields.Boolean(
        string="Live Meeting Assignment")
    module_fsieducation_live_attendance = fields.Boolean(
        string="Live Meeting Attendance")
    module_fsieducation_live_attentiveness = fields.Boolean(
        string="Live Meeting Attentiveness")
    module_fsieducation_attendance_face_recognition = fields.Boolean(
        string="Attendance Face Recognition")
    module_fsieducation_omr = fields.Boolean(
        string="OMR")
    module_auto_database_backup = fields.Boolean(
        string="Database Backup to Local Server")
    module_auto_database_backup_dropbox = fields.Boolean(
        string="Database Backup to Dropbox")
    module_auto_database_backup_ftp = fields.Boolean(
        string="Database Backup to Remote FTP Server")
    module_auto_database_backup_google_drive = fields.Boolean(
        string="Database Backup to Google Drive")
    module_auto_database_backup_onedrive = fields.Boolean(
        string="Database Backup to Onedrive")
    module_auto_database_backup_sftp = fields.Boolean(
        string="Database Backup to Remote SFTP Server")
    attendance_subject_generic = fields.Selection([('subject', 'Subject Wise'), ('generic', 'Generic')],
                                                  help="Subject-specific attendance will be gathered during a "
                                                       "particular session, whereas general attendance will be "
                                                       "collected by one responsible faculty member for the "
                                                       "entire day.",
                                                  config_parameter="attendance_subject_generic_parameter",
                                                  default='subject')
