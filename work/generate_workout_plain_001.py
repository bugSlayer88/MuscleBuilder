from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

# from workout_list_001 import Ui_WorkoutListMain
from workout_list_10_moves import Ui_WorkoutList10Main
from builder import GetWorkouts
splits = ['Upper Body', 'Lower Body', 'Full Body']

time_min = ['30', '60']

equipment = ['Full Gym', 'At Home w Weights', 'At Home No Weights']

upper_focus = ['Chest', 'Back', 'Biceps', 'Triceps', 'Shoulders']

lower_focus = ['Legs', 'Glutes']

full_focus = ['Chest', 'Back', 'Triceps', 'Biceps',  'Shoulders', 'Glutes', 'Legs']

class Ui_GenerateWorkoutMain(object):
    def setupUi(self, GenerateWorkoutMain):
        GenerateWorkoutMain.setObjectName("GenerateWorkoutMain")
        GenerateWorkoutMain.resize(670, 185)

        self.focus_combo = QtWidgets.QComboBox(parent=GenerateWorkoutMain)
        self.focus_combo.setGeometry(QtCore.QRect(180, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.focus_combo.setFont(font)
        self.focus_combo.setCurrentText("")
        self.focus_combo.setObjectName("focus_combo")

        self.focus_combo.addItem('Select Focus')
        # self.focus_combo.addItems(focus)

        self.equipment_combo = QtWidgets.QComboBox(parent=GenerateWorkoutMain)
        self.equipment_combo.setGeometry(QtCore.QRect(500, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.equipment_combo.setFont(font)
        self.equipment_combo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.equipment_combo.setEditable(False)
        self.equipment_combo.setCurrentText("")
        self.equipment_combo.setObjectName("equipment_combo")

        self.equipment_combo.addItem('Select Equipment')
        self.equipment_combo.addItems(equipment)

        self.split_combo = QtWidgets.QComboBox(parent=GenerateWorkoutMain)
        self.split_combo.setGeometry(QtCore.QRect(20, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.split_combo.setFont(font)
        self.split_combo.setCurrentText("")
        self.split_combo.setObjectName("split_combo")

        self.split_combo.addItem('Select Split')
        self.split_combo.addItems(splits)
        self.split_combo.currentTextChanged.connect(self.split_combo_updated)

        self.time_combo = QtWidgets.QComboBox(parent=GenerateWorkoutMain)
        self.time_combo.setGeometry(QtCore.QRect(340, 70, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.time_combo.setFont(font)
        self.time_combo.setCurrentText("")
        self.time_combo.setObjectName("time_combo")

        self.time_combo.addItem('Select Time')
        self.time_combo.addItems(time_min)

        self.generate_btn = QtWidgets.QPushButton(parent=GenerateWorkoutMain)
        self.generate_btn.setGeometry(QtCore.QRect(220, 130, 231, 24))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.generate_btn.setFont(font)
        self.generate_btn.setObjectName("generate_btn")

        self.generate_btn.clicked.connect(self.launch_workout_window)

        self.label = QtWidgets.QLabel(parent=GenerateWorkoutMain)
        self.label.setGeometry(QtCore.QRect(230, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(GenerateWorkoutMain)
        QtCore.QMetaObject.connectSlotsByName(GenerateWorkoutMain)

    def get_prefs(self):
        split_pref = self.split_combo.currentText()
        focus_pref = self.focus_combo.currentText()
        time_pref = self.time_combo.currentText()
        equipment_pref = self.equipment_combo.currentText()

        return split_pref, focus_pref, time_pref, equipment_pref

    def split_combo_updated(self):
        split_selected = self.split_combo.currentText()

        if split_selected == 'Upper Body':
            self.focus_combo.clear()
            self.focus_combo.addItems(upper_focus)
        if split_selected == 'Lower Body':
            self.focus_combo.clear()
            self.focus_combo.addItems(lower_focus)
        elif split_selected == 'Full Body':
            self.focus_combo.clear()
            self.focus_combo.addItems(full_focus)

    def launch_workout_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_WorkoutList10Main()
        self.ui.setupUi(self.window)

        split_pref = self.split_combo.currentText()
        focus_pref = self.focus_combo.currentText()

        workout_plan = GetWorkouts(split_pref=split_pref,focus_pref=focus_pref)

        self.ui.workout_lbl.setText('Workout Plan for {} Day with Focus on {}'.format(split_pref,focus_pref))

        self.ui.warm_up_ex_lbl.setText(workout_plan.warm_up_moves()[0])

        self.ui.exercise_01_lbl.setText(workout_plan.main_focus_moves()[0])
        self.ui.exercise_02_lbl.setText(workout_plan.main_focus_moves()[1])
        self.ui.exercise_03_lbl.setText(workout_plan.main_focus_moves()[2])
        self.ui.exercise_04_lbl.setText(workout_plan.main_focus_moves()[3])
        self.ui.exercise_05_lbl.setText(workout_plan.main_focus_moves()[4])

        self.ui.exercise_06_lbl.setText(workout_plan.secondary_focus_moves()[0])
        self.ui.exercise_07_lbl.setText(workout_plan.secondary_focus_moves()[1])
        self.ui.exercise_08_lbl.setText(workout_plan.secondary_focus_moves()[2])

        self.ui.exercise_09_lbl.setText(workout_plan.ab_moves()[0])
        self.ui.exercise_10_lbl.setText(workout_plan.ab_moves()[1])

        self.window.show()


    def retranslateUi(self, GenerateWorkoutMain):
        _translate = QtCore.QCoreApplication.translate
        GenerateWorkoutMain.setWindowTitle(_translate("GenerateWorkoutMain", "Generate Workout"))
        self.focus_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Select Focus"))
        self.equipment_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Pick Equipment"))
        self.split_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Pick Split"))
        self.time_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Pick Time"))
        self.generate_btn.setText(_translate("GenerateWorkoutMain", "Generate Workout"))
        self.label.setText(_translate("GenerateWorkoutMain", "Set Workout Details:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateWorkoutMain = QtWidgets.QWidget()
    ui = Ui_GenerateWorkoutMain()
    ui.setupUi(GenerateWorkoutMain)
    GenerateWorkoutMain.show()
    sys.exit(app.exec())
