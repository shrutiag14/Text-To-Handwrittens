from PIL import Image

class convertor:
    def __init__(self,BG,sizeOfSheet,allowedChars): 
        self.BG = BG
        self.sizeOfSheet = sizeOfSheet
        self.gap = 0
        self._ = 0
        self.allowedChars = allowedChars
        self.p = 0
        self.imagelist = []

    def writee(self,char):
        if char == '\n':
            pass                    
        else:
            char.lower()                                          
            cases = Image.open("Letters/%s.png"%char)
            self.BG.paste(cases, (self.gap, self._))
            size = cases.width
            self.gap += size
            del cases

    def letterwrite(self,word):
        if self.gap > self.sizeOfSheet - 95*(len(word)):
            self.gap = 0
            self._ += 200
        for letter in word:        
            if letter in self.allowedChars:
                if letter.islower():
                    pass
                elif letter.isupper():
                    letter = letter.lower()
                    letter += 'upper'            
                elif letter == '.':
                    letter = "fullstop"
                elif letter == '!':
                    letter = 'exclamation'
                elif letter == '?':
                    letter = 'question'
                elif letter == ',':
                    letter = 'comma'
                elif letter == '(':
                    letter = 'braketop'
                elif letter == ')':
                    letter = 'braketcl'
                elif letter == '-':
                    letter = 'hiphen'
                #return letter
                self.writee(letter)

    def worddd(self,Input):
        wordlist=Input.split(' ')
        for i in wordlist:
            self.letterwrite(i)
            self.writee('space')

    def run(self,upload):
        try:
            with open(upload, 'r') as file:
                data = file.read().replace('\n', '')
            l=len(data)
            nn=len(data)//600
            chunks, chunk_size = len(data), len(data)//(nn+1)
            self.p=[ data[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
            
            for i in range(0,len(self.p)):
                self.worddd(self.p[i])
                self.writee('\n')
                self.BG.save('%d.png'%i)
                BG1= Image.open("Letters/bg.png")
                self.BG=BG1
                self.gap = 0
                self._ =0
        except ValueError as E:
            print("{}\nTry again".format(E))

    def makeimage(self):
        for i in range(0, len(self.p)):
            self.imagelist.append('%d.png' % i)
        #First create a pdf file if not created
        self.pdf_creation(self.imagelist.pop(0))

    def pdf_creation(self,PNG_FILE, flag=False):
        rgba = Image.open(PNG_FILE)
        rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
        rgb.paste(rgba, mask=rgba.split()[3])  # paste using alpha channel as mask
        rgb.save('final.pdf',append=flag)

    def makepdf(self):
        #Now save multiple images in same pdf file

        #Now I am opening each images and converting them to pdf
        #Appending them to pdfs
        for PNG_FILE in self.imagelist:
            self.pdf_creation(PNG_FILE, flag=True)
