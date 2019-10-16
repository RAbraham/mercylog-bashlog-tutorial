import mercylog_bashlog

m = mercylog_bashlog.BashlogV1()
_ = m._

father = m.relation('father')
mother = m.relation('mother')
facts = [
    father('Aks', 'Bob'),
    father('Bob', 'Cad'),
    father('Yan', 'Zer'),
    mother('Mary', 'Marla'),
    mother('Marla', 'Kay'),
    mother('Jane', 'Zanu')
]

# X, Y, Z = m.variables('X', 'Y', 'Z')
# X, Y, Z = m.variables('X', 'Y', 'Z')

paternal_grandfather = m.relation('paternal_grandfather')
maternal_grandmother = m.relation('maternal_grandmother')


def transitive(head, clause):
    X, Y, Z = m.variables('X', 'Y', 'Z')
    return head(X, Z) <= [clause(X, Y), clause(Y, Z)]


rules = [
    transitive(paternal_grandfather, father),
    transitive(maternal_grandmother, mother)
]

# rules = [
#     paternal_grandfather(X, Y) <= [father(X, Z), father(Z, Y)],
#     maternal_grandmother(X, Y) <= [mother(X, Z), mother(Z, Y)]
# ]

if __name__ == '__main__':
    # X, Y, Z = m.variables('X', 'Y', 'Z')
    X = m.variables('X')
    # A = m.variables('A')

    print(m.run(facts, rules, [paternal_grandfather(X, _)]))  # ['Aks']

    print(m.run(facts, rules, [maternal_grandmother(X, _)]))  # ['Mary']
