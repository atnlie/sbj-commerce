# -*- coding: utf-8 -*-
###############################################################################
#
# Cybrosys Technologies Pvt. Ltd.
#
# Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
# Author: Ayana KP (odoo@cybrosys.com)
#
# You can modify it under the terms of the GNU AFFERO
# GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
# You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
# (AGPL v3) along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    """Inherit model product template and fields for
        product specification and product details"""
    _inherit = 'product.template'

    product_spec = fields.Text(
        string='Product Specification', translate=True,
        help="The Specification of the Product.")
    product_detail = fields.Text(
        string='Product Detail', translate=True,
        help="The Details of the Product ")