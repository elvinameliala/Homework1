DNA = 'TGCCAATG'
RNA = 'UGCCAAUG'
def countNucleotide (sequence):
    counter1 = sequence.count('T')
    counter2 = sequence.count('G')
    counter3 = sequence.count('C')
    counter4 = sequence.count('A')
    counter5 = sequence.count('U')

    print ('T=' + str(counter1))
    print ('G=' + str(counter2))
    print ('C=' + str(counter3))
    print ('A=' + str(counter4))
    print ('U=' + str(counter5))


countNucleotide(DNA)




