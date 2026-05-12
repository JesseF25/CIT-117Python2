'''
Name Jesse Ferguson
#Assignment- Planetary Weights Dictionaries -works
#Reflection: What I liked about this assigmnent is adding the Dictionary
#and Pickeling to the Planetary Weigjts code assigment.
# What I struggled with in this assignment is...
# Two things I learned on this assignment is
# 1) creating and using Dictionaries list.
# 2) Use of Pickling.
# 
#Inter Planetary Weights Part 2
'''
sName = ""
#input  Get the user's first name.
sName = input('Enter your first name: ')
#sName = (first_name)
#
print('Hello', sName)
#
def main():

    #get Earth Weight
    iYour_Weight = float(input('How much do you weight?'))
    # saftey check weight will be 70.5
    # List and Calculate
    iPlanets = tuple("Mercury, Venus, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto")

    iWeight = tuple("0.38, 0.91, 0.165 , 0.38, 2.34, 0.93, 0.92, 1.12, 0.66")
    MERCURY = 0.38 

    VENUS = 0.91 

    MOON = 0.165

    MARS = 0.38

    JUPITER = 2.34

    SATURN = 0.93

    URANUS = 0.92

    NEPTUNE =1.12

    PLUTO = 0.066

    # Output - These are the the weights on planetts on our soloar system.

    print (sName, 'here are your weights on our Solar Systems planets: ')
    print ('weight on MERCURY {MERCURY *iWeight:12.2f}')
    print ('weight on VENUS   {VENUS *iWeight:12.2f}')
    print ('weight on MOON    {MOON *iWeight:12.2f}')
    print ('weight on MARS    {MARS *iWeight:12.2f}')
    print ('weight on JUPITER {JUPITER *iWeight:12.2f}')
    print ('weight on SATURN  {SATURN *iWeight:12.2f}')
    print ('weight on URANUS  {URANUS *iWeight:12.2f}')
    print ('weight on NEPTUNE {NEPTUNE *iWeight:12.2f}')
    print ('weight on PLUTO   {PLUTO *iWeight:12.2f}')
main()
# History while loop
sHist(input("What is your name Enter Key to Quit"))


