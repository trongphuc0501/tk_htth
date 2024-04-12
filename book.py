# -*- coding: utf-8 -*- #su dung bo ma Unicode
from openerp.osv import fields,osv

# class tnhp(osv.osv):
#     _name = 'tnhp.tnhp'
#     _columns = {
#         'hoc_phan': fields.char('Học Phần', size=25, required=True, translate=True),
#         'so_tin_chi': fields.integer('Số tín chỉ', size=5, required=True, translate=True), 
#         #'hoc_phan_tien_quyet': fields.char('Học phần tiên quyết')
#         'hoc_phan_tien_quyet': fields.many2many('tnhp.tnhp', 'hoc_phan', 'Học phần tiên quyết')
#     }
#     _defaults = {
#         #'hoc_phan_tien_quyet': 'null',
#         'so_tin_chi': 1
#     }
#     def _check_stc(self, cr, uid, ids, context=None):
#         for tnhp in self.browse(cr, uid, ids, context=context):
#             if tnhp.so_tin_chi<=0:
#                 return False
#         return True
#     _constraints = [
#         (_check_stc, 'Số tín chỉ phải lớn hơn 0!', ['so_tin_chi']),
#     ]

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

# class tnhp (osv.osv):
#     _name='tnhp.tnhp'
#     _columns = {
#         #cac thuoc tinh cua lop tnhp
#         'name':fields.char('Tên sách', size=25, required=True, translate=True),
#         'pages':fields.integer('Tổng số trang'),
#         'author':fields.char('Tác giả',size=100, required=True, translate=True),
#         'genre':fields.selection([('tt','Truyện tranh'),('tn','Truyện ngắn'),
#                                  ('tth','Tiểu thuyết'),('th','Thơ')],'Thể loại'),
#         'published_date':fields.datetime('Ngày phát hành'),
#         'active':fields.boolean('Đang bán ?'),
#         'notes':fields.text('Chi tiết')
#     }
#     _defaults={
#         'pages':0,
#         'active':True
#     }
# tnhp() #tao 1 the hien cho lop tnhp_tnhp
