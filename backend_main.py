import json
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QHeaderView, QMainWindow, QMessageBox

from ui_main import Ui_MainWindow

DT_FMT = '%H:%M:%S,%f'


class ItemsModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = []
        self.number = []
        self.name = []
        self.surname = []
        self.result = []

    def set_items(self, items, position):
        number = []
        name = []
        surname = []
        result = []

        for pos in range(1, len(items) + 1):
            pos = str(pos)
            number.append(items[pos]['Нагрудный номер'])
            name.append(items[pos]['Имя'])
            surname.append(items[pos]['Фамилия'])
            result.append(items[pos]['Результат'])

        self.beginResetModel()
        self.position = position
        self.number = number
        self.name = name
        self.surname = surname
        self.result = result
        self.endResetModel()

    def rowCount(self, *args, **kwargs):
        return len(self.position)

    def columnCount(self, *args, **kwargs):
        return 5

    def data(self, index: QtCore.QModelIndex, role=QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            col = index.column()
            if col == 0:
                return self.position[index.row()]
            elif col == 1:
                return self.number[index.row()]
            elif col == 2:
                return self.name[index.row()]
            elif col == 3:
                return self.surname[index.row()]
            elif col == 4:
                return self.result[index.row()]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role=QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Занятое место',
                    1: 'Нагрудный номер',
                    2: 'Имя',
                    3: 'Фамилия',
                    4: 'Результат',
                }.get(section)


class ResultCalculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.competitors = None
        self.time = None
        self.competitors_result = {}
        self.model = ItemsModel()
        self.tableView_2.setModel(self.model)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.btn_upload_competitors.clicked.connect(self.event_btn_competitors_file_clicked)
        self.btn_upload_result.clicked.connect(self.event_btn_result_file_clicked)
        self.btn_calculate.clicked.connect(self.event_btn_calculate_clicked)
        self.btn_save.clicked.connect(self.event_btn_save_clicked)

    def event_btn_competitors_file_clicked(self):
        res = QFileDialog.getOpenFileName(self, 'OpenFile', '.', 'JSON File (*.json)')
        if res:
            with open(res[0], 'r', encoding='utf-8') as file:
                data = file.read()
                self.competitors = json.loads(data.replace('\ufeff', ''))

    def event_btn_result_file_clicked(self):
        res = QFileDialog.getOpenFileName(self, 'OpenFile', '.', 'TXT File (*.txt)')
        if res:
            with open(res[0], 'r', encoding='utf-8') as file:
                data = file.read()
                self.time = data.replace(data[0], '').rstrip().split('\n')

    def event_btn_calculate_clicked(self):
        positions_list = []
        try:
            tmp = dict()
            result = list()

            for res in self.time[::-1]:
                data = res.split(' ')
                if tmp.get('number') == data[0]:
                    calc = tmp['time'] - datetime.strptime(data[2], DT_FMT)
                    tmp['time'] = str(calc)
                    result.append(tmp)
                tmp = {
                    'number': data[0],
                    'time': datetime.strptime(data[2], DT_FMT),
                }

            result = sorted(result, key=lambda x: x['time'])

            position = 1
            for comp in result:
                self.competitors_result[str(position)] = {
                        'Нагрудный номер': comp['number'],
                        'Имя': self.competitors[comp['number']]['Surname'],
                        'Фамилия': self.competitors[comp['number']]['Name'],
                        'Результат': comp['time'],
                    }
                positions_list.append(position)
                position += 1

            self.model.set_items(self.competitors_result, positions_list)

        except (Exception, ):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Invalid data")
            dlg.setText("A valid files must be uploaded!")
            dlg.exec()

    def event_btn_save_clicked(self):
        if self.competitors_result:
            res = QFileDialog.getSaveFileName(self, 'Save File', "./result.json", "JSON (*.json)")
            if res:
                with open(res[0], 'w', encoding='utf-8') as file:
                    data = json.dumps(self.competitors_result, indent=4, ensure_ascii=False)
                    file.write(data)
