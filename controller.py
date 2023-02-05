import jorrnal.view as view
import jorrnal.modul as modul
import json

def start():
    modul.set_class(view.input_class())
    modul.set_subject(view.input_subject())
    modul.open_file()
    student = ''
    while True:
        journal = modul.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        mark = int(view.what_mark())
        modul.student_mark(student, mark)
    modul.save_file()
