
import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def __init__(self):
        self.results = {
            'Статус': 'Количество',
            'Active': 0,
            'Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            'Rejected': 0,
            'Superseded': 0,
            'Withdrawn': 0,
            'Draft': 0,
            'Total': 0,
        }

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        self.results['Total'] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        results_keys = list(self.results.keys())
        results_values = list(self.results.values())
        results = []
        for i in range(len(results_keys)):
            results.append((results_keys[i], results_values[i]))
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel-tab')
            writer.writerows(results)
