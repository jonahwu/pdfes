import pdftotext

# Load your PDF
#file='pdfdata/ECD.pdf'
file='pdfdata/TestingDoc.pdf'
with open(file, "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
#with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
npage=1
for page in pdf:
    print('-----------------')
    print(npage)
    print(page)
    npage=npage+1

# Read some individual pages
#print(pdf[0])
#print(pdf[1])

# Read all the text into one string
print('----- rejoin all to a text -------')
print("\n\n".join(pdf))
