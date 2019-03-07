#WAP to accept a filename from user and print those lines which have a specific word more than once




def PrintLinesWithWordMoreThanOnce(file,word):
    fd=open(file)
    count=0
    line = fd.readline()
    while line != '':
        res=dict()
        #print res
        if word in line:
            for ch in line.split():
                if res.get(ch) != None:
                    res[ch] += 1
                else:
                    res[ch] = 1
    
            if res.get(word) >= 2:
                print line
        line=fd.readline()

            
def main():
    f1=input('Enter the filename:')
    w1=input('Enter the word which repeats more than once in a line:')
    PrintLinesWithWordMoreThanOnce(f1,w1)



if __name__ == '__main__':
    main()


'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/hw_3_3/print_lines_having_word_more_than_twice.py 
Enter the filename:'file1.txt'
Enter the word which repeats more than once in a line:'far'
far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. 

>>>
'''
'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/hw_3_3/print_lines_having_word_more_than_twice.py 
Enter the filename:'file1.txt'
Enter the word which repeats more than once in a line:'the'
far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. 

Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. 

Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life.

One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. 

She packed her seven versalia, put her initial into the belt and made herself on the way. 

When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane.
>>> 
'''
