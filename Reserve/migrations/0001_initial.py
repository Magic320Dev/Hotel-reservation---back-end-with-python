# Generated by Django 2.0.2 on 2018-04-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminid', models.AutoField(db_column='AdminID', primary_key=True, serialize=False)),
                ('adminname', models.CharField(db_column='AdminName', max_length=50)),
            ],
            options={
                'db_table': 'Admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('billid', models.AutoField(db_column='BillID', primary_key=True, serialize=False)),
                ('total', models.CharField(blank=True, db_column='Total', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Billpay',
            fields=[
                ('billpayid', models.AutoField(db_column='BillPayID', primary_key=True, serialize=False)),
                ('dateid', models.DateTimeField(blank=True, db_column='DateId', null=True)),
            ],
            options={
                'db_table': 'BillPay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingid', models.AutoField(db_column='BookingID', primary_key=True, serialize=False)),
                ('cin_date', models.DateTimeField(blank=True, db_column='CIN_Date', null=True)),
                ('cout_date', models.DateTimeField(blank=True, db_column='COUT_Date', null=True)),
            ],
            options={
                'db_table': 'Booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='First_Name', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, db_column='Last_Name', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paytype',
            fields=[
                ('payid', models.AutoField(db_column='PayID', primary_key=True, serialize=False)),
                ('ptype', models.CharField(db_column='PType', max_length=50)),
            ],
            options={
                'db_table': 'PayType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('ratingid', models.AutoField(db_column='RatingID', primary_key=True, serialize=False)),
                ('rat_description', models.CharField(blank=True, db_column='Rat_Description', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Ratings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('rentid', models.AutoField(db_column='RentID', primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, db_column='Account', max_length=1, null=True)),
                ('from_date', models.DateTimeField(blank=True, db_column='From_Date', null=True)),
                ('to_date', models.DateTimeField(blank=True, db_column='To_Date', null=True)),
                ('isactive', models.NullBooleanField(db_column='ISactive')),
            ],
            options={
                'db_table': 'Rent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomid', models.AutoField(db_column='RoomID', primary_key=True, serialize=False)),
                ('is_reserved', models.NullBooleanField(db_column='IS_Reserved')),
            ],
            options={
                'db_table': 'ROOM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roomratings',
            fields=[
                ('roomratingid', models.AutoField(db_column='RoomRatingID', primary_key=True, serialize=False)),
                ('from_date', models.DateTimeField(blank=True, db_column='From_Date', null=True)),
                ('to_date', models.DateTimeField(blank=True, db_column='To_Date', null=True)),
                ('isactive', models.NullBooleanField(db_column='ISactive')),
            ],
            options={
                'db_table': 'RoomRatings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('roomtypeid', models.AutoField(db_column='RoomTypeID', primary_key=True, serialize=False)),
                ('roomtype', models.CharField(blank=True, db_column='RoomType', max_length=20, null=True)),
            ],
            options={
                'db_table': 'RoomType',
                'managed': False,
            },
        ),
    ]
