# Marvish Chandra
'''This program is designed to help an average size family determine what tax deductibles they can make in their yearly taxes.'''

class Tax Deductions:

    def medDental(self, individual,partner,child1,child2):
        individual = input("Did you visit the hospital or get dental treatment at all this year?")
        print(individual)
        individual_yes = input("Please type how much you spent in total.")
        partner = input("Did you visit the hospital or get dental treatment at all this year?")
        print(partner)
        partner_yes = input("Please type how much you spent in total.")
        child1 = input("Did your first child visit the hospital or get dental treatment this year?")
        print(child1)
        child1_yes = input("Please type how much you spent in total.")
        child2 = input("Did your second child visit the hospital or get dental treatment this year?")
        print(child2)
        child2_yes = input("Please type how much you spent in total.")
        family_cost = "The total family spent on medical and hospital expenses is :" + str(individual_yes) + str(partner_yes) + str(child1_yes) + str(child2_yes) + "./n"
        print(family_cost)

    def investmentExpenses(self,individual,partner):
        individual = input("Did you invest in a company or more than one company this year?")
        individual_yes = input("Please enter how much money you have invested in.")
        partner = input("Did you invest in a company or more than one company this year?")
        partner_yes = input("Please enter how much money you have invested in.")
        print("You and your partner have decided to invest: " + str(individual_yes) + str(partner_yes) + "dollars./n")

    def mortgageExpenses(self,individual,partner):
        print("As a couple, the both of you have to pay the following taxes: property, mortgage interest, and insurance.")
        individual_property = 5,000
        couple_property = 10,000
        mortgage_interest = input("Enter the time span of your home loan being either: 15, 20, or 30 years.")
        mortgage_insurance = input("Enter how much your home insurance is which ranges from: $1,500-$3,000.")
        indivProp("I have spent" + str(individual_property) + "in property taxes./n")
        print(indivProp)
        coupProp("We have spent" + str(couple_property) + "in property taxes./n")
        print(coupProp)
        totalMorin("My current home loan is" + str(mortgage_interest) + "total years./n")
        print(totalMorin)
        mortInsurance("Every year I spend," + str(mortgage_insurance) + "dollars./n")
        print(mortInsurance)

    def educationalExpenses(self,eduIndividual,eduPartner,eduChild1,eduChild2):
        print("If you, partner, or children are in an education system, you qualify for a tax deduction.")
        int vocationalSchool = 16,500
        int publicBachelor = 31,750
        int childSchool = 13,641
        eduIndividual = input("Are you currently attending vocational school or college?")
        print(eduIndividual)
        eduPartner = input("Are you currently attending adult school or some college?")
        print(eduPartner)
        eduChild1 = input("Are you currently in the K-12 system or attending some college?")
        print(eduChild1)
        eduChild2 = input("Are you currently in the K-12 system or attending some college?")
        print(eduChild2)

        # if both children are attending k-12
        # if both children are attending college
        # if both adults are attending college
        if eduIndividual == publicBachelor: "You are attending college, you pay:" + str(publicBachelor) + "./n"
        if eduIndividual == vocationalSchool: "You are attending vocational school, you pay:" + str(vocationalSchool) + "./n"
        if eduPartner == publicBachelor: "You are attending college, you pay:" + str(publicBachelor) + "./n"
        if eduPartner == vocationalSchool: "You are attending vocational school, you pay:" + str(vocationalSchool) + "./n"
        if eduChild1 == publicBachelor: "You are attending college, you pay:" + str(publicBachelor) + "."
        if eduChild2 == vocationalSchool: "You are attending vocational school, you pay:" + str(vocationalSchool) + "./n"
        else: print("None of your family is currently enrolled in education, you are ineligible for any education deductibles./n")

    def charityExpenses(self,individualDon,partnerDon):
        print("Have either you or your partner make any donations this year, you qualify for a tax deduction.")
        print("If either of you have not donated, then there is no qualification for a tax deduction.")
        individualDon = input("How much have you donated this year?")
        print(individualDon)
        partnerDon = input("How much have you donated this year?")
        print(partnerDon)
        total_donated = individualDon + partnerDon
        print("Your total contribution equals to" + str(total_donated) + "dollars.")







