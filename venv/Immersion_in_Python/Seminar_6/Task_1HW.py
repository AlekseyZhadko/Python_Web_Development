# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import Task_7_1S as date
from sys import argv

date.check_date(argv[-1])
