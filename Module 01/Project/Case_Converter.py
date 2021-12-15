class Case_Converter:
    def convert(self, string: str, case: str = "camel") -> str:
        if string == "":
            return "Enter a valid sentence"
        stringArray = string.split(",")
        if (case == "camel") or (case == "Camel"):
            return self.__camelConverter(stringArray)

        elif (case == "snake") or (case == "Snake"):
            return self.__snakeCasing(stringArray)

        elif (case == "kebab") or (case == "Kebab"):
            return self.__kebabCasing(stringArray)

        elif (case == "pascal") or (case == "Pascal"):
            return self.__pascalConverter(stringArray)

        elif (case =="uppersnake") or (case == "UpperSnake"):
            return self.__upperSnakeCasing(stringArray)

        return "No matched found"

    def __camelConverter(self, stringArray: list[str]) -> str:
        """Method for converting to the camel Casing"""
        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint: 
            if startingPoint == 0:
                newString = ""
                for j in range(len(stringArray[startingPoint])):
                    if str.isalnum(stringArray[startingPoint][j]):
                        newString += stringArray[startingPoint][j].lower()

                stringArray[startingPoint] = newString

                if startingPoint == endingPoint: 
                    startingPoint += 1
                    endingPoint -= 1
                    continue

                newString = ""
                for j in range(len(stringArray[endingPoint])):
                    if j == 0 and str.isnumeric(stringArray[endingPoint][j]):
                        newString += stringArray[endingPoint][j]

                    elif j == 0 and str.isalpha(stringArray[endingPoint][j]):
                        newString += stringArray[endingPoint][j].upper()

                    elif (stringArray[endingPoint][j-1] == " " or str.isnumeric(stringArray[endingPoint][j-1])) and str.isalpha(stringArray[endingPoint][j]):
                        newString += stringArray[endingPoint][j].upper()

                    elif str.isalpha(stringArray[endingPoint][j]): 
                        newString += stringArray[endingPoint][j]

                stringArray[endingPoint] = newString
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""
            for j in range(len(stringArray[startingPoint])):
                if j == 0 and str.isnumeric(stringArray[startingPoint][j]):
                    newString += stringArray[startingPoint][j]

                elif j == 0 and str.isalpha(stringArray[startingPoint][j]):
                    newString += stringArray[startingPoint][j].upper()

                elif (stringArray[startingPoint][j-1] == " " or str.isnumeric(stringArray[startingPoint][j-1]))and str.isalpha(stringArray[startingPoint][j]):
                    newString += stringArray[startingPoint][j].upper()

                elif str.isalpha(stringArray[startingPoint][j]) : 
                    newString += stringArray[startingPoint][j]

            stringArray[startingPoint] = newString

            if startingPoint == endingPoint: 
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""
            for j in range(len(stringArray[endingPoint])):
                if j == 0 and str.isnumeric(stringArray[endingPoint][j]):
                    newString += stringArray[endingPoint][j]

                elif j == 0 and str.isalpha(stringArray[endingPoint][j]):
                    newString += stringArray[endingPoint][j].upper()

                elif (stringArray[endingPoint][j-1] == " " or str.isnumeric(stringArray[endingPoint][j-1])) and str.isalpha(stringArray[endingPoint][j]):
                    newString += stringArray[endingPoint][j].upper()

                elif str.isalpha(stringArray[endingPoint][j]) : 
                    newString += stringArray[endingPoint][j].lower()

            stringArray[endingPoint] = newString
            startingPoint += 1
            endingPoint -= 1

        return "".join(stringArray)


    def __snakeCasing(self, stringArray: list[str]) -> str:
        """
        This is for snake casing
        """
        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint:
            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[startingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].lower()
                        isThereACharacter = True
                
                else:
                    if (stringArray[startingPoint][i-1] == " " or str.isnumeric(stringArray[startingPoint][i-1]))and str.isalpha(stringArray[startingPoint][i]):
                        newString += ("_"+stringArray[startingPoint][i].lower())
                    elif stringArray[startingPoint][i-1] == " " and str.isnumeric(stringArray[startingPoint][i]):
                        newString += ("_"+stringArray[startingPoint][i].lower())
                    elif str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].lower()

            stringArray[startingPoint] = newString

            if startingPoint == endingPoint:
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[endingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].lower()
                        isThereACharacter = True
                
                else:
                    if (stringArray[endingPoint][i-1] == " " or str.isnumeric(stringArray[endingPoint][i-1]))and str.isalpha(stringArray[endingPoint][i]):
                        newString += ("_"+stringArray[endingPoint][i].lower())
                    elif stringArray[endingPoint][i-1] == " " and str.isnumeric(stringArray[endingPoint][i]):
                        newString += ("_"+stringArray[endingPoint][i].lower())
                    elif str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].lower()
                        
            stringArray[endingPoint] = newString

            startingPoint += 1
            endingPoint -= 1

        return "_".join(stringArray)

    def __upperSnakeCasing(self, stringArray: list[str]) -> str:
        """
        This is for upper snake casing
        """
        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint:
            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[startingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].upper()
                        isThereACharacter = True
                
                else:
                    if (stringArray[startingPoint][i-1] == " " or str.isnumeric(stringArray[startingPoint][i-1]))and str.isalpha(stringArray[startingPoint][i]):
                        newString += ("_"+stringArray[startingPoint][i].upper())
                    elif stringArray[startingPoint][i-1] == " " and str.isnumeric(stringArray[startingPoint][i]):
                        newString += ("_"+stringArray[startingPoint][i].upper())
                    elif str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].upper()

            stringArray[startingPoint] = newString

            if startingPoint == endingPoint:
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[endingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].upper()
                        isThereACharacter = True
                
                else:
                    if (stringArray[endingPoint][i-1] == " " or str.isnumeric(stringArray[endingPoint][i-1]))and str.isalpha(stringArray[endingPoint][i]):
                        newString += ("_"+stringArray[endingPoint][i].upper())
                    elif stringArray[endingPoint][i-1] == " " and str.isnumeric(stringArray[endingPoint][i]):
                        newString += ("_"+stringArray[endingPoint][i].upper())
                    elif str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].upper()
                        
            stringArray[endingPoint] = newString

            startingPoint += 1
            endingPoint -= 1

        return "_".join(stringArray)

    
    def __kebabCasing(self, stringArray: list[str]) -> str:
        """
        This is for kebab casing
        """
        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint:
            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[startingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].lower()
                        isThereACharacter = True
                
                else:
                    if (stringArray[startingPoint][i-1] == " " or str.isnumeric(stringArray[startingPoint][i-1]))and str.isalpha(stringArray[startingPoint][i]):
                        newString += ("-"+stringArray[startingPoint][i].lower())
                    elif stringArray[startingPoint][i-1] == " " and str.isnumeric(stringArray[startingPoint][i]):
                        newString += ("-"+stringArray[startingPoint][i].lower())
                    elif str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].lower()

            stringArray[startingPoint] = newString

            if startingPoint == endingPoint:
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""
            isThereACharacter = False

            for i in range(len(stringArray[endingPoint])):
                if not isThereACharacter:
                    if str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].lower()
                        isThereACharacter = True
                
                else:
                    if (stringArray[endingPoint][i-1] == " " or str.isnumeric(stringArray[endingPoint][i-1]))and str.isalpha(stringArray[endingPoint][i]):
                        newString += ("-"+stringArray[endingPoint][i].lower())
                    elif stringArray[endingPoint][i-1] == " " and str.isnumeric(stringArray[endingPoint][i]):
                        newString += ("-"+stringArray[endingPoint][i].lower())
                    elif str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].lower()
                        
            stringArray[endingPoint] = newString

            startingPoint += 1
            endingPoint -= 1

        return "-".join(stringArray)


    def __pascalConverter(self, stringArray: list[str]) -> str:
        """This function is used to convert to the Pascal Casing"""

        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint:
            newString = ""

            for i in range(len(stringArray[startingPoint])):
                if i == 0:
                    if str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].upper()

                else:
                    if (stringArray[startingPoint][i-1] == " " or str.isnumeric(stringArray[startingPoint][i-1])) and str.isalpha(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].upper()

                    elif str.isalnum(stringArray[startingPoint][i]):
                        newString += stringArray[startingPoint][i].lower()

            stringArray[startingPoint] = newString

            if startingPoint == endingPoint:
                startingPoint += 1
                endingPoint -= 1
                continue

            newString = ""

            for i in range(len(stringArray[endingPoint])):
                if i == 0:
                    if str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].upper()

                else:
                    if (stringArray[endingPoint][i-1] == " " or str.isnumeric(stringArray[endingPoint][i-1])) and str.isalpha(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].upper()

                    elif str.isalnum(stringArray[endingPoint][i]):
                        newString += stringArray[endingPoint][i].lower()

            stringArray[endingPoint] = newString

            startingPoint += 1
            endingPoint -= 1

        return "".join(stringArray)
            


caseConverter = Case_Converter()
print(caseConverter.convert("Hello, World.", "camel"))
print(caseConverter.convert("Hello, World.", "snake"))
print(caseConverter.convert("Hello, World.", "kebab"))
print(caseConverter.convert("Hello, World.", "pascal"))
print(caseConverter.convert("Hello, World.", "uppersnake"))