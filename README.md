# Описание
Скрипт многократно сокращает трудозатраты на обработку логов, на одну устройство уходит ~15 секунд.
Важное замечание, логи и скрипт должны быть в одной папке. При обработке следующего устройства итоговый файл 
не очищается.
## Как пользоваться
Помещаем скрипт в папку с логами, запускаем, Profit!
usage: logs_script.py [-h] [--file LOG_FILE] [--out OUT_FILE] [--remove_double] [--all]

Creates a file that contains all the errors from the logs. Using: script.py --file file_with_logs extension doesn't
matter

options:
  -h, --help       show this help message and exit
  --file LOG_FILE  sample: --file messages.1
  --out OUT_FILE   Optionally, the name of the output file, the file will be created in the current directory,
                   default: logs.txt, sample: --out logs.txt
  --remove_double  Removes identical errors from the output file default: False
  --all            Processing all files with logs in the current directory, no --file argument required, default:
                   False
Примеры использования:
python logs_script.py --all --remove_double 
Обработает все файлы в текущей директории, в выходном файле будут все ошибки, которые встретились,
итоговый файл logs.txt в текущей директории.
python logs_script.py --file file_name
Обработает заданный файл, итоговый файл logs.txt в текущей директории.