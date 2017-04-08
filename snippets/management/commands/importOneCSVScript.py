from django.core.management.base import BaseCommand
import csv
from snippets.models import SystemOverview, SystemState, Test
import pytz
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
import logging, logging.handlers
from django.core import serializers

class Command(BaseCommand):
    def string_to_float(self, input):
        if input:
            return float(input)
        return 0.0

    def string_to_int(self, input):
        if input:
            return int(input)
        return 0

    def handle(self, *args, **options):
        # DELETE ALL
        # Test.objects.all().delete()
        # all = Test.objects.all().count()
        # print(all)

        # PRINT SYSTEM OVERVIEW
        # obj = SystemOverview.objects.filter(serial=1)
        # print(serializers.serialize("json", obj))
        # print(SystemOverview.toJSONObject(obj))

        # PRINT SYSTEM STATE
        obj = SystemState.objects.filter(systemId=2883)
        print(serializers.serialize("json", obj))

        # snippet = Snippet.objects.get(code__startswith='sup')
        # snippet = Snippet.objects.all()
        # print(snippet.count())
        # print(snippet.toJSONObject())

        # IMPORT 2883 FILE
        with open('csvFiles/2883-perform.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader,None)


            for current_row in reader:
                print(int(current_row[0]))

                SystemState.objects.get_or_create(systemId=self.string_to_int(current_row[0]),
                                                  from_date=pytz.utc.localize(
                                                      datetime.strptime(current_row[1],
                                                                        '%Y-%m-%d %H:%M:%S')),
                                                  to_date=pytz.utc.localize(
                                                      datetime.strptime(current_row[2],
                                                                        '%Y-%m-%d %H:%M:%S')),
                                                  patch=current_row[3],
                                                  patch_previous=current_row[4],
                                                  vv_count=self.string_to_int(current_row[5]),
                                                  vv_count_previous=self.string_to_int(current_row[6]),
                                                  vv_total_io=self.string_to_float(current_row[7]),
                                                  port_total_io=self.string_to_float(current_row[8]),
                                                  delayed_acks=self.string_to_int(current_row[9]),
                                                  delayed_acks_pct=self.string_to_float(current_row[10]),
                                                  writes_over_16s=self.string_to_float(current_row[11]),
                                                  writes_over_32ms_pct=self.string_to_float(current_row[12]),
                                                  writes_over_64ms_pct=self.string_to_float(current_row[13]),
                                                  writes_over_128ms_pct=self.string_to_float(current_row[14]),
                                                  writes_over_256ms_pct=self.string_to_float(current_row[15]),
                                                  writes_over_512ms_pct=self.string_to_float(current_row[16]),
                                                  writes_over_1024ms_pct=self.string_to_float(current_row[17]),
                                                  writes_over_2048ms_pct=self.string_to_float(current_row[18]),
                                                  writes_over_4096ms_pct=self.string_to_float(current_row[19]),
                                                  writes_between_0_62ms_pct=self.string_to_float(current_row[20]),
                                                  writes_between_0_125ms_pct=self.string_to_float(current_row[21]),
                                                  writes_between_0_25ms_pct=self.string_to_float(current_row[22]),
                                                  writes_between_0_5ms_pct=self.string_to_float(current_row[23]),
                                                  writes_between_0_1ms_pct=self.string_to_float(current_row[24]),
                                                  writes_between_1_2ms_pct=self.string_to_float(current_row[25]),
                                                  writes_between_2_4ms_pct=self.string_to_float(current_row[26]),
                                                  writes_between_4_8ms_pct=self.string_to_float(current_row[27]),
                                                  writes_between_8_16ms_pct=self.string_to_float(current_row[28]),
                                                  writes_between_16_32ms_pct=self.string_to_float(current_row[29]),
                                                  writes_between_32_64ms_pct=self.string_to_float(current_row[30]),
                                                  writes_between_64_128ms_pct=self.string_to_float(current_row[31]),
                                                  writes_between_128_256ms_pct=self.string_to_float(current_row[32]),
                                                  writes_between_256_512ms_pct=self.string_to_float(current_row[33]),
                                                  writes_between_512_1024ms_pct=self.string_to_float(current_row[34]),
                                                  writes_between_1024_2048ms_pct=self.string_to_float(current_row[35]),
                                                  writes_between_2048_4096ms_pct=self.string_to_float(current_row[36]),
                                                  writes_between_4096_8192ms_pct=self.string_to_float(current_row[37]),
                                                  writes_between_8192_16384ms_pct=self.string_to_float(current_row[38]),
                                                  writes_between_16384_32768ms_pct=self.string_to_float(
                                                      current_row[39]),
                                                  writes_between_32768_65536ms_pct=self.string_to_float(
                                                      current_row[40]),
                                                  reads_over_32ms_pct=self.string_to_float(current_row[41]),
                                                  reads_over_64ms_pct=self.string_to_float(current_row[42]),
                                                  reads_over_128ms_pct=self.string_to_float(current_row[43]),
                                                  reads_over_256ms_pct=self.string_to_float(current_row[44]),
                                                  reads_over_512ms_pct=self.string_to_float(current_row[45]),
                                                  reads_over_1024ms_pct=self.string_to_float(current_row[46]),
                                                  reads_over_2048ms_pct=self.string_to_float(current_row[47]),
                                                  reads_over_4096ms_pct=self.string_to_float(current_row[48]),
                                                  reads_between_0_62ms_pct=self.string_to_float(current_row[49]),
                                                  reads_between_0_125ms_pct=self.string_to_float(current_row[50]),
                                                  reads_between_0_25ms_pct=self.string_to_float(current_row[51]),
                                                  reads_between_0_5ms_pct=self.string_to_float(current_row[52]),
                                                  reads_between_0_1ms_pct=self.string_to_float(current_row[53]),
                                                  reads_between_1_2ms_pct=self.string_to_float(current_row[54]),
                                                  reads_between_2_4ms_pct=self.string_to_float(current_row[55]),
                                                  reads_between_4_8ms_pct=self.string_to_float(current_row[56]),
                                                  reads_between_8_16ms_pct=self.string_to_float(current_row[57]),
                                                  reads_between_16_32ms_pct=self.string_to_float(current_row[58]),
                                                  reads_between_32_64ms_pct=self.string_to_float(current_row[59]),
                                                  reads_between_64_128ms_pct=self.string_to_float(current_row[60]),
                                                  reads_between_128_256ms_pct=self.string_to_float(current_row[61]),
                                                  reads_between_256_512ms_pct=self.string_to_float(current_row[62]),
                                                  reads_between_512_1024ms_pct=self.string_to_float(current_row[63]),
                                                  reads_between_1024_2048ms_pct=self.string_to_float(current_row[64]),
                                                  reads_between_2048_4096ms_pct=self.string_to_float(current_row[65]),
                                                  reads_between_4096_8192ms_pct=self.string_to_float(current_row[66]),
                                                  reads_between_8192_16384ms_pct=self.string_to_float(current_row[67]),
                                                  reads_between_16384_32768ms_pct=self.string_to_float(current_row[68]),
                                                  reads_between_32768_65536ms_pct=self.string_to_float(current_row[69]),
                                                  rw_over_32ms_pct=self.string_to_float(current_row[70]),
                                                  rw_over_64ms_pct=self.string_to_float(current_row[71]),
                                                  rw_over_128ms_pct=self.string_to_float(current_row[72]),
                                                  rw_over_256ms_pct=self.string_to_float(current_row[73]),
                                                  rw_over_512ms_pct=self.string_to_float(current_row[74]),
                                                  rw_over_1024ms_pct=self.string_to_float(current_row[75]),
                                                  rw_over_2048ms_pct=self.string_to_float(current_row[76]),
                                                  rw_over_4096ms_pct=self.string_to_float(current_row[77]),
                                                  rw_between_0_62ms_pct=self.string_to_float(current_row[78]),
                                                  rw_between_0_125ms_pct=self.string_to_float(current_row[79]),
                                                  rw_between_0_25ms_pct=self.string_to_float(current_row[80]),
                                                  rw_between_0_5ms_pct=self.string_to_float(current_row[81]),
                                                  rw_between_0_1ms_pct=self.string_to_float(current_row[82]),
                                                  rw_between_1_2ms_pct=self.string_to_float(current_row[83]),
                                                  rw_between_2_4ms_pct=self.string_to_float(current_row[84]),
                                                  rw_between_4_8ms_pct=self.string_to_float(current_row[85]),
                                                  rw_between_8_16ms_pct=self.string_to_float(current_row[86]),
                                                  rw_between_16_32ms_pct=self.string_to_float(current_row[87]),
                                                  rw_between_32_64ms_pct=self.string_to_float(current_row[88]),
                                                  rw_between_64_128ms_pct=self.string_to_float(current_row[89]),
                                                  rw_between_128_256ms_pct=self.string_to_float(current_row[90]),
                                                  rw_between_256_512ms_pct=self.string_to_float(current_row[91]),
                                                  rw_between_512_1024ms_pct=self.string_to_float(current_row[92]),
                                                  rw_between_1024_2048ms_pct=self.string_to_float(current_row[93]),
                                                  rw_between_2048_4096ms_pct=self.string_to_float(current_row[94]),
                                                  rw_between_4096_8192ms_pct=self.string_to_float(current_row[95]),
                                                  rw_between_8192_16384ms_pct=self.string_to_float(current_row[96]),
                                                  rw_between_16384_32768ms_pct=self.string_to_float(current_row[97]),
                                                  rw_between_32768_65536ms_pct=self.string_to_float(current_row[98]),
                                                  read_bandwidth_mbps=self.string_to_float(current_row[99]),
                                                  write_bandwidth_mbps=self.string_to_float(current_row[100]),
                                                  total_bandwidth_mbps=self.string_to_float(current_row[101]),
                                                  cpu_system_avg=self.string_to_float(current_row[102]),
                                                  cpu_user_avg=self.string_to_float(current_row[103]),
                                                  cpu_total_avg=self.string_to_int(current_row[104]),
                                                  cpu_system_max_pct=self.string_to_int(current_row[105]),
                                                  cpu_user_max_pct=self.string_to_int(current_row[106]),
                                                  cpu_total_max_pct=self.string_to_float(current_row[107]),
                                                  io_read_size_avg_kb=self.string_to_float(current_row[108]),
                                                  io_write_size_avg_kb=self.string_to_float(current_row[109]),
                                                  io_total_size_avg_kb=self.string_to_float(current_row[110]),
                                                  dedupe_size=self.string_to_float(current_row[111]),
                                                  node_last_online=pytz.utc.localize(
                                                      datetime.strptime(current_row[112],
                                                                        '%Y-%m-%d %H:%M:%S')),
                                                  node_offline_count=self.string_to_int(current_row[113]),
                                                  node_missing_count=self.string_to_int(current_row[114]),
                                                  dedupe_prev_size=self.string_to_float(current_row[115]))

        # with open('csvFiles/perform-summary.csv', 'r') as f:
        #     reader = csv.reader(f)
        #     next(reader,None)


            # for summary_current_row in reader:
            #     print(int(summary_current_row[0]))
                # try:
                #     valid_datetime = datetime.strptime(summary_current_row[3].decode('ascii'),
                #                                        '%Y-%m-%d %H:%M:%S')
                #     print(valid_datetime)
                #     # print("valid")
                # except ValueError:
                #     print("ERROR!!!")
                #     print(ValueError)

                # Test.objects.create(serial=int(summary_current_row[0]),
                #                                   company=summary_current_row[1],
                #                                   model=summary_current_row[2],
                #                                 updated_date=pytz.utc.localize(datetime.strptime(summary_current_row[3].decode('ascii'),'%Y-%m-%d %H:%M:%S'))
                #                     )

                # SystemOverview.objects.create(serial=int(summary_current_row[0]),
                #                                                      company=summary_current_row[1],
                #                                                      model=summary_current_row[2],
                #                                                      updated_date=pytz.utc.localize(datetime.strptime(
                #                                                          summary_current_row[3].decode('ascii'),
                #                                                          '%Y-%m-%d %H:%M:%S')),
                #                                                      installed_date=pytz.utc.localize(datetime.strptime(
                #                                                          summary_current_row[4].decode('ascii'), '%Y-%m-%d')),
                #                                                      storage_capacity=self.string_to_float(
                #                                                          summary_current_row[5]),
                #                                                      storage_free_pct=self.string_to_float(
                #                                                          summary_current_row[6]),
                #                                                      storage_capacity_fc=self.string_to_float(
                #                                                          summary_current_row[7]),
                #                                                      storage_capacity_nl=self.string_to_float(
                #                                                          summary_current_row[8]),
                #                                                      storage_capacity_ssd=self.string_to_float(
                #                                                          summary_current_row[9]),
                #                                                      dedupe_ratio=self.string_to_float(summary_current_row[10]),
                #                                                      tdvv_count=self.string_to_int(summary_current_row[11]),
                #                                                      tdvv_capacity=self.string_to_float(
                #                                                          summary_current_row[12]), )