import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_ two_letter': word[-2:]}
# gender_features('Shrek') = {'last_letter': 'k'}

male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
#entries are    ({'last_letter': 'g'}, 'male')
train_set, test_set = featuresets[6500:], featuresets[:6500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

ans1 = classifier.classify(gender_features('akansha'))
ans2 = classifier.classify(gender_features('marku'))
print("The accuracy percenatge is :",nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)
print("Akansha is:", ans1)
print("MARKU is:", ans2)






