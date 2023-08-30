from django.db import models
# from userprofile.models import UserProfile

# 扫雷用户
class UserMS(models.Model):
    # user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='profile')
    # realname = models.CharField(max_length=10, unique=False, blank=True, default='无名氏', null=False)
    # # 头像
    # avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True, null=True)
    # # 签名
    # bio = models.TextField(max_length=188, blank=True, null=True)

    # 标准、盲扫、竞速无猜、递归的记录
    b_time_best = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    b_time_best_id = models.BigIntegerField(null=True)
    i_time_best = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    i_time_best_id = models.BigIntegerField(null=True)
    e_time_best = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    e_time_best_id = models.BigIntegerField(null=True)
    b_bvs_best = models.FloatField(null=True)
    b_bvs_best_id = models.BigIntegerField(null=True)
    i_bvs_best = models.FloatField(null=True)
    i_bvs_best_id = models.BigIntegerField(null=True)
    e_bvs_best = models.FloatField(null=True)
    e_bvs_best_id = models.BigIntegerField(null=True)
    b_stnb_best = models.FloatField(null=True)
    b_stnb_best_id = models.BigIntegerField(null=True)
    i_stnb_best = models.FloatField(null=True)
    i_stnb_best_id = models.BigIntegerField(null=True)
    e_stnb_best = models.FloatField(null=True)
    e_stnb_best_id = models.BigIntegerField(null=True)
    b_ioe_best = models.FloatField(null=True)
    b_ioe_best_id = models.BigIntegerField(null=True)
    i_ioe_best = models.FloatField(null=True)
    i_ioe_best_id = models.BigIntegerField(null=True)
    e_ioe_best = models.FloatField(null=True)
    e_ioe_best_id = models.BigIntegerField(null=True)
    b_path_best = models.FloatField(null=True)
    b_path_best_id = models.BigIntegerField(null=True)
    i_path_best = models.FloatField(null=True)
    i_path_best_id = models.BigIntegerField(null=True)
    e_path_best = models.FloatField(null=True)
    e_path_best_id = models.BigIntegerField(null=True)

    b_time_best_nf = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    b_time_best_id_nf = models.BigIntegerField(null=True)
    i_time_best_nf = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    i_time_best_id_nf = models.BigIntegerField(null=True)
    e_time_best_nf = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    e_time_best_id_nf = models.BigIntegerField(null=True)
    b_bvs_best_nf = models.FloatField(null=True)
    b_bvs_best_id_nf = models.BigIntegerField(null=True)
    i_bvs_best_nf = models.FloatField(null=True)
    i_bvs_best_id_nf = models.BigIntegerField(null=True)
    e_bvs_best_nf = models.FloatField(null=True)
    e_bvs_best_id_nf = models.BigIntegerField(null=True)
    b_stnb_best_nf = models.FloatField(null=True)
    b_stnb_best_id_nf = models.BigIntegerField(null=True)
    i_stnb_best_nf = models.FloatField(null=True)
    i_stnb_best_id_nf = models.BigIntegerField(null=True)
    e_stnb_best_nf = models.FloatField(null=True)
    e_stnb_best_id_nf = models.BigIntegerField(null=True)
    b_ioe_best_nf = models.FloatField(null=True)
    b_ioe_best_id_nf = models.BigIntegerField(null=True)
    i_ioe_best_nf = models.FloatField(null=True)
    i_ioe_best_id_nf = models.BigIntegerField(null=True)
    e_ioe_best_nf = models.FloatField(null=True)
    e_ioe_best_id_nf = models.BigIntegerField(null=True)
    b_path_best_nf = models.FloatField(null=True)
    b_path_best_id_nf = models.BigIntegerField(null=True)
    i_path_best_nf = models.FloatField(null=True)
    i_path_best_id_nf = models.BigIntegerField(null=True)
    e_path_best_nf = models.FloatField(null=True)
    e_path_best_id_nf = models.BigIntegerField(null=True)

    b_time_best_ng = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    b_time_best_id_ng = models.BigIntegerField(null=True)
    i_time_best_ng = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    i_time_best_id_ng = models.BigIntegerField(null=True)
    e_time_best_ng = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    e_time_best_id_ng = models.BigIntegerField(null=True)
    b_bvs_best_ng = models.FloatField(null=True)
    b_bvs_best_id_ng = models.BigIntegerField(null=True)
    i_bvs_best_ng = models.FloatField(null=True)
    i_bvs_best_id_ng = models.BigIntegerField(null=True)
    e_bvs_best_ng = models.FloatField(null=True)
    e_bvs_best_id_ng = models.BigIntegerField(null=True)
    b_stnb_best_ng = models.FloatField(null=True)
    b_stnb_best_id_ng = models.BigIntegerField(null=True)
    i_stnb_best_ng = models.FloatField(null=True)
    i_stnb_best_id_ng = models.BigIntegerField(null=True)
    e_stnb_best_ng = models.FloatField(null=True)
    e_stnb_best_id_ng = models.BigIntegerField(null=True)
    b_ioe_best_ng = models.FloatField(null=True)
    b_ioe_best_id_ng = models.BigIntegerField(null=True)
    i_ioe_best_ng = models.FloatField(null=True)
    i_ioe_best_id_ng = models.BigIntegerField(null=True)
    e_ioe_best_ng = models.FloatField(null=True)
    e_ioe_best_id_ng = models.BigIntegerField(null=True)
    b_path_best_ng = models.FloatField(null=True)
    b_path_best_id_ng = models.BigIntegerField(null=True)
    i_path_best_ng = models.FloatField(null=True)
    i_path_best_id_ng = models.BigIntegerField(null=True)
    e_path_best_ng = models.FloatField(null=True)
    e_path_best_id_ng = models.BigIntegerField(null=True)

    b_time_best_dg = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    b_time_best_id_dg = models.BigIntegerField(null=True)
    i_time_best_dg = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    i_time_best_id_dg = models.BigIntegerField(null=True)
    e_time_best_dg = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    e_time_best_id_dg = models.BigIntegerField(null=True)
    b_bvs_best_dg = models.FloatField(null=True)
    b_bvs_best_id_dg = models.BigIntegerField(null=True)
    i_bvs_best_dg = models.FloatField(null=True)
    i_bvs_best_id_dg = models.BigIntegerField(null=True)
    e_bvs_best_dg = models.FloatField(null=True)
    e_bvs_best_id_dg = models.BigIntegerField(null=True)
    b_stnb_best_dg = models.FloatField(null=True)
    b_stnb_best_id_dg = models.BigIntegerField(null=True)
    i_stnb_best_dg = models.FloatField(null=True)
    i_stnb_best_id_dg = models.BigIntegerField(null=True)
    e_stnb_best_dg = models.FloatField(null=True)
    e_stnb_best_id_dg = models.BigIntegerField(null=True)
    b_ioe_best_dg = models.FloatField(null=True)
    b_ioe_best_id_dg = models.BigIntegerField(null=True)
    i_ioe_best_dg = models.FloatField(null=True)
    i_ioe_best_id_dg = models.BigIntegerField(null=True)
    e_ioe_best_dg = models.FloatField(null=True)
    e_ioe_best_id_dg = models.BigIntegerField(null=True)
    b_path_best_dg = models.FloatField(null=True)
    b_path_best_id_dg = models.BigIntegerField(null=True)
    i_path_best_dg = models.FloatField(null=True)
    i_path_best_id_dg = models.BigIntegerField(null=True)
    e_path_best_dg = models.FloatField(null=True)
    e_path_best_id_dg = models.BigIntegerField(null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
