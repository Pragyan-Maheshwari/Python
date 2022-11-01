Para ="""giving more is invitation to more joy and happiness in life. if you give minus to others, you can never get plus as per the cosmic law. the definition of karma is very deep and wide, as the thinking too is taken as an integrated part of karma. karma is not only doing but thinking too. note as our life is fully being scanned by the divine scanner. there is divine surveillance on our life. and in the last there is divine audit too. go for infinite giving for infinite joys in life. we need to master and perfect in the art of living. those who have not learnt this art have missed living the life well. give back to society as this only is the time to give. now or never. now it is your turn to give. it is our moral duty to make the society better, healthier, happier, sustainable, clean, green, habitable, livable. give more than what you took. happiness in life can not be thought of without giving. the giving life only is meaningful and worthy life. now is the time to give back to society. giving gives the most lasting happiness. it empowers and makes you stronger. go on giving and go on living. the real worship of god lies in serving the creation of the creator. human being is the best creation of god. man must prove himself as the best caretaker of other living species in the whole of biodiversity. for our present position in the society we owe too much to others. now is the time to return back not to those who helped but to who need your help. there are limitless deprived, have-nots and people below poverty line who do not get even a one time meal in a day. there is too much suffering in the world that yours is nothing. we are far better placed."""
P1=""
p = Para.split(". ")

for i in p:
    i=i.capitalize()
    P1 = P1+i
    P1 = P1+". "

P1 = P1[0:124]+P1[124:135].upper()+P1[135:333]+P1[333:347].upper()+P1[347:358]+P1[358:376].title()+P1[376:416]+P1[416:429].title()+P1[429:582]+P1[582:956].upper()
print(P1)