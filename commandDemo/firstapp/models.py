# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
bool_status_choices = (
    (0, '否'),
    (1, '是')
)


class ProduceItem(models.Model):
    assign_item_id = models.CharField('订单明细ID', max_length=200)
    apply_order_id = models.CharField('申请单号', max_length=200)
    template_id = models.CharField('模板ID', max_length=200 )
    template_name = models.CharField('模板名称，线下约定的物料名', max_length=200)
    asset_pic_url = models.CharField('收钱码吊牌和贴纸类型不为空', max_length=200, blank=True, null=True)
    count = models.CharField('数量', max_length=200)
    apply_date = models.CharField('申请日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200)
    receiver_name = models.CharField('收货人姓名', max_length=200, blank=True, null=True)
    receiver_mobile = models.CharField('联系人电话', max_length=200, blank=True, null=True)
    receiver_address = models.CharField('收货人地址', max_length=200, blank=True, null=True)
    province = models.CharField('省', max_length=200, blank=True, null=True)
    city = models.CharField('city', max_length=200, blank=True, null=True)
    district = models.CharField('区', max_length=200, blank=True, null=True)
    postcode = models.CharField('收件人地址邮编', max_length=200, blank=True, null=True)
    logistics_no = models.CharField('物流运单号; 个性码不为空', max_length=2000, blank=True, null=True)
    logistics_name = models.CharField('物流公司，收钱码吊牌和贴纸类型不为空', max_length=200, blank=True, null=True)
    supplier_pid = models.CharField('物料供应商PID', max_length=200, blank=True, null=True)
    create_date = models.CharField('订单创建日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField('更新时间', blank=True, null=True, auto_now_add=True)
    sync_status = models.BooleanField('已同步', choices=bool_status_choices, default=False)
    complete_status = models.BooleanField('已完成', choices=bool_status_choices, default=False)
    sync_retry_count = models.IntegerField(default=0)
    complete_retry_count = models.IntegerField(default=0)
    source = models.IntegerField('来源', default=1)
    # eric add
    importto_task_status = models.BooleanField('已入库', choices=bool_status_choices, default=False)
    importto_task_batchno = models.CharField('入库批次号', max_length=20, blank=False, null=False)

    # Xing Add
    goods_send = models.BooleanField('发货标志', choices=bool_status_choices, default=False)
    goods_send_time = models.DateTimeField('发货时间', blank=True, null=True)
    product_type = models.IntegerField('产品类型（1:个性码 2:空码）', default=0)
    # 为了确保数据一致性, 冗余保存该字段
    asset_resource = models.CharField('目前只有空码生产的码图片url从这里获取', max_length=4000, blank=True, null=True)
    data_version = models.CharField('数据版本 1：旧模式，需要在生产完成后反馈运单号 2：新模式：不需要在生产完成后反馈运单号', max_length=200, default='1')
    qrcode_status = models.BooleanField('已获取码值', choices=bool_status_choices, default=True)
    error_code = models.CharField('错误代码', max_length=200, blank=True, null=True)
    # eric add
    goods_produce = models.BooleanField('生产完成标志', choices=bool_status_choices, default=False)
    goods_produce_time = models.DateTimeField('生产完成时间', blank=True, null=True)
    # eric add 2017-10-24
    produce_order = models.CharField('生产单号', max_length=64, blank=True, null=True)
    memo = models.CharField('备注', max_length=500, blank=True, null=True)
    biz_tag = models.CharField('业务渠道', max_length=500, blank=True, null=True)
    # eric add 2017-12-23
    supplier_id = models.CharField('供应商id', max_length=32, blank=True, null=True)
    supplier_name = models.CharField('供应商', max_length=64, blank=True, null=True)
    # eric add 2018-05-11
    parent_template_id = models.CharField('主物料id', max_length=64, blank=True, null=True)
    # batch_no = models.CharField('完成批次号', max_length=64, blank=True, null=True)
    # batch_no_amount = models.CharField('完成批次物料数量', max_length=128, blank=True, null=True)
    # batch_no_completestatus = models.SmallIntegerField('完成批次反馈状态', default=0, blank=True, null=True)
    complete_amount = models.IntegerField('订单已完成总量', default=0, blank=True, null=True)
    complete_detail = models.CharField('已完成详情', max_length=500, blank=True, null=True)
    to_warehouse_id = models.CharField('仓库ID', max_length=64, blank=True, null=True)
    to_warehouse_name = models.CharField('仓库名称', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.assign_item_id

    class Meta:
        db_table = 'ant_product_item'
        verbose_name = '生产指令'
        verbose_name_plural = '生产指令'


class DupProduceItem(models.Model):
    assign_item_id = models.CharField('订单明细ID', max_length=200)
    apply_order_id = models.CharField('申请单号', max_length=200)
    template_id = models.CharField('模板ID', max_length=200 )
    template_name = models.CharField('模板名称，线下约定的物料名', max_length=200)
    asset_pic_url = models.CharField('收钱码吊牌和贴纸类型不为空', max_length=200, blank=True, null=True)
    count = models.CharField('数量', max_length=200)
    apply_date = models.CharField('申请日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200)
    receiver_name = models.CharField('收货人姓名', max_length=200)
    receiver_mobile = models.CharField('联系人电话', max_length=200)
    receiver_address = models.CharField('收货人地址', max_length=200)
    province = models.CharField('省', max_length=200, blank=True, null=True)
    city = models.CharField('city', max_length=200, blank=True, null=True)
    district = models.CharField('区', max_length=200, blank=True, null=True)
    postcode = models.CharField('收件人地址邮编', max_length=200, blank=True, null=True)
    logistics_no = models.CharField('物流运单号; 个性码不为空', max_length=200, blank=True, null=True)
    logistics_name = models.CharField('物流公司，收钱码吊牌和贴纸类型不为空', max_length=200, blank=True, null=True)
    supplier_pid = models.CharField('物料供应商PID', max_length=200, blank=True, null=True)
    create_date = models.CharField('订单创建日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField('更新时间', blank=True, null=True, auto_now_add=True)
    sync_status = models.BooleanField('已同步', choices=bool_status_choices, default=False)
    complete_status = models.BooleanField('已完成', choices=bool_status_choices, default=False)
    sync_retry_count = models.IntegerField(default=0)
    complete_retry_count = models.IntegerField(default=0)
    source = models.IntegerField('来源', default=1)

    def __str__(self):
        return self.assign_item_id

    class Meta:
        db_table = 'ant_dup_product_item'
        verbose_name = '重复生产指令'
        verbose_name_plural = '重复生产指令'

#
# class Resource(models.Model):
#     assign_item_id = models.CharField('订单明细ID', max_length=200)
#     seq = models.IntegerField('顺序号', default=1)
#     url = models.CharField('数量', max_length=200)
#     # 以下皆冗余字段
#     count = models.CharField('数量', max_length=200)
#     apply_order_id = models.CharField('申请单号', max_length=200)
#     template_id = models.CharField('模板ID', max_length=200 )
#     template_name = models.CharField('模板名称，线下约定的物料名', max_length=256)
#     create_date = models.CharField('订单创建日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200, blank=True, null=True)
#     create_time = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
#     update_time = models.DateTimeField('更新时间', blank=True, null=True, auto_now_add=True)
#
#     def __str__(self):
#         return self.assign_item_id
#
#     class Meta:
#         db_table = 'ant_resource'
#         verbose_name = '空码生产码图片URL'
#         verbose_name_plural = '空码生产码图片URL'


class DeliveryItem(models.Model):
    assign_item_id = models.CharField('订单明细ID', max_length=200)
    assign_out_order_id = models.CharField('配送流水号，可用于对账', max_length=200)
    apply_order_id = models.CharField('申请单号', max_length=200)
    supplier_id = models.CharField('供应商id', max_length=200)
    gmt_assign = models.CharField('配送指令生成日期, 格式:yyyy-MM-dd HH：mm:ss', max_length=200, blank=True, null=True)

    item_id = models.CharField('物料id', max_length=200 )
    item_name = models.CharField('物料名称', max_length=200)
    amount = models.CharField('数量', max_length=200)
    from_address_province = models.CharField('省', max_length=400, blank=True, null=True)
    from_address_city = models.CharField('市', max_length=400, blank=True, null=True)
    from_address_district = models.CharField('区', max_length=400, blank=True, null=True)
    from_address_address = models.CharField('地址', max_length=400, blank=True, null=True)
    from_address_contact_name = models.CharField('联系人', max_length=400, blank=True, null=True)
    from_address_contact_phone = models.CharField('联系电话', max_length=400, blank=True, null=True)
    from_address_zip_code = models.CharField('邮编', max_length=400, blank=True, null=True)

    to_address_province = models.CharField('省', max_length=400, blank=True, null=True)
    to_address_city = models.CharField('市', max_length=400, blank=True, null=True)
    to_address_district = models.CharField('区', max_length=400, blank=True, null=True)
    to_address_address = models.CharField('地址', max_length=400, blank=True, null=True)
    to_address_contact_name = models.CharField('联系人', max_length=400, blank=True, null=True)
    to_address_contact_phone = models.CharField('联系电话', max_length=400, blank=True, null=True)
    to_address_zip_code = models.CharField('邮编', max_length=400, blank=True, null=True)

    logistics_no = models.CharField('物流运单号; 个性码不为空', max_length=4000, blank=True, null=True)
    logistics_name = models.CharField('物流公司，收钱码吊牌和贴纸类型不为空', max_length=200, blank=True, null=True)
    logistics_code = models.CharField('物流公司code', max_length=200, blank=True, null=True)
    memo = models.CharField('物料供应商PID', max_length=256, blank=True, null=True)
    create_time = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField('更新时间', blank=True, null=True, auto_now_add=True)
    sync_status = models.BooleanField('已同步', choices=bool_status_choices, default=False)
    complete_status = models.BooleanField('已完成', choices=bool_status_choices, default=False)
    sync_retry_count = models.IntegerField(default=0)
    complete_retry_count = models.IntegerField(default=0)
    import_status = models.BooleanField('入库状态', choices=bool_status_choices, default=False)
    import_batch_no = models.CharField('入库批次号', max_length=64, blank=True, null=True)
    goods_send = models.BooleanField('发货状态', choices=bool_status_choices, default=False)
    goods_send_time = models.DateTimeField('发货时间', blank=True, null=True)
    product_type = models.IntegerField('产品类型（1:个性码 2:空码）', default=0)
    error_code = models.CharField('错误代码', max_length=200, blank=True, null=True)

    # eric add 2017-11-24
    biz_tag = models.CharField('业务渠道', max_length=500, blank=True, null=True)
    supplier_name = models.CharField('供应商', max_length=64, blank=True, null=True)

    # eric add 2018-2-6
    print_data = models.CharField('菜鸟面单', max_length=5000, blank=True, null=True)
    action_type = models.CharField('动作类型', max_length=128, blank=True, null=True)

    # eric add 2018-05-11
    parent_item_id = models.CharField('主物料id', max_length=64, blank=True, null=True)
    batch_no = models.CharField('完成批次号', max_length=64, blank=True, null=True)
    # batch_no_amount = models.CharField('完成批次物料数量', max_length=128, blank=True, null=True)
    from_warehouse_id = models.CharField('发送仓库ID', max_length=64, blank=True, null=True)
    from_warehouse_name = models.CharField('发送仓库名称', max_length=64, blank=True, null=True)
    to_warehouse_id = models.CharField('接收仓库ID', max_length=64, blank=True, null=True)
    to_warehouse_name = models.CharField('接收仓库名称', max_length=64, blank=True, null=True)

    produce_order_item_id = models.CharField('关联生产指令', max_length=64, blank=True, null=True)
    record_type = models.CharField('指令类型', max_length=64, blank=True, null=True)

    complete_amount = models.IntegerField('订单已配送总量', default=0, blank=True, null=True)

    def __str__(self):
        return self.assign_item_id

    class Meta:
        db_table = 'ant_delivery_item'
        verbose_name = '配送指令'
        verbose_name_plural = '配送指令'


# eric add 2018-06-15
class ProductDeliveryDetail(models.Model):
    rowid = models.AutoField(primary_key=True)
    customer = models.CharField(verbose_name=u'客户', max_length=30, blank=True, null=True)
    product = models.CharField(verbose_name=u'产品', max_length=30, blank=True, null=True)
    importbatchno = models.CharField(verbose_name=u'入库批次号', max_length=30, blank=True, null=True)
    apply_order_id = models.CharField(verbose_name=u'AO单号', max_length=30, blank=True, null=True)
    produce_order_item_id = models.CharField('关联生产指令', max_length=64, blank=True, null=True)

    produce_date = models.CharField(verbose_name=u'生产日期', max_length=10, blank=True, null=True)
    produce_time = models.DateTimeField(verbose_name=u'生产时间', auto_now_add=True, blank=True, null=True)
    produce_batchno = models.CharField(verbose_name=u'生产批次号', max_length=20, blank=True, null=True)
    produce_amount = models.IntegerField(verbose_name=u'生产数量', default=0)
    produce_sync = models.SmallIntegerField(verbose_name=u'API反馈生产状态', default=0)
    produce_sync_amount = models.IntegerField(verbose_name=u'API未反馈生产数量', default=0)

    delivery_date = models.CharField(verbose_name=u'出货日期', max_length=10, blank=True, null=True)
    delivery_time = models.DateTimeField(verbose_name=u'出货时间', auto_now_add=True, blank=True, null=True)
    delivery_batchno = models.CharField(verbose_name=u'出货批次号', max_length=20, blank=True, null=True)
    delivery_amount = models.IntegerField(verbose_name=u'出货数量', default=0)
    delivery_sync = models.SmallIntegerField(verbose_name=u'API反馈出货状态', default=0)
    delivery_sync_amount = models.IntegerField(verbose_name=u'API未反馈出货数量', default=0)

    class Meta:
        managed = True
        db_table = 'mayi_productdeliverydetail'
        verbose_name = u'产品出货详情'
        verbose_name_plural = u"产品出货详情"

    def __unicode__(self):
        return self.importbatchno  # 一定要返回字符串类型，否则django custom action操作过程里会报错