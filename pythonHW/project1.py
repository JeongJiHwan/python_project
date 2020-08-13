import sys
import os

def check_grade(total):
    grade = ''
    if total>=90:
        grade='A'
    elif total>=80:
        grade='B'
    elif total>=70:
        grade='C'
    elif total>=60:
        grade='D'
    else:
        grade='F'
    return grade

def get_average(student):
    avg = (int(student[2]) + int(student[3])) / 2
    grade = check_grade(avg)
    
    if len(student)<5:
        student.append(avg)
        student.append(grade)
    else:
        student[4] = avg
        student[5] = grade

def get_student_list(path):
    fr = open(path, 'r')
    ls = []
    for line in fr:
        line = line.rstrip('\n')
        tmp = line.split('\t')
        get_average(tmp)        
        ls.append(tmp)
    fr.close()
    
    return ls

def print_title():
    print('\t{:>8}\t{:>12}\t{:^7}\t {:^5}\t{:^7}\t {:^5}'.format('Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade'))
    print('-'*70)

def print_student_list(ls):
    ls.sort(key=lambda student: student[4], reverse=True)
    print_title()
    for student in ls:
         print('\t{:>8}\t{:>12}\t{:^7}\t {:^5}\t{:^7}\t {:^5}'.format(student[0], student[1], student[2], student[3], student[4], student[5]))
    print()
    
def print_student(student):
    print_title()
    print('\t{:>8}\t{:>12}\t{:^7}\t{:^5}\t {:^7} {:^5}'.format(student[0], student[1], student[2], student[3], student[4], student[5]))
    print()

def print_student_changed(ls):
    print_title()
    print('\t{:>8}\t{:>12}\t{:^7}\t{:^5}\t {:^7} {:^5}'.format(ls[0][0], ls[0][1], ls[0][2], ls[0][3], ls[0][4], ls[0][5]))
    print('Score changed.')
    print('\t{:>8}\t{:>12}\t{:^7}\t{:^5}\t {:^7} {:^5}'.format(ls[1][0], ls[1][1], ls[1][2], ls[1][3], ls[1][4], ls[1][5]))
    print()
    
def search_student(ls, num):
    tmp = []
    if len(num)==1:
        for student in ls:
            if num in student:
                tmp.append(student)
    else:
        for student in ls:
            if num in student:
                return student
    return tmp

def search(student_list):
    num = input('Student ID : ')
    student = search_student(student_list, num)

    if student:
        print_student(student)
    else:
        print('NO SUCH PERSON.\n')

def changescore(student_list):
    num = input('Student ID : ')
    student = search_student(student_list, num)
    
    if student:
        test = input('Mid/Final : ')
        test = test.lower()
        if test != 'mid' and test != 'final':
            print()
            return
        score = input('Input new score : ')
        if int(score) <0 or int(score)>100:
            print()
            return
        tmp = student[:]
        if test == 'mid':
            student[2] = score
        else:
            student[3] = score
        ls = []
        ls.append(tmp)
        get_average(student)
        ls.append(student)
        print_student_changed(ls)
    else:
        print('NO SUCH PERSON.\n')
        
def searchgrade(student_list):
    grade = input('Grade to search : ')
    if not ((ord(grade)>=65 and ord(grade)<=68) or ord(grade)==70):
        print()
        return
    students = search_student(student_list, grade)
    if students:
        print_student_list(students)
    else:
        print('NO RESULTS.\n')
        
def add_student(student_list):
    num = input('Student ID : ')
    student = search_student(student_list, num)
    
    if student:
        print('ALREADY EXISTS.\n')
        return
    
    name = input('Name : ')
    mid = input('Mid Score : ')
    fin = input('Final Score : ')
    student.append(num)
    student.append(name)
    student.append(mid)
    student.append(fin)
    get_average(student)
    
    student_list.append(student)
    print('Student added.\n')

def remove_student(student_list):
    if not student_list:
        print('List is empty.\n')
        return

    num = input('Student ID : ')
    student = search_student(student_list, num)
    
    if student:
        student_list.remove(student)
        print('Student removed\n')
    else:
        print('NO SUCH PERSON\n')

def save_student_list(ls, path):
    ls.sort(key=lambda student: student[4], reverse=True)
    fw = open(path, 'w')
    
    for student in ls:
        fw.write('%s\t%s\t%s\t%s\n' %(student[0], student[1], student[2], student[3]))
    
    fw.close()
        
def quit(student_list):
    check = input('Save data?[yes/no] : ')
    
    if check != 'yes':
        print()
        return
    
    path = input('File name : ')
    save_student_list(student_list, path)
        
def main():
    path = 'students.txt'
    if len(sys.argv)>1:
        path = sys.argv[1]
    if not os.path.exists(path):
        print('파일이 존재하지 않습니다.')
        sys.exit(1)
        
    student_list = get_student_list(path)
    print_student_list(student_list)
    
    while True:
        com = input('# ').lower()
        if com == 'show':
            print_student_list(student_list)
        elif com == 'search':
            search(student_list)            
        elif com == 'changescore':
            changescore(student_list)
        elif com == 'searchgrade':
            searchgrade(student_list)            
        elif com == 'add':
            add_student(student_list)
        elif com == 'remove':
            remove_student(student_list)
            pass
        elif com == 'quit':
            quit(student_list)
            break
        else:
            print('그런 명령어는 없어요\n')
            
if __name__ == '__main__':
    main()