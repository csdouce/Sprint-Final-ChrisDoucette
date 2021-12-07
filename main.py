# QAP4 project
# Program to enter and calculate new insurance policies.
# Also will print a receipt and two reports at end of program's running
# Chris Doucette
# Completed December 7, 2021

# Imports
import datetime

# Functions
def insurance_prem_calc(num_cars):
    # Function that calculates the Insurance premiums based on how many cars are insured
    insur_prem = BASIC_PREM

    if num_cars > 1:
        insur_prem += ((num_cars - 1) * BASIC_PREM) - ((num_cars - 1) * BASIC_PREM * ADD_CAR_PREM)

    return insur_prem


def dollar_format(dollar, pad_amt):
    # Formatting currency amount with padding to be passed in
    dollar_str = "${:,.2f}".format(dollar)
    dollar_pad = "{:>{}}".format(dollar_str, pad_amt)
    return dollar_pad


def str_length(string_format, length):
    # Formatting the length of string before printing
    string_format = string_format[0:length]

    return string_format

# Read values from file OSICDef.dat
f = open("OSICDef.dat", "r")

PolicyNum = f.readline().strip()
BASIC_PREM = float(f.readline())
ADD_CAR_PREM = float(f.readline())
EX_LIABILITY_COST = float(f.readline())
GLASS_COVER_COST = float(f.readline())
LOANER_CAR_COVER_COST = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())

f.close()

# Creating province list for input validation
ProvinceList = ["AB", "BC", "MB", "SK", "ON", "QC", "NB", "NS", "PE", "NL", "NU", "YT", "NT"]

# Loop that will exit on user commands
while True:
    # User inputted values
    # FirstName input validation
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")

        FirstName = input("Enter the firstname: ")

        if FirstName == "" or set(FirstName).issubset(allowed_char) == False:
            print("First name must not be blank or contain numbers - Please re-enter.")
        else:
            FirstName = FirstName.title()
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")

        LastName = input("Enter the lastname: ")

        if LastName == "" or set(LastName).issubset(allowed_char) == False:
            print("Last name must not be blank or contain numbers - Please re-enter.")
        else:
            LastName = LastName.title()
            break

    # Input validation for Street Address - Checking for empty
    while True:
        StAddr = input("Enter the street address: ").title()

        if StAddr == "":
            print("Street address cannot be empty - Please re-enter.")
        else:
            break

    # Input validation for City - Checking for empty
    while True:
        City = input("Enter the city: ").title()

        if City == "":
            print("City cannot be empty - Please re-enter.")
        else:
            break

    # Input validation for Province
    while True:
        Province = input("Enter the province (XX): ").upper()
        ProvMatch = "NO"

        for Prov in ProvinceList:
            if Prov == Province:
                ProvMatch = "YES"
                break

        if ProvMatch == "NO":
            print("Enter a valid two character code for province (XX)- Please re-enter.")
        else:
            break

    # Input validation for Postal Code
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        allowed_num = set("1234567890")

        PostCode = input("Enter the postal code (A1A1A1):").upper()

        if set(PostCode[0]).issubset(allowed_char) == False or set(PostCode[2]).issubset(allowed_char) == False \
                or set(PostCode[4]).issubset(allowed_char) == False or set(PostCode[1]).issubset(allowed_num) == False \
                or set(PostCode[3]).issubset(allowed_num) == False or set(PostCode[5]).issubset(allowed_num) == False:
            print("Postal code not in the format A1A1A1 - Please re-enter.")
        else:
            PostCode = PostCode.upper()
            break

    # Input validation for Phone Number
    while True:
        allowed_num = set("1234567890")

        PhNum = input("Enter the phone number (9999999999): ")

        if len(PhNum) != 10:
            print("Phone number must be exactly ten digits (9999999999) - Please re-enter.")
        elif set(PhNum).issubset(allowed_num) == False:
            print("Invalid characters. There can only be numbers in phone number (9999999999) - Please re-enter.")
        else:
            break

    # Input validation for Number of cars
    while True:
        try:
            NumCars = int(input("Enter the number of cars to insure: "))
        except:
            print("Invalid input. Enter only digits for number of cars - Please re-enter.")
        else:
            break

    # Input validation for Extra Liability
    while True:
        ExLiability = input("Enter if customer wants extra liability insurance (Y/N): ").upper()

        if ExLiability != "Y" and ExLiability != "N":
            print("Extra Liability must be either 'Y' or 'N' - Please re-enter.")
        else:
            break

    # Input validation for Glass Coverage
    while True:
        GlassCoverage = input("Enter if customer wants glass coverage insurance (Y/N): ").upper()

        if GlassCoverage != "Y" and GlassCoverage != "N":
            print("Glass Coverage must be either 'Y' or 'N' - Please re-enter.")
        else:
            break

    # Input validation for Loaner Car
    while True:
        LoanerCar = input("Enter if customer wants loaner car insurance (Y/N): ").upper()

        if LoanerCar != "Y" and LoanerCar != "N":
            print("Loaner Car coverage must be either 'Y' or 'N' - Please re-enter.")
        else:
            break

    # Input validation for Pay Type
    while True:
        PayType = input("Enter if customers wants to pay in full or monthly (F/M): ").upper()

        if PayType != "F" and PayType != "M":
            print("If user wants to pay Full or Monthly must be either a 'F' or 'M' - Please re-enter.")
        else:
            break

    PolicyDate = datetime.datetime.now()

    # Updating the PolicyNum to include customer initials at end of policy number
    PolicyNum = PolicyNum + "-" + FirstName[0] + LastName[0]

    # Calculations of insurance premiums and the additional car discount if user has more than 1 car insured
    InsurPrem = insurance_prem_calc(NumCars)

    # Determining what extra costs were selected by user
    ExtraCosts = 0.0

    if ExLiability == "Y":
        ExtraCosts += NumCars * EX_LIABILITY_COST

    if GlassCoverage == "Y":
        ExtraCosts += NumCars * GLASS_COVER_COST

    if LoanerCar == "Y":
        ExtraCosts += NumCars * LOANER_CAR_COVER_COST

    # Calculating the total insurance premium, HST and total costs
    TotalPrem = InsurPrem + ExtraCosts

    TaxPaid = TotalPrem * HST_RATE

    TotalCost = TotalPrem + TaxPaid

    # Calcualting monthly payment if that option is selected by user
    MonthlyPayment = 0.0

    if PayType == "M":
        MonthlyPayment = (TotalCost + PROCESS_FEE) / 12

    # Formatting before printing
    PhNumFormat = PhNum[0:3] + "-" + PhNum[3:6] + "-" + PhNum[6:]
    FullName = FirstName + " " + LastName

    if len(FullName) > 28:
        FullName = str_length(FullName, 28)

    StAddrFormat = StAddr
    if len(StAddrFormat) > 28:
        StAddrFormat = str_length(StAddrFormat, 28)

    CityFormat = City
    if len(CityFormat) > 17:
        CityFormat = str_length(CityFormat, 17)

    BasicPremPad = dollar_format(BASIC_PREM, 7)
    ReducedRatePad = dollar_format(InsurPrem-BASIC_PREM, 9)
    InsurPremPad = dollar_format(InsurPrem, 10)

    if ExLiability == "Y":
        ExLiabilityPad = dollar_format(NumCars * EX_LIABILITY_COST, 9)
    else:
        ExLiabilityPad = dollar_format(0.00, 9)

    if GlassCoverage == "Y":
        GlassCoveragePad = dollar_format(NumCars * GLASS_COVER_COST, 9)
    else:
        GlassCoveragePad = dollar_format(0.00, 9)

    if LoanerCar == "Y":
        LoanerCarPad = dollar_format(NumCars * LOANER_CAR_COVER_COST, 9)
    else:
        LoanerCarPad = dollar_format(0.00, 9)

    ExtraCostsPad = dollar_format(ExtraCosts, 10)
    TotalPremPad = dollar_format(TotalPrem, 10)
    TaxPaidPad = dollar_format(TaxPaid, 7)
    TotalCostPad = dollar_format(TotalCost, 11)
    ProcessFeePad = dollar_format(PROCESS_FEE, 6)
    TotCostMonthPad = dollar_format(TotalCost + PROCESS_FEE, 11)
    MonthlyPaymentPad = dollar_format(MonthlyPayment, 9)

    # Printing all inputted and calculated values to receipt
    print()
    print("      ONE STOP INSURANCE COMPANY RECEIPT")
    print(f"      {datetime.datetime.now().strftime('%A, %B %-d, %Y')}")
    print()
    print("      Customer Information:")
    print()
    print(f"      {FullName}")
    print(f"      {StAddrFormat}")
    print(f"      {CityFormat} {Province}, {PostCode}")
    print(f"      {PhNumFormat}")
    print()
    print(f"      Policy Date:     {PolicyDate.strftime('%d-%b-%Y')}")
    print(f"      Policy Number:       {PolicyNum}")
    print()
    print("      Claim Information:")
    print()
    print("      Number of Cars:" + " "*27 + f"{NumCars:>2}")
    print("      First Car at Regular Rate:" + " "*11 + BasicPremPad)
    print("      Remaining Cars at Reduced Rate:"+ " "*4 + ReducedRatePad)
    print(" "*6 + "="*44)
    print("      Insurance Premium Total:" + " "*10 + InsurPremPad)
    print()
    print("      Extras:")
    print()
    print(f"      Extra Liability:     {ExLiability}" + " "*13 + ExLiabilityPad)
    print(f"      Glass Coverage:      {GlassCoverage}" + " "*13 + GlassCoveragePad)
    print(f"      Loaner Car:          {LoanerCar}" + " "*13 + LoanerCarPad)
    print(" " * 6 + "=" * 44)
    print("      Total Extras:" + " "*21 + ExtraCostsPad)
    print()
    print("      Total Premiums:" + " "*19 + TotalPremPad)
    print("      Taxes Paid:" + " "*26 + TaxPaidPad)
    print(" " * 6 + "=" * 44)
    print("      Total Cost:" + " "*22 + TotalCostPad)
    print()

    # Determining the starting payment date for full payment or monthly payments
    if PolicyDate.day > 25:
        PaymentDate = PolicyDate + datetime.timedelta(days=40)
        PaymentDate = PaymentDate.replace(day=1)
    else:
        PaymentDate = PolicyDate + datetime.timedelta(days=30)
        PaymentDate = PaymentDate.replace(day=1)

    # Changing what prints based on if paying in full or monthly
    if PayType == "F":
        print("      Pay Type Chosen: Full")
        print(f"      Please Pay ${TotalCost} in full by {datetime.datetime.strftime(PaymentDate, '%d-%b-%Y')}")
    else:
        print("      Pay Type Chosen: Monthly")
        print("      Total Cost:" + " "*22 + TotalCostPad)
        print("      Processing Fee:" + " "*23 + ProcessFeePad)
        print(" " * 6 + "=" * 44)
        print("      Total Cost with Processing Fee:" + " "*2 + TotCostMonthPad)
        print()
        print("      Your Monthly Cost:" + " "*17 + MonthlyPaymentPad)
        print()

        print(f"      First Monthly Payment is due on {datetime.datetime.strftime(PaymentDate, '%d-%b-%Y')}")
    print()
    print("              Thank you for your business!")
    print()

    # Appending values to file Policies.dat
    f = open("Policies.dat", "a")

    f.write(PolicyNum + ",")
    f.write(PolicyDate.strftime("%Y-%m-%d") + ",")
    f.write(FirstName + ",")
    f.write(LastName + ",")
    f.write(StAddr + ",")
    f.write(City + ",")
    f.write(Province + ",")
    f.write(PostCode + ",")
    f.write(PhNum + ",")
    f.write(str(NumCars) + ",")
    f.write(ExLiability + ",")
    f.write(GlassCoverage + ",")
    f.write(LoanerCar + ",")
    f.write(PayType + ",")
    f.write(str(TotalCost) + "\n")

    f.close()

    print("      Policy has been processed and saved.")
    print()

    # Changing PolicyNum to Integer, Incrementing and changing back to string
    PolicyNum = PolicyNum[0:-3]

    PolicyNum = int(PolicyNum)
    PolicyNum += 1
    PolicyNum = str(PolicyNum)

    # Checking if user wants to continue program
    ToQuit = input("     Do you want to quit the program (Y/N)? ").upper()
    print()
    
    if ToQuit == "Y":
        # Opening OSICDef.dat file and writing defaults back to file
        f = open("OSICDef.dat", "w")

        f.write(PolicyNum + "\n")
        f.write(str(BASIC_PREM) + "\n")
        f.write(str(ADD_CAR_PREM) + "\n")
        f.write(str(EX_LIABILITY_COST) + "\n")
        f.write(str(GLASS_COVER_COST) + "\n")
        f.write(str(LOANER_CAR_COVER_COST) + "\n")
        f.write(str(HST_RATE) + "\n")
        f.write(str(PROCESS_FEE) + "\n")

        f.close()

        break

# Once the option to quit is selected the main program is complete
# Printing two reports now

# Printing Policy Listing report (Detailed)
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTINGS AS OF {datetime.datetime.now().strftime('%d-%b-%y')}")
print()
print("POLICY   CUSTOMER                 INSURANCE        EXTRA          TOTAL")
print("NUMBER   NAME                      PREMIUM         COSTS          PREMIUM")
print("="*73)

# Assigning zero's to Accumulators and Counter
Counter = 0
TotalInsurancePremiumAcc = 0.0
TotalExtraCostsAcc = 0.0
TotalPremiumCostAcc = 0.0

# Opening file before printing form file
f = open("Policies.dat", "r")

for CustData in f:
    # Loop to print lines from file
    # Reading from file

    Customer = CustData.split(",")

    PolicyNumber = Customer[0]
    FullName = Customer[2] + " " + Customer[3]
    NumberCars = int(Customer[9])
    ExtraLiabilitiesSelected = Customer[10].strip()
    GlassCoverageSelected = Customer[11].strip()
    LoanerCarSelected = Customer[12].strip()

    # Completing Calculations before printing
    if len(FullName) > 20:
        FullName = FullName[0:20]

    InsurancePremiumLine = insurance_prem_calc(NumberCars)

    ExtraCostsLine = 0.0

    if ExtraLiabilitiesSelected == "Y":
        ExtraCostsLine += NumberCars * EX_LIABILITY_COST

    if GlassCoverageSelected == "Y":
        ExtraCostsLine += NumberCars * GLASS_COVER_COST

    if LoanerCarSelected == "Y":
        ExtraCostsLine += NumberCars * LOANER_CAR_COVER_COST

    TotalPremiumCost = InsurancePremiumLine + ExtraCostsLine

    # Formatting before printing
    InsurancePremiumLinePad = dollar_format(InsurancePremiumLine, 9)
    ExtraCostsLinePad = dollar_format(ExtraCostsLine, 9)
    TotalPremiumCostPad = dollar_format(TotalPremiumCost, 9)

    # Printing Lines
    print(f"{PolicyNumber}  {FullName:<20}     {InsurancePremiumLinePad}      {ExtraCostsLinePad}      {TotalPremiumCostPad}")

    # Adding to counters and accumulators
    Counter += 1
    TotalInsurancePremiumAcc += InsurancePremiumLine
    TotalExtraCostsAcc += ExtraCostsLine
    TotalPremiumCostAcc += TotalPremiumCost

# Closing file after loop and printing final columns
f.close()

print("="*73)

# Formatting before printing
TotalInsurancePremiumAccPad = dollar_format(TotalInsurancePremiumAcc, 10)
TotalExtraCostsAccPad = dollar_format(TotalExtraCostsAcc, 10)
TotalPremiumCostAccPad = dollar_format(TotalPremiumCostAcc, 10)

print(f"Total Policies: {Counter:>3}              {TotalInsurancePremiumAccPad}     {TotalExtraCostsAccPad}     {TotalPremiumCostAccPad}")
print()
print()

# Creating second report that was requested
# This is a Monthly Payment Listing (exception) report
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {datetime.datetime.now().strftime('%d-%b-%y')}")
print()
print("POLICY  CUSTOMER               TOTAL                   TOTAL     MONTHLY")
print("NUMBER  NAME                  PREMIUM      HST         COST      PAYMENT")
print("="*73)

# Setting counters and accumulators to zero
Counter = 0
InsurancePremiumAcc = 0.0
HstAcc = 0.0
TotalCostAcc = 0.0
MonthlyPaymentAcc = 0.0

# Opening file and going through loop to read file and print lines
f = open("Policies.dat", "r")

for CustData in f:

    Customer = CustData.split(",")

    PayTypeLine = Customer[13].strip()

    # Only need lines that customer is paying monthly
    if PayTypeLine == "M":
        PolicyNumberLine = Customer[0]
        CustomerNameLine = Customer[2] + " " + Customer[3]
        NumberCarsLine = int(Customer[9])
        ExtraLiabilitiesLine = Customer[10]
        GlassCoverageLine = Customer[11]
        LoanerCarLine = Customer[12]

        # Calculating Insurance premiums
        InsurancePremiumLine = insurance_prem_calc(NumberCarsLine)

        # Calculating extra costs
        ExtraCostsLine = 0.0

        if ExtraLiabilitiesLine == "Y":
            ExtraCostsLine += NumberCarsLine * EX_LIABILITY_COST

        if GlassCoverageLine == "Y":
            ExtraCostsLine += NumberCarsLine * GLASS_COVER_COST

        if LoanerCarLine == "Y":
            ExtraCostsLine += NumberCarsLine * LOANER_CAR_COVER_COST

        TotalPremiumLine = InsurancePremiumLine + ExtraCostsLine

        #  Calculating HST, Total Cost and Monthly Payment
        HstLine = TotalPremiumLine * HST_RATE

        TotalCostLine = TotalPremiumLine + HstLine

        MonthlyPaymentLine = (TotalCostLine + PROCESS_FEE) / 12

        # Formatting before printing
        if len(CustomerNameLine) > 20:
            CustomerNameLine = CustomerNameLine[0:20]

        TotalPremiumLinePad = dollar_format(TotalPremiumLine, 9)
        HstLinePad = dollar_format(HstLine, 7)
        TotalCostLinePad = dollar_format(TotalCostLine, 9)
        MonthlyPaymentLinePad = dollar_format(MonthlyPaymentLine, 9)

        # Printing required information
        print(f"{PolicyNumberLine} {CustomerNameLine:<20} {TotalPremiumLinePad}    {HstLinePad}    {TotalCostLinePad}  {MonthlyPaymentLinePad}")

        # Adding to Counter and Accumulators
        Counter += 1
        InsurancePremiumAcc += InsurancePremiumLine
        HstAcc += HstLine
        TotalCostAcc += TotalCostLine
        MonthlyPaymentAcc += MonthlyPaymentLine

# Closing file and printing closing lines of report
f.close()

# Formatting before printing
InsurancePremiumAccPad = dollar_format(InsurancePremiumAcc, 10)
HstAccPad = dollar_format(HstAcc, 9)
TotalCostAccPad = dollar_format(TotalCostAcc, 10)
MonthlyPaymentAccPad = dollar_format(MonthlyPaymentAcc, 10)

print("="*73)
print(f"Total policies: {Counter:>3}         {InsurancePremiumAccPad}  {HstAccPad}   {TotalCostAccPad} {MonthlyPaymentAccPad}")
print()