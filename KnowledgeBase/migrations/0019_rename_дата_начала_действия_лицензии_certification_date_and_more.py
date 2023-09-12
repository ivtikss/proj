# Generated by Django 4.2.2 on 2023-06-28 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0018_rename_логотип_vendor_logo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='Дата начала действия лицензии',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='certification',
            old_name='Файлы',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='certification',
            old_name='Наименование',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Номер телефона',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Месенджер',
            new_name='messanger',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='ФИО',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Электронная почта',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='id Продукта',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='Описание',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='Наименование',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='Брошюра с официального статуса',
            new_name='brochure',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='Вебинар по продукту',
            new_name='partner_webinar',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='Закрытый вебинар для партнера',
            new_name='presentation',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='Презентация продукта',
            new_name='presentation_product',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='id Продукта',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='extrainfo',
            old_name='Презентация',
            new_name='webinar',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Дополнительный комментарий',
            new_name='extra_comment',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Анкета регестрации сделок',
            new_name='pilot_description',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Дистрибутив',
            new_name='pilot_path',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Описание блока <Как проведения пилота>',
            new_name='pilot_plan',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='ПМИ',
            new_name='pilot_pmi',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Панкета по пилоту',
            new_name='pilot_quest',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='id Продукта',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Перечень характеристик',
            new_name='reg_axoft',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='План пилота блока <Для проведения пилота>',
            new_name='reg_partnership_status',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Продажа через Axoft',
            new_name='reg_quest_register_deal',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Схема вознаграждения',
            new_name='reg_reward_scheme',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Статус Вендора',
            new_name='tz_44fz',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='Дата начала действия лицензии',
            new_name='tz_date',
        ),
        migrations.RenameField(
            model_name='infodeal',
            old_name='ТЗ по 44-ФЗ',
            new_name='tz_description',
        ),
        migrations.RenameField(
            model_name='licence',
            old_name='Дата начала действия лицензии',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='licence',
            old_name='Описание',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='licence',
            old_name='Наименование',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='Описание',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='Прайсы',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='Наименование',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Аналоги',
            new_name='analogs',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Компетенции',
            new_name='battle_card',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Кому и для чего',
            new_name='brif_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Общая анкета',
            new_name='competencies',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Контактное лицо партнера>',
            new_name='contact_face',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Общая анкета ',
            new_name='gen_form',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Название продукта',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Принцип владения',
            new_name='owner_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Тип продукта',
            new_name='product_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Комплект отгрузки',
            new_name='ship_kit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Техническая поддержка',
            new_name='tech_support',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Топ',
            new_name='top',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Краткое описание',
            new_name='whom_and_what_for',
        ),
        migrations.RenameField(
            model_name='realisation',
            old_name='Наименование',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='Контакты',
            new_name='contacts',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='Партнеры',
            new_name='partners',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='Цены',
            new_name='prices',
        ),
        migrations.RenameField(
            model_name='vendorpartner',
            old_name='Срок действия статуса',
            new_name='period',
        ),
        migrations.RenameField(
            model_name='vendorpartner',
            old_name='Список специалтстов',
            new_name='requirement',
        ),
        migrations.RenameField(
            model_name='vendorpartner',
            old_name='Статус',
            new_name='specialist_list',
        ),
        migrations.RenameField(
            model_name='vendorpartner',
            old_name='Требования к статусу',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='vendorpartner',
            old_name='id Вендора',
            new_name='vendor_id',
        ),
        migrations.RenameField(
            model_name='vendorpartnerspecialist',
            old_name='Срок действия сертификата',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='vendorpartnerspecialist',
            old_name='Сертификат',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='vendorpartnerspecialist',
            old_name='Имя специалиста',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vendorpartnerspecialist',
            old_name='id блока Партнерства',
            new_name='vendor_partner_id',
        ),
        migrations.RenameField(
            model_name='vendorprices',
            old_name='Дата начала действия прайса',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='vendorprices',
            old_name='Прайсы',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='vendorprices',
            old_name='Сертификат',
            new_name='price',
        ),
    ]
