from faker import Faker
fake = Faker()

words_list = ['ready', 'small', 'expert', 'those', 'improve', 'understand', 'tell', 'age', 'fear', 'product']
sentence_list = ['Might green catch medical.', 'Ahead receive board.' 'New customer expert save dinner account suggest society.' 'Turn side measure evidence election.' 'About executive model offer modern.' 'Lot research skill better position pretty sister whom.' 'They surface the family protect save.' 'Once choose class main those.' 'Contain response send beat common beyond bar.' 'Office pay worker reach watch organization develop watch.']

print("Dummy Word: ", fake.word())
print("Dummy Words: ", fake.words(nb=3, ext_word_list=words_list))
print("Dummy Text: ", fake.text())
print("Dummy Texts: ", fake.texts())
print("Dummy Sentence: ", fake.sentence())
print("Dummy Sentences: ", fake.sentences(nb=2, ext_word_list=words_list))
print("Dummy Paragraph: ", fake.paragraph(nb_sentences=10))