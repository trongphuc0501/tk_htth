# -*- coding: utf-8 -*- #su dung bo ma Unicode
from openerp.osv import fields,osv
from datetime import datetime
import random

class tnhp(osv.osv):
    _name = 'tnhp.tnhp'
    _columns = {
        'hoc_phan': fields.char('Học Phần', size=25, required=True, translate=True),
        'so_tin_chi': fields.integer('Số tín chỉ', size=5, required=True, translate=True), 
        'hoc_phan_tien_quyet': fields.many2many('tnhp.tnhp', 'hoc_phan_tien_quyet_rel', 'hoc_phan_id', 'hoc_phan_tien_quyet_id', 'Học phần tiên quyết')
    }
    _defaults = {
        'so_tin_chi': 1
    }
    def _check_stc(self, cr, uid, ids, context=None):
        for tnhp in self.browse(cr, uid, ids, context=context):
            if tnhp.so_tin_chi <= 0:
                return False
        return True
    _constraints = [
        (_check_stc, 'Số tín chỉ phải lớn hơn 0!', ['so_tin_chi']),
    ]
    def name_get(self, cr, uid, ids, context=None):
        result = []
        for record in self.browse(cr, uid, ids, context=context):
            result.append((record.id, record.hoc_phan))  # Hiển thị tên của học phần
        return result

tnhp() #tao 1 the hien cho lop tnhp_tnhp

class tnlhp(osv.osv):
    _name = 'tnlhp.tnlhp'
    _columns = {
        'ma_lop_hp': fields.char('Mã lớp học phần', size=25, required=True, translate=True),
        'ten_hp':fields.selection([('nmlt','Nhập môn lập trình'),('ktlt','Kỹ thuật lập trình'),
                                  ('csdl','Cơ sở dữ liệu'),('tkhttt','Triển khai HTTT')],'Tên học phần'), 
        'giang_vien':fields.selection([('tny','Trần Như Ý'),('ltnd','Lê Triệu Ngọc Đức'),
                                  ('at','An Thư'),('lav','Lương An Vinh')],'Giảng viên'),
        'ngay_bd':fields.datetime('Ngày bắt đầu'),
        'ngay_kt':fields.datetime('Ngày kết thúc'),
        'thong_bao':fields.text('Thông báo thêm')
    }

tnlhp()

class tndk(osv.osv):
    _name = 'tndk.tndk'
    _columns = {
        'ma_dang_ky': fields.char('Mã đăng ký',),
        'noi_dung': fields.many2many('tnlhp.tnlhp', 'tndk_noi_dung_rel', 'tndk_id', 'tnlhp_id', 'Nội dung')
    }
    def _generate_ma_dang_ky(self, cr, uid, context=None):
        ngay_dang_ky = datetime.now().strftime("%Y%m%d")
        so_ngau_nhien = '{:02}'.format(random.randint(0, 99))
        ma_dang_ky = "{}{}".format(ngay_dang_ky, so_ngau_nhien)
        return ma_dang_ky

    _defaults = {
        'ma_dang_ky': _generate_ma_dang_ky
    }
    # def name_get(self, cr, uid, ids, context=None):
    #     result = []
    #     for record in self.browse(cr, uid, ids, context=context):
    #         # Tạo chuỗi hiển thị từ các trường dữ liệu của đối tượng record
    #         display_name = "[{}] {} - {} - {} - {}".format(record.ma_lop_hp, record.ten_hp, record.giang_vien, record.ngay_bd, record.ngay_kt)
    #         result.append((record.id, display_name))  # Thêm vào kết quả
    #     return result
    def name_get(self, cr, uid, ids, context=None):
        result = []
        for record in self.browse(cr, uid, ids, context=context):
            ten_hp = ''
            # Lấy thông tin từ trường many2many 'noi_dung' để hiển thị
            for tnlhp_record in record.noi_dung:
                ten_hp += tnlhp_record.ten_hp + ', '
            display_name = "{} - {}".format(record.ma_dang_ky, ten_hp)
            result.append((record.id, display_name))
        return result
tndk()




