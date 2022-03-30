from nltk import PorterStemmer

stemmer = PorterStemmer()
plurals = ["caresses", "flies", "dies", "mules", "denied",
"died", "agreed", "owned", "humbled", "sized",
"meeting", "stating", "siezing", "itemization",
"sensational", "traditional", "reference", "colonizer",
"plotted"]
print([stemmer.stem(plural) for plural in plurals])