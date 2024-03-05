from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

from workout_list_08_moves import Ui_WorkoutListMain
from workout_list_10_moves import Ui_WorkoutList10Main
from workout_list_12_moves import Ui_WorkoutList12Main
from builder_fav_only import GetWorkouts

splits = ['Upper Body', 'Lower Body', 'Full Body']

upper_focus = ['Chest', 'Back', 'Biceps', 'Triceps', 'Shoulders']

lower_focus = ['Legs', 'Glutes']

full_focus = ['Chest', 'Back', 'Triceps', 'Biceps',  'Shoulders', 'Glutes', 'Legs']

move_amt = ['8','10','12']

class Ui_GenerateWorkoutMain(object):
    def setupUi(self, GenerateWorkoutMain):
        GenerateWorkoutMain.setObjectName("GenerateWorkoutMain")
        GenerateWorkoutMain.resize(453, 185)

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

        self.amt_combo = QtWidgets.QComboBox(parent=GenerateWorkoutMain)
        self.amt_combo.setGeometry(QtCore.QRect(340, 70, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.amt_combo.setFont(font)
        self.amt_combo.setCurrentText("")
        self.amt_combo.setObjectName("amt_combo")

        self.amt_combo.addItems(move_amt)

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

        self.generate_btn = QtWidgets.QPushButton(parent=GenerateWorkoutMain)
        self.generate_btn.setGeometry(QtCore.QRect(110, 120, 231, 24))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.generate_btn.setFont(font)
        self.generate_btn.setObjectName("generate_btn")

        self.generate_btn.clicked.connect(self.launch_workout_window)

        self.label = QtWidgets.QLabel(parent=GenerateWorkoutMain)
        self.label.setGeometry(QtCore.QRect(120, 20, 211, 21))
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

        amt_pref = self.amt_combo.currentText()

        if amt_pref == '8':
            self.ui = Ui_WorkoutListMain()
            self.ui.setupUi(self.window)

            split_pref = self.split_combo.currentText()
            focus_pref = self.focus_combo.currentText()

            workout_plan = GetWorkouts(split_pref=split_pref, focus_pref=focus_pref)

            self.ui.workout_lbl.setText('Workout Plan for {} Day with Focus on {}'.format(split_pref, focus_pref))

            self.ui.warm_up_ex_lbl.setText(workout_plan.warm_up_moves()[0])

            self.ui.exercise_01_lbl.setText(workout_plan.main_focus_moves()[0])
            self.ui.exercise_02_lbl.setText(workout_plan.main_focus_moves()[1])
            self.ui.exercise_03_lbl.setText(workout_plan.main_focus_moves()[2])
            self.ui.exercise_04_lbl.setText(workout_plan.main_focus_moves()[3])

            self.ui.exercise_05_lbl.setText(workout_plan.secondary_focus_moves()[0])
            self.ui.exercise_06_lbl.setText(workout_plan.secondary_focus_moves()[1])

            self.ui.exercise_07_lbl.setText(workout_plan.ab_moves()[0])
            self.ui.exercise_08_lbl.setText(workout_plan.ab_moves()[1])

            self.window.show()
        elif amt_pref == '10':
            self.ui = Ui_WorkoutList10Main()
            self.ui.setupUi(self.window)

            split_pref = self.split_combo.currentText()
            focus_pref = self.focus_combo.currentText()

            workout_plan = GetWorkouts(split_pref=split_pref, focus_pref=focus_pref)

            self.ui.workout_lbl.setText('Workout Plan for {} Day with Focus on {}'.format(split_pref, focus_pref))

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

        elif amt_pref == '12':
            self.ui = Ui_WorkoutList12Main()
            self.ui.setupUi(self.window)

            split_pref = self.split_combo.currentText()
            focus_pref = self.focus_combo.currentText()

            workout_plan = GetWorkouts(split_pref=split_pref, focus_pref=focus_pref)

            self.ui.workout_lbl.setText('Workout Plan for {} Day with Focus on {}'.format(split_pref, focus_pref))

            self.ui.warm_up_ex_lbl.setText(workout_plan.warm_up_moves()[0])

            self.ui.exercise_01_lbl.setText(workout_plan.main_focus_moves()[0])
            self.ui.exercise_02_lbl.setText(workout_plan.main_focus_moves()[1])
            self.ui.exercise_03_lbl.setText(workout_plan.main_focus_moves()[2])
            self.ui.exercise_04_lbl.setText(workout_plan.main_focus_moves()[3])
            self.ui.exercise_05_lbl.setText(workout_plan.main_focus_moves()[4])

            self.ui.exercise_06_lbl.setText(workout_plan.secondary_focus_moves()[0])
            self.ui.exercise_07_lbl.setText(workout_plan.secondary_focus_moves()[1])
            self.ui.exercise_08_lbl.setText(workout_plan.secondary_focus_moves()[2])
            self.ui.exercise_09_lbl.setText(workout_plan.secondary_focus_moves()[3])

            self.ui.exercise_10_lbl.setText(workout_plan.ab_moves()[0])
            self.ui.exercise_11_lbl.setText(workout_plan.ab_moves()[1])
            self.ui.exercise_12_lbl.setText(workout_plan.ab_moves()[2])

            self.window.show()

        # self.ui = Ui_WorkoutListMain()


    def retranslateUi(self, GenerateWorkoutMain):
        _translate = QtCore.QCoreApplication.translate
        GenerateWorkoutMain.setWindowTitle(_translate("GenerateWorkoutMain", "Form"))
        self.focus_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Pick Focus"))
        self.amt_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "No. Moves"))
        self.split_combo.setPlaceholderText(_translate("GenerateWorkoutMain", "Pick Split"))
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
