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


class TestLibraryCommon(common.TransactionCase):
    def setUp(self):
        super(TestLibraryCommon, self).setUp()
        self.fsi_library_card_type = self.env['fsi.library.card.type']
        self.fsi_library_card = self.env['fsi.library.card']
        self.fsi_media = self.env['fsi.media']
        self.fsi_media_unit = self.env['fsi.media.unit']
        self.fsi_media_movement = self.env['fsi.media.movement']
        self.fsi_media_purchase = self.env['fsi.media.purchase']
        self.fsi_media_queue = self.env['fsi.media.queue']
        self.wizard_issue = self.env['issue.media']
        self.reserve_media = self.env['reserve.media']
        self.return_media = self.env['return.media']
