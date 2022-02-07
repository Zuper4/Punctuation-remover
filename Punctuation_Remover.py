print("\nThis program will remove all the punctuations from a string that you will input.")

punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''

my_str = str(input("\nYour string :"))

no_punct = ""

for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

print("\nThe new version of your string :")
print("\n" +no_punct)

