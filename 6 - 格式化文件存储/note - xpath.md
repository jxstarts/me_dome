# XPath
- ��XML�ļ��в�����Ϣ��һ�׹���/���ԣ� ����XML��Ԫ�ػ������Խ��б���
- http://www.w3school.com.cn/xpath/index.asp

# XPatth ��������
- ��Դ��XPath���ʽ�༭���ߣ�XMLQuire
- Chrome�����XPath Helper
- Firefox�����XPath Checker

# ѡȡ�ڵ�
- nodename��ѡȡ�˽ڵ�������ӽڵ�
- /:�Ӹ��ڵ㿪ʼѡȡ
        
        /Student��û�н��
        /School��ѡȡSchool�ڵ�
- //��ѡȡ�ڵ㣬������λ��

        //age��ѡȡ�������ڵ㣬һ������б���
- .��ѡȡ��ǰ�ڵ�
- ..��ѡȡ��ǰ�ڵ�ĸ��ڵ�
- @ ��ѡȡ����
- XPath�в���һ�㰴��·���������ң�������·����ʾ����

        School/Teacher������Teacher
        School/Student����������Student�ڵ�
        //Student��ѡȡ����Student�Ľڵ㣬������λ��
        School//Age��ѡȡSchool���������Age�ڵ�
        //@Other:ѡȡOther����
        //Age[@Detail]:ѡȡ��������Detail��AgeԪ��

# ν�� - Predicates
- /School/Student[1]:ѡȡSchool����ĵ�һ��Student�ڵ�
- /School/Student[last()]: ѡȡSchool��������һ��Student�ڵ�
- /School/Student[last()-1]:ѡȡSchool����ĵ����ڶ���Student�ڵ�
- /School/Student[last()<3]:ѡȡSchool�����ǰ����Student�ڵ�
- //Student[@score]:ѡȡ��������Score��Student�ڵ�
- //Student[@score="99"]:ѡȡ��������score��������ֵ��99��Student�ڵ�
- //Student[@score]/Age��ѡȡ��������score��Student�ڵ���ӽڵ�Age

# XPath��һЩ����
- |������
        
        //Student[@score] | //Teacher:ѡȡ��������score��Student��Teacher�ڵ�
    
- ���಻������XPath������Ű���+��-��*��div, < , >
