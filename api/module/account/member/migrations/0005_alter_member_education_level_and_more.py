# Generated by Django 4.2.3 on 2023-07-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_member_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='education_level',
            field=models.IntegerField(blank=True, choices=[(1, 'Tiểu học'), (2, 'Trung học cơ sở'), (3, 'Trung học phổ thông hệ 10/10'), (4, 'Hệ 12/12')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='foreign_language_level',
            field=models.IntegerField(blank=True, choices=[(1, 'Bậc 1'), (2, 'Bậc 2'), (3, 'Bậc 3'), (4, 'Bậc 4'), (5, 'Bậc 5'), (6, 'Bậc 6')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='it_level',
            field=models.IntegerField(blank=True, choices=[(1, 'Chuẩn kỹ năng sử dụng CNTT cơ bản'), (2, 'Chuẩn kỹ năng sử dụng CNTT nâng cao')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='political_theory_level',
            field=models.IntegerField(blank=True, choices=[(1, 'Sơ cấp'), (2, 'Trung cấp'), (3, 'Cao cấp'), (4, 'Cử nhân'), (5, 'Chưa có')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='qualification',
            field=models.IntegerField(blank=True, choices=[(1, 'Sơ cấp'), (2, 'Trung cấp chuyên nghiệp'), (3, 'Cao đẳng'), (4, 'Cử nhân'), (5, 'Thạc sĩ'), (6, 'Tiến sĩ')], null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='religion',
            field=models.IntegerField(blank=True, choices=[(1, 'Tin Lành'), (2, 'Không'), (3, 'Cao Đài'), (4, 'Công giáo'), (5, 'Phật giáo'), (6, 'Hòa Hảo'), (7, 'Hồi giáo'), (8, "Bahá'í"), (9, 'Bà La Môn'), (10, 'Đạo Tứ ấn hiếu nghĩa'), (11, 'Tịnh độ cư sĩ Phật hội Việt Nam'), (12, 'Bửu sơn Kỳ hương'), (13, 'Minh Sư Đạo'), (14, 'Minh Lý Đạo')], null=True),
        ),
    ]
