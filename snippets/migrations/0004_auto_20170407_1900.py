# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_remove_snippet_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=0)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('installed_date', models.DateTimeField(blank=True, null=True)),
                ('storage_capacity', models.DecimalField(decimal_places=10, max_digits=15)),
                ('storage_free_pct', models.DecimalField(decimal_places=10, max_digits=15)),
                ('storage_capacity_fc', models.DecimalField(decimal_places=10, max_digits=15)),
                ('storage_capacity_nl', models.DecimalField(decimal_places=10, max_digits=15)),
                ('storage_capacity_ssd', models.DecimalField(decimal_places=10, max_digits=15)),
                ('dedupe_ratio', models.DecimalField(decimal_places=10, max_digits=15)),
                ('tdvv_count', models.IntegerField(default=0)),
                ('tdvv_capacity', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='SystemState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemId', models.IntegerField(default=0)),
                ('from_date', models.DateTimeField(blank=True, null=True)),
                ('to_date', models.DateTimeField(blank=True, null=True)),
                ('patch', models.CharField(blank=True, max_length=255, null=True)),
                ('patch_previous', models.CharField(blank=True, max_length=255, null=True)),
                ('vv_count', models.IntegerField(default=0)),
                ('vv_count_previous', models.IntegerField(default=0)),
                ('vv_total_io', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('port_total_io', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('delayed_acks', models.IntegerField(default=0)),
                ('delayed_acks_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_16s', models.IntegerField(default=0)),
                ('writes_over_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_over_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_0_62ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_0_125ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_0_25ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_0_5ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_0_1ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_1_2ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_2_4ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_4_8ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_8_16ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_16_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_32_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_64_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_128_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_256_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_512_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_1024_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_2048_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_4096_8192ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_8192_16384ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_16384_32768ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('writes_between_32768_65536ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_over_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_0_62ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_0_125ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_0_25ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_0_5ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_0_1ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_1_2ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_2_4ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_4_8ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_8_16ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_16_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_32_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_64_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_128_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_256_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_512_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_1024_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_2048_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_4096_8192ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_8192_16384ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_16384_32768ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('reads_between_32768_65536ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_over_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_0_62ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_0_125ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_0_25ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_0_5ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_0_1ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_1_2ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_2_4ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_4_8ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_8_16ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_16_32ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_32_64ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_64_128ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_128_256ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_256_512ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_512_1024ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_1024_2048ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_2048_4096ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_4096_8192ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_8192_16384ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_16384_32768ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rw_between_32768_65536ms_pct', models.DecimalField(decimal_places=3, max_digits=6)),
                ('read_bandwidth_mbps', models.DecimalField(decimal_places=10, max_digits=15)),
                ('write_bandwidth_mbps', models.DecimalField(decimal_places=10, max_digits=15)),
                ('total_bandwidth_mbps', models.DecimalField(decimal_places=10, max_digits=15)),
                ('cpu_system_avg', models.IntegerField(default=0)),
                ('cpu_user_avg', models.IntegerField(default=0)),
                ('cpu_total_avg', models.IntegerField(default=0)),
                ('cpu_system_max_pct', models.IntegerField(default=0)),
                ('cpu_user_max_pct', models.IntegerField(default=0)),
                ('cpu_total_max_pct', models.IntegerField(default=0)),
                ('io_read_size_avg_kb', models.DecimalField(decimal_places=10, max_digits=15)),
                ('io_write_size_avg_kb', models.DecimalField(decimal_places=10, max_digits=15)),
                ('io_total_size_avg_kb', models.DecimalField(decimal_places=10, max_digits=15)),
                ('dedupe_size', models.DecimalField(decimal_places=10, max_digits=15)),
                ('node_last_online', models.DateTimeField(blank=True, null=True)),
                ('node_offline_count', models.IntegerField(default=0)),
                ('node_missing_count', models.IntegerField(default=0)),
                ('dedupe_prev_size', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
        ),
        migrations.AddField(
            model_name='systemoverview',
            name='records',
            field=models.ManyToManyField(blank=True, to='snippets.SystemState'),
        ),
    ]
