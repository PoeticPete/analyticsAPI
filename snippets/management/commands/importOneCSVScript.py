import csv
from snippets.models import SystemOverview, SystemState


with open('perform-summary.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader,None)
    for summary_current_row in reader:
        print(int(summary_current_row[0]))
        SystemOverview.objects.get_or_create(serial=int(summary_current_row[0]),
                                                             company=summary_current_row[1],
                                                             model=summary_current_row[2],
                                                             updated_date=pytz.utc.localize(datetime.strptime(
                                                                 summary_current_row[3].decode('ascii'),
                                                                 '%Y-%m-%d %H:%M:%S')),
                                                             installed_date=pytz.utc.localize(datetime.strptime(
                                                                 summary_current_row[4].decode('ascii'), '%Y-%m-%d')),
                                                             storage_capacity=self.string_to_float(
                                                                 summary_current_row[5]),
                                                             storage_free_pct=self.string_to_float(
                                                                 summary_current_row[6]),
                                                             storage_capacity_fc=self.string_to_float(
                                                                 summary_current_row[7]),
                                                             storage_capacity_nl=self.string_to_float(
                                                                 summary_current_row[8]),
                                                             storage_capacity_ssd=self.string_to_float(
                                                                 summary_current_row[9]),
                                                             dedupe_ratio=self.string_to_float(summary_current_row[10]),
                                                             tdvv_count=self.string_to_int(summary_current_row[11]),
                                                             tdvv_capacity=self.string_to_float(
                                                                 summary_current_row[12]), )
