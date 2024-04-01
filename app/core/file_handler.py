import csv
import os
from dataclasses import asdict
from datetime import date

from .logger import get_logger
from .types import Record


logger = get_logger()

STORAGE_PATH = "/Users/ostaphyba/TG_Assistant/app/file_storage"


def save_record(
    user_id: int,
    record: Record,
    target_date: date = date.today(),
):
    logger.info('Initiating writing to the file')

    file_path = os.path.join(
        STORAGE_PATH,
        str(user_id),
        record.type,
        str(target_date.year),
        f'{target_date.month}.csv'
    )
    # !handle: if dir not exists
    
    logger.info('Starting writing to the file')

    rows = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
        
    record_dict = asdict(record)

    rows.append(record_dict)
    
    fieldnames = record_dict.keys()

    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    logger.info('Successfully writed to the file')


class GoogleFileHandler:
    
    def __init__(self):
        pass
    
    def save_record(self, user_id: int, record: Record):
        pass

    def get_records(self, user_id: int, start_date: date, end_date: date):
        pass
