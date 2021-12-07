# Sprint-Final-ChrisDoucette
QAP4 - Data Files and Reports
The One Stop Insurance Company needs a program to enter and calculate new insurance policy information for its customers. Create a data file called OSICDef.dat that contains the next policy number, the basic premium, the discount for additional cars, the cost of extra liability coverage, the cost of glass coverage, the cost for loaner car coverage, the HST rate, and the processing fee for monthly payments. The file will look as follows:
1944 
869.00
0.25 
130.00 
86.00 
58.00 
0.15 
39.99
As the program starts, read the values from the defaults file. Write the current values back to the defaults file before the program ends.
The user will input the customer’s first and last name, address, city, province, postal code and phone number. They will also enter the number of cars being insured, and options for extra liability up to $1,000,000 (enter Y for Yes or N for No), optional glass coverage (Y or N), and optional loaner car (Y or N). Finally enter a value to indicate if they want to pay in full or monthly (F or M). No validations required – but go for it if you want.
Insurance premiums are calculated using a basic rate of $869.00 for the first automobile, with each additional automobile offered at a discount of 25%. If the user enters a Y for any of the options, the costs are $130.00 per car for extra liability, $86.00 per car for glass coverage, and $58.00 per car for the loaner car option. All these values are added together for the total extra costs. The total insurance premium is the premium plus the total extra costs. HST is calculated at 15% on the total insurance premium, and the total cost is the total insurance premium plus the HST. Customers can pay for their insurance in full or monthly. Calculate the monthly payment by adding a processing fee of $39.99 to the total cost and dividing the total cost by 12.
Display all input and calculated values to the screen in a well-designed receipt. Save the Policy number, all input values and the total premium to a file called Policies.dat for future reference. Increment the policy number by 1. Display the message “Policy processed and saved.” A sample line in the file might appear as follows:
1944, John, Smith, 12 Main St., St. John’s, NL, A1A8H4, 123-123-1234, 2, Y, N, Y, F, 1329.00
Allow the user to enter as many policies as they need. When the user is done entering policies and exits the program, write the current values back to the defaults file.
BONUS: Add the customer initials at the end of the policy number so it has the format 9999-XX. Set the policy date as the current date. The first monthly payment date will be the beginning of the next month – if it is after the 25th, the first payment date will be the following month. Display these values with printed results and add the policy date to the data file after the policy number.
At the end of the program (After the last line) I want you to print the following reports. One is a detailed report, and one is an exception report. You can just code them one after the other – place a few comments to show where each report starts. Normally these would be separate programs from a menu system but just put it all together for this project.
The first report is a Policy Listing that will print for each policy in the file (Detailed). The second report is Monthly Payment Listing for only those policies that are paid monthly (Exception). Use the following guidelines when creating the reports.
