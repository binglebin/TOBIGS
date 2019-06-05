from Student import Student
from Ban import Ban

# 파일 읽기 전용 열기
with open('student.txt', 'r', encoding='UTF-8') as f:
    school = []
    max_no = len(school)
    '''
    school : 반 객체를 담을 list
    max_no : school list에 있는 반 객체의 수
    '''

    # 파일 내용 한 줄 씩 읽어오기
    for line in f:
        name, no, idx = line.split()
        no = int(no)
        idx = int(idx)
        
        '''
        name : 현재 학생의 이름 
        no : 현재 학생의 반
        idx : 현재 학생의 번호
        '''

        if max_no < no:
            for i in range(no-max_no):
                school.append(Ban(i+max_no+1))
            max_no = len(school)
        
        '''
        현재 학생의 반이 school list에 있는 반 객체 수보다 크면
        1반부터 현재 학생의 반까지 school list에 반 객체를 추가해주기
        '''

        school[no-1].append_student(Student(idx, name))
        
        '''
        현재 학생의 객체를 생성해서 학생에 해당하는 반 객체의 list에 append 하기
        '''

    for i in school:
        i.student_list.sort()
    '''
    각 반 객체 list 오름차순으로 sort
    '''

#출력
for i in school:
    print(i)
    for j in i.student_list:
        print(j)
    print('\n')